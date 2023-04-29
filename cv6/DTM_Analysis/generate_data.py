import random as r
from itertools import repeat

from algorithms import *
import geopandas as gpd
from random import *
from math import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from QPoint3DF import *


class Generate:

    def __init__(self):
        self.points = list[QPoint3DF]

    def PorM(self):
        x = random()
        if x < 0.5:
            return 1
        else:
            return -1

    def GeneratePointCloud(self):
        # Create borders
        xm = 750
        ym = 450
        min = 20
        max_points = 500
        bord_a = QPoint3DF(min, min, random()*100)
        bord_b = QPoint3DF(min, ym, random()*100)
        bord_c = QPoint3DF(xm, min, random()*100)
        bord_d = QPoint3DF(xm, ym, random()*100)
        self.points = [bord_a, bord_b, bord_c, bord_d]
        for i in range (min,ym,100):
            y = QPoint3DF(min, i, QPoint3DF.getZ(bord_a)+((i-min)/(ym-min))*(QPoint3DF.getZ(bord_b)-QPoint3DF.getZ(bord_a)))
            self.points.append(y)
        for i in range (min,xm,100):
            x = QPoint3DF(i, min, QPoint3DF.getZ(bord_a)+((i-min)/(xm-min))*(QPoint3DF.getZ(bord_c)-QPoint3DF.getZ(bord_a)))
            self.points.append(x)
        for i in range (min,ym,100):
            y = QPoint3DF(xm, i, QPoint3DF.getZ(bord_c)+((i-min)/(ym-min))*(QPoint3DF.getZ(bord_d)-QPoint3DF.getZ(bord_c)))
            self.points.append(y)
        for i in range (min,xm,100):
            x = QPoint3DF(i, ym, QPoint3DF.getZ(bord_b)+((i-min)/(xm-min))*(QPoint3DF.getZ(bord_d)-QPoint3DF.getZ(bord_b)))
            self.points.append(x)
        a = Algorithms()

        # Incialize number of starting points

        s = 4
        for i in range(s):
            xi = r.randint(min+50, xm-50)+random()*10
            yi = r.randint(min+50, ym-50)+random()*10
            zi = random() * 1000
            pi = QPoint3DF(xi, yi, zi)
            i_min = a.getNearestPoint(pi, self.points)
            #closest point
            cl_p = self.points[i_min]
            d = sqrt((cl_p.x() - pi.x()) ** 2 + (cl_p.y() - pi.y()) ** 2)
            if d > 20:
                self.points.append(pi)
        n = s+4
        while n < max_points:
            x0 = r.randint(min+20, xm-20)+random()*10
            y0 = r.randint(min+20, ym-20)+random()*10
            z0 = 0
            p0 = QPoint3DF(x0, y0, z0)
            temp_list = self.points.copy()
            n_p = []
            d = []
            for j in range(3):
                i_min = a.getNearestPoint(p0, temp_list)
                pj = temp_list[i_min]
                dist = sqrt((pj.x() - p0.x()) ** 2 + (pj.y() - p0.y()) ** 2)
                n_p.append(pj)
                d.append(dist)
                temp_list.pop(i_min)
            if d[0] > 10:
                z1 = QPoint3DF.getZ(n_p[0])
                z2 = QPoint3DF.getZ(n_p[1])
                z3 = QPoint3DF.getZ(n_p[2])
                z = (z1/d[0] + z2/d[1] + z3/d[2])/(1/d[0] + 1/d[1] + 1/d[2])+self.PorM()*random()*20
                p = QPoint3DF(x0, y0, z)
                self.points.append(p)
                n = n+1

    def number(self):
        return len(self.points)

    def getPoi(self, p):
        return self.points[p]
