"""Floris Mihnea
Student number: 4663675
Out of the Windows view assignment"""



import numpy as np
from numpy.linalg import solve,norm
import pygame 
from math import *
import sys
import time


def runway():
    raw = np.genfromtxt("runway_lights.dat", delimiter = ",", skip_header = 1)        
    lightpos = raw[:,:3]
    x= lightpos[:,1]
    y= lightpos[:,0]
    z= np.zeros(697).T
    lightpos = np.column_stack((x,y,z))
    lightpos = lightpos.T
    lightcol = raw[:,2:]
    lightcol = lightcol.astype(int)
    return lightpos, lightcol
        
R= runway()





""""
F = otwvtools.Framework()
F.setupscr()
F.drawhorizon()
input("Press enter:")
F.closescr()
F.drawlights(self.lightpos, self.lightcol)

"""
