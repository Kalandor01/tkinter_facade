"""
This module provides proxies for classes and methods in tkinter.
"""
__version__ = "0.2.1"

import tkinter as tk


if __name__ == "__main__":
    from utils import get_children_recursive
    from base_classes import Misc, BaseWidget, Widget, Tk
    from button import Button, Action_button
else:
    from tkinter_proxy.utils import get_children_recursive
    from tkinter_proxy.base_classes import Misc, BaseWidget, Widget, Tk
    from tkinter_proxy.button import Button, Action_button


if __name__ == "__main__":
    move = False
    size = 3
    
    # window = tk.Tk()
    # window.title("Noughts And Crosses")
    # window.geometry("400x400")

    # v = tk.StringVar()
    # tk.Label(window, textvariable=v,pady=10).pack()
    # v.set("Noughts And Crosses")

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


    def get_config_values(item:tk.Misc):
        for key in item.configure():
            print(end=f"{key}: ")
            value = item.configure(key)
            for i in value:
                if type(i) == str:
                    print(end=f"{i} ")
                else:
                    print(end=f"{type(i)}:{i} ")
            print()


    # draw_board()
    # window.children
    # chch = get_children_recursive(window)
    # for key, val in chch.items():
    #     print(key, val)
    # window.mainloop()

    def test_click(btn:Action_button):
        print("yo:", btn.width)
        print(btn.command)
        btn.command = test_click2
    

    def test_click2(btn:Action_button):
        print("yo2:", btn.height)
        print(btn.command)
    

    window2 = tk.Tk()
    window2.geometry("200x200")

    bt = Button(window2, "lol", 15, 12, test_click)
    print(bt.width)
    bt.width = 150
    print(bt.width)
    print(Button().configure("command"))

    # get_config_values(tk.Widget(window2, "button"))

    # row_frame = tk.Frame(window2)
    # row_frame.pack(side="top")
    # btn = Action_button(window2, "hey", 4646, command=test_click)
    # btn.pack(side="left")

    # window2.mainloop()
