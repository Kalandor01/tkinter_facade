import tkinter as tk

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