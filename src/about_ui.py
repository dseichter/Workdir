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

import webbrowser

import gui
import helper
import icons


GITHUB_URL = "https://github.com/dseichter/Workdir"
LOGO_ICON_NAME = "folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48"
LOGO_SIZE = 48


class DialogAbout(gui.DialogAbout):
    def __init__(self, parent: object = None) -> None:
        """Initialize the About dialog."""
        super().__init__(parent)

        self._set_texts()
        self._set_icons()

    def _set_texts(self) -> None:
        """Set dialog texts based on current application metadata."""
        self.name_label.setText(f"{helper.NAME} {helper.VERSION}")
        self.licence_label.setText(f"Licenced under {helper.LICENCE}")

    def _set_icons(self) -> None:
        """Set window and logo icons for the about dialog."""
        logo_icon = icons.get_icon(LOGO_ICON_NAME)
        self.setWindowIcon(logo_icon)

        pixmap = logo_icon.pixmap(LOGO_SIZE, LOGO_SIZE)
        self.logo_label.setPixmap(pixmap)

    def openGithub(self, event: object) -> None:
        """Open the GitHub page for Workdir."""
        webbrowser.open_new_tab(GITHUB_URL)
