import tkinter as tk
def inputBlock(frame, _row, _column, _width=3):
    input = tk.Entry(frame, width=_width)
    input.grid(row=_row, column=_column)
    return input

def textBlock(frame, _row, _column, _text):
    text = tk.Label(frame, text=_text)
    text.grid(row=_row, column=_column)
    return text
    