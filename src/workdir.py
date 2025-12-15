# Copyright (c) 2024 Daniel Seichter
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon
import webbrowser
import subprocess
import os

import gui
import settings
import configuration_ui
import about_ui
import helper
import icons


class WorkDirFrame(gui.MainFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set icons
        self.setWindowIcon(icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48'))
        self.close_action.setIcon(icons.get_icon('logout_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.config_action.setIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.support_action.setIcon(icons.get_icon('globe_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.update_action.setIcon(icons.get_icon('update_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))
        self.about_action.setIcon(icons.get_icon('info_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

    def execute_command(self, cmd_name, directory):
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
        
        subprocess.Popen(executecmd, cwd=directory, env=env, shell=True)

    def workdirShow(self):
        settings.create_config()
        self.setWindowTitle(f"{helper.NAME} {helper.VERSION}")
        
        directories = settings.load_directories()
        
        # Clear central widget
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QGridLayout(widget)
        
        for row, directory in enumerate(directories):
            # Directory label
            dir_label = QLabel(directory)
            layout.addWidget(dir_label, row, 0)
            
            # Command buttons
            for col in range(1, 7):
                cmd_name = f"CMD{col}"
                cmd = settings.load_command(cmd_name)
                
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
        if helper.check_for_new_release():
            reply = QMessageBox.question(self, 'Update available',
                                       'A new release is available.\nWould you like to open the download page?',
                                       QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            QMessageBox.information(self, 'No update', 'No new release available.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = WorkDirFrame()
    frame.show()
    sys.exit(app.exec())