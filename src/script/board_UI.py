from tkinter import *

#override
class FullScreenApp(object): #borderless fullscreen
    def __init__(self, master, **kwargs):
        self.master=master
        master.overrideredirect(1)
        master.attributes('-topmost',1)
        self._geom='200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth(), master.winfo_screenheight()))
        master.bind('<Escape>',self.toggle_geom)
    def toggle_geom(self,event):
        geom=self.master.winfo_geometry()
        print(geom,self._geom)
        self.master.geometry(self._geom)
        self._geom=geom


#UI_setting
root=Tk()
gameStart=FullScreenApp(root)



















