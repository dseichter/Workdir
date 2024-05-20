# importing wx files
import wx
# import the newly created GUI file
import gui

# import workdir specific libraries
import settings

class dialogConfiguration(gui.dialogConfiguration):
    # constructor
    def __init__(self, parent):
        # initialize parent class
        gui.dialogConfiguration.__init__(self, parent)
        
    def configurationShow(self, event):
       
        # load the configuration
        directories = settings.load_directories()
        if directories is not None:
            # parse arra of strings into a single string
            directories = '\n'.join(directories)
            self.textCtrlDirectories.SetValue(directories)

        # load the environment variables
        env = settings.load_env_vars()
        if env is not None:
            env = '\n'.join(env)
            self.textCtrlEnvVars.SetValue(env)    
            
        # load the commands
        cmd1 = settings.load_command('CMD1')
        if cmd1 is not None:
            self.textCtrlLabelCMD1.SetValue(cmd1['label'])
            self.textCtrlCommandCMD1.SetValue(cmd1['command'])
            self.textCtrlParameterCMD1.SetValue(cmd1['parameters'])
            self.checkBoxConfirmCMD1.SetValue(cmd1['use_env'])
            self.checkBoxEnvVarCMD1.SetValue(cmd1['confirmation'])
            self.colourPickerCMD1.SetColour(cmd1['colour'])
            
        cmd2 = settings.load_command('CMD2')
        if cmd2 is not None:
            self.textCtrlLabelCMD2.SetValue(cmd2['label'])
            self.textCtrlCommandCMD2.SetValue(cmd2['command'])
            self.textCtrlParameterCMD2.SetValue(cmd2['parameters'])
            self.checkBoxConfirmCMD2.SetValue(cmd2['use_env'])
            self.checkBoxEnvVarCMD2.SetValue(cmd2['confirmation'])
            self.colourPickerCMD2.SetColour(cmd2['colour'])
            
        cmd3 = settings.load_command('CMD3')
        if cmd3 is not None:
            self.textCtrlLabelCMD3.SetValue(cmd3['label'])
            self.textCtrlCommandCMD3.SetValue(cmd3['command'])
            self.textCtrlParameterCMD3.SetValue(cmd3['parameters'])
            self.checkBoxConfirmCMD3.SetValue(cmd3['use_env'])
            self.checkBoxEnvVarCMD3.SetValue(cmd3['confirmation'])
            self.colourPickerCMD3.SetColour(cmd3['colour'])
            
        cmd4 = settings.load_command('CMD4')
        if cmd4 is not None:
            self.textCtrlLabelCMD4.SetValue(cmd4['label'])
            self.textCtrlCommandCMD4.SetValue(cmd4['command'])
            self.textCtrlParameterCMD4.SetValue(cmd4['parameters'])
            self.checkBoxConfirmCMD4.SetValue(cmd4['use_env'])
            self.checkBoxEnvVarCMD4.SetValue(cmd4['confirmation'])
            self.colourPickerCMD4.SetColour(cmd4['colour'])
            
        cmd5 = settings.load_command('CMD5')
        if cmd5 is not None:
            self.textCtrlLabelCMD5.SetValue(cmd5['label'])
            self.textCtrlCommandCMD5.SetValue(cmd5['command'])
            self.textCtrlParameterCMD5.SetValue(cmd5['parameters'])
            self.checkBoxConfirmCMD5.SetValue(cmd5['use_env'])
            self.checkBoxEnvVarCMD5.SetValue(cmd5['confirmation'])
            self.colourPickerCMD5.SetColour(cmd5['colour'])
            
        cmd6 = settings.load_command('CMD6')
        if cmd6 is not None:
            self.textCtrlLabelCMD6.SetValue(cmd6['label'])
            self.textCtrlCommandCMD6.SetValue(cmd6['command'])
            self.textCtrlParameterCMD6.SetValue(cmd6['parameters'])
            self.checkBoxConfirmCMD6.SetValue(cmd6['use_env'])
            self.checkBoxEnvVarCMD6.SetValue(cmd6['confirmation'])
            self.colourPickerCMD6.SetColour(cmd6['colour'])
            

    def configurationSave(self, event):
        # save the configuration
        directories = {}
        
        # save textCtrlDirectories into array of strings
        directories = self.textCtrlDirectories.GetValue().split('\n')
        settings.save_directories(directories)
        
        env = {}
        env = self.textCtrlEnvVars.GetValue().split('\n')
        settings.save_env_vars(env)
        
        cmd1 = {}
        cmd1['label'] = self.textCtrlLabelCMD1.GetValue()
        cmd1['command'] = self.textCtrlCommandCMD1.GetValue()
        cmd1['parameters'] = self.textCtrlParameterCMD1.GetValue()
        cmd1['use_env'] = self.checkBoxConfirmCMD1.GetValue()
        cmd1['confirmation'] = self.checkBoxEnvVarCMD1.GetValue()
        cmd1['colour'] = self.colourPickerCMD1.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD1', cmd1)
        
        cmd2 = {}
        cmd2['label'] = self.textCtrlLabelCMD2.GetValue()
        cmd2['command'] = self.textCtrlCommandCMD2.GetValue()
        cmd2['parameters'] = self.textCtrlParameterCMD2.GetValue()
        cmd2['use_env'] = self.checkBoxConfirmCMD2.GetValue()
        cmd2['confirmation'] = self.checkBoxEnvVarCMD2.GetValue()
        cmd2['colour'] = self.colourPickerCMD2.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD2', cmd2)
        
        cmd3 = {}
        cmd3['label'] = self.textCtrlLabelCMD3.GetValue()
        cmd3['command'] = self.textCtrlCommandCMD3.GetValue()
        cmd3['parameters'] = self.textCtrlParameterCMD3.GetValue()
        cmd3['use_env'] = self.checkBoxConfirmCMD3.GetValue()
        cmd3['confirmation'] = self.checkBoxEnvVarCMD3.GetValue()
        cmd3['colour'] = self.colourPickerCMD3.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD3', cmd3)
        
        cmd4 = {}
        cmd4['label'] = self.textCtrlLabelCMD4.GetValue()
        cmd4['command'] = self.textCtrlCommandCMD4.GetValue()
        cmd4['parameters'] = self.textCtrlParameterCMD4.GetValue()
        cmd4['use_env'] = self.checkBoxConfirmCMD4.GetValue()
        cmd4['confirmation'] = self.checkBoxEnvVarCMD4.GetValue()
        cmd4['colour'] = self.colourPickerCMD4.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD4', cmd4)
        
        cmd5 = {}
        cmd5['label'] = self.textCtrlLabelCMD5.GetValue()
        cmd5['command'] = self.textCtrlCommandCMD5.GetValue()
        cmd5['parameters'] = self.textCtrlParameterCMD5.GetValue()
        cmd5['use_env'] = self.checkBoxConfirmCMD5.GetValue()
        cmd5['confirmation'] = self.checkBoxEnvVarCMD5.GetValue()
        cmd5['colour'] = self.colourPickerCMD5.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD5', cmd5)
        
        cmd6 = {}
        cmd6['label'] = self.textCtrlLabelCMD6.GetValue()
        cmd6['command'] = self.textCtrlCommandCMD6.GetValue()
        cmd6['parameters'] = self.textCtrlParameterCMD6.GetValue()
        cmd6['use_env'] = self.checkBoxConfirmCMD6.GetValue()
        cmd6['confirmation'] = self.checkBoxEnvVarCMD6.GetValue()
        cmd6['colour'] = self.colourPickerCMD6.GetColour().GetAsString(wx.C2S_HTML_SYNTAX)
        settings.save_command('CMD6', cmd6)
