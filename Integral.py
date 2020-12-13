import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from Parser.ParserWyrazen import ParserWyrazen
from Layout import *

parser = ParserWyrazen()

fig = Figure(figsize=(15, 10))
ax1 = fig.add_subplot(111, projection='3d')

window = tk.Tk()
window.title("Całka - wizualizacja")
# window.attributes('-zoomed', True)
window.columnconfigure(0, minsize=400)

inputs = tk.LabelFrame(window, text="Dane wejściowe", width=300)
inputs.grid(row=0, column=0)

formula_frame = tk.Frame(inputs)
formula_label = textBlock(formula_frame, 0, 0, "F(x,y) = ")
formula = inputBlock(formula_frame, 0, 1, 10)
formula_frame.pack(pady = (0,5))

x_frame = tk.Frame(inputs)
label_domain_x = textBlock(x_frame, 0, 0, "Dziedzina X:")
domain_x_min = inputBlock(x_frame, 0, 1)
label_domain_x_sep = textBlock(x_frame, 0, 2, " - ")
domain_x_max = inputBlock(x_frame, 0, 3)
x_frame.pack(pady = (0,5))

y_frame = tk.Frame(inputs)
label_domain_y = textBlock(y_frame, 0, 0, "Dziedzina Y:")
domain_y_min = inputBlock(y_frame, 0, 1)
label_domain_y_sep = textBlock(y_frame, 0, 2, " - ")
domain_y_max = inputBlock(y_frame, 0, 3)
y_frame.pack(pady = (0,5))

bars = tk.Frame(inputs)
bars_label = textBlock(bars, 0, 0, "Liczba słupków:")
bars_count = inputBlock(bars, 0, 1, 6)
bars.pack(pady = (0,5))

submit = tk.Button(inputs, text="GENERUJ", command=lambda:integral_figure(int(domain_x_min.get()), int(domain_x_max.get()), int(domain_y_min.get()), int(domain_y_max.get()), formula.get(), int(bars_count.get())))
submit.pack()

plot = tk.LabelFrame(window, text="Wykres funkcji")
plot.grid(row=0, column=1)
canvas = FigureCanvasTkAgg(fig, master=plot)
canvas.draw()
canvas.get_tk_widget().pack()

def integral_figure(x_min, x_max, y_min, y_max, formula_string, bars_count):
    ax1.clear()
    global canvas
    width = depth = (x_max - x_min) / bars_count
    _x = [x_min + depth*i for i in range(bars_count)]
    _y = [y_min + depth*i for i in range(bars_count)]
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    operation = parser.parsuj(formula_string)

    top = [operation.wykonaj(a[0], a[1]) for a in zip(x,y)]
    bottom = np.zeros_like(top)
    colormat = ['g' if a>0 else 'r' for a in top]
    ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color=colormat)
    plot.winfo_children()[0].destroy()
    canvas = FigureCanvasTkAgg(fig, master=plot)
    canvas.draw()
    canvas.get_tk_widget().pack()

tk.mainloop()
