# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 1000))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setStyleSheet("image: url(:/images/roboter.png);\n"
"\n"
"height: auto;\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.verticalLayout.addWidget(self.widget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btnLeft = QtWidgets.QPushButton(self.centralwidget)
        self.btnLeft.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/corner-up-left.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLeft.setIcon(icon)
        self.btnLeft.setIconSize(QtCore.QSize(64, 64))
        self.btnLeft.setObjectName("btnLeft")
        self.gridLayout.addWidget(self.btnLeft, 1, 0, 1, 1)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/stop-circle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnStop.setIcon(icon1)
        self.btnStop.setIconSize(QtCore.QSize(64, 64))
        self.btnStop.setObjectName("btnStop")
        self.gridLayout.addWidget(self.btnStop, 1, 1, 1, 1)
        self.btnForward = QtWidgets.QPushButton(self.centralwidget)
        self.btnForward.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/arrow-circle-up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnForward.setIcon(icon2)
        self.btnForward.setIconSize(QtCore.QSize(64, 64))
        self.btnForward.setObjectName("btnForward")
        self.gridLayout.addWidget(self.btnForward, 0, 1, 1, 1)
        self.btnRight = QtWidgets.QPushButton(self.centralwidget)
        self.btnRight.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/corner-up-right.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnRight.setIcon(icon3)
        self.btnRight.setIconSize(QtCore.QSize(64, 64))
        self.btnRight.setObjectName("btnRight")
        self.gridLayout.addWidget(self.btnRight, 1, 2, 1, 1)
        self.btnBackward = QtWidgets.QPushButton(self.centralwidget)
        self.btnBackward.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/arrow-circle-down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBackward.setIcon(icon4)
        self.btnBackward.setIconSize(QtCore.QSize(64, 64))
        self.btnBackward.setObjectName("btnBackward")
        self.gridLayout.addWidget(self.btnBackward, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnSound1 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSound1.sizePolicy().hasHeightForWidth())
        self.btnSound1.setSizePolicy(sizePolicy)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/music.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSound1.setIcon(icon5)
        self.btnSound1.setIconSize(QtCore.QSize(32, 32))
        self.btnSound1.setObjectName("btnSound1")
        self.horizontalLayout.addWidget(self.btnSound1)
        self.btnSound2 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSound2.sizePolicy().hasHeightForWidth())
        self.btnSound2.setSizePolicy(sizePolicy)
        self.btnSound2.setIcon(icon5)
        self.btnSound2.setIconSize(QtCore.QSize(32, 32))
        self.btnSound2.setObjectName("btnSound2")
        self.horizontalLayout.addWidget(self.btnSound2)
        self.btnSound3 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSound3.sizePolicy().hasHeightForWidth())
        self.btnSound3.setSizePolicy(sizePolicy)
        self.btnSound3.setIcon(icon5)
        self.btnSound3.setIconSize(QtCore.QSize(32, 32))
        self.btnSound3.setObjectName("btnSound3")
        self.horizontalLayout.addWidget(self.btnSound3)
        self.btnSound4 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSound4.sizePolicy().hasHeightForWidth())
        self.btnSound4.setSizePolicy(sizePolicy)
        self.btnSound4.setIcon(icon5)
        self.btnSound4.setIconSize(QtCore.QSize(32, 32))
        self.btnSound4.setObjectName("btnSound4")
        self.horizontalLayout.addWidget(self.btnSound4)
        self.btnSound5 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSound5.sizePolicy().hasHeightForWidth())
        self.btnSound5.setSizePolicy(sizePolicy)
        self.btnSound5.setIcon(icon5)
        self.btnSound5.setIconSize(QtCore.QSize(32, 32))
        self.btnSound5.setObjectName("btnSound5")
        self.horizontalLayout.addWidget(self.btnSound5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnLEDSlow = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLEDSlow.sizePolicy().hasHeightForWidth())
        self.btnLEDSlow.setSizePolicy(sizePolicy)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/eva-icons/fill/png/128/bulb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLEDSlow.setIcon(icon6)
        self.btnLEDSlow.setIconSize(QtCore.QSize(32, 32))
        self.btnLEDSlow.setObjectName("btnLEDSlow")
        self.horizontalLayout_2.addWidget(self.btnLEDSlow)
        self.btnLEDFast = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnLEDFast.sizePolicy().hasHeightForWidth())
        self.btnLEDFast.setSizePolicy(sizePolicy)
        self.btnLEDFast.setIcon(icon6)
        self.btnLEDFast.setIconSize(QtCore.QSize(32, 32))
        self.btnLEDFast.setObjectName("btnLEDFast")
        self.horizontalLayout_2.addWidget(self.btnLEDFast)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.btnInit = QtWidgets.QPushButton(self.centralwidget)
        self.btnInit.setObjectName("btnInit")
        self.verticalLayout.addWidget(self.btnInit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 39))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionContinuousModeSwitch = QtWidgets.QAction(MainWindow)
        self.actionContinuousModeSwitch.setCheckable(True)
        self.actionContinuousModeSwitch.setObjectName("actionContinuousModeSwitch")
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionContinuousModeSwitch)
        self.menuDatei.addAction(self.actionQuit)
        self.menubar.addAction(self.menuDatei.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mein Roboter"))
        self.btnSound1.setText(_translate("MainWindow", "Sound 1"))
        self.btnSound2.setText(_translate("MainWindow", "Sound 2"))
        self.btnSound3.setText(_translate("MainWindow", "Sound 3"))
        self.btnSound4.setText(_translate("MainWindow", "Sound 4"))
        self.btnSound5.setText(_translate("MainWindow", "Sound 5"))
        self.btnLEDSlow.setText(_translate("MainWindow", "LED Blink Slow"))
        self.btnLEDFast.setText(_translate("MainWindow", "LED Blink Fast"))
        self.btnInit.setText(_translate("MainWindow", "Init Live Mode"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.actionQuit.setText(_translate("MainWindow", "Beenden"))
        self.actionContinuousModeSwitch.setText(_translate("MainWindow", "Momentan Modus"))
import ressources_rc