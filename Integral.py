import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from Parser.ParserWyrazen import ParserWyrazen
from Layout import *

try:
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
    formula = inputBlock(formula_frame, 0, 1, 16)
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
    bars_label = textBlock(bars, 0, 0, "Liczba słupków [1,100]:")
    bars_count = inputBlock(bars, 0, 1, 6)
    bars.pack(pady = (0,5))

    submit = tk.Button(inputs, text="GENERUJ", command=lambda:integral_figure(float(domain_x_min.get()), float(domain_x_max.get()), float(domain_y_min.get()), float(domain_y_max.get()), formula.get(), int(bars_count.get()), "normal"))
    submit.pack()

    interactive = tk.Button(inputs, text="INTERAKTYWNIE", command=lambda:integral_figure(float(domain_x_min.get()), float(domain_x_max.get()), float(domain_y_min.get()), float(domain_y_max.get()), formula.get(), int(bars_count.get()), "interactive"))
    interactive.pack()

    plot = tk.LabelFrame(window, text="Wykres funkcji")
    plot.grid(row=0, column=1)
    canvas = FigureCanvasTkAgg(fig, master=plot)
    canvas.draw()
    canvas.get_tk_widget().pack()
except Exception as e:
    tk.messagebox.showwarning(title="Wystąpił błąd", message="Wystąpił nieoczekiwany błąd programu")
    print(e)

def calculate_integral(x_min, x_max, y_min, y_max, formula_string, bars_count):
    width = (x_max - x_min) / bars_count
    depth = (y_max - y_min) / bars_count
    _x = [x_min + depth*i for i in range(bars_count)]
    _y = [y_min + depth*i for i in range(bars_count)]
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()

    operation = parser.parsuj(formula_string)

    tk.messagebox.showinfo(title="Parser", message="Wprowadzono funkcję F(x,y) = " + str(operation))

    top = [operation.wykonaj(a[0], a[1]) for a in zip(x,y)]
    bottom = np.zeros_like(top)

    return [x, y, bottom, width, depth, top]

def integral_figure(x_min, x_max, y_min, y_max, formula_string, bars_count, type):
    try:
        if x_max < x_min or y_max<y_min:
            raise Exception("Podana dziedzina funkcji jest błędna")
        if bars_count < 1 or bars_count > 100:
            raise Exception("Podano błędną liczbę słupków. Podaj wartość pomiędzy 1 i 100")
        data = calculate_integral(x_min, x_max, y_min, y_max, formula_string, bars_count)
        
        colormat = ['g' if a>0 else 'r' for a in data[5]]

        if(type=="normal"):
            ax1.clear()
            global canvas
            ax1.bar3d(*data, shade=True, color=colormat)
            plot.winfo_children()[0].destroy()
            canvas = FigureCanvasTkAgg(fig, master=plot)
            canvas.draw()
            canvas.get_tk_widget().pack()
        else:
            interactive_figure = plt.figure(figsize=(12,8))
            interactive_figure_ax1 = interactive_figure.add_subplot(111, projection='3d')
            interactive_figure_ax1.bar3d(*data, shade=True, color=colormat)
            interactive_figure.show()
    except ValueError:
        tk.messagebox.showwarning(title="Wystąpił błąd", message="Dla niektórych argumentów podanej dzidziny nie można obliczyć wartości funkcji")
    except Exception as e:
        tk.messagebox.showwarning(title="Wystąpił błąd", message=e)

tk.mainloop()
