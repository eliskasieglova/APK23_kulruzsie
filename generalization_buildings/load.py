import geopandas as gpd
import numpy as np

from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Load:

    def __init__(self, path):
        self.__data = gpd.read_file(path)

        if path == 'data\\bud_vily.shp':
            self.__a = 732670
            self.__b = 2.4
            self.__c = 1044800
            self.__d = 2.4
        elif path == 'data\\bud_sidliste.shp':
            self.__a = 741780
            self.__b = 1.3
            self.__c = 1050180
            self.__d = 1.3
        elif path == 'data\\bud_centrum.shp':
            self.__a = 743500
            self.__b = 2
            self.__c = 1045150
            self.__d = 2

    polygony = []

    def readPol(self):
        g = [i for i in self.__data.geometry]
        for p in range(self.__data.shape[0]):
            # get x and y coordinates
            pol = list(g[p].boundary.coords.xy)


            polygon = []
            for i in range(len(pol[0])-1):
                polygon.append(QPointF((pol[0][i] + self.__a) * self.__b, (-pol[1][i] - self.__c) * self.__d))

            self.polygony.append(polygon)

    def getPol(self, p):

        return QPolygonF(self.polygony[p])

    def number(self):
        n = range(self.__data.shape[0]-1)
        return n