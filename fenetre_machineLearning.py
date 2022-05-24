# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\fenetre_machineLearning.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 825)
        MainWindow.setStyleSheet("background-color: rgb(16, 25, 30);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_3.setGeometry(QtCore.QRect(20, 100, 991, 701))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_3.setStyleSheet("QTabBar{border:none;}\n"
"QTabBar::tab {\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(16,25,30,255);\n"
"padding:5px 5px;\n"
"border-radius: 10px; }\n"
"\n"
" QTabBar::tab:selected, QTabBar::tab:hover {\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0.00502513 rgb(91, 125, 148), stop:1 rgba(200, 200, 200, 255));\n"
"color:rgb(28, 40, 48); }\n"
"")
        self.tabWidget_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.tabWidget_3.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.tableView_data = QtWidgets.QTableView(self.tab_11)
        self.tableView_data.setGeometry(QtCore.QRect(10, 356, 361, 226))
        self.tableView_data.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.tableView_data.setObjectName("tableView_data")
        self.plotOriginalSignals = MplWidget(self.tab_11)
        self.plotOriginalSignals.setGeometry(QtCore.QRect(390, 120, 561, 461))
        self.plotOriginalSignals.setStyleSheet("background-color:white")
        self.plotOriginalSignals.setObjectName("plotOriginalSignals")
        self.plotSignalButton = QtWidgets.QPushButton(self.tab_11)
        self.plotSignalButton.setGeometry(QtCore.QRect(579, 600, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.plotSignalButton.setFont(font)
        self.plotSignalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plotSignalButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.plotSignalButton.setObjectName("plotSignalButton")
        self.clearSignalButton = QtWidgets.QPushButton(self.tab_11)
        self.clearSignalButton.setGeometry(QtCore.QRect(672, 600, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.clearSignalButton.setFont(font)
        self.clearSignalButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearSignalButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.clearSignalButton.setObjectName("clearSignalButton")
        self.resetButton = QtWidgets.QPushButton(self.tab_11)
        self.resetButton.setGeometry(QtCore.QRect(60, 600, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.resetButton.setFont(font)
        self.resetButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resetButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.resetButton.setObjectName("resetButton")
        self.concatenateButton = QtWidgets.QPushButton(self.tab_11)
        self.concatenateButton.setGeometry(QtCore.QRect(210, 600, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.concatenateButton.setFont(font)
        self.concatenateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.concatenateButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.concatenateButton.setObjectName("concatenateButton")
        self.acq_box = QtWidgets.QGroupBox(self.tab_11)
        self.acq_box.setGeometry(QtCore.QRect(436, 10, 491, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box.setFont(font)
        self.acq_box.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box.setTitle("")
        self.acq_box.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box.setFlat(False)
        self.acq_box.setObjectName("acq_box")
        self.stop_img_acq_button = QtWidgets.QPushButton(self.acq_box)
        self.stop_img_acq_button.setGeometry(QtCore.QRect(390, 220, 191, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stop_img_acq_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stop_img_acq_button.setFont(font)
        self.stop_img_acq_button.setStyleSheet("\n"
"background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
" border-radius: 10px;\n"
"")
        self.stop_img_acq_button.setObjectName("stop_img_acq_button")
        self.frame = QtWidgets.QFrame(self.acq_box)
        self.frame.setGeometry(QtCore.QRect(0, 0, 491, 30))
        self.frame.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(0, 0, 491, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.openButton_load = QtWidgets.QToolButton(self.acq_box)
        self.openButton_load.setGeometry(QtCore.QRect(40, 40, 61, 41))
        self.openButton_load.setMinimumSize(QtCore.QSize(61, 41))
        self.openButton_load.setMaximumSize(QtCore.QSize(61, 41))
        self.openButton_load.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openButton_load.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image : url(:/folder.png);\n"
"background-color:rgba(40,55,65,255);\n"
"border-radius: 20px;")
        self.openButton_load.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../ProjetMistrasEUROSONIC/images/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton_load.setIcon(icon)
        self.openButton_load.setIconSize(QtCore.QSize(50, 50))
        self.openButton_load.setObjectName("openButton_load")
        self.fileLoadedPath = QtWidgets.QLineEdit(self.acq_box)
        self.fileLoadedPath.setGeometry(QtCore.QRect(117, 46, 241, 30))
        self.fileLoadedPath.setStyleSheet("background-color:rgba(16,25,30,255);\n"
"selection-background-color: rgba(16,25,30,255);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.fileLoadedPath.setObjectName("fileLoadedPath")
        self.checkloadTrain = QtWidgets.QCheckBox(self.acq_box)
        self.checkloadTrain.setGeometry(QtCore.QRect(390, 40, 21, 21))
        self.checkloadTrain.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkloadTrain.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.checkloadTrain.setChecked(True)
        self.checkloadTrain.setAutoExclusive(True)
        self.checkloadTrain.setObjectName("checkloadTrain")
        self.checkloadTest = QtWidgets.QCheckBox(self.acq_box)
        self.checkloadTest.setGeometry(QtCore.QRect(390, 70, 21, 21))
        self.checkloadTest.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkloadTest.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.checkloadTest.setAutoExclusive(True)
        self.checkloadTest.setObjectName("checkloadTest")
        self.label_30 = QtWidgets.QLabel(self.acq_box)
        self.label_30.setGeometry(QtCore.QRect(421, 42, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_30.setFont(font)
        self.label_30.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(self.acq_box)
        self.label_31.setGeometry(QtCore.QRect(420, 73, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_31.setFont(font)
        self.label_31.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_31.setObjectName("label_31")
        self.frame.raise_()
        self.stop_img_acq_button.raise_()
        self.openButton_load.raise_()
        self.fileLoadedPath.raise_()
        self.checkloadTrain.raise_()
        self.checkloadTest.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.acq_box_2 = QtWidgets.QGroupBox(self.tab_11)
        self.acq_box_2.setGeometry(QtCore.QRect(10, 9, 361, 331))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box_2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box_2.setFont(font)
        self.acq_box_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box_2.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box_2.setTitle("")
        self.acq_box_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box_2.setFlat(False)
        self.acq_box_2.setObjectName("acq_box_2")
        self.frame_2 = QtWidgets.QFrame(self.acq_box_2)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 361, 30))
        self.frame_2.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_21 = QtWidgets.QLabel(self.frame_2)
        self.label_21.setGeometry(QtCore.QRect(0, 0, 361, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.listLoadData = QtWidgets.QListWidget(self.acq_box_2)
        self.listLoadData.setGeometry(QtCore.QRect(10, 96, 211, 81))
        self.listLoadData.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"")
        self.listLoadData.setObjectName("listLoadData")
        self.listTargets = QtWidgets.QListWidget(self.acq_box_2)
        self.listTargets.setGeometry(QtCore.QRect(264, 96, 71, 81))
        self.listTargets.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
"border: 0px solid white;\n"
"")
        self.listTargets.setObjectName("listTargets")
        self.label_6 = QtWidgets.QLabel(self.acq_box_2)
        self.label_6.setGeometry(QtCore.QRect(10, 42, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_18 = QtWidgets.QLabel(self.acq_box_2)
        self.label_18.setGeometry(QtCore.QRect(268, 42, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_18.setFont(font)
        self.label_18.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.line = QtWidgets.QFrame(self.acq_box_2)
        self.line.setGeometry(QtCore.QRect(10, 188, 341, 16))
        self.line.setStyleSheet("background-color: rgb(28, 40, 48);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.listLoadData_test = QtWidgets.QListWidget(self.acq_box_2)
        self.listLoadData_test.setGeometry(QtCore.QRect(10, 230, 211, 81))
        self.listLoadData_test.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"")
        self.listLoadData_test.setObjectName("listLoadData_test")
        self.listTargets_test = QtWidgets.QListWidget(self.acq_box_2)
        self.listTargets_test.setGeometry(QtCore.QRect(264, 230, 71, 81))
        self.listTargets_test.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
"border: 0px solid white;\n"
"")
        self.listTargets_test.setObjectName("listTargets_test")
        self.label_4 = QtWidgets.QLabel(self.acq_box_2)
        self.label_4.setGeometry(QtCore.QRect(10, 205, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.acq_box_2)
        self.label_5.setGeometry(QtCore.QRect(10, 70, 321, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.statusConcat = QtWidgets.QLabel(self.tab_11)
        self.statusConcat.setGeometry(QtCore.QRect(176, 640, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setBold(True)
        font.setWeight(75)
        self.statusConcat.setFont(font)
        self.statusConcat.setStyleSheet("color: rgb(255, 227, 82)\n"
"")
        self.statusConcat.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.statusConcat.setObjectName("statusConcat")
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_2.setGeometry(QtCore.QRect(260, 60, 171, 221))
        self.groupBox_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_2.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.check_t_Amp = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_t_Amp.setGeometry(QtCore.QRect(10, 60, 21, 21))
        self.check_t_Amp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_t_Amp.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_t_Amp.setObjectName("check_t_Amp")
        self.check_t_LMH = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_t_LMH.setGeometry(QtCore.QRect(10, 90, 21, 21))
        self.check_t_LMH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_t_LMH.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_t_LMH.setObjectName("check_t_LMH")
        self.check_t_RMS = QtWidgets.QCheckBox(self.groupBox_2)
        self.check_t_RMS.setGeometry(QtCore.QRect(10, 30, 21, 21))
        self.check_t_RMS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_t_RMS.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_t_RMS.setObjectName("check_t_RMS")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(0, 0, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(40, 65, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(40, 95, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setGeometry(QtCore.QRect(40, 35, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_3.setGeometry(QtCore.QRect(440, 60, 211, 221))
        self.groupBox_3.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.check_f_RMS = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_f_RMS.setGeometry(QtCore.QRect(30, 30, 21, 21))
        self.check_f_RMS.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_f_RMS.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_f_RMS.setObjectName("check_f_RMS")
        self.check_f_Amp = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_f_Amp.setGeometry(QtCore.QRect(30, 60, 21, 21))
        self.check_f_Amp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_f_Amp.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_f_Amp.setObjectName("check_f_Amp")
        self.check_f_LMH = QtWidgets.QCheckBox(self.groupBox_3)
        self.check_f_LMH.setGeometry(QtCore.QRect(30, 90, 21, 21))
        self.check_f_LMH.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_f_LMH.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_f_LMH.setObjectName("check_f_LMH")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(62, 35, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(60, 65, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(60, 95, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_13.setFont(font)
        self.label_13.setToolTip("")
        self.label_13.setStatusTip("")
        self.label_13.setWhatsThis("")
        self.label_13.setObjectName("label_13")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_4.setGeometry(QtCore.QRect(660, 60, 261, 221))
        self.groupBox_4.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.saveButton = QtWidgets.QPushButton(self.tab_5)
        self.saveButton.setGeometry(QtCore.QRect(520, 610, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.saveButton.setObjectName("saveButton")
        self.generateButton = QtWidgets.QPushButton(self.tab_5)
        self.generateButton.setGeometry(QtCore.QRect(384, 610, 111, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.generateButton.setFont(font)
        self.generateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.generateButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.generateButton.setObjectName("generateButton")
        self.tableView_features = QtWidgets.QTableView(self.tab_5)
        self.tableView_features.setGeometry(QtCore.QRect(30, 330, 931, 271))
        self.tableView_features.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.tableView_features.setObjectName("tableView_features")
        self.cocherButton = QtWidgets.QPushButton(self.tab_5)
        self.cocherButton.setGeometry(QtCore.QRect(400, 295, 141, 25))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.cocherButton.setFont(font)
        self.cocherButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cocherButton.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.cocherButton.setObjectName("cocherButton")
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_5)
        self.groupBox_5.setGeometry(QtCore.QRect(80, 60, 171, 221))
        self.groupBox_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox_5.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.check_madian = QtWidgets.QCheckBox(self.groupBox_5)
        self.check_madian.setGeometry(QtCore.QRect(10, 60, 21, 21))
        self.check_madian.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_madian.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_madian.setObjectName("check_madian")
        self.check_var = QtWidgets.QCheckBox(self.groupBox_5)
        self.check_var.setGeometry(QtCore.QRect(10, 90, 21, 21))
        self.check_var.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_var.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_var.setObjectName("check_var")
        self.check_mean = QtWidgets.QCheckBox(self.groupBox_5)
        self.check_mean.setGeometry(QtCore.QRect(10, 30, 21, 21))
        self.check_mean.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_mean.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_mean.setObjectName("check_mean")
        self.label_32 = QtWidgets.QLabel(self.groupBox_5)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_32.setFont(font)
        self.label_32.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        self.label_33.setGeometry(QtCore.QRect(40, 65, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        self.label_34.setGeometry(QtCore.QRect(40, 95, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        self.label_35.setGeometry(QtCore.QRect(40, 35, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.check_std = QtWidgets.QCheckBox(self.groupBox_5)
        self.check_std.setGeometry(QtCore.QRect(10, 120, 21, 21))
        self.check_std.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.check_std.setStyleSheet("QCheckBox{\n"
"color:rgb(91,125,148);\n"
"background-color:rgba(91,125,148,255);\n"
"border-radius: 100px;\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"\n"
"\n"
"border: 2px solid black;\n"
"\n"
"width: 15px;\n"
"\n"
"height: 15px;\n"
"\n"
"subcontrol-position: center;\n"
"\n"
"\n"
"\n"
"subcontrol-origin: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked{\n"
"\n"
"background-color:white;\n"
"\n"
"border:5px white;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked{\n"
"\n"
"background-color:rgb(28, 40, 48);\n"
"\n"
"\n"
"border:5px black;\n"
"\n"
"}")
        self.check_std.setObjectName("check_std")
        self.label_36 = QtWidgets.QLabel(self.groupBox_5)
        self.label_36.setGeometry(QtCore.QRect(40, 125, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget_5 = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget_5.setGeometry(QtCore.QRect(10, 90, 911, 561))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_5.setFont(font)
        self.tabWidget_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_5.setStyleSheet("")
        self.tabWidget_5.setObjectName("tabWidget_5")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.visualData = MplWidget(self.tab_9)
        self.visualData.setGeometry(QtCore.QRect(130, 20, 581, 381))
        self.visualData.setStyleSheet("background-color:white")
        self.visualData.setObjectName("visualData")
        self.acq_box_4 = QtWidgets.QGroupBox(self.tab_9)
        self.acq_box_4.setGeometry(QtCore.QRect(210, 420, 461, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box_4.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box_4.setFont(font)
        self.acq_box_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box_4.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box_4.setTitle("")
        self.acq_box_4.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box_4.setFlat(False)
        self.acq_box_4.setObjectName("acq_box_4")
        self.stop_img_acq_button_3 = QtWidgets.QPushButton(self.acq_box_4)
        self.stop_img_acq_button_3.setGeometry(QtCore.QRect(390, 220, 191, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stop_img_acq_button_3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stop_img_acq_button_3.setFont(font)
        self.stop_img_acq_button_3.setStyleSheet("\n"
"background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
" border-radius: 10px;\n"
"")
        self.stop_img_acq_button_3.setObjectName("stop_img_acq_button_3")
        self.frame_4 = QtWidgets.QFrame(self.acq_box_4)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 461, 30))
        self.frame_4.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_25 = QtWidgets.QLabel(self.frame_4)
        self.label_25.setGeometry(QtCore.QRect(0, 0, 461, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.visualDataY = QtWidgets.QComboBox(self.acq_box_4)
        self.visualDataY.setGeometry(QtCore.QRect(240, 54, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.visualDataY.setFont(font)
        self.visualDataY.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualDataY.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.visualDataY.setObjectName("visualDataY")
        self.visualDataX = QtWidgets.QComboBox(self.acq_box_4)
        self.visualDataX.setGeometry(QtCore.QRect(20, 55, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.visualDataX.setFont(font)
        self.visualDataX.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualDataX.setStyleSheet("color: rgb(91, 125, 148);\n"
"")
        self.visualDataX.setObjectName("visualDataX")
        self.label_26 = QtWidgets.QLabel(self.acq_box_4)
        self.label_26.setGeometry(QtCore.QRect(20, 30, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.acq_box_4)
        self.label_27.setGeometry(QtCore.QRect(240, 30, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_27.setStyleSheet("color: rgb(91, 125, 148);\n"
"background-color: rgb(28, 40, 48);")
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.tabWidget_5.addTab(self.tab_9, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.matrixCorrelation = MplWidget(self.tab_10)
        self.matrixCorrelation.setGeometry(QtCore.QRect(130, 40, 741, 451))
        self.matrixCorrelation.setStyleSheet("background-color:white")
        self.matrixCorrelation.setObjectName("matrixCorrelation")
        self.tabWidget_5.addTab(self.tab_10, "")
        self.acq_box_3 = QtWidgets.QGroupBox(self.tab_3)
        self.acq_box_3.setGeometry(QtCore.QRect(300, 6, 391, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box_3.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box_3.setFont(font)
        self.acq_box_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box_3.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box_3.setTitle("")
        self.acq_box_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box_3.setFlat(False)
        self.acq_box_3.setObjectName("acq_box_3")
        self.stop_img_acq_button_2 = QtWidgets.QPushButton(self.acq_box_3)
        self.stop_img_acq_button_2.setGeometry(QtCore.QRect(390, 220, 191, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stop_img_acq_button_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stop_img_acq_button_2.setFont(font)
        self.stop_img_acq_button_2.setStyleSheet("\n"
"background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
" border-radius: 10px;\n"
"")
        self.stop_img_acq_button_2.setObjectName("stop_img_acq_button_2")
        self.frame_3 = QtWidgets.QFrame(self.acq_box_3)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 391, 30))
        self.frame_3.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_24 = QtWidgets.QLabel(self.frame_3)
        self.label_24.setGeometry(QtCore.QRect(0, 0, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.openButton_featFile = QtWidgets.QToolButton(self.acq_box_3)
        self.openButton_featFile.setGeometry(QtCore.QRect(20, 40, 61, 41))
        self.openButton_featFile.setMinimumSize(QtCore.QSize(61, 41))
        self.openButton_featFile.setMaximumSize(QtCore.QSize(61, 41))
        self.openButton_featFile.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.openButton_featFile.setStyleSheet("background-repeat: no-repeat;\n"
"background-position: center;\n"
"background-image : url(:/folder.png);\n"
"background-color:rgba(40,55,65,255);\n"
"border-radius: 20px;")
        self.openButton_featFile.setText("")
        self.openButton_featFile.setIcon(icon)
        self.openButton_featFile.setIconSize(QtCore.QSize(50, 50))
        self.openButton_featFile.setObjectName("openButton_featFile")
        self.featFile_path_feats = QtWidgets.QLineEdit(self.acq_box_3)
        self.featFile_path_feats.setGeometry(QtCore.QRect(120, 46, 241, 31))
        self.featFile_path_feats.setStyleSheet("background-color:rgba(16,25,30,255);\n"
"selection-background-color: rgba(16,25,30,255);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.featFile_path_feats.setObjectName("featFile_path_feats")
        self.tabWidget_3.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 951, 651))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pipelineClassif = QtWidgets.QGroupBox(self.tab)
        self.pipelineClassif.setGeometry(QtCore.QRect(120, 20, 551, 121))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.pipelineClassif.setFont(font)
        self.pipelineClassif.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.pipelineClassif.setTitle("")
        self.pipelineClassif.setAlignment(QtCore.Qt.AlignCenter)
        self.pipelineClassif.setObjectName("pipelineClassif")
        self.transformerCombo = QtWidgets.QComboBox(self.pipelineClassif)
        self.transformerCombo.setGeometry(QtCore.QRect(30, 50, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.transformerCombo.setFont(font)
        self.transformerCombo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.transformerCombo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.transformerCombo.setStyleSheet("\n"
"color: rgb(91, 125, 148);")
        self.transformerCombo.setObjectName("transformerCombo")
        self.transformerCombo.addItem("")
        self.transformerCombo.addItem("")
        self.estimatorCombo = QtWidgets.QComboBox(self.pipelineClassif)
        self.estimatorCombo.setGeometry(QtCore.QRect(300, 50, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.estimatorCombo.setFont(font)
        self.estimatorCombo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.estimatorCombo.setStyleSheet("\n"
"color: rgb(91, 125, 148);")
        self.estimatorCombo.setObjectName("estimatorCombo")
        self.estimatorCombo.addItem("")
        self.estimatorCombo.addItem("")
        self.estimatorCombo.addItem("")
        self.estimatorCombo.addItem("")
        self.estimatorCombo.addItem("")
        self.label = QtWidgets.QLabel(self.pipelineClassif)
        self.label.setGeometry(QtCore.QRect(30, 30, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(91, 125, 148);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.pipelineClassif)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_10 = QtWidgets.QLabel(self.pipelineClassif)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.trainButton = QtWidgets.QPushButton(self.tab)
        self.trainButton.setGeometry(QtCore.QRect(100, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.trainButton.setFont(font)
        self.trainButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trainButton.setStyleSheet("color: rgb(91, 125, 148);")
        self.trainButton.setObjectName("trainButton")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab)
        self.tabWidget_2.setGeometry(QtCore.QRect(400, 160, 511, 451))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tabWidget_2.setStyleSheet("background-color: rgb(16, 25, 30);")
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.Score = QtWidgets.QWidget()
        self.Score.setObjectName("Score")
        self.graphScore = MplWidget(self.Score)
        self.graphScore.setGeometry(QtCore.QRect(20, 20, 431, 371))
        self.graphScore.setStyleSheet("background-color:white")
        self.graphScore.setObjectName("graphScore")
        self.tabWidget_2.addTab(self.Score, "")
        self.MatriceDeConfusion = QtWidgets.QWidget()
        self.MatriceDeConfusion.setObjectName("MatriceDeConfusion")
        self.graphConfusion = MplWidget(self.MatriceDeConfusion)
        self.graphConfusion.setGeometry(QtCore.QRect(20, 5, 471, 411))
        self.graphConfusion.setStyleSheet("background-color:white")
        self.graphConfusion.setObjectName("graphConfusion")
        self.tabWidget_2.addTab(self.MatriceDeConfusion, "")
        self.acq_box_5 = QtWidgets.QGroupBox(self.tab)
        self.acq_box_5.setGeometry(QtCore.QRect(30, 240, 330, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box_5.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box_5.setFont(font)
        self.acq_box_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box_5.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box_5.setTitle("")
        self.acq_box_5.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box_5.setFlat(False)
        self.acq_box_5.setObjectName("acq_box_5")
        self.stop_img_acq_button_4 = QtWidgets.QPushButton(self.acq_box_5)
        self.stop_img_acq_button_4.setGeometry(QtCore.QRect(390, 220, 191, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stop_img_acq_button_4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stop_img_acq_button_4.setFont(font)
        self.stop_img_acq_button_4.setStyleSheet("\n"
"background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
" border-radius: 10px;\n"
"")
        self.stop_img_acq_button_4.setObjectName("stop_img_acq_button_4")
        self.frame_5 = QtWidgets.QFrame(self.acq_box_5)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 331, 30))
        self.frame_5.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_28 = QtWidgets.QLabel(self.frame_5)
        self.label_28.setGeometry(QtCore.QRect(0, 0, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.outputText = QtWidgets.QTextBrowser(self.acq_box_5)
        self.outputText.setGeometry(QtCore.QRect(9, 59, 311, 151))
        self.outputText.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputText.setStyleSheet("color:white")
        self.outputText.setObjectName("outputText")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pipelineClassif_2 = QtWidgets.QGroupBox(self.tab_2)
        self.pipelineClassif_2.setGeometry(QtCore.QRect(130, 20, 551, 121))
        self.pipelineClassif_2.setStyleSheet("background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;")
        self.pipelineClassif_2.setTitle("")
        self.pipelineClassif_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pipelineClassif_2.setObjectName("pipelineClassif_2")
        self.transformerCombo_2 = QtWidgets.QComboBox(self.pipelineClassif_2)
        self.transformerCombo_2.setGeometry(QtCore.QRect(30, 50, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.transformerCombo_2.setFont(font)
        self.transformerCombo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.transformerCombo_2.setStyleSheet("\n"
"color: rgb(91, 125, 148);")
        self.transformerCombo_2.setObjectName("transformerCombo_2")
        self.transformerCombo_2.addItem("")
        self.transformerCombo_2.addItem("")
        self.estimatorCombo_2 = QtWidgets.QComboBox(self.pipelineClassif_2)
        self.estimatorCombo_2.setGeometry(QtCore.QRect(300, 50, 221, 22))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.estimatorCombo_2.setFont(font)
        self.estimatorCombo_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.estimatorCombo_2.setStyleSheet("\n"
"color: rgb(91, 125, 148);")
        self.estimatorCombo_2.setObjectName("estimatorCombo_2")
        self.estimatorCombo_2.addItem("")
        self.estimatorCombo_2.addItem("")
        self.estimatorCombo_2.addItem("")
        self.estimatorCombo_2.addItem("")
        self.label_19 = QtWidgets.QLabel(self.pipelineClassif_2)
        self.label_19.setGeometry(QtCore.QRect(30, 30, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_19.setFont(font)
        self.label_19.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.label_22 = QtWidgets.QLabel(self.pipelineClassif_2)
        self.label_22.setGeometry(QtCore.QRect(300, 30, 221, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_22.setFont(font)
        self.label_22.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.pipelineClassif_2)
        self.label_23.setGeometry(QtCore.QRect(0, 0, 551, 20))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("background-color: rgba(40,55,65,255);\n"
"\n"
"\n"
"\n"
"color: rgb(91, 125, 148);\n"
"\n"
"\n"
"\n"
"border-top-left-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-top-right-radius: 10px;\n"
"\n"
"\n"
"\n"
"border-bottom-left-radius: 1px;\n"
"\n"
"\n"
"\n"
"border-bottom-right-radius: 1px;")
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.trainRegreButton = QtWidgets.QPushButton(self.tab_2)
        self.trainRegreButton.setGeometry(QtCore.QRect(71, 190, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.trainRegreButton.setFont(font)
        self.trainRegreButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.trainRegreButton.setStyleSheet("color: rgb(91, 125, 148);")
        self.trainRegreButton.setObjectName("trainRegreButton")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_2)
        self.tabWidget_4.setGeometry(QtCore.QRect(390, 150, 531, 461))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setStyleSheet("background-color: rgb(16, 25, 30);")
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.Score_2 = QtWidgets.QWidget()
        self.Score_2.setObjectName("Score_2")
        self.graphResultRegression = MplWidget(self.Score_2)
        self.graphResultRegression.setGeometry(QtCore.QRect(23, 7, 481, 421))
        self.graphResultRegression.setStyleSheet("background-color:white")
        self.graphResultRegression.setObjectName("graphResultRegression")
        self.tabWidget_4.addTab(self.Score_2, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.graphTestRegression = MplWidget(self.tab_6)
        self.graphTestRegression.setGeometry(QtCore.QRect(10, 3, 511, 361))
        self.graphTestRegression.setStyleSheet("background-color:white")
        self.graphTestRegression.setObjectName("graphTestRegression")
        self.featsTestPlot_combo = QtWidgets.QComboBox(self.tab_6)
        self.featsTestPlot_combo.setGeometry(QtCore.QRect(203, 370, 150, 31))
        self.featsTestPlot_combo.setStyleSheet("\n"
"color: rgb(91, 125, 148);")
        self.featsTestPlot_combo.setObjectName("featsTestPlot_combo")
        self.tabWidget_4.addTab(self.tab_6, "")
        self.acq_box_6 = QtWidgets.QGroupBox(self.tab_2)
        self.acq_box_6.setGeometry(QtCore.QRect(30, 240, 330, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(28, 40, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.acq_box_6.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.acq_box_6.setFont(font)
        self.acq_box_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.acq_box_6.setStyleSheet("QGroupBox{\n"
"background-color: rgb(28, 40, 48);\n"
"color: rgb(91, 125, 148);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"\n"
"background-color:rgba(40,55,65,255);\n"
"\n"
"\n"
"} \n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.acq_box_6.setTitle("")
        self.acq_box_6.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.acq_box_6.setFlat(False)
        self.acq_box_6.setObjectName("acq_box_6")
        self.stop_img_acq_button_5 = QtWidgets.QPushButton(self.acq_box_6)
        self.stop_img_acq_button_5.setGeometry(QtCore.QRect(390, 220, 191, 81))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(91, 125, 148))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 55, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.stop_img_acq_button_5.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.stop_img_acq_button_5.setFont(font)
        self.stop_img_acq_button_5.setStyleSheet("\n"
"background-color:rgba(40,55,65,255);\n"
"color: rgb(91, 125, 148);\n"
" border-radius: 10px;\n"
"")
        self.stop_img_acq_button_5.setObjectName("stop_img_acq_button_5")
        self.frame_6 = QtWidgets.QFrame(self.acq_box_6)
        self.frame_6.setGeometry(QtCore.QRect(0, 0, 331, 30))
        self.frame_6.setStyleSheet("background-color:rgba(40,55,65,255);\n"
"border-top-left-radius :10px;\n"
"border-top-right-radius : 10px; \n"
"border-bottom-left-radius : 1px; \n"
"border-bottom-right-radius : 1px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setGeometry(QtCore.QRect(0, 0, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet("color: rgb(91, 125, 148);")
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.outputText_2 = QtWidgets.QTextBrowser(self.acq_box_6)
        self.outputText_2.setGeometry(QtCore.QRect(10, 60, 311, 151))
        self.outputText_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.outputText_2.setStyleSheet("color:white")
        self.outputText_2.setObjectName("outputText_2")
        self.testRegressionButton = QtWidgets.QPushButton(self.tab_2)
        self.testRegressionButton.setGeometry(QtCore.QRect(220, 190, 120, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.testRegressionButton.setFont(font)
        self.testRegressionButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.testRegressionButton.setStyleSheet("color: rgb(91, 125, 148);")
        self.testRegressionButton.setObjectName("testRegressionButton")
        self.tabWidget.addTab(self.tab_2, "")
        self.tabWidget_3.addTab(self.tab_4, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.tabWidget_3.addTab(self.tab_12, "")
        self.horizontalFrame = QtWidgets.QFrame(self.centralwidget)
        self.horizontalFrame.setGeometry(QtCore.QRect(0, 0, 1020, 91))
        self.horizontalFrame.setStyleSheet("background-color:rgba(40,55,65,255);")
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_17 = QtWidgets.QLabel(self.horizontalFrame)
        self.label_17.setMaximumSize(QtCore.QSize(300, 100))
        self.label_17.setText("")
        self.label_17.setPixmap(QtGui.QPixmap(":/logo.PNG"))
        self.label_17.setScaledContents(True)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.label_3 = QtWidgets.QLabel(self.horizontalFrame)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.cocherButton.clicked.connect(self.check_t_RMS.toggle)
        self.cocherButton.clicked.connect(self.check_t_Amp.toggle)
        self.cocherButton.clicked.connect(self.check_t_LMH.toggle)
        self.cocherButton.clicked.connect(self.check_f_LMH.toggle)
        self.cocherButton.clicked.connect(self.check_f_RMS.toggle)
        self.cocherButton.clicked.connect(self.check_f_Amp.toggle)
        self.concatenateButton.clicked.connect(self.statusConcat.show)
        self.resetButton.clicked.connect(self.statusConcat.hide)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Accèss IA Signaux"))
        self.plotSignalButton.setText(_translate("MainWindow", "Plot"))
        self.clearSignalButton.setText(_translate("MainWindow", "Effacer"))
        self.resetButton.setText(_translate("MainWindow", "Réinitialiser"))
        self.concatenateButton.setText(_translate("MainWindow", "Concaténer"))
        self.stop_img_acq_button.setText(_translate("MainWindow", "Stop Acquisition"))
        self.label_20.setText(_translate("MainWindow", "Signaux originaux"))
        self.checkloadTrain.setText(_translate("MainWindow", "f_RMS"))
        self.checkloadTest.setText(_translate("MainWindow", "f_RMS"))
        self.label_30.setText(_translate("MainWindow", "Train"))
        self.label_31.setText(_translate("MainWindow", "Test"))
        self.label_21.setText(_translate("MainWindow", "Liste des fichiers"))
        self.label_6.setText(_translate("MainWindow", "Fichiers:"))
        self.label_18.setText(_translate("MainWindow", "Target:"))
        self.label_4.setText(_translate("MainWindow", "Test Dataset"))
        self.label_5.setText(_translate("MainWindow", "Train Dataset"))
        self.statusConcat.setText(_translate("MainWindow", "Concaténation en cours..."))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MainWindow", "Chargement des données"))
        self.check_t_Amp.setText(_translate("MainWindow", "t_Ampliude max + temps"))
        self.check_t_LMH.setText(_translate("MainWindow", "t_LMH"))
        self.check_t_RMS.setText(_translate("MainWindow", "t_RMS"))
        self.label_8.setText(_translate("MainWindow", "Domaine temporel"))
        self.label_14.setText(_translate("MainWindow", "t_(Amp_max,t_max)"))
        self.label_15.setText(_translate("MainWindow", "t_LMH"))
        self.label_16.setText(_translate("MainWindow", "t_RMS"))
        self.check_f_RMS.setText(_translate("MainWindow", "f_RMS"))
        self.check_f_Amp.setText(_translate("MainWindow", "f_Amplitude max + frequence"))
        self.check_f_LMH.setStatusTip(_translate("MainWindow", "Fréquence LMH"))
        self.check_f_LMH.setWhatsThis(_translate("MainWindow", "Fréquence LMH"))
        self.check_f_LMH.setText(_translate("MainWindow", "f_LMH"))
        self.label_7.setText(_translate("MainWindow", "Domaine fréquentiel"))
        self.label_11.setText(_translate("MainWindow", "f_RMS"))
        self.label_12.setText(_translate("MainWindow", "f_(Amp_max,f_max)"))
        self.label_13.setText(_translate("MainWindow", "f_LMH"))
        self.label_9.setText(_translate("MainWindow", "Ondelettes (wavelet)"))
        self.saveButton.setText(_translate("MainWindow", "Sauvegarder"))
        self.generateButton.setText(_translate("MainWindow", "Générer"))
        self.cocherButton.setText(_translate("MainWindow", "Tout cocher /décocher"))
        self.check_madian.setText(_translate("MainWindow", "t_Ampliude max + temps"))
        self.check_var.setText(_translate("MainWindow", "t_LMH"))
        self.check_mean.setText(_translate("MainWindow", "t_RMS"))
        self.label_32.setText(_translate("MainWindow", "Statistiques"))
        self.label_33.setText(_translate("MainWindow", "median"))
        self.label_34.setText(_translate("MainWindow", "var"))
        self.label_35.setText(_translate("MainWindow", "mean"))
        self.check_std.setText(_translate("MainWindow", "t_LMH"))
        self.label_36.setText(_translate("MainWindow", "std"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), _translate("MainWindow", "Extractions des caractéristiques"))
        self.stop_img_acq_button_3.setText(_translate("MainWindow", "Stop Acquisition"))
        self.label_25.setText(_translate("MainWindow", "Choix des axes"))
        self.label_26.setText(_translate("MainWindow", "Abscisses:"))
        self.label_27.setText(_translate("MainWindow", "Ordonnées:"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9), _translate("MainWindow", "Caractéristiques"))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_10), _translate("MainWindow", "Matrice de corrélation"))
        self.stop_img_acq_button_2.setText(_translate("MainWindow", "Stop Acquisition"))
        self.label_24.setText(_translate("MainWindow", "Chargement des features"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_3), _translate("MainWindow", "Visualisation des caractéristiques"))
        self.transformerCombo.setItemText(0, _translate("MainWindow", "PolynomialFeatures"))
        self.transformerCombo.setItemText(1, _translate("MainWindow", "None"))
        self.estimatorCombo.setItemText(0, _translate("MainWindow", "RandomForest"))
        self.estimatorCombo.setItemText(1, _translate("MainWindow", "LogisticRegression"))
        self.estimatorCombo.setItemText(2, _translate("MainWindow", "AdaBoost"))
        self.estimatorCombo.setItemText(3, _translate("MainWindow", "SVM"))
        self.estimatorCombo.setItemText(4, _translate("MainWindow", "KNN"))
        self.label.setText(_translate("MainWindow", "Transformer"))
        self.label_2.setText(_translate("MainWindow", "Estimator"))
        self.label_10.setText(_translate("MainWindow", "Pipeline"))
        self.trainButton.setText(_translate("MainWindow", "Entraînement"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Score), _translate("MainWindow", "Score"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.MatriceDeConfusion), _translate("MainWindow", "Matrice de confusion"))
        self.stop_img_acq_button_4.setText(_translate("MainWindow", "Stop Acquisition"))
        self.label_28.setText(_translate("MainWindow", "Résultats"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Classification"))
        self.transformerCombo_2.setItemText(0, _translate("MainWindow", "None"))
        self.transformerCombo_2.setItemText(1, _translate("MainWindow", "PolynomialFeatures"))
        self.estimatorCombo_2.setItemText(0, _translate("MainWindow", "None"))
        self.estimatorCombo_2.setItemText(1, _translate("MainWindow", "LinearRegression"))
        self.estimatorCombo_2.setItemText(2, _translate("MainWindow", "Ridge"))
        self.estimatorCombo_2.setItemText(3, _translate("MainWindow", "Lasso"))
        self.label_19.setText(_translate("MainWindow", "Transformer"))
        self.label_22.setText(_translate("MainWindow", "Estimator"))
        self.label_23.setText(_translate("MainWindow", "Pipeline"))
        self.trainRegreButton.setText(_translate("MainWindow", "Entraînement"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.Score_2), _translate("MainWindow", "Résultat Target"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_6), _translate("MainWindow", "Résultat Caractéristiques"))
        self.stop_img_acq_button_5.setText(_translate("MainWindow", "Stop Acquisition"))
        self.label_29.setText(_translate("MainWindow", "Résultats"))
        self.testRegressionButton.setText(_translate("MainWindow", "Test"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Régression"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_4), _translate("MainWindow", "Machine Learning"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MainWindow", "Deep Learning"))
        self.label_3.setText(_translate("MainWindow", "AccessIA Signaux"))

from mplwidget import MplWidget
import resources_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

