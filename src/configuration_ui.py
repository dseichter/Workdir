# Copyright (c) 2024 Daniel Seichter

from PySide6.QtWidgets import QColorDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import gui
import settings
import icons


class DialogConfiguration(gui.DialogConfiguration):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

    def configurationShow(self):
        # Load directories
        directories = settings.load_directories()
        if directories:
            self.directories_text.setPlainText('\n'.join(directories))

        # Load environment variables
        env = settings.load_env_vars()
        if env:
            self.env_vars_text.setPlainText('\n'.join(env))

        # Load commands
        for i in range(1, 7):
            cmd_name = f"CMD{i}"
            cmd = settings.load_command(cmd_name)
            if cmd:
                controls = self.cmd_controls[cmd_name]
                controls['label'].setText(cmd['label'])
                controls['command'].setText(cmd['command'])
                controls['parameters'].setText(cmd['parameters'])
                controls['use_env'].setChecked(cmd['use_env'])
                controls['confirmation'].setChecked(cmd['confirmation'])
                controls['color_value'] = cmd['colour']
                controls['color'].setStyleSheet(f"background-color: {cmd['colour']}")

    def configurationSave(self):
        # Save directories
        directories = self.directories_text.toPlainText().split('\n')
        directories = [d for d in directories if d.strip()]
        settings.save_directories(directories)

        # Save environment variables
        env = self.env_vars_text.toPlainText().split('\n')
        env = [e for e in env if e.strip()]
        settings.save_env_vars(env)

        # Save commands
        for i in range(1, 7):
            cmd_name = f"CMD{i}"
            controls = self.cmd_controls[cmd_name]
            
            cmd = {
                'label': controls['label'].text(),
                'command': controls['command'].text(),
                'parameters': controls['parameters'].text(),
                'use_env': controls['use_env'].isChecked(),
                'confirmation': controls['confirmation'].isChecked(),
                'colour': controls['color_value']
            }
            settings.save_command(cmd_name, cmd)

        self.accept()