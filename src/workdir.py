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
import subprocess  # nosec B404
import sys
import webbrowser

from PySide6.QtCore import QObject, QThread, Signal
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
        self.config_action.setIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.support_action.setIcon(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.update_action.setIcon(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.about_action.setIcon(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

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
        subprocess.Popen(executecmd, cwd=directory, env=env, shell=True) # nosec B602

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