# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stats.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 200, 30))
        font = QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.fatigue = QLabel(self.centralwidget)
        self.fatigue.setObjectName(u"fatigue")
        self.fatigue.setGeometry(QRect(50, 115, 200, 30))
        self.recSleep = QLabel(self.centralwidget)
        self.recSleep.setObjectName(u"recSleep")
        self.recSleep.setGeometry(QRect(50, 175, 200, 30))
        self.recWake = QLabel(self.centralwidget)
        self.recWake.setObjectName(u"recWake")
        self.recWake.setGeometry(QRect(50, 235, 200, 30))
        self.targetSleep = QLabel(self.centralwidget)
        self.targetSleep.setObjectName(u"targetSleep")
        self.targetSleep.setGeometry(QRect(50, 295, 200, 30))
        self.sleepDuration = QLabel(self.centralwidget)
        self.sleepDuration.setObjectName(u"sleepDuration")
        self.sleepDuration.setGeometry(QRect(50, 355, 200, 30))
        self.exit = QPushButton(self.centralwidget)
        self.exit.setObjectName(u"exit")
        self.exit.setGeometry(QRect(50, 500, 150, 30))
        self.lastSlept = QLabel(self.centralwidget)
        self.lastSlept.setObjectName(u"lastSlept")
        self.lastSlept.setGeometry(QRect(50, 415, 200, 30))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.fatigue.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.recSleep.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.recWake.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.targetSleep.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.sleepDuration.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lastSlept.setText(QCoreApplication.translate("MainWindow", u"Stats", None))
    # retranslateUi

