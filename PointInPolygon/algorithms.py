import numpy as np
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Algorithms:

    def __init__(self):
        pass

    def getPointPolygonPositionR(self, q, pol):
        # initialize amount of intersections
        k = 0
        n = len(pol)

        # process all vertices
        for i in range(n):
            # reduce coordinate
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            xi1r = pol[(i+1)%n].x() - q.x()
            yi1r = pol[(i+1)%n].y() - q.y()

            # point is on the corner
            if xir == 0 and yir == 0:
                return 3

            # suitable segment
            if (yi1r > 0) and (yir <= 0) or (yir > 0) and (yi1r <= 0):

                # compute intersection
                xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)

                # increment amount of intersections
                if xm > 0:
                    k += 1
                # point is on the border
                elif xm == 0:
                    return 2
        # point is inside
        if k % 2 == 1:
                return 1

        return 0

    def getPointPolygonPositionW(self, q, pol):

        n = len(pol)
        uhel = 0

        for i in range(n - 1):
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            xi1r = pol[(i + 1) % n].x() - q.x()
            yi1r = pol[(i + 1) % n].y() - q.y()

            # point is on the corner
            if xir == 0 and yir == 0:
                return 3

            # dot product
            scalar = xir * xi1r + yir * yi1r

            # product of lengths of vectors from point to vertices
            length = (xir ** 2 + yir ** 2) ** (1 / 2) * (xi1r ** 2 + yi1r ** 2) ** (1 / 2)

            # angle between vectors
            fi = np.arccos(scalar / length)

            # point is on the border
            if fi >= 3.14:
                return 2

            # horizontal edge:
            # point is above
            if yir == yi1r and yir > 0:
                # left-right orientation
                if xir < xi1r:
                    uhel += fi
                # right-left orientation
                elif xir > xi1r:
                    uhel -= fi
            # point is below
            elif yir == yi1r and yir < 0:
                # left-right orientation
                if xir < xi1r:
                    uhel -= fi
                # right-left orientation
                elif xir > xi1r:
                    uhel += fi
            # non-horizontal edge:
            else:
                # intersection
                xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)

            # edge orientation is upward
            if yir > yi1r:
                # point is on the left from the edge
                if xm > 0:
                    uhel += fi
                # point is on the right from the edge
                elif xm < 0:
                    uhel -= fi
            # edge orientation is downward
            elif yir < yi1r:
                # point is on the left from the edge
                if xm < 0:
                    uhel += fi
                # point is on the right from the edge
                elif xm > 0:
                    uhel -= fi
        # point is inside
        if uhel >= 6.28:
            return 1

        return 0