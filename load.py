import geopandas as gpd
import numpy as np

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Load:

    def __init__(self, path):
        self.__data = gpd.read_file(path)

    polygony = []

    def readPol(self):
        g = [i for i in self.__data.geometry]
        for p in range(self.__data.shape[0]):
            # get x and y coordinates
            pol = list(g[p].boundary.coords.xy)


            polygon = []
            for i in range(len(pol[0])-1):
                polygon.append(QPointF((pol[0][i] + 732500) * 2, (-pol[1][i] - 1044450) * 2))

            self.polygony.append(polygon)

    def getPol(self, p):

        return QPolygonF(self.polygony[p])

    def number(self):
        n = range(self.__data.shape[0]-1)
        return n