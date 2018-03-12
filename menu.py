import os

from gi.repository import Nautilus, GObject

class ColumnExtension(GObject.GObject, Nautilus.MenuProvider):
    def __init__(self):
        pass
    def menu_activate_cb(self, menu, file):
         os.system("variety --next")
	
    def get_background_items(self, window, file):
        item = Nautilus.MenuItem(name='ExampleMenuProvider::Bar', 
                                         label='Next Background', 
                                         tip='Next Variety background',
                                         icon='')
        item.connect('activate', self.menu_activate_cb, file)
        
    		
        return item,
