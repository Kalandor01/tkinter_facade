import tkinter as tk
from typing import Callable


class Button(tk.Button):
    """
    Proxy class for `tkinter.Button`.
    """
    #TO IMPLEMENT:  activebackground, activeforeground, background, bitmap, borderwidth, cursor, disabledforeground, font, foreground, highlightbackground, highlightcolor
    #               highlightthickness, image, justify, padx, pady, relief, repeatdelay, repeatinterval, takefocus, textvariable, underline, wraplength, compound, default
    #               overrelief, state

    def __init__(self, master:tk.Misc|None=None, text:str|None=None, width:int|None=None, height:int|None=None, command:Callable|None=None):
        super().__init__(master=master)
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if command is not None:
            self.command = command
        if text is not None:
            self.text = text


    def _get_text(self) -> str:
        return self.configure("text")[4]


    def _get_width(self) -> int:
        return self.configure("width")[4]
    

    def _get_height(self) -> int:
        return self.configure("height")[4]
    

    def _get_command(self) -> Callable:
        return self.configure("command")[4]


    def _set_text(self, text:str):
        self.config(text=text)


    def _set_width(self, width:int):
        self.config(width=width)
    

    def _set_height(self, height:int):
        self.config(height=height)
    

    def _set_command(self, command:Callable):
        self.config(command=command)
    

    text:str = property(_get_text, _set_text)
    width:int = property(_get_width, _set_width)
    height:int = property(_get_height, _set_height)
    command:Callable = property(_get_command, _set_command)


class Action_button(Button):
    """
    `Button`, but the first argument of the command function will be the button instance;
    """
    def __init__(self, master:tk.Misc|None=None, text:str|None=None, width:int|None=None, height:int|None=None, command:Callable|None=None):
        self._command:Callable = None
        super().__init__(master, text, width, height, command)
        

    def _get_command(self) -> Callable:
        return self._command
    

    def _set_command(self, command:Callable):
        self._command = command
        self.config(command=lambda btn=self: command(btn))
    

    command:Callable = property(_get_command, _set_command)