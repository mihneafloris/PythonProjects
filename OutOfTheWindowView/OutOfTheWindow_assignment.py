"""Floris Mihnea
Student number: 4663675
Out of the Windows view assignment"""

#____________________________Main___________________________

import numpy as np
from numpy.linalg import solve,norm
import pygame 
from math import *
import sys


def main():

    runway_lights = np.genfromtxt("runway_lights.dat", delimiter = ",", skip_header = 1)
    lightpos = runway_lights.T[0:3,:]
    lightcol = runway_lights[:,-3:]
    lightpos[2]=np.zeros(697)
    lightcol.astype(int)
    return lightpos, lightcol
