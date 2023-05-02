# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt
from PyQt5.QtGui import QFont
################################################################################
## Form generated from reading UI file 'GUIssEKys.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PyQt5.QtWidgets import *

import bg_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 737)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"background-image: url(:/bg/bg.jpg);\n"
"\n"
"")
        self.actionYOLO_Resnet50 = QAction(MainWindow)
        self.actionYOLO_Resnet50.setObjectName(u"actionYOLO_Resnet50")
        self.actionYOLO_Resnet18 = QAction(MainWindow)
        self.actionYOLO_Resnet18.setObjectName(u"actionYOLO_Resnet18")
        self.actionYOLO_MoblieNet = QAction(MainWindow)
        self.actionYOLO_MoblieNet.setObjectName(u"actionYOLO_MoblieNet")
        self.actionYOLOv5s = QAction(MainWindow)
        self.actionYOLOv5s.setObjectName(u"actionYOLOv5s")
        self.frame = QWidget(MainWindow)
        self.frame.setObjectName(u"frame")
        self.imgBtn = QPushButton(self.frame)
        self.imgBtn.setObjectName(u"imgBtn")
        self.imgBtn.setGeometry(QRect(10, 180, 121, 41))
        font = QFont()
        font.setFamily(u"Bodoni MT")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.imgBtn.setFont(font)
        self.imgBtn.setStyleSheet(u"border-radius:3px;\n"
"background-color:rgb(225, 225, 225)")
        self.exitBtn = QPushButton(self.frame)
        self.exitBtn.setObjectName(u"exitBtn")
        self.exitBtn.setGeometry(QRect(10, 600, 121, 41))
        font1 = QFont()
        font1.setFamily(u"Bodoni MT")
        font1.setPointSize(11)
        self.exitBtn.setFont(font1)
        self.exitBtn.setStyleSheet(u"border-radius:3px;\n"
"background-color:rgb(225, 225, 225)")
        self.videoBtn = QPushButton(self.frame)
        self.videoBtn.setObjectName(u"videoBtn")
        self.videoBtn.setGeometry(QRect(10, 390, 121, 41))
        self.videoBtn.setFont(font)
        self.videoBtn.setStyleSheet(u"border-radius:3px;\n"
"background-color:rgb(225, 225, 225)")
        self.titleLabel = QLabel(self.frame)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(30, 20, 161, 41))
        font2 = QFont()
        font2.setFamily(u"Script MT Bold")
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.titleLabel.setFont(font2)
        self.titleLabel.setAutoFillBackground(False)
        self.titleLabel.setStyleSheet(u"background-color:rgba(255, 255, 255,0)")
        self.imgLabel = QLabel(self.frame)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(210, 70, 811, 541))
        # self.imgLabel.setStyleSheet(u"background-color:rgba(255, 255, 255,0)")
        self.closeBtn = QPushButton(self.frame)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setGeometry(QRect(1070, 20, 16, 16))
        font3 = QFont()
        font3.setFamily(u"Berlin Sans FB")
        font3.setPointSize(12)
        self.closeBtn.setFont(font3)
        self.closeBtn.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"color:rgb(63, 63, 63);\n"
"")
        self.minimalBtn = QPushButton(self.frame)
        self.minimalBtn.setObjectName(u"minimalBtn")
        self.minimalBtn.setGeometry(QRect(1050, 20, 16, 16))
        font4 = QFont()
        font4.setFamily(u"Berlin Sans FB")
        font4.setPointSize(16)
        self.minimalBtn.setFont(font4)
        self.minimalBtn.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"color:rgb(63, 63, 63);\n"
"")
        self.resultLabel = QLabel(self.frame)
        self.resultLabel.setObjectName(u"resultLabel")
        self.resultLabel.setGeometry(QRect(280, 630, 631, 41))
        font5 = QFont()
        font5.setFamily(u"Century Schoolbook")
        font5.setPointSize(16)
        self.resultLabel.setFont(font5)
        self.resultLabel.setLayoutDirection(Qt.LeftToRight)
        self.resultLabel.setStyleSheet(u"background-color:rgba(255, 255, 255,0)")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.modelsCombo = QComboBox(self.frame)
        self.modelsCombo.addItem("")
        self.modelsCombo.addItem("")
        self.modelsCombo.addItem("")
        self.modelsCombo.setObjectName(u"modelsCombo")
        self.modelsCombo.setGeometry(QRect(10, 80, 131, 31))
        self.modelsCombo.setStyleSheet(u"background-color: rgba(85, 255, 0,0);\n"
"alternate-background-color: rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.frame)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1101, 22))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.BottomToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"YOLOv5-Fresh and Rotten fruits", None))
        self.actionYOLO_Resnet50.setText(QCoreApplication.translate("MainWindow", u"YOLO-Resnet50", None))
        self.actionYOLO_Resnet18.setText(QCoreApplication.translate("MainWindow", u"YOLO-Resnet18", None))
        self.actionYOLO_MoblieNet.setText(QCoreApplication.translate("MainWindow", u"YOLO-MoblieNet", None))
        self.actionYOLOv5s.setText(QCoreApplication.translate("MainWindow", u"YOLOv5s", None))
        self.imgBtn.setText(QCoreApplication.translate("MainWindow", u"Image/png", None))
        self.exitBtn.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.videoBtn.setText(QCoreApplication.translate("MainWindow", u"Video", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"YOLOv5", None))
        self.imgLabel.setText("")
        self.closeBtn.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.minimalBtn.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.resultLabel.setText("")
        self.modelsCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"ResnetLarge", None))
        self.modelsCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"ResnetTiny", None))
        self.modelsCombo.setItemText(2, QCoreApplication.translate("MainWindow", u"MobileNetV3", None))

        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

