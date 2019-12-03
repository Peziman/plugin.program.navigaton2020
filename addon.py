import xbmc
import xbmcgui
import xbmcaddon

# Get global paths
addon = xbmcaddon.Addon(id='plugin.program.navigation2020')
addonpath = addon.getAddonInfo('path').decode("utf-8")

#control
BACK_BUTTON  = 1100



class Navigation2020(xbmcgui.WindowXMLDialog):
    def onInit(self):
        Nvigation2020.button_back=self.getControl(BACK_BUTTON)
      
    def onAction(self):
        pass
    
    def onClick(self, controlID):
        
        if controlID == BACK_BUTTON:
            self.close()
           
    def onFocus(self, controlID):
        pass
    
    def onControl(self, controlID):
        pass
    
navigation2020dialog = Navigation2020("navigation2020.xml", addonpath, 'default', '720')

navigation2020dialog.doModal()
del navigation2020dialog
          

