import matplotlib.pyplot as plt
import numpy as np
from qutip import *
from mpl_toolkits.mplot3d import Axes3D # hacer gráfico 3Dfrom numpy import *

class sistema:

    def __init__(self, M, N, omega, epsilon, R, d, r):
        self.N = N
        self.M = M
        self.omega = omega
        self.epsilon = epsilon
        self.R = R
        self.d = d
        self.r = r

    def a0(self):
        return self.omega * self.R / self.d 
    