from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from load import Load

class Draw(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #Building, convex hull and enclosing rectangle
        self.__pol = QPolygonF()
        #self.__ch = QPolygonF()
        #self.__er = QPolygonF()
        self.polLoad = []
        self.polRes = []

    def mousePressEvent(self, e:QMouseEvent):
        #Left mouse button click
        x = e.position().x()
        y = e.position().y()

        #Add point to polygon
        p = QPointF(x,y)

        #Append p to polygon
        self.__pol.append(p)

        #Repaint screen
        self.repaint()

    def paintEvent(self, e:QPaintEvent):
        #Draw polygon

        #Create graphic object
        qp = QPainter(self)

        #Start draw
        qp.begin(self)

        #Set attributes, building

        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.green)

        #Draw building
        qp.drawPolygon(self.__pol)

        # Set attributes, convex hull
        #qp.setPen(Qt.GlobalColor.blue)
        #qp.setBrush(Qt.GlobalColor.yellow)

        # Draw convex hull
        #qp.drawPolygon(self.__ch)

        # Draw loaded buildings
        qp.setPen(Qt.GlobalColor.blue)
        qp.setBrush(Qt.GlobalColor.green)

        # Draw building
        #qp.drawPolygon(self.__er)

        for p in range(len(self.polLoad)):
            qp.drawPolygon(self.polLoad[p])

        qp.setPen(Qt.GlobalColor.red)
        qp.setBrush(Qt.GlobalColor.transparent)

        # Draw convex hull or enclosing rectangle
        for p in range(len(self.polRes)):
            qp.drawPolygon(self.polRes[p])

        #End draw
        qp.end()

    def input(self, path):
        self.data = Load(path)
        self.data.readPol()

        for p in self.data.number():
            self.polLoad.append(self.data.getPol(p))
        self.repaint()
    #
    #     pols = Load()
    #     # load data
    #     pols.readPol(data1)
    #     n = pols.number(data1)
    #     # process all polygons
    #     for pl in n:
    #         self.__pol.clear()
    #         xy = pols.xy(pl)
    #
    #         # process all vertices in analyzed polygon
    #         for i in range(len(xy)):
    #             # create point
    #             p = QPointF((xy[i].x() - 14) * 1284 - 100, 400 - (xy[i].y() - 50) * 2000)
    #
    #             # append p to polygon
    #             self.__pol.append(p)
    #
    #
    #         self.__pols.append(QPolygonF(self.__pol))
    #
    #         self.repaint()

    def getPolygon(self):
        #Get polygon
        return self.__pol

    # def setCH(self, pol:QPolygonF):
    #     #Set polygon as the convex hull
    #     self.__ch = pol
    #
    # def setER(self, pol:QPolygonF):
    #     self.__er = pol

    def clearAll(self):
        self.polRes.clear()

    def clearLoadedData(self):
        self.polLoad.clear()
        self.__pol.clear()

    def polisEmpty(self):
        if self.__pol:
            return False
        return True

    def polLoadisEmpty(self):
        if self.polLoad:
            return False
        return True