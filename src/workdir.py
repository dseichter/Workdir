# Copyright (c) 2024-2026 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import os
import shlex
import shutil
import subprocess  # nosec B404  # NOSONAR
import sys
import webbrowser
from pathlib import Path

from PySide6.QtCore import QObject, QEvent, QStandardPaths, QThread, QTimer, Signal, Qt
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QMenu,
    QMessageBox,
    QPushButton,
    QSystemTrayIcon,
    QWidget,
)

import about_ui
import configuration_ui
import gui
import helper
import icons
import settings


class UpdateCheckWorker(QObject):
    finished = Signal(bool)

    def run(self) -> None:
        self.finished.emit(helper.check_for_new_release())


class WorkDirFrame(gui.MainFrame):
    """
    Main application window for Workdir.
    Inherits from gui.MainFrame and connects UI actions.
    """
    def __init__(self, parent=None):
        self._commands: dict[str, dict] = {}
        self._update_thread: QThread | None = None
        self._update_worker: UpdateCheckWorker | None = None
        self._tray_icon: QSystemTrayIcon | None = None
        self._tray_menu: QMenu | None = None
        self._tray_directory_entries: list = []
        self._tray_quit_separator = None
        self._tray_hint_shown = False
        self._is_quitting = False
        self._minimize_to_tray = True

        super().__init__(parent)
        # Set icons
        self.setWindowIcon(icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48'))
        self.close_action.setIcon(icons.get_icon('logout_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.desktop_link_action.setIcon(icons.get_icon('folder_open_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.config_action.setIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.support_action.setIcon(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.update_action.setIcon(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.about_action.setIcon(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self._init_tray_icon()
        self._update_tray_menu(settings.load_directories() or [])

    def _init_tray_icon(self) -> None:
        if not QSystemTrayIcon.isSystemTrayAvailable():
            return

        self._tray_icon = QSystemTrayIcon(self.windowIcon(), self)
        self._tray_icon.setToolTip(helper.NAME)

        self._tray_menu = QMenu(self)

        show_action = self._tray_menu.addAction('Show Workdir')
        show_action.triggered.connect(self._restore_from_tray)

        self._tray_menu.addSeparator()
        self._tray_quit_separator = self._tray_menu.addSeparator()
        quit_action = self._tray_menu.addAction('Quit')
        quit_action.triggered.connect(self._quit_from_tray)

        self._tray_icon.setContextMenu(self._tray_menu)
        self._tray_icon.activated.connect(self._on_tray_activated)
        self._tray_icon.show()

    def _restore_from_tray(self) -> None:
        self.showNormal()
        self.raise_()
        self.activateWindow()

    def _quit_from_tray(self) -> None:
        self._is_quitting = True
        if self._tray_icon is not None:
            self._tray_icon.hide()
        self.close()
        QApplication.quit()

    def _on_tray_activated(self, reason: QSystemTrayIcon.ActivationReason) -> None:
        if reason in (QSystemTrayIcon.Trigger, QSystemTrayIcon.DoubleClick):
            self._restore_from_tray()

    def _update_tray_menu(self, directories: list[str]) -> None:
        if self._tray_menu is None or self._tray_quit_separator is None:
            return

        for entry in self._tray_directory_entries:
            self._tray_menu.removeAction(entry)
        self._tray_directory_entries = []

        if not directories:
            no_dirs_action = self._tray_menu.insertAction(self._tray_quit_separator, self._tray_menu.addAction('No directories configured'))
            no_dirs_action.setEnabled(False)
            self._tray_directory_entries.append(no_dirs_action)
            return

        for directory in directories:
            self._add_directory_to_tray_menu(directory)

    def _add_directory_to_tray_menu(self, directory: str) -> None:
        if self._tray_menu is None or self._tray_quit_separator is None:
            return

        dir_menu = QMenu(directory, self._tray_menu)

        has_command = False
        for col in range(1, 7):
            cmd_name = f'CMD{col}'
            cmd = self._commands.get(cmd_name)
            if cmd is None or cmd.get('command', '') == '':
                continue

            label = cmd.get('label') or cmd_name
            action = dir_menu.addAction(label)
            action.setToolTip(f"{cmd.get('command', '')} {cmd.get('parameters', '')}")
            action.triggered.connect(lambda checked=False, c=cmd_name, d=directory: self.execute_command(c, d))
            has_command = True

        if not has_command:
            no_cmd_action = dir_menu.addAction('No command configured')
            no_cmd_action.setEnabled(False)

        action = self._tray_menu.insertMenu(self._tray_quit_separator, dir_menu)
        self._tray_directory_entries.append(action)

    def changeEvent(self, event) -> None:
        tray_icon = getattr(self, '_tray_icon', None)
        minimize_to_tray = getattr(self, '_minimize_to_tray', False)
        is_quitting = getattr(self, '_is_quitting', False)

        if (
            tray_icon is not None
            and event.type() == QEvent.WindowStateChange
            and self.isMinimized()
            and minimize_to_tray
            and not is_quitting
        ):
            QTimer.singleShot(0, self.hide)
            if not self._tray_hint_shown:
                tray_icon.showMessage(
                    helper.NAME,
                    'Workdir is still running in the system tray.',
                    QSystemTrayIcon.Information,
                    3000,
                )
                self._tray_hint_shown = True
            event.accept()
            return

        super().changeEvent(event)

    @staticmethod
    def _get_desktop_directory_linux() -> Path:
        desktop_dir = Path.home() / "Desktop"
        try:
            result = subprocess.run(  # nosec B603, B607  # NOSONAR
                ["xdg-user-dir", "DESKTOP"],
                capture_output=True,
                text=True,
                check=True,
            )
            candidate = Path(result.stdout.strip())
            if candidate:
                desktop_dir = candidate
        except (OSError, subprocess.SubprocessError):
            pass
        return desktop_dir

    @staticmethod
    def _get_desktop_directory_windows() -> Path:
        desktop_dir = Path.home() / "Desktop"
        try:
            result = subprocess.run(  # nosec B603, B607  # NOSONAR
                [
                    "powershell",
                    "-NoProfile",
                    "-NonInteractive",
                    "-Command",
                    "[Environment]::GetFolderPath('Desktop')",
                ],
                capture_output=True,
                text=True,
                check=True,
            )
            candidate = Path(result.stdout.strip())
            if candidate:
                desktop_dir = candidate
        except (OSError, subprocess.SubprocessError):
            pass
        return desktop_dir

    @staticmethod
    def _get_launch_target_and_arguments() -> tuple[str, str, str]:
        if getattr(sys, 'frozen', False):
            target = os.path.abspath(sys.executable)
            arguments = ""
            working_directory = str(Path(target).parent)
        else:
            script_path = os.path.abspath(__file__)
            target = sys.executable
            arguments = f'"{script_path}"'
            working_directory = str(Path(script_path).parent)
        return target, arguments, working_directory

    @staticmethod
    def _get_desktop_icon_path() -> str:
        app_data_location = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        if app_data_location:
            icon_dir = Path(app_data_location)
        else:
            icon_dir = Path.home() / ".local" / "share" / helper.NAME

        try:
            icon_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            return ""

        icon = icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48')
        if icon.isNull():
            return ""

        pixmap = icon.pixmap(256, 256)
        if pixmap.isNull():
            return ""

        icon_path = icon_dir / "workdir_shortcut_icon.png"
        if not pixmap.save(str(icon_path), "PNG"):
            return ""
        return str(icon_path)

    @staticmethod
    def _get_windows_desktop_icon_path() -> str:
        app_data_location = QStandardPaths.writableLocation(QStandardPaths.AppDataLocation)
        if app_data_location:
            icon_dir = Path(app_data_location)
        else:
            icon_dir = Path.home() / "AppData" / "Local" / helper.NAME

        try:
            icon_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            return ""

        icon = icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48')
        if icon.isNull():
            return ""

        pixmap = icon.pixmap(256, 256)
        if pixmap.isNull():
            return ""

        icon_path = icon_dir / "workdir_shortcut_icon.ico"
        if pixmap.save(str(icon_path), "ICO"):
            return str(icon_path)
        return ""

    def _create_linux_desktop_link(self) -> Path:
        desktop_dir = self._get_desktop_directory_linux()
        desktop_dir.mkdir(parents=True, exist_ok=True)
        target_path = desktop_dir / "Workdir.desktop"

        target, arguments, _ = self._get_launch_target_and_arguments()
        executable = f'"{target}"'
        if arguments:
            executable = f"{executable} {arguments}"

        icon_path = self._get_desktop_icon_path()
        icon_line = f"Icon={icon_path}\n" if icon_path else ""

        desktop_entry = (
            "[Desktop Entry]\n"
            "Version=1.0\n"
            "Type=Application\n"
            "Name=Workdir\n"
            "Comment=Start Workdir\n"
            f"Exec={executable}\n"
            f"{icon_line}"
            "Terminal=false\n"
            "Categories=Utility;Development;\n"
        )

        target_path.write_text(desktop_entry, encoding='utf-8')
        target_path.chmod(0o755)
        return target_path

    def _create_windows_desktop_link(self) -> Path:
        desktop_dir = self._get_desktop_directory_windows()
        desktop_dir.mkdir(parents=True, exist_ok=True)
        target_path = desktop_dir / "Workdir.lnk"

        target, arguments, working_directory = self._get_launch_target_and_arguments()
        icon_path = self._get_windows_desktop_icon_path() or self._get_desktop_icon_path() or target

        def _ps_escape(value: str) -> str:
            return value.replace("'", "''")

        ps_script = (
            "$shell = New-Object -ComObject WScript.Shell; "
            f"$shortcut = $shell.CreateShortcut('{_ps_escape(str(target_path))}'); "
            f"$shortcut.TargetPath = '{_ps_escape(target)}'; "
            f"$shortcut.Arguments = '{_ps_escape(arguments)}'; "
            f"$shortcut.WorkingDirectory = '{_ps_escape(working_directory)}'; "
            f"$shortcut.IconLocation = '{_ps_escape(icon_path)}'; "
            "$shortcut.Save()"
        )

        subprocess.run(  # nosec B603, B607  # NOSONAR
            ["powershell", "-NoProfile", "-NonInteractive", "-Command", ps_script],
            capture_output=True,
            text=True,
            check=True,
        )
        return target_path

    def execute_command(self, cmd_name: str, directory: str) -> None:
        """
        Execute a command in the specified directory.
        """
        cmd = self._commands.get(cmd_name)
        if cmd is None:
            cmd = settings.load_command(cmd_name)
        command = cmd['command'].replace('{directory}', directory)
        parameters = cmd['parameters'].replace('{directory}', directory)
        executecmd = command + ' ' + parameters

        env = os.environ.copy()

        if cmd['use_env']:
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                if '=' in customenv:
                    key, value = customenv.split('=', 1)
                    env[key] = value

        if cmd['confirmation']:
            reply = self._show_message_box(
                QMessageBox.Question,
                'Confirmation',
                f'Execute command: {executecmd}',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No,
            )
            if reply == QMessageBox.No:
                return

        if not self._is_command_available(command):
            self._show_message_box(
                QMessageBox.Critical,
                'Command not found',
                f'Unable to find command:\n{command}\n\nPlease update your configuration.',
                QMessageBox.Ok,
            )
            return

        # We need shell=True, to be able run everything!
        try:
            subprocess.Popen(executecmd, cwd=directory, env=env, shell=True)  # nosec B602  # NOSONAR
        except OSError as exc:
            self._show_message_box(QMessageBox.Critical, 'Command error', f'Failed to start command:\n{exc}', QMessageBox.Ok)

    def _show_message_box(
        self,
        icon: QMessageBox.Icon,
        title: str,
        text: str,
        buttons: QMessageBox.StandardButtons,
        default_button: QMessageBox.StandardButton = QMessageBox.NoButton,
    ) -> int:
        parent = self if self.isVisible() and not self.isMinimized() else None
        message_box = QMessageBox(parent)
        message_box.setIcon(icon)
        message_box.setWindowTitle(title)
        message_box.setText(text)
        message_box.setStandardButtons(buttons)
        if default_button != QMessageBox.NoButton:
            message_box.setDefaultButton(default_button)

        if parent is None:
            message_box.setWindowModality(Qt.ApplicationModal)
            message_box.adjustSize()
            screen = QApplication.screenAt(QCursor.pos()) or QApplication.primaryScreen()
            if screen is not None:
                geometry = screen.availableGeometry()
                frame = message_box.frameGeometry()
                frame.moveCenter(geometry.center())
                message_box.move(frame.topLeft())

        return message_box.exec()

    @staticmethod
    def _host_executable_from_command(executable: str) -> str:
        if os.path.isabs(executable):
            return os.path.basename(executable)
        return executable

    @classmethod
    def _is_command_available(cls, command: str) -> bool:
        command = command.strip()
        if not command:
            return False

        if os.name == 'nt':
            shell_builtins = {'cmd', 'powershell', 'pwsh'}
        else:
            shell_builtins = {'cd', 'echo', 'test', 'pwd', 'true', 'false'}

        try:
            parts = shlex.split(command, posix=(os.name != 'nt'))
        except ValueError:
            return True

        if not parts:
            return False

        executable = parts[0]
        if executable.lower() in shell_builtins:
            return True

        if os.path.isabs(executable) or os.path.sep in executable:
            return os.path.isfile(executable)

        return shutil.which(executable) is not None

    def workdirShow(self):
        settings.create_config()
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")
        self._minimize_to_tray = settings.load_minimize_to_tray()

        directories = settings.load_directories()
        self._commands = {f"CMD{i}": settings.load_command(f"CMD{i}") for i in range(1, 7)}
        
        # Clear central widget
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout(widget)
        self.adjustSize()
        
        for row, directory in enumerate(directories):
            # Directory label
            dir_label = QLabel(directory)
            layout.addWidget(dir_label, row, 0)
            
            # Command buttons
            for col in range(1, 7):
                cmd_name = f"CMD{col}"
                cmd = self._commands[cmd_name]
                
                button = QPushButton(cmd['label'])
                button.setToolTip(f"{cmd['command']} {cmd['parameters']}")
                button.setEnabled(cmd['command'] != '')
                button.setStyleSheet(f"color: {cmd['colour']}")
                button.clicked.connect(lambda checked, c=cmd_name, d=directory: self.execute_command(c, d))
                
                layout.addWidget(button, row, col)

            self._update_tray_menu(directories)

    def miFileClose(self):
        self._quit_from_tray()

    def miExtrasConfiguration(self):
        dlg = configuration_ui.DialogConfiguration(self)
        dlg.exec()
        self.workdirShow()

    def miExtrasCreateDesktopLink(self):
        try:
            if sys.platform == 'win32':
                target_path = self._create_windows_desktop_link()
            else:
                target_path = self._create_linux_desktop_link()

            QMessageBox.information(self, 'Desktop link', f'Desktop link created:\n{target_path}')
        except (OSError, subprocess.SubprocessError) as exc:
            QMessageBox.critical(self, 'Desktop link', f'Failed to create desktop link:\n{exc}')

    def miHelpAbout(self):
        dlg = about_ui.DialogAbout(self)
        dlg.exec()

    def miHelpSupport(self):
        webbrowser.open_new_tab('https://github.com/dseichter/Workdir')

    def miHelpUpdate(self):
        if self._update_thread is not None and self._update_thread.isRunning():
            return

        self.update_action.setEnabled(False)
        self._update_thread = QThread(self)
        self._update_worker = UpdateCheckWorker()
        self._update_worker.moveToThread(self._update_thread)

        self._update_thread.started.connect(self._update_worker.run)
        self._update_worker.finished.connect(self._on_update_check_finished)
        self._update_worker.finished.connect(self._update_thread.quit)
        self._update_worker.finished.connect(self._update_worker.deleteLater)
        self._update_thread.finished.connect(self._cleanup_update_thread)
        self._update_thread.finished.connect(self._update_thread.deleteLater)
        self._update_thread.start()

    def workdirClose(self, event) -> None:
        if self._update_thread is not None and self._update_thread.isRunning():
            self._update_thread.quit()
            if not self._update_thread.wait(10000):
                self._update_thread.terminate()
                self._update_thread.wait(1000)

        if self._is_quitting and self._tray_icon is not None:
            self._tray_icon.hide()

        if event is not None:
            event.accept()

    def _on_update_check_finished(self, has_update: bool) -> None:
        if has_update:
            reply = QMessageBox.question(
                self,
                'Update available',
                'A new release is available.\nWould you like to open the download page?',
                QMessageBox.Yes | QMessageBox.No,
            )
            if reply == QMessageBox.Yes:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            QMessageBox.information(self, 'No update', 'No new release available.')

    def _cleanup_update_thread(self) -> None:
        self._update_worker = None
        self._update_thread = None
        self.update_action.setEnabled(True)


def main() -> None:
    """
    Main entry point for the Workdir application.
    """
    app = QApplication(sys.argv)
    window = WorkDirFrame()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()