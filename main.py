import numpy as np

from matplotlib.pyplot import *  # Grab MATLAB plotting functions
from control.matlab import *     # MATLAB-like functions

J = 0.01
b = 0.1
K = 0.01
R = 1
L = 0.5

A = ([-b/J,   K/J], [-K/L,   -R/L])
B = ([0], [1/L])
C = ([1, 0])
D = 0
motor = ss(A, B, C, D)

figure(1)
bode(motor, dB=1)
show()
