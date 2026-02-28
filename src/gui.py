# -*- coding: utf-8 -*-

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


from PySide6.QtWidgets import QMainWindow, QWidget, QDialog, QColorDialog, QVBoxLayout, QGridLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QTextEdit, QDialogButtonBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QColor

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Workdir")
        self.resize(660, 387)
        
        # Create menu bar
        self.menu_bar = self.menuBar()
        
        # File menu
        self.file_menu = self.menu_bar.addMenu("File")
        self.close_action = QAction("Close", self)
        self.close_action.triggered.connect(self.miFileClose)
        self.file_menu.addAction(self.close_action)
        
        # Extras menu
        self.extras_menu = self.menu_bar.addMenu("Extras")
        self.config_action = QAction("Configuration", self)
        self.config_action.triggered.connect(self.miExtrasConfiguration)
        self.extras_menu.addAction(self.config_action)
        
        # Help menu
        self.help_menu = self.menu_bar.addMenu("Help")
        self.support_action = QAction("Support...", self)
        self.support_action.triggered.connect(self.miHelpSupport)
        self.help_menu.addAction(self.support_action)
        
        self.update_action = QAction("Check for updates", self)
        self.update_action.triggered.connect(self.miHelpUpdate)
        self.help_menu.addAction(self.update_action)
        
        self.about_action = QAction("About...", self)
        self.about_action.triggered.connect(self.miHelpAbout)
        self.help_menu.addAction(self.about_action)
        
        # Central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Connect events
        self.workdirShow()

    def closeEvent(self, event):
        self.workdirClose(event)

    # Virtual event handlers, override them in your derived class
    def workdirClose(self, event):
        if event is not None:
            event.accept()

    def workdirShow(self):
        raise NotImplementedError("Derived class must implement workdirShow().")

    def miFileClose(self):
        raise NotImplementedError("Derived class must implement miFileClose().")

    def miExtrasConfiguration(self):
        raise NotImplementedError("Derived class must implement miExtrasConfiguration().")

    def miHelpSupport(self):
        raise NotImplementedError("Derived class must implement miHelpSupport().")

    def miHelpUpdate(self):
        raise NotImplementedError("Derived class must implement miHelpUpdate().")

    def miHelpAbout(self):
        raise NotImplementedError("Derived class must implement miHelpAbout().")


###########################################################################
## Class DialogConfiguration
###########################################################################

class DialogConfiguration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Configuration")
        self.resize(901, 546)
        
        layout = QVBoxLayout(self)
        
        # Commands panel
        commands_widget = QWidget()
        commands_layout = QGridLayout(commands_widget)
        
        # Headers
        commands_layout.addWidget(QLabel(""), 0, 0)
        commands_layout.addWidget(QLabel("Label"), 0, 1)
        commands_layout.addWidget(QLabel("Command"), 0, 2)
        commands_layout.addWidget(QLabel("Parameter"), 0, 3)
        commands_layout.addWidget(QLabel("Confirmation?"), 0, 4)
        commands_layout.addWidget(QLabel("Env Var?"), 0, 5)
        commands_layout.addWidget(QLabel("Font color"), 0, 6)
        
        # CMD1-6 rows
        self.cmd_controls = {}
        for i in range(1, 7):
            row = i
            cmd_name = f"CMD{i}"
            
            commands_layout.addWidget(QLabel(cmd_name), row, 0)
            
            label_edit = QLineEdit()
            command_edit = QLineEdit()
            param_edit = QLineEdit()
            confirm_check = QCheckBox()
            env_check = QCheckBox()
            color_button = QPushButton()
            color_button.setStyleSheet("background-color: black")
            
            commands_layout.addWidget(label_edit, row, 1)
            commands_layout.addWidget(command_edit, row, 2)
            commands_layout.addWidget(param_edit, row, 3)
            commands_layout.addWidget(confirm_check, row, 4)
            commands_layout.addWidget(env_check, row, 5)
            commands_layout.addWidget(color_button, row, 6)
            
            self.cmd_controls[cmd_name] = {
                'label': label_edit,
                'command': command_edit,
                'parameters': param_edit,
                'confirmation': confirm_check,
                'use_env': env_check,
                'color': color_button,
                'color_value': '#000000'
            }
            
            # Connect color button using signal/slot
            color_button.clicked.connect(self._make_color_slot(cmd_name))

        layout.addWidget(commands_widget)

        # Directories and Environment Variables panel
        dirs_env_widget = QWidget()
        dirs_env_layout = QGridLayout(dirs_env_widget)

        dirs_env_layout.addWidget(QLabel("Directories"), 0, 0)
        dirs_env_layout.addWidget(QLabel("Environment Variables"), 0, 1)

        self.directories_text = QTextEdit()
        self.env_vars_text = QTextEdit()

        dirs_env_layout.addWidget(self.directories_text, 1, 0)
        dirs_env_layout.addWidget(self.env_vars_text, 1, 1)

        dirs_env_layout.addWidget(QLabel("Add one directory each line. If a directory is not available, no commands will be enabled."), 2, 0)
        dirs_env_layout.addWidget(QLabel("Add one Key/Pair (Key=Value) in each line to provide as environment variable."), 2, 1)

        layout.addWidget(dirs_env_widget)

        # Buttons
        button_box = QDialogButtonBox(QDialogButtonBox.Save | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.configurationSave)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

        # Show configuration
        self.configurationShow()

    def _make_color_slot(self, cmd_name: str):
        def slot():
            self.choose_color(cmd_name)
        return slot
    
    def choose_color(self, cmd_name):
        color = QColorDialog.getColor(QColor(self.cmd_controls[cmd_name]['color_value']), self)
        if color.isValid():
            self.cmd_controls[cmd_name]['color_value'] = color.name()
            self.cmd_controls[cmd_name]['color'].setStyleSheet(f"background-color: {color.name()}")

    # Virtual event handlers, override them in your derived class
    def configurationShow(self):
        raise NotImplementedError("Derived class must implement configurationShow().")

    def configurationSave(self):
        raise NotImplementedError("Derived class must implement configurationSave().")


###########################################################################
## Class DialogAbout
###########################################################################

class DialogAbout(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Workdir")
        
        layout = QVBoxLayout(self)
        
        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo_label)
        
        self.name_label = QLabel("MyLabel")
        self.name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.name_label)
        
        self.licence_label = QLabel("Licenced under")
        self.licence_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.licence_label)
        
        self.github_label = QLabel("More on GitHub")
        self.github_label.setAlignment(Qt.AlignCenter)
        self.github_label.setStyleSheet("color: blue; text-decoration: underline;")
        self.github_label.mousePressEvent = self.openGithub
        layout.addWidget(self.github_label)
        
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        layout.addWidget(button_box)

    # Virtual event handlers, override them in your derived class
    def openGithub(self, event):
        raise NotImplementedError("Derived class must implement openGithub().")
