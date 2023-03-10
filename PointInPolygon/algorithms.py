import numpy as np
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Algorithms:

    def __init__(self):
        pass

    def getPointPolygonPositionR(self, q, pol):
        kr = 0  # pocet pruseciku paprsku a hran na prave strane
        kl = 0  # leva strana
        n = len(pol)

        # proces all vertices
        for i in range(n):
            #reduce coordinate - pocatek sourad systemu posunu do bodu q
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()

            #is on the corner
            if xir == 0 and yir == 0:
                return 3

            #Suitable segment
            if (yi1r > 0) and (yir <= 0) or (yir > 0) and (yi1r <= 0):  # lezi mezi y-sourad

                #compute intersection
                xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)

                #print(xm)
                # increment amount of intersections
                if xm > 0:
                    kr += 1
                elif xm < 0:
                    kl += 1
                elif xm == 0:
                    return 2
        #same amount of intersections on left and right
        if kr % 2 == 1:
                return 1
        #point is on the border

        return 0

    def getPointPolygonPositionW(self, q, pol):

        n = len(pol)
        uhel = 0
        # print(pol[0].x())

        for i in range(n - 1):

            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            xi1r = pol[(i + 1) % n].x() - q.x()
            yi1r = pol[(i + 1) % n].y() - q.y()

            if xir == 0 and yir == 0:
                return 3

            xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)

            scalar = xir * xi1r + yir * yi1r

            length = (xir ** 2 + yir ** 2) ** (1 / 2) * (xi1r ** 2 + yi1r ** 2) ** (1 / 2)

            fi = np.arccos(scalar / length)

            if fi > 3.14:
                return 2

            if pol[i].y() > pol[(i + 1) % n].y():  # orientace hrany je nahoru
                if xm > 0:  # bod je nalevo od hrany ve smeru orientace (+)
                    uhel += fi
                elif xm < 0:  # bod je napravo od hrany (-)
                    uhel -= fi

            elif pol[i].y() < pol[(i + 1) % n].y():  # orientace hrany je dolu
                if xm < 0:  # bod je nalevo od hrany (+)
                    uhel += fi
                elif xm > 0:  # bod je napravo od hrany (-)
                    uhel -= fi

        if uhel > 6.2:
            return 1

        return 0