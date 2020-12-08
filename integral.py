import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

fig = Figure(figsize=(15, 10))
ax1 = fig.add_subplot(111, projection='3d')

window = tk.Tk()
window.title("Całka - wizualizacja")
window.attributes('-zoomed', True)
window.columnconfigure(0, minsize=400)

inputs = tk.LabelFrame(window, text="Dane wejściowe", width=300)
inputs.grid(row=0, column=0)

formula_frame = tk.Frame(inputs)
formula_label = tk.Label(formula_frame, text="F(x,y) = ")
formula_label.grid(row=0, column=0)
formula = tk.Entry(formula_frame, width=10)
formula.grid(row=0, column=1)
formula_frame.pack(pady = (0,5))

x_frame = tk.Frame(inputs)
label_domain_x = tk.Label(x_frame, text="Dziedzina X:")
label_domain_x.grid(row=0, column=0)
domain_x_min = tk.Entry(x_frame, width=3)
domain_x_min.grid(row=0, column=1)
label_domain_x_sep = tk.Label(x_frame, text=" - ")
label_domain_x_sep.grid(row=0, column=2)
domain_x_max = tk.Entry(x_frame, width=3)
domain_x_max.grid(row=0, column=3)
x_frame.pack(pady = (0,5))

y_frame = tk.Frame(inputs)
label_domain_y = tk.Label(y_frame, text="Dziedzina Y:")
label_domain_y.grid(row=0, column=0)
domain_y_min = tk.Entry(y_frame, width=3)
domain_y_min.grid(row=0, column=1)
label_domain_y_sep = tk.Label(y_frame, text=" - ")
label_domain_y_sep.grid(row=0, column=2)
domain_y_max = tk.Entry(y_frame, width=3)
domain_y_max.grid(row=0, column=3)
y_frame.pack(pady = (0,5))

submit = tk.Button(inputs, text="GENERUJ", command=lambda:integral_figure(int(domain_x_min.get()), int(domain_x_max.get()), int(domain_y_min.get()), int(domain_y_max.get()), formula.get()))
submit.pack()

plot = tk.LabelFrame(window, text="Wykres funkcji")
plot.grid(row=0, column=1)
canvas = FigureCanvasTkAgg(fig, master=plot)
canvas.draw()
canvas.get_tk_widget().pack()

def integral_figure(x_min, x_max, y_min, y_max, formula_string):
    global canvas
    _x = list(range(x_min, x_max))
    _y = list(range(y_min, y_max))
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    
    top = [eval(formula_string, {'x': a[0], 'y': a[1]}) for a in zip(x,y)]
    bottom = np.zeros_like(top)
    width = depth = 1
    ax1.bar3d(x, y, bottom, width, depth, top, shade=True, color='green')
    
    plot.winfo_children()[0].destroy()
    canvas = FigureCanvasTkAgg(fig, master=plot)
    canvas.draw()
    canvas.get_tk_widget().pack()

tk.mainloop()
