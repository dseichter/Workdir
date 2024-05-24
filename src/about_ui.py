# import the newly created GUI file
import gui

# import workdir specific libraries
import helper
import webbrowser
import icons


class dialogAbout(gui.dialogAbout):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogAbout.__init__(self, parent)

        self.staticTextName.SetLabelText(helper.NAME + ' ' + helper.VERSION)
        self.staticTextLicence.SetLabelText(self.staticTextLicence.GetLabelText() + ' ' + helper.LICENCE)

        # specify all the icons
        gui.dialogAbout.SetIcon(self, icons.info.GetIcon())
        self.bitmapLogo.SetBitmap(icons.opened_folder.GetBitmap())
        self.Fit()

    def openGithub(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/Workdir')  # Add the URL of the GitHub repository

    def openIcons8(self, event):
        webbrowser.open_new_tab('https://icons8.com/')
