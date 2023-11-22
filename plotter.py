import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rcParams
import numpy as np
import tkinter as tk

# NOTES

# Potentially faster to recalculate wave functions for probability density; 
# Python could cache results and save the time that would be needed to save array in variables?

# Mess with time, E, and frame rate to make animation smooth

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# constants
h = 6.582 * (1 / np.power(10, 16)) # approx
E = h * np.pi
L = 1
# params
n = 2
t = 0 # Potentially not needed?
x = np.linspace(0, 1, 100)

def real_wavfunc(n, x, t, h, E, L):
    return np.cos((-1*(E*t))/h) * np.sqrt(2/L) * np.sin((n*np.pi*x)/L)

def i_wavfunc(n, x, t, h, E, L):
    return np.sin((-1*(E*t))/h) * np.sqrt(2/L) * np.sin((n*np.pi*x)/L)

def prob_density(real_y, imag_y):
    return np.square(real_y) + np.square(imag_y)

# prepare plot
fig, ax = plt.subplots()

real_y = real_wavfunc(n, x, 0, h, E, L)
real_line, = ax.plot(x, real_y, label='real', color='blue')

imag_y = i_wavfunc(n, x, 0, h, E, L)
imag_line, = ax.plot(x, imag_y, label='imaginary', color='red')

prob_line, = ax.plot(x, prob_density(real_y, imag_y), label='probability', color='green')

ax.set_ylim(bottom=-2, top=2.5)

# aesthetic changes
ax.set_xlabel('x', color='white')
ax.set_ylabel('Ψ', color='white')

ax.set_title('Real and Imaginary Portions of Wavefunction', color='white')
ax.legend()

fig.set_facecolor('black')
ax.set_facecolor('black')

ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['right'].set_color('white')
ax.hlines(0, 0, 1, colors='white')

ax.legend(facecolor='black', edgecolor='white', loc='upper right', fontsize='small', labelcolor='white',)

ax.tick_params(axis='x', color='white', labelcolor='white')
ax.tick_params(axis='y', color='white', labelcolor='white')

# make animation

def update(frame):
    real_y = real_wavfunc(n, x, frame, h, E, L)
    real_line.set_ydata(real_y)
    
    imag_y = i_wavfunc(n, x, frame, h, E, L)
    imag_line.set_ydata(imag_y)
    
    prob_line.set_ydata(prob_density(real_y, imag_y))
    return real_line, imag_line, prob_line

animation = FuncAnimation(fig, update, frames=np.linspace(0, 2, 60), interval=34)



plt.show()


