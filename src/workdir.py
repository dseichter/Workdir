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
import subprocess  # nosec B404  # NOSONAR
import sys
import webbrowser
from pathlib import Path

from PySide6.QtCore import QObject, QStandardPaths, QThread, Signal
from PySide6.QtWidgets import QApplication, QGridLayout, QLabel, QMessageBox, QPushButton, QWidget

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
        super().__init__(parent)
        self._commands: dict[str, dict] = {}
        self._update_thread: QThread | None = None
        self._update_worker: UpdateCheckWorker | None = None
        # Set icons
        self.setWindowIcon(icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48'))
        self.close_action.setIcon(icons.get_icon('logout_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.desktop_link_action.setIcon(icons.get_icon('folder_open_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.config_action.setIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.support_action.setIcon(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.update_action.setIcon(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.about_action.setIcon(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

    @staticmethod
    def _get_desktop_directory_linux() -> Path:
        desktop_dir = Path.home() / "Desktop"
        try:
            result = subprocess.run(
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
            result = subprocess.run(
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

        subprocess.run(
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
            reply = QMessageBox.question(self, 'Confirmation', f'Execute command: {executecmd}',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.No:
                return

        # We need shell=True, to be able run everything!
        subprocess.Popen(executecmd, cwd=directory, env=env, shell=True)  # nosec B602  # NOSONAR

    def workdirShow(self):
        settings.create_config()
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")

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

    def miFileClose(self):
        self.close()
        QApplication.quit()

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