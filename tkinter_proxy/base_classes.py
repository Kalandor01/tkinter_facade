import tkinter as tk

class Misc(tk.Misc):
    """
    Internal class.
    """
    #TO IMPLEMENT?: bd, borderwidth, class, menu, relief, screen, use, background, bg, colormap, container, cursor, highlightbackground, highlightcolor, highlightthickness, padx, pady, takefocus, visual


    def _get_width(self) -> int:
        return self.configure("width")[4]
    
    def _set_width(self, width:int):
        self.configure(width=width)
    

    def _get_height(self) -> int:
        return self.configure("height")[4]
    

    def _set_height(self, height:int):
        self.configure(height=height)
    

    width:int = property(_get_width, _set_width)
    height:int = property(_get_height, _set_height)


class BaseWidget(tk.BaseWidget, Misc):
    """Internal class."""
    pass


class Widget(tk.Widget, BaseWidget):
    """Internal class."""
    pass



class Tk(tk.Tk, Misc):
    pass