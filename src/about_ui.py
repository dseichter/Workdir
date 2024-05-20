# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings

class dialogAbout(gui.dialogAbout):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogAbout.__init__(self, parent)