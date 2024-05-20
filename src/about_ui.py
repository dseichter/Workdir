# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings
import helper


class dialogAbout(gui.dialogAbout):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogAbout.__init__(self, parent)

        self.staticTextName.SetLabelText(helper.NAME + ' ' + helper.VERSION)
        self.staticTextLicence.SetLabelText(self.staticTextLicence.GetLabelText() + ' ' + helper.LICENCE)
