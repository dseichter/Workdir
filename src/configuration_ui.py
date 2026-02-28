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

import gui
import settings
import icons


class DialogConfiguration(gui.DialogConfiguration):
    def __init__(self, parent: object = None) -> None:
        """
        Initialize the Configuration dialog.
        """
        super().__init__(parent)
        self.setWindowIcon(icons.get_icon('settings_24dp_8B1A10_FILL0_wght400_GRAD0_opsz24'))

    def configurationShow(self) -> None:
        """
        Load and display configuration settings in the dialog.
        """
        directories = settings.load_directories()
        if directories:
            self.directories_text.setPlainText('\n'.join(directories))

        env = settings.load_env_vars()
        if env:
            self.env_vars_text.setPlainText('\n'.join(env))

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

    def configurationSave(self) -> None:
        """
        Save configuration settings from the dialog.
        """
        directories = self.directories_text.toPlainText().split('\n')
        directories = [d for d in directories if d.strip()]
        settings.save_directories(directories)

        env = self.env_vars_text.toPlainText().split('\n')
        env = [e for e in env if e.strip()]
        settings.save_env_vars(env)

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