# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from load import Load
from algorithms import *

data1 = 'data\\bud_centrum.shp'
data2 = 'data\\bud_sidliste.shp'
data3 = 'data\\bud_vily.shp'

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Canvas = Draw(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Canvas.sizePolicy().hasHeightForWidth())
        self.Canvas.setSizePolicy(sizePolicy)
        self.Canvas.setObjectName("Canvas")
        self.horizontalLayout.addWidget(self.Canvas)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSimplify = QtWidgets.QMenu(self.menubar)
        self.menuSimplify.setObjectName("menuSimplify")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpenCenter = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icons/open_center.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpenCenter.setIcon(icon8)
        self.actionOpenCenter.setObjectName("actionOpenCenter")

        self.actionOpenVilla = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icons/open_villa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpenVilla.setIcon(icon9)
        self.actionOpenVilla.setObjectName("actionOpenVilla")

        self.actionOpenUrban = QtGui.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icons/open_urban.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpenUrban.setIcon(icon10)
        self.actionOpenUrban.setObjectName("actionOpenUrban")

        self.actionClose = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClose.setIcon(icon1)
        self.actionClose.setObjectName("actionClose")
        self.actionMinimum_Area_Enclosing_Rectangle = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/maer.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionMinimum_Area_Enclosing_Rectangle.setIcon(icon2)
        self.actionMinimum_Area_Enclosing_Rectangle.setObjectName("actionMinimum_Area_Enclosing_Rectangle")
        self.actionWall_Average = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/wa.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWall_Average.setIcon(icon3)
        self.actionWall_Average.setObjectName("actionWall_Average")
        self.actionClear = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon4)
        self.actionClear.setObjectName("actionClear")
        self.actionLongest_Edge = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/le.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionLongest_Edge.setIcon(icon5)
        self.actionLongest_Edge.setObjectName("actionLongest_Edge")
        self.actionWeighted_Bisector = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icons/wb.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWeighted_Bisector.setIcon(icon6)
        self.actionWeighted_Bisector.setObjectName("actionWeighted_Bisector")
        self.actionGraham_Scan = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icons/gs.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionGraham_Scan.setIcon(icon7)
        self.actionGraham_Scan.setObjectName("actionGraham_Scan")
        self.actionClearData = QtGui.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icons/clear_data.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClearData.setIcon(icon11)
        self.actionClearData.setObjectName("actionClearData")


        self.menuFile.addAction(self.actionOpenCenter)
        self.menuFile.addAction(self.actionOpenVilla)
        self.menuFile.addAction(self.actionOpenUrban)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuSimplify.addAction(self.actionMinimum_Area_Enclosing_Rectangle)
        self.menuSimplify.addAction(self.actionWall_Average)
        self.menuSimplify.addAction(self.actionLongest_Edge)
        self.menuSimplify.addAction(self.actionWeighted_Bisector)
        self.menuSimplify.addAction(self.actionGraham_Scan)
        self.menuSimplify.addSeparator()
        self.menuSimplify.addAction(self.actionClear)
        self.menuSimplify.addAction(self.actionClearData)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSimplify.menuAction())
        self.toolBar.addAction(self.actionOpenCenter)
        self.toolBar.addAction(self.actionOpenVilla)
        self.toolBar.addAction(self.actionOpenUrban)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionMinimum_Area_Enclosing_Rectangle)
        self.toolBar.addAction(self.actionWall_Average)
        self.toolBar.addAction(self.actionLongest_Edge)
        self.toolBar.addAction(self.actionWeighted_Bisector)
        self.toolBar.addAction(self.actionGraham_Scan)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addAction(self.actionClearData)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Connect signals and slots
        self.actionMinimum_Area_Enclosing_Rectangle.triggered.connect(self.createMAER)
        self.actionWall_Average.triggered.connect(self.createWA)
        self.actionGraham_Scan.triggered.connect(self.createCHGS)
        self.actionLongest_Edge.triggered.connect(self.simplifyLEClick)
        #self.actionWeighted_Bisector.triggered.connect(self.simplifyWBClick)
        self.actionClear.triggered.connect(self.clearClick)
        self.actionClearData.triggered.connect(self.clearData)
        self.actionClose.triggered.connect(self.close)
        self.actionOpenCenter.triggered.connect(self.openCenter)
        self.actionOpenVilla.triggered.connect(self.openVilla)
        self.actionOpenUrban.triggered.connect(self.openUrban)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Building simplify"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSimplify.setTitle(_translate("MainWindow", "Simplify"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpenCenter.setText(_translate("MainWindow", "Open center"))
        self.actionOpenCenter.setToolTip(_translate("MainWindow", "Open file with city center"))
        self.actionOpenCenter.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionOpenVilla.setText(_translate("MainWindow", "Open residential"))
        self.actionOpenVilla.setToolTip(_translate("MainWindow", "Open  with residential quarter"))
        self.actionOpenVilla.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionOpenUrban.setText(_translate("MainWindow", "Open flats"))
        self.actionOpenUrban.setToolTip(_translate("MainWindow", "Open file with blocks of flats"))
        self.actionOpenUrban.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionClose.setText(_translate("MainWindow", "Exit"))
        self.actionClose.setToolTip(_translate("MainWindow", "Close application"))
        self.actionMinimum_Area_Enclosing_Rectangle.setText(_translate("MainWindow", "Minimum Area Enclosing Rectangle"))
        self.actionMinimum_Area_Enclosing_Rectangle.setToolTip(_translate("MainWindow", "Simplify building using Minimum Area Enclosing Rectangle"))
        self.actionWall_Average.setText(_translate("MainWindow", "Wall Average"))
        self.actionWall_Average.setToolTip(_translate("MainWindow", "Simplify building using Wall Average"))
        self.actionLongest_Edge.setText(_translate("MainWindow", "Longest Edge"))
        self.actionLongest_Edge.setToolTip(_translate("MainWindow", "Simplify building using Longest Edge"))
        self.actionWeighted_Bisector.setText(_translate("MainWindow", "Weighted Bisector"))
        self.actionWeighted_Bisector.setToolTip(_translate("MainWindow", "Simplify building using Weighted Bisector"))
        self.actionGraham_Scan.setText(_translate("MainWindow", "Graham Scan"))
        self.actionGraham_Scan.setToolTip(_translate("MainWindow", "Create convex hull using Graham Scan"))
        self.actionClear.setText(_translate("MainWindow", "Clear"))
        self.actionClear.setToolTip(_translate("MainWindow", "Clear results"))
        self.actionClearData.setText(_translate("MainWindow", "Clear data"))
        self.actionClearData.setToolTip(_translate("MainWindow", "Clear all data"))


    def createMAER(self):
        a = Algorithms()

        self.Canvas.polRes.clear()

        if not self.Canvas.polisEmpty():
            pol = a.minAreaEnclosingRectangle(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        for p in self.Canvas.data.number():
            pol = a.minAreaEnclosingRectangle(self.Canvas.data.getPol(p))

            self.Canvas.polRes.append(pol)

        self.Canvas.repaint()

    def createWA(self):
        a = Algorithms()

        self.Canvas.polRes.clear()

        if not self.Canvas.polisEmpty():
            pol = a.wallAverage(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        for p in self.Canvas.data.number():
            pol = a.wallAverage(self.Canvas.data.getPol(p))

            self.Canvas.polRes.append(pol)

        self.Canvas.repaint()

    def createCHGS(self):
        a = Algorithms()

        self.Canvas.polRes.clear()

        if not self.Canvas.polisEmpty():
            pol = a.createCHGS(self.Canvas.getPolygon())  # a.minAreaEnclosingRectangle(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        for p in self.Canvas.data.number():
            pol = a.createCHGS(self.Canvas.data.getPol(p))  # a.minAreaEnclosingRectangle(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        self.Canvas.repaint()

    # def simplifyERClick (self):
    #     #Get polygon
    #     pol = ui.Canvas.getPolygon()
    #
    #     #Create convex hull
    #     a = Algorithms()
    #     er = a.minAreaEnclosingRectangle(pol)
    #
    #     #Set results and repaint
    #     ui.Canvas.setER(er)
    #     ui.Canvas.repaint()

    def simplifyLEClick (self):
        a = Algorithms()

        self.Canvas.polRes.clear()

        if not self.Canvas.polisEmpty():
            pol = a.longestEdge(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        for p in self.Canvas.data.number():
            pol = a.longestEdge(self.Canvas.data.getPol(p))

            self.Canvas.polRes.append(pol)

        self.Canvas.repaint()

    def simplifyWBClick(self):
        a = Algorithms()

        self.Canvas.polRes.clear()

        if not self.Canvas.polisEmpty():
            pol = a.weightedBisector(self.Canvas.getPolygon())

            self.Canvas.polRes.append(pol)

        for p in self.Canvas.data.number():
            pol = a.weightedBisector(self.Canvas.data.getPol(p))

            self.Canvas.polRes.append(pol)

        self.Canvas.repaint()

    def clearClick(self):
        #Clear all
        ui.Canvas.clearAll()
        ui.Canvas.repaint()

    def clearData(self):
        ui.Canvas.clearLoadedData()
        ui.Canvas.clearAll()
        ui.Canvas.repaint()


    def openCenter(self):
        old = self.Canvas.polisEmpty()
        if old == True:
            self.Canvas.input(data1)

    def openVilla(self):
        old = self.Canvas.polisEmpty()
        if old == True:
            self.Canvas.input(data3)

    def openUrban(self):
        old = self.Canvas.polisEmpty()
        if old == True:
            self.Canvas.input(data2)

    def close(self):
        quit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
