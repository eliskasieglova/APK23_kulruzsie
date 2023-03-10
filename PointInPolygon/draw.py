from load import Load
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Query point and polygon
        self.__q = QPointF(0,0)
        self.__pol = QPolygonF()

        self.__pols = []
        self.polsNew = []

        self.__add_vertex = True

    def mousePressEvent(self, e:QMouseEvent):
        #Left mouse button click
        x = e.position().x()
        y = e.position().y()

        #Add point to polygon
        if self.__add_vertex:
            #Create point
            p = QPointF(x,y)

            #Append p to polygon
            self.__pol.append(p)

        #Set x,y to point
        else:
            self.__q.setX(x)
            self.__q.setY(y)

        #Repaint screen
        self.repaint()

    def input(self):

        pols = Load()
        pols.readPol('TMMESTSKECASTI_P.shp')
        #print('Ano')
        for pl in range(57):
            self.__pol.clear()
            xy = pols.xy(pl)
            #print(xy)
            for i in range(len(xy)):
                if self.__add_vertex:
                    # Create point
                    p = QPointF((xy[i].x() - 14) * 642, 300 - (xy[i].y() - 50) * 1000)

                    # Append p to polygon
                    self.__pol.append(p)

                # Set x,y to point
                else:
                    self.__q.setX(xy[i].x())
                    self.__q.setY(xy[i].y())
            self.__pols.append(QPolygonF(self.__pol))
            #print(list(self.__pol))
            self.repaint()

    def paintEvent(self, e:QPaintEvent):
        #Draw polygon

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes
        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.yellow)

        #Draw polygon
        for p in range(len(self.__pols)):
            qp.drawPolygon(self.__pols[p])

        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.green)

        for p in range(len(self.polsNew)):
            qp.drawPolygon(self.polsNew[p])

        #Draw point
        d = 1
        qp.drawEllipse(int(self.__q.x() - d/2), int(self.__q.y() - d/2), d, d)

        #End draw
        qp.end()

    def switchSource(self):
        #Move point or add vertex
        self.__add_vertex = not(self.__add_vertex)

    def getPoint(self):
        #Get point
        return self.__q

    def getPolygon(self, p):
        #Get polygon
        return self.__pols[p]

