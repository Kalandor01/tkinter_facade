"""
This module provides proxies for classes and methods in tkinter.
"""
__version__ = "0.1"

import tkinter as tk

if __name__ == "__main__":
    pass
else:
    pass


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Noughts And Crosses")
    window.geometry("400x400")

    v = tk.StringVar()
    tk.Label(window, textvariable=v,pady=10).pack()
    v.set("Noughts And Crosses")

    buttons:list[tk.Button] = []

    def DrawBoard():
        for x in range(3*3):
            if x % 3 == 0:
                row_frame = tk.Frame(window)
                row_frame.pack(side="top")
            btn = tk.Button(row_frame, text="-", relief=tk.GROOVE, width=2, command = lambda: click_button(x))
            btn.pack(side="left")
            buttons.append(btn)


    def click_button(button_index:int):
        buttons[button_index]["text"] = "X"
        # btn.destroy()
        # DrawBoard()


    DrawBoard()
    window.mainloop()
