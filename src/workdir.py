# Copyright (c) 2024 Daniel Seichter
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

# importing wx files
import wx
# import the newly created GUI file
import gui
# import common libraries
import webbrowser
import subprocess
import os
# import workdir specific libraries
import settings
import configuration_ui
import about_ui
import helper
import icons


class WorkDirFrame(gui.MainFrame):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.MainFrame.__init__(self, parent)

        # specify all the icons
        gui.MainFrame.SetIcon(self, icons.opened_folder.GetIcon())
        self.menuitemFileClose.SetBitmap(icons.cancel.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemExtrasConfiguration.SetBitmap(icons.settings.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpSupport.SetBitmap(icons.get_help.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpUpdate.SetBitmap(icons.restart.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())
        self.menuitemHelpAbout.SetBitmap(icons.info.GetBitmap().ConvertToImage().Rescale(16, 16).ConvertToBitmap())

    def newbuttonCMD1Click(self, event, dir=None):
        cmd = settings.load_command('CMD1')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return
        subprocess.Popen(executecmd, cwd=dir, env=env)

    def newbuttonCMD2Click(self, event, dir=None):
        cmd = settings.load_command('CMD2')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return

        subprocess.Popen(executecmd, cwd=dir, env=env)

    def newbuttonCMD3Click(self, event, dir=None):
        cmd = settings.load_command('CMD3')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return

        subprocess.Popen(executecmd, cwd=dir, env=env)

    def newbuttonCMD4Click(self, event, dir=None):
        cmd = settings.load_command('CMD4')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return

        subprocess.Popen(executecmd, cwd=dir, env=env)

    def newbuttonCMD5Click(self, event, dir=None):
        cmd = settings.load_command('CMD5')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return

        subprocess.Popen(executecmd, cwd=dir, env=env)

    def newbuttonCMD6Click(self, event, dir=None):
        cmd = settings.load_command('CMD6')
        command = cmd['command'].replace('{directory}', dir)
        parameters = cmd['parameters'].replace('{directory}', dir)
        executecmd = command + ' ' + parameters
        env = os.environ.copy()
        if cmd['use_env']:
            # extend the environment with the additional environment variables
            additionalenv = settings.load_env_vars()
            for customenv in additionalenv:
                key = customenv.split('=')[0]
                value = customenv.split('=')[1]
                env[key] = value

        if cmd['confirmation']:
            dlg = wx.MessageDialog(self, 'Execute command: ' + executecmd, 'Confirmation', wx.YES_NO | wx.ICON_QUESTION)
            result = dlg.ShowModal()
            if result == wx.ID_NO:
                return

        subprocess.Popen(executecmd, cwd=dir, env=env)

    def workdirShow(self, event):
        # check if config.json exists, if not create it, if available, update it
        settings.create_config()

        # add the version to the label
        self.SetTitle(helper.NAME + ' ' + helper.VERSION)

        directories = settings.load_directories()

        fgSizerMain = wx.FlexGridSizer(0, 1, 0, 0)
        fgSizerMain.SetFlexibleDirection(wx.BOTH)
        fgSizerMain.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # add a panel so it looks the correct on all platforms
        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizerMain.Add(self.panel, 1, wx.EXPAND | wx.ALL, 5)

        # add a sizer to the panel
        fgSizerDirectory = wx.FlexGridSizer(0, 7, 0, 0)
        fgSizerDirectory.SetFlexibleDirection(wx.BOTH)
        fgSizerDirectory.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        # add the sizer to the panel
        self.panel.SetSizer(fgSizerDirectory)
        self.panel.Layout()
        fgSizerDirectory.Fit(self.panel)

        for directory in directories:
            directoryname = wx.StaticText(self.panel, wx.ID_ANY, directory, wx.DefaultPosition, wx.DefaultSize, 0)
            directoryname.Wrap(-1)
            fgSizerDirectory.Add(directoryname, 1, wx.ALL | wx.EXPAND, 5)

            cmd = settings.load_command('CMD1')
            newbuttonCMD1 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD1.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD1.Enable(cmd['command'] != '')
            newbuttonCMD1.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD1.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD1Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD1, 0, wx.ALL, 5)

            cmd = settings.load_command('CMD2')
            newbuttonCMD2 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD2.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD2.Enable(cmd['command'] != '')
            newbuttonCMD2.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD2.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD2Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD2, 0, wx.ALL, 5)

            cmd = settings.load_command('CMD3')
            newbuttonCMD3 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD3.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD3.Enable(cmd['command'] != '')
            newbuttonCMD3.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD3.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD3Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD3, 0, wx.ALL, 5)

            cmd = settings.load_command('CMD4')
            newbuttonCMD4 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD4.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD4.Enable(cmd['command'] != '')
            newbuttonCMD4.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD4.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD4Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD4, 0, wx.ALL, 5)

            cmd = settings.load_command('CMD5')
            newbuttonCMD5 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD5.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD5.Enable(cmd['command'] != '')
            newbuttonCMD5.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD5.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD5Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD5, 0, wx.ALL, 5)

            cmd = settings.load_command('CMD6')
            newbuttonCMD6 = wx.Button(self.panel, wx.ID_ANY, cmd['label'], wx.DefaultPosition, wx.DefaultSize, 0)
            newbuttonCMD6.SetToolTip(cmd['command'] + ' ' + cmd['parameters'])
            newbuttonCMD6.Enable(cmd['command'] != '')
            newbuttonCMD6.ForegroundColour = wx.Colour(cmd['colour'])
            newbuttonCMD6.Bind(wx.EVT_BUTTON, lambda event, dir=directory: self.newbuttonCMD6Click(event, dir))
            fgSizerDirectory.Add(newbuttonCMD6, 0, wx.ALL, 5)

        self.SetSizer(fgSizerMain)
        self.Layout()
        self.Fit()

    def miFileClose(self, event):
        self.Close()
        wx.Exit()

    def miExtrasConfiguration(self, event):
        # open the configuration dialog
        dlg = configuration_ui.DialogConfiguration(self)
        dlg.ShowModal()
        dlg.Destroy()
        self.workdirShow(event)

    def miHelpAbout(self, event):
        # open the about dialog
        dlg = about_ui.DialogAbout(self)
        dlg.ShowModal()
        dlg.Destroy()

    def miHelpSupport(self, event):
        webbrowser.open_new_tab('https://github.com/dseichter/Workdir')  # Add the URL of the GitHub repository

    def miHelpUpdate(self, event):
        if helper.check_for_new_release():
            result = wx.MessageBox('A new release is available.\nWould you like to open the download page?', 'Update available', wx.YES_NO | wx.ICON_INFORMATION)
            if result == wx.YES:
                webbrowser.open_new_tab(helper.RELEASES)
        else:
            wx.MessageBox('No new release available.', 'No update', wx.OK | wx.ICON_INFORMATION)


# mandatory in wx, create an app, False stands for not deteriction stdin/stdout
# refer manual for details
app = wx.App(False)

# create an object of CalcFrame
frame = WorkDirFrame(None)

# show the frame
frame.Show(True)

# start the applications
app.MainLoop()
