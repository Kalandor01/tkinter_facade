"""
This module provides proxies for classes and methods in tkinter.
"""
__version__ = "0.1.1"

import tkinter as tk

if __name__ == "__main__":
    pass
else:
    pass


def get_children_recursive(widget:tk.Misc, previous_widget_name:str|None=None):
    children:dict[str, tk.Widget] = {}
    ch = widget.children
    if len(ch) > 0:
        for key, chi in ch.items():
            ch_widget_name = None
            if previous_widget_name is not None:
                ch_widget_name = f"{previous_widget_name}.{key}"
                children[ch_widget_name] = chi
            else:
                children[key] = chi
                ch_widget_name = key
            children.update(get_children_recursive(chi, ch_widget_name))
    return children


if __name__ == "__main__":
    move = False
    size = 3
    
    window = tk.Tk()
    window.title("Noughts And Crosses")
    window.geometry("400x400")

    v = tk.StringVar()
    tk.Label(window, textvariable=v,pady=10).pack()
    v.set("Noughts And Crosses")

    buttons:list[tk.Button] = []

    def draw_board():
        row_frame = tk.Frame(window)
        row_frame.pack(side="top")
        for x in range(size**2):
            if x % size == 0:
                row_frame = tk.Frame(window)
                row_frame.pack(side="top")
            btn = tk.Button(row_frame, width=5, text="", relief=tk.GROOVE)
            btn.config(command=lambda btn=btn, x=x: click_button(btn, x))
            btn.pack(side="left")


    def click_button(button:tk.Button, x:int):
        global move
        # button.destroy()
        if button.config()["text"][4] == "":
            button.config(text=("X" if move else "O"))
            move = not move
            print(x)


    draw_board()
    window.children
    chch = get_children_recursive(window)
    for key, val in chch.items():
        print(key, val)
    window.mainloop()
