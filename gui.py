from tkinter import *
from tkinter import ttk
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
from plot import Plot
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)  # needed to unblur text and enlar

# Config mainframe in root
root = Tk()
root.title("Wavefunction Plots")
mainframe = ttk.Frame(root, padding="12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# generate graph
plot = Plot(Plot.h * np.pi, 1, 1)
graph = plot.graph()

# make widget out of graph
canvas = FigureCanvasTkAgg(graph, master=mainframe)
canvas.draw()
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(column=0, row=0, sticky=(N, W, E, S), padx=2, pady=5)

# add info line
n_info = ttk.Label(mainframe,
                   text='The plot above shows the wavefunction and probability distribution for a particle in a 1-D box.')
n_info.grid(column=0, row=1, sticky=(W, E))

# new frame to hold buttons
subframe = ttk.Frame(mainframe, padding="0 12")
subframe.grid(column=0, row=2, sticky=(N, W, E, S))

# add info field
n_info = ttk.Label(subframe, text='Enter a value for "n" in the wavefunction:')
n_info.grid(column=0, row=1, sticky=(W, E))

# make n entry field
n_entry = ttk.Entry(subframe, width=2, justify=CENTER)
n_entry.grid(column=1, row=1, sticky=(W, E), padx=2)

# make button to update n
update_n = ttk.Button(subframe, text='Update n',
                      command=lambda: update_n_action())
update_n.grid(column=3, row=1, sticky=(W, E), padx=2)

# bind Enter key to the button
n_entry.bind('<Return>', lambda event: update_n_action())


def update_n_action():
    # Extract the value from the entry field
    n_value = int(n_entry.get())

    # Perform the update operation with the extracted value
    plot.update(nconst=n_value)

    # Clear the content of the entry field
    n_entry.delete(0, 'end')


root.mainloop()
