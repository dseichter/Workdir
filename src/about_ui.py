# Copyright (c) 2024 Daniel Seichter

import gui
import helper
import webbrowser
import icons


class DialogAbout(gui.DialogAbout):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.name_label.setText(f"{helper.NAME} {helper.VERSION}")
        self.licence_label.setText(f"Licenced under {helper.LICENCE}")
        
        self.setWindowIcon(icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48'))
        pixmap = icons.get_icon('folder_open_48dp_8B1A10_FILL0_wght400_GRAD0_opsz48').pixmap(48, 48)
        self.logo_label.setPixmap(pixmap)

    def openGithub(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/Workdir')
