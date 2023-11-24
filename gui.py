from tkinter import *
from tkinter import ttk

import numpy as np

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

from plot import Plot

from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)  # needed to unblur text

# Config mainframe in root
root = Tk()
root.title("Wavefunction Plots")
mainframe = ttk.Frame(root, padding="12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# generate graph
plot = Plot(Plot.h * np.pi, 1, 2)
graph = plot.graph()

# make widget out of graph
canvas = FigureCanvasTkAgg(graph, master=mainframe)
canvas.draw()
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=0, sticky=(N, W, E, S))

# make n entry field
n_entry = ttk.Entry(mainframe, width=7)
n_entry.grid(column=0, row=1, sticky=(W, E))

# make button to update n
update_n = ttk.Button(mainframe, text='Update', command=lambda: plot.update(nconst=int(n_entry.get())))
update_n.grid(column=1, row=1, sticky=(W, E))

root.mainloop()