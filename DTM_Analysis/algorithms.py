
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from math import *
from QPoint3DF import *
from Edge import *
from triangle import *

class Algorithms:

    def __init__(self):
        pass

    def getPointPolygonPositionR(self, q, pol):
        k = 0
        n = len(pol)

        # proces all vertices
        for i in range(n):
            # reduce coordinate
            xir = pol[i].x() - q.x()
            yir = pol[i].y() - q.y()
            xi1r = pol[(i + 1) % n].x() - q.x()
            yi1r = pol[(i + 1) % n].y() - q.y()

            # Suitable segment
            if (yi1r > 0) and (yir <= 0) or (yir > 0) and (yi1r <= 0):

                # compute intersection
                xm = (xi1r * yir - xir * yi1r) / (yi1r - yir)

                # increment amount of intersections
                if xm > 0:
                    k += 1

        # point is inside
        if k % 2 == 1:
            return 1

        return 0

    def get2LinesAngle(self, p1: QPointF, p2: QPointF, p3: QPointF, p4: QPointF):
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p4.x() - p3.x()
        vy = p4.y() - p3.y()

        # Dot product
        dp = ux * vx + uy * vy

        # Norms
        nu = (ux ** 2 + uy ** 2) ** 0.5
        nv = (vx ** 2 + vy ** 2) ** 0.5

        arg = dp / (nu * nv)
        arg = max(min(arg, 1), -1)

        return acos(arg)

    def getPointAndLinePosition(self, p: QPoint3DF, p1: QPoint3DF, p2: QPoint3DF):
        # Point and line position
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        vx = p.x() - p1.x()
        vy = p.y() - p1.y()

        # Test criterion
        t = ux * vy - uy * vx

        # Point is in the left halfplane
        if t > 0:
            return 1

        # Point is in the right halfplane
        if t < 0:
            return 0

        # Colinear point
        return -1

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

                if pj != pol[i]:
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

    def rotate(self, pol: QPolygonF, sig: float) -> QPolygonF:
        # Rotate polygon according to a given angle
        pol_rot = QPolygonF()

        # Process all polygon vertices
        for i in range(len(pol)):
            # Rotate point
            x_rot = pol[i].x() * cos(sig) - pol[i].y() * sin(sig)
            y_rot = pol[i].x() * sin(sig) + pol[i].y() * cos(sig)

            # Create QPoint
            vertex = QPointF(x_rot, y_rot)

            # Add vertex to rotated polygon
            pol_rot.append(vertex)

        return pol_rot

    def minMaxBox(self, pol: QPolygonF):
        # Create minmax box

        # Find extreme coordinates
        x_min = min(pol, key=lambda k: k.x()).x()
        x_max = max(pol, key=lambda k: k.x()).x()
        y_min = min(pol, key=lambda k: k.y()).y()
        y_max = max(pol, key=lambda k: k.y()).y()

        # Create minmax box vertices
        v1 = QPointF(x_min, y_min)
        v2 = QPointF(x_max, y_min)
        v3 = QPointF(x_max, y_max)
        v4 = QPointF(x_min, y_max)

        # Create min-max box
        minmax_box = QPolygonF([v1, v2, v3, v4])

        # Compute minmaxbox area
        area = (x_max - x_min) * (y_max - y_min)

        return minmax_box, area

    def minAreaEnclosingRectangle(self, pol: QPolygonF):
        # Create minimum area enclosing rectangle

        # Create convex hull
        ch = self.createCH(pol)

        # Get minmax box, area and sigma
        mmb_min, area_min = self.minMaxBox(ch)
        sigma_min = 0

        # Process all segments of ch
        for i in range(len(ch) - 1):
            # Compute sigma
            dx = ch[i + 1].x() - ch[i].x()
            dy = ch[i + 1].y() - ch[i].y()
            sigma = atan2(dy, dx)

            # Rotate convex hull by sigma
            ch_rot = self.rotate(ch, -sigma)

            # Find minmaxbox over rotated ch
            mmb, area = self.minMaxBox(ch_rot)

            # actualize minimum area
            if area < area_min:
                area_min = area
                mmb_min = mmb
                sigma_min = sigma

        # Rotate minmax box
        er = self.rotate(mmb_min, sigma_min)

        # Resize rectangle
        er_r = self.resizeRectangle(er, pol)

        return er_r

    def computeArea(self, pol: QPolygonF):
        # Comnpute area
        n = len(pol)
        area = 0

        # Process all vertices
        for i in range(n):
            # Area increment
            area += pol[i].x() * (pol[(i + 1) % n].y() - pol[(i - 1 + n) % n].y())

        return 0.5 * abs(area)

    def resizeRectangle(self, er: QPolygonF, pol: QPolygonF):
        # Building area
        Ab = abs(self.computeArea(pol))

        # Enclosing rectangle area
        A = abs(self.computeArea(er))

        # Fraction of Ab and A
        k = Ab / A

        # Center of mass
        x_t = (er[0].x() + er[1].x() + er[2].x() + er[3].x()) / 4
        y_t = (er[0].y() + er[1].y() + er[2].y() + er[3].y()) / 4

        # Vectors
        u1_x = er[0].x() - x_t
        u2_x = er[1].x() - x_t
        u3_x = er[2].x() - x_t
        u4_x = er[3].x() - x_t
        u1_y = er[0].y() - y_t
        u2_y = er[1].y() - y_t
        u3_y = er[2].y() - y_t
        u4_y = er[3].y() - y_t

        # Coordinates of new vertices
        v1_x = x_t + sqrt(k) * u1_x
        v1_y = y_t + sqrt(k) * u1_y

        v2_x = x_t + sqrt(k) * u2_x
        v2_y = y_t + sqrt(k) * u2_y

        v3_x = x_t + sqrt(k) * u3_x
        v3_y = y_t + sqrt(k) * u3_y

        v4_x = x_t + sqrt(k) * u4_x
        v4_y = y_t + sqrt(k) * u4_y

        # Create new vertices
        v1 = QPointF(v1_x, v1_y)
        v2 = QPointF(v2_x, v2_y)
        v3 = QPointF(v3_x, v3_y)
        v4 = QPointF(v4_x, v4_y)

        # Create rectangle
        er_r = QPolygonF([v1, v2, v3, v4])

        return er_r

    def wallAverage(self, pol: QPolygonF):
        r_aver = 0

        # Compute sigma
        dx = pol[1].x() - pol[0].x()
        dy = pol[1].y() - pol[0].y()
        sigma = atan2(dy, dx)

        # process all edges
        n = len(pol)

        for i in range(1, n):
            # Compute sigma i
            dx_i = pol[(i + 1) % n].x() - pol[i].x()
            dy_i = pol[(i + 1) % n].y() - pol[i].y()
            sigma_i = atan2(dy_i, dx_i)

            # Direction diferences
            delta_sigma_i = sigma_i - sigma

            # Corect delta sigma
            if delta_sigma_i < 0:
                delta_sigma_i += 2 * pi

            # Fraction by pi/2
            ki = round(2 * delta_sigma_i / pi)

            # Remainder
            r_i = delta_sigma_i - (ki * pi / 2)

            # Average remainder
            r_aver = r_aver + r_i

        # Average remainder
        r_aver = r_aver / n

        # Average direction
        sigma_aver = sigma + r_aver

        # Rotate building by sigma
        pol_rot = self.rotate(pol, -sigma_aver)

        # Find minmaxbox over rotated building
        mmb, area = self.minMaxBox(pol_rot)

        # Rotate min-max box
        er = self.rotate(mmb, sigma_aver)

        # Resize building
        er_r = self.resizeRectangle(er, pol)

        return er_r

    def getDelaunayPoint(self, p1: QPoint3DF, p2: QPoint3DF, points: list[QPoint3DF]):
        # Find optimal Delaunay point
        idx_max = -1
        om_max = 0

        # Process all points
        for i in range(len(points)):
            # Exclude identical points
            if (points[i] != p1) and (points[i] != p2):
                # Point in the left halfplane
                if self.getPointAndLinePosition(points[i], p1, p2) == 1:

                    # Compute angle
                    omega = self.get2LinesAngle(points[i], p1, points[i], p2)

                    # Actualize maximum
                    if omega > om_max:
                        om_max = omega
                        idx_max = i

        return idx_max

    def getNearestPoint(self, p: QPoint3DF, points: list[QPoint3DF]):
        # Find nearest point
        idx_min = -1
        d_min = inf

        # Browse all points
        for i in range(len(points)):

            # Point p is different from points[i]
            if p != points[i]:
                # Compute distance
                d_x = points[i].x() - p.x()
                d_y = points[i].y() - p.y()
                d = sqrt(d_x ** 2 + d_y ** 2)

                # Update minimum
                if d < d_min:
                    d_min = d
                    idx_min = i

        return idx_min

    def getNearestPoint2(self, p: QPoint3DF, points: list[QPoint3DF]):
        # Find nearest point
        idx_min = -1
        d_min = inf

        # Browse all points
        for i in range(len(points)):

            # Point p is different from points[i]
            if p != points[i]:
                # Compute distance
                d_x = points[i].x() - p.x()
                d_y = points[i].y() - p.y()
                d = sqrt(d_x ** 2 + d_y ** 2)

                # Update minimum
                if d < d_min:
                    d_min = d
                    idx_min = i
        if d_min > 10:
            return idx_min
        else:
            print(d_min)
            return -1
    def updateAEL(self, e: Edge, AEL: list[Edge]):
        # Update of AEL

        # Change orientation
        eo = e.switchOrientation()

        # Opposite edge in AEL
        if eo in AEL:
            AEL.remove(eo)

        # Opposite edge on in AEL
        else:
            AEL.append(e)

    def createDT(self, points: list[QPoint3DF]):
        # Create Delaunay triangulation

        # Supplementary data structures
        dt:list[Edge] = []
        ael:list[Edge] = []

        # Find a point with the x coordinate
        p1 = min(points, key=lambda k: k.x())

        # Find nearest point to p1
        p2 = points[self.getNearestPoint(p1, points)]

        # Create Edge and opposite edge
        e = Edge(p1, p2)
        eo = Edge(p2, p1)

        # Add two edges to AEL
        ael.append(e)
        ael.append(eo)

        # Process AEL until ti is mepty
        while ael:
            # Take the first edge
            e1 = ael.pop()

            # Switch orientation of e1
            e1o = e1.switchOrientation()

            # Get Delaunay point
            idx = self.getDelaunayPoint(e1o.getStart(), e1o.getEnd(), points)

            # If suitable point found
            if idx != -1:
                # Create remaining edges of the triangle
                e2 = Edge(e1o.getEnd(), points[idx])
                e3 = Edge(points[idx], e1o.getStart())

                # add edges to DT
                dt.append(e1o)
                dt.append(e2)
                dt.append(e3)

                # Update AEL
                self.updateAEL(e2, ael)
                self.updateAEL(e3, ael)

        return dt

    def getContourLinePoint(self, p1: QPoint3DF, p2: QPoint3DF, z: float):
        # Intersection of line and horizontal plane
        xb = (p2.x() - p1.x()) * (z - p1.getZ()) / (p2.getZ() - p1.getZ()) + p1.x()
        yb = (p2.y() - p1.y()) * (z - p1.getZ()) / (p2.getZ() - p1.getZ()) + p1.y()

        return QPoint3DF(xb, yb, z)

    def createContourLines(self, dt: list[Edge], zmin: float, zmax: float, dz: float):
        # Create contour lines inside the given interval and step
        contours: list[Edge] = []

        # Process all triangles
        for i in range(0, len(dt), 3):
            # Get triangle vertices
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i + 1].getEnd()

            # Get elevations of points
            z1 = p1.getZ()
            z2 = p2.getZ()
            z3 = p3.getZ()

            # test intersections of all planes
            for z in range(zmin, zmax, dz):
                # Get heigh differencies
                dz1 = z - z1
                dz2 = z - z2
                dz3 = z - z3

                # Triangle is coplanar
                if dz1 == 0 and dz2 == 0 and dz3 == 0:
                    continue

                # Edges (p1,p2) and (p2,p3) are intersected by plane
                if dz1 * dz2 <= 0 and dz2 * dz3 <= 0:
                    # Compute intersections
                    a = self.getContourLinePoint(p1, p2, z)
                    b = self.getContourLinePoint(p2, p3, z)

                    # Create edge
                    e = Edge(a, b)

                    # Add contour to list of contours
                    contours.append(e)

                # Edges (p2,p3) and (p3,p1) are intersected by plane
                elif dz2 * dz3 <= 0 and dz3 * dz1 <= 0:
                    # Compute intersections
                    a = self.getContourLinePoint(p2, p3, z)
                    b = self.getContourLinePoint(p3, p1, z)

                    # Create edge
                    e = Edge(a, b)

                    # Add contour to list of contours
                    contours.append(e)

                # Edges (p3,p1) and (p1,p          2) are intersected by plane
                elif dz3 * dz1 <= 0 and dz1 * dz2 <= 0:
                    # Compute intersections
                    a = self.getContourLinePoint(p3, p1, z)
                    b = self.getContourLinePoint(p1, p2, z)

                    # Create edge
                    e = Edge(a, b)

                    # Add contour to list of contours
                    contours.append(e)

        return contours

    def getSlope(self, p1:QPoint3DF, p2:QPoint3DF, p3:QPoint3DF):
        #Get triangle slope
        #First vector
        ux = p2.x() - p1.x()
        uy = p2.y() - p1.y()
        uz = p2.getZ() - p1.getZ()

        # Second vector
        vx = p3.x() - p1.x()
        vy = p3.y() - p1.y()
        vz = p3.getZ() - p1.getZ()

        #Normal vector, components
        nx = uy * vz - vy * uz
        ny = -(ux * vz - uz * vx)
        nz = ux * vy - vx * uy

        #Norm
        n = sqrt(nx*nx + ny*ny + nz*nz)

        #Compute slope
        return acos(nz/n)


    def analyzeDTMSlope(self, dt:list[Edge]):
        dtm:list[Triangle] = []

        # Process all triangles
        for i in range(0, len(dt), 3):
            # Get triangle vertices
            p1 = dt[i].getStart()
            p2 = dt[i].getEnd()
            p3 = dt[i+1].getEnd()

            # Compute slope
            slope = self.getSlope(p1, p2, p3)

            #Create triangle
            triangle = Triangle(p1, p2, p3, slope, 0)

            #Add triangle to the list
            dtm.append(triangle)

        #Return analyzed DTM
        return dtm







