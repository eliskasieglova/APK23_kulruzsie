import geopandas as gpd
import numpy as np

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Load:

    def __init__(self):
        pass

    polygony = []

    def readPol(self, path):
        data = gpd.read_file(path)
        n = 0
        for p in range(data.shape[0]):
            g = [i for i in data.geometry]
            # get x and y coordinates
            pol = list(g[p].boundary.coords.xy)

            polygon = []
            for i in range(len(pol[0])):
                polygon.append(QPointF(pol[0][i], pol[1][i]))
            n = n+1
            self.polygony.append(polygon)

    def xy(self, p):

        return self.polygony[p]

    def number(self, path):
        data = gpd.read_file(path)
        n = range(data.shape[0])
        return n