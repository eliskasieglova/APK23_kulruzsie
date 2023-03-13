from load import Load
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

data = 'TMMESTSKECASTI_P.shp'


class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # query point and polygon
        self.__q = QPointF(0,0)
        self.__pol = QPolygonF()

        self.__pols = []
        self.polsNew = []

        self.__add_vertex = False

    def mousePressEvent(self, e:QMouseEvent):
        # left mouse button click
        x = e.position().x()
        y = e.position().y()

        # add point to polygon
        if self.__add_vertex:
            # create point
            p = QPointF(x,y)

            # append p to polygon
            self.__pol.append(p)

        # set x,y to point
        else:
            self.__q.setX(x)
            self.__q.setY(y)

        # repaint screen
        self.repaint()

    def input(self):

        pols = Load()
        # load data
        pols.readPol(data)
        n = pols.number(data)
        # process all polygons
        for pl in n:
            self.__pol.clear()
            xy = pols.xy(pl)

            # process all vertices in analyzed polygon
            for i in range(len(xy)):
                # create point
                p = QPointF((xy[i].x() - 14) * 1284 - 100, 400 - (xy[i].y() - 50) * 2000)

                # append p to polygon
                self.__pol.append(p)


            self.__pols.append(QPolygonF(self.__pol))

            self.repaint()

    def num(self):
        pols = Load()
        n = pols.number(data)
        return n

    def paintEvent(self, e:QPaintEvent):

        # create graphic object
        qp = QPainter(self)

        # start draw
        qp.begin(self)

        # set attributes
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.yellow)

        # draw polygon
        for p in range(len(self.__pols)):
            qp.drawPolygon(self.__pols[p])

        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.green)

        for p in range(len(self.polsNew)):
            qp.drawPolygon(self.polsNew[p])

        # draw point
        d = 3
        qp.drawEllipse(int(self.__q.x() - d/2), int(self.__q.y() - d/2), d, d)

        # end draw
        qp.end()

    def switchSource(self):
        # move point or add vertex
        self.__add_vertex = not(self.__add_vertex)

    def getPoint(self):
        # get point
        return self.__q

    def getPolygon(self, p):
        # get polygon
        return self.__pols[p]

