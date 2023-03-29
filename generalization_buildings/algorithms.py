from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import *

class Algorithms:

    def __init__(self):
        pass

    def get2LinesAngle(self, p1:QPointF,p2:QPointF,p3:QPointF,p4:QPointF):
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        #Dot product
        dp = ux*vx + uy*vy

        #Norms
        nu = (ux ** 2 + uy ** 2) ** 0.5
        nv = (vx ** 2 + vy ** 2) ** 0.5

        #Correct argument to the interval [-1,1]
        arg = dp / (nu * nv)
        arg = max(min(arg, 1), -1)

        return acos(arg)

    def createCH(self, pol: QPolygonF):
        # Create CH using Jarvis scan
        ch = QPolygonF()

        # Find pivot
        q = min(pol, key=lambda k: k.y())

        # Initialize pj-1, pj
        pj1 = QPointF(q.x() - 1, q.y())
        pj = q

        # Add q to convex hull
        ch.append(q)

        # Jarvis scan
        while True:
            # Initialize maximum
            phi_max = 0
            i_max = -1

            # Find suitable point maximizing angle
            for i in range(len(pol)):

                if pj != pol[i] and pj1 != pol[i]:
                    # Measure angle
                    phi = self.get2LinesAngle(pj, pj1, pj, pol[i])

                    # Actualize phi_max
                    if phi > phi_max:
                        phi_max = phi
                        i_max = i

            # Append point to CH
            ch.append(pol[i_max])

            # Actualize last two points
            pj1 = pj
            pj = pol[i_max]

            # Stop condition
            if pj == q:
                break

        return ch

    def createCHGS(self, pol: QPolygonF):
        # Convex hull using Graham scan
        sorted = []

        # Find pivot
        q = min(pol, key=lambda k: k.y())

        pj1 = QPointF(q.x() - 1, q.y())
        pj = q

        Q = [1] * len(pol)
        sorted.append(q)

        i_max = -1
        # For each vertex of polygon
        for n in range(len(pol) - 1):
            phi_max = 0
            # For all other vertices
            for i in range(len(pol)):
                if (pj != pol[i]) and (Q[i] == 1):
                    phi = self.get2LinesAngle(pj, pj1, pj, pol[i])

                    if phi > phi_max:
                        phi_max = phi
                        i_max = i

            sorted.append(pol[i_max])
            Q[i_max] = 0
        j = 2
        while j < (len(sorted)):
            print(j)
            dx = (sorted[j - 1].x() - sorted[j - 2].x())
            dy = (sorted[j - 1].y() - sorted[j - 2].y())

            if dx != 0:
                a = dy / dx
                b = sorted[j - 1].y() - a * sorted[j - 1].x()

                if dy * a > 0:
                    print('1')
                    if sorted[j].y() > (a * sorted[j].x() + b):
                        j += 1
                    else:
                        sorted.pop(j - 1)
                        j -= 1
                elif dy * a < 0:
                    print('2')
                    if sorted[j].y() < (a * sorted[j].x() + b):
                        j += 1
                    else:
                        sorted.pop(j - 1)
                        j -= 1
                else:
                    print('else 1')
                    if dx > 0:
                        if sorted[j].y() > sorted[j - 1].y():
                            j += 1
                        else:
                            sorted.pop(j - 1)
                            j -= 1
                    elif dx < 0:
                        if sorted[j].y() < sorted[j - 1].y():
                            j += 1
                        else:
                            sorted.pop(j - 1)
                            j -= 1
            else:
                print('else 2')
                if dy > 0:
                    print('else 2-1')
                    if sorted[j].x() < sorted[j - 1].x():
                        j += 1
                    else:
                        sorted.pop(j - 1)
                        j -= 1
                elif dy < 0:
                    print('else 2-2')
                    if sorted[j].x() > sorted[j - 1].x():
                        j += 1
                    else:
                        sorted.pop(j - 1)
                        j -= 1
        return QPolygonF(sorted)


    def rotate(self, pol:QPolygonF, sig:float)->QPolygonF:
        #Rotate polygon according to a given angle
        pol_rot = QPolygonF()

        #Process all polygon vertices
        for i in range(len(pol)):

            #Rotate point
            x_rot = pol[i].x() * cos(sig) - pol[i].y() * sin(sig)
            y_rot = pol[i].x() * sin(sig) + pol[i].y() * cos(sig)

            #Create QPoint
            vertex = QPointF(x_rot, y_rot)

            # Add vertex to rotated polygon
            pol_rot.append(vertex)

        return pol_rot

    def minMaxBox (self, pol: QPolygonF):
        #Create minmax box

        # Find extreme coordinates
        x_min = min(pol, key= lambda k: k.x()).x()
        x_max = max(pol, key = lambda k: k.x()).x()
        y_min = min(pol, key=lambda k: k.y()).y()
        y_max = max(pol, key=lambda k: k.y()).y()

        # Create minmax box vertices
        v1 = QPointF(x_min, y_min)
        v2 = QPointF(x_max, y_min)
        v3 = QPointF(x_max, y_max)
        v4 = QPointF(x_min, y_max)

        #Create min-max box
        minmax_box = QPolygonF([v1, v2, v3, v4])

        #Compute minmaxbox area
        area = (x_max - x_min) * (y_max - y_min)

        return minmax_box, area


    def minAreaEnclosingRectangle(self, pol: QPolygonF):
        # Create minimum area enclosing rectangle

        #Create convex hull
        ch = self.createCH(pol)

        #Get minmax box, area and sigma
        mmb_min, area_min = self.minMaxBox(ch)
        sigma_min = 0

        # Process all segments of ch
        for i in range(len(ch)-1):
            # Compute sigma
            dx = ch[i+1].x() - ch[i].x()
            dy = ch[i+1].y() - ch[i].y()
            sigma = atan2(dy,dx)

            #Rotate convex hull by sigma
            ch_rot = self.rotate(ch, -sigma)

            #Find minmaxbox over rotated ch
            mmb, area = self.minMaxBox(ch_rot)

            #actualize minimum area
            if area < area_min:
                area_min = area
                mmb_min = mmb
                sigma_min = sigma

        #Rotate minmax box
        er = self.rotate(mmb_min, sigma_min)

        #Resize rectangle
        er_r = self.resizeRectangle(er, pol)

        return er_r


    def computeArea (self, pol : QPolygonF):
        #Compute area
        n = len(pol)
        area = 0

        #Process all vertices
        for i in range(n):
            #Area increment
            area += pol[i].x()*(pol[(i+1)%n].y()-pol[(i-1+n)%n].y())

        return 0.5 * abs(area)


    def resizeRectangle(self, er: QPolygonF, pol:QPolygonF):
        #Building area
        Ab = abs(self.computeArea(pol))

        #Enclosing rectangle area
        A = abs(self.computeArea(er))

        # Fraction of Ab and A
        k = Ab/A

        #Center of mass
        x_t = (er[0].x() + er[1].x() + er[2].x() + er[3].x())/4
        y_t = (er[0].y() + er[1].y() + er[2].y() + er[3].y())/4

        #Vectors
        u1_x = er[0].x() - x_t
        u2_x = er[1].x() - x_t
        u3_x = er[2].x() - x_t
        u4_x = er[3].x() - x_t
        u1_y = er[0].y() - y_t
        u2_y = er[1].y() - y_t
        u3_y = er[2].y() - y_t
        u4_y = er[3].y() - y_t

        #Coordinates of new vertices
        v1_x = x_t + sqrt(k) * u1_x
        v1_y = y_t + sqrt(k) * u1_y

        v2_x = x_t + sqrt(k) * u2_x
        v2_y = y_t + sqrt(k) * u2_y

        v3_x = x_t + sqrt(k) * u3_x
        v3_y = y_t + sqrt(k) * u3_y

        v4_x = x_t + sqrt(k) * u4_x
        v4_y = y_t + sqrt(k) * u4_y

        #Create new vertices
        v1 = QPointF(v1_x, v1_y)
        v2 = QPointF(v2_x, v2_y)
        v3 = QPointF(v3_x, v3_y)
        v4 = QPointF(v4_x, v4_y)

        #Create rectangle
        er_r = QPolygonF([v1, v2, v3, v4])

        return er_r

    def wallAverage(self, pol: QPolygonF):
        # Create enclosing rectangle using wall average
        r_aver = 0

        # Compute sigma
        dx = pol[1].x() - pol[0].x()
        dy = pol[1].y() - pol[0].y()
        sigma = atan2(dy, dx)

        # Process all edges
        n = len(pol)

        for i in range(1,n):
            # Compute sigma i
            dx_i = pol[(i+1)%n].x() - pol[i].x()
            dy_i = pol[(i+1)%n].y() - pol[i].y()
            sigma_i = atan2(dy_i, dx_i)

            # Direction diferences
            delta_sigma_i = sigma_i - sigma

            # Corect delta sigma
            if delta_sigma_i < 0:
                delta_sigma_i += 2*pi

            # Fraction by pi/2
            ki = round(2*delta_sigma_i/pi)

            #Remainder
            r_i = delta_sigma_i - (ki * pi/2)

            #Average remainder
            r_aver = r_aver + r_i

        #Average remainder
        r_aver = r_aver/n

        #Average direction
        sigma_aver = sigma + r_aver

        # Rotate building by sigma
        pol_rot = self.rotate(pol, -sigma_aver)

        # Find minmaxbox over rotated building
        mmb, area = self.minMaxBox(pol_rot)

        #Rotate min-max box
        er = self.rotate(mmb, sigma_aver)

        #Resize building
        er_r = self.resizeRectangle(er, pol)

        return er_r

    def longestEdge(self, pol: QPolygonF):
        # Create enclosing rectangle using longest edge

        # Initialize longest edge and sigma
        len_max = 0
        sigma = 0

        # Process all edges
        n = len(pol)
        for i in range(n):
            # calculate length of segment
            x1 = pol[i].x()
            y1 = pol[i].y()
            x2 = pol[(i + 1) % n].x()
            y2 = pol[(i + 1) % n].y()

            length = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

            # If length is larger than current max length --> assign max length
            if length > len_max:
                len_max = length

                # compute sigma
                dx = pol[i].x() - pol[(i + 1) % n].x()
                dy = pol[i].y() - pol[(i + 1) % n].y()
                sigma = atan2(dy, dx)

            # Rotate building by sigma
            pol_rot = self.rotate(pol, -sigma)

            # Find minmaxbox over rotated building
            mmb, area = self.minMaxBox(pol_rot)

            # Rotate min-max box
            er = self.rotate(mmb, sigma)

            # Resize building
            er_r = self.resizeRectangle(er, pol)

        return er_r

'''
    def weightedBisector(self, pol: QPolygonF):
        # Simplifies polygon using Weighted Bisector

        # Initialize longest edges and sigmas
        len_max1 = 0
        len_max2 = 0
        sigma1 = 0
        sigma2 = 0

        # Remember edge points
        e1p1 = 0
        e1p2 = 0
        e2p1 = 0
        e2p2 = 0

        n = len(pol)

        for i in range(n):
            # Find longest diagonal for point i
            if (pol[i] != e1p1) & (pol[i] != e1p2) & (pol[i] != e2p1) & (pol[i] != e2p2) & (pol[i] != e1p1):

                d_length = 0
                idx_d = 0
                for j in range(n):
                    # calculate length of segment
                    if pol[j] != pol[i]:
                        length = sqrt((pol[i].x() - pol[j].x()) ** 2 + (pol[i].y() - pol[j].y()) ** 2)

                        # Find longest diagonal
                        if length > d_length:
                            d_length = length
                            idx_d = j #index druhyho bodu

                # Update max length
                if d_length > len_max2:
                    len_max2 = len_max1
                    len_max1 = d_length

                    e2p1 = e1p1
                    e2p2 = e1p2
                    e1p1 = pol[i]
                    e1p2 = pol[idx_d]

                    # Compute sigma
                    dx = pol[idx_d].x() - pol[i].x()
                    dy = pol[idx_d].y() - pol[i].y()
                    sigma = atan2(dy, dx)

                    sigma2 = sigma1
                    sigma1 = sigma

        #Main direction
        sigma = (len_max1 * sigma1 + len_max2 * sigma2)/(len_max1 + len_max2)

        # Rotate building by sigma
        pol_rot = self.rotate(pol, -sigma)

        # Find minmaxbox over rotated building
        mmb, area = self.minMaxBox(pol_rot)

        # Rotate min-max box
        er = self.rotate(mmb, sigma)

        # Resize building
        er_r = self.resizeRectangle(er, pol)

        return er_r'''
