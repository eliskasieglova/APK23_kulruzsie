# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from draw import Draw
from algorithms import *

class Ui_MainForm(object):
    def setupUi(self, MainForm):
        MainForm.setObjectName("MainForm")
        MainForm.resize(1000, 700)
        self.centralwidget = QtWidgets.QWidget(MainForm)
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
        MainForm.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainForm)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 17))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuDraw = QtWidgets.QMenu(self.menubar)
        self.menuDraw.setObjectName("menuDraw")
        self.menuAnalyze = QtWidgets.QMenu(self.menubar)
        self.menuAnalyze.setObjectName("menuAnalyze")
        MainForm.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainForm)
        self.statusbar.setObjectName("statusbar")
        MainForm.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainForm)
        self.toolBar.setObjectName("toolBar")
        MainForm.addToolBar(QtCore.Qt.ToolBarArea.TopToolBarArea, self.toolBar)
        self.actionOpen = QtGui.QAction(MainForm)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/open_file.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionOpen.setIcon(icon)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtGui.QAction(MainForm)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/exit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionExit.setIcon(icon1)
        self.actionExit.setObjectName("actionExit")
        self.actionPoint_Polygon = QtGui.QAction(MainForm)
        self.actionPoint_Polygon.setCheckable(True)
        self.actionPoint_Polygon.setChecked(False)
        self.actionPoint_Polygon.setObjectName("actionPoint_Polygon")
        self.actionClear = QtGui.QAction(MainForm)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/clear.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionClear.setIcon(icon2)
        self.actionClear.setObjectName("actionClear")

        self.actionWindingNumber = QtGui.QAction(MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/wn.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionWindingNumber.setIcon(icon3)
        self.actionWindingNumber.setObjectName("actionWindingNumber")

        self.actionRayCrossing = QtGui.QAction(MainForm)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/rc.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actionRayCrossing.setIcon(icon3)
        self.actionRayCrossing.setObjectName("actionRayCrossing")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuDraw.addAction(self.actionPoint_Polygon)
        self.menuDraw.addAction(self.actionClear)
        self.menuAnalyze.addAction(self.actionRayCrossing)
        self.menuAnalyze.addAction(self.actionWindingNumber)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuDraw.menuAction())
        self.menubar.addAction(self.menuAnalyze.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRayCrossing)
        self.toolBar.addAction(self.actionWindingNumber)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        # Connect menu item and function
        self.actionPoint_Polygon.triggered.connect(self.switchSourceClick)
        self.actionRayCrossing.triggered.connect(self.analyzeClickR)
        self.actionWindingNumber.triggered.connect(self.analyzeClickW)
        self.actionOpen.triggered.connect(self.open)
        self.actionExit.triggered.connect(self.exit)
        self.actionClear.triggered.connect(self.clear)

        self.retranslateUi(MainForm)
        QtCore.QMetaObject.connectSlotsByName(MainForm)

    def retranslateUi(self, MainForm):
        _translate = QtCore.QCoreApplication.translate
        MainForm.setWindowTitle(_translate("MainForm", "Point and polygon position"))
        self.menuFile.setTitle(_translate("MainForm", "File"))
        self.menuDraw.setTitle(_translate("MainForm", "Draw"))
        self.menuAnalyze.setTitle(_translate("MainForm", "Analyze"))
        self.toolBar.setWindowTitle(_translate("MainForm", "toolBar"))
        self.actionOpen.setText(_translate("MainForm", "Open"))
        self.actionExit.setText(_translate("MainForm", "Exit"))
        self.actionPoint_Polygon.setText(_translate("MainForm", "Point/Polygon"))
        self.actionClear.setText(_translate("MainForm", "Clear"))
        self.actionRayCrossing.setText(_translate("MainForm", "Ray crossing method"))
        self.actionRayCrossing.setShortcut(_translate("MainForm", "Ctrl+R"))
        self.actionWindingNumber.setText(_translate("MainForm", "Winding number method"))
        self.actionWindingNumber.setShortcut(_translate("MainForm", "Ctrl+W"))



    def switchSourceClick(self):
        # change source
        self.Canvas.switchSource()

    def analyzeClickR(self):
        # analyze point and position

        # get point and polygon
        q = self.Canvas.getPoint()
        a = Algorithms()
        res = 0
        pol = 0
        border = False
        corner = False
        self.Canvas.polsNew.clear()
        n = self.Canvas.num()
        for p in n:
            pol = self.Canvas.getPolygon(p)

        # analyze position

            res = a.getPointPolygonPositionR(q, pol)

            if res == 1:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()

            if res == 2:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()
                border = True

            if res == 3:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()
                corner = True

        # print results
        if corner:
            border = False
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("On the corner")
            dialog.exec()

        if border:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("On the border")
            dialog.exec()


    def analyzeClickW(self):
        # analyze point and position

        # get point and polygon
        q = self.Canvas.getPoint()
        a = Algorithms()
        res = 0
        pol = 0
        border = False
        corner = False
        self.Canvas.polsNew.clear()
        n = self.Canvas.num()

        for p in n:
            pol = self.Canvas.getPolygon(p)

        # analyze position

            res = a.getPointPolygonPositionW(q, pol)

            if res == 1:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()

            if res == 2:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()
                border = True

            if res == 3:
                self.Canvas.polsNew.append(pol)
                self.Canvas.repaint()
                corner = True

        # print results
        if corner:
            border = False
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("On the corner")
            dialog.exec()

        if border:
            dialog = QtWidgets.QMessageBox()
            dialog.setWindowTitle("Warning")
            dialog.setText("On the border")
            dialog.exec()



    def open(self):
        self.Canvas.input()


    def exit(self):
        quit()

    def clear(self):
        self.Canvas.polsNew.clear()
        self.Canvas.repaint()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainForm = QtWidgets.QMainWindow()
    ui = Ui_MainForm()
    ui.setupUi(MainForm)
    MainForm.show()
    sys.exit(app.exec())