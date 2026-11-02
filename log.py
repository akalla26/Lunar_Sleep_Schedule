# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'log.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTimeEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 300, 30))
        font = QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.logSleep = QPushButton(self.centralwidget)
        self.logSleep.setObjectName(u"logSleep")
        self.logSleep.setGeometry(QRect(50, 450, 150, 30))
        palette = QPalette()
        brush = QBrush(QColor(5, 77, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.logSleep.setPalette(palette)
        self.cancelLog = QPushButton(self.centralwidget)
        self.cancelLog.setObjectName(u"cancelLog")
        self.cancelLog.setGeometry(QRect(50, 500, 150, 30))
        palette1 = QPalette()
        brush1 = QBrush(QColor(240, 0, 4, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.cancelLog.setPalette(palette1)
        self.sleepStartTitle = QLabel(self.centralwidget)
        self.sleepStartTitle.setObjectName(u"sleepStartTitle")
        self.sleepStartTitle.setGeometry(QRect(50, 110, 300, 30))
        font1 = QFont()
        font1.setPointSize(9)
        self.sleepStartTitle.setFont(font1)
        self.sleepEndTitle = QLabel(self.centralwidget)
        self.sleepEndTitle.setObjectName(u"sleepEndTitle")
        self.sleepEndTitle.setGeometry(QRect(480, 110, 300, 30))
        self.sleepEndTitle.setFont(font1)
        self.notif = QLabel(self.centralwidget)
        self.notif.setObjectName(u"notif")
        self.notif.setGeometry(QRect(510, 430, 200, 100))
        self.sleepStartLogDate = QCalendarWidget(self.centralwidget)
        self.sleepStartLogDate.setObjectName(u"sleepStartLogDate")
        self.sleepStartLogDate.setGeometry(QRect(50, 210, 256, 192))
        self.sleepEndLogDate = QCalendarWidget(self.centralwidget)
        self.sleepEndLogDate.setObjectName(u"sleepEndLogDate")
        self.sleepEndLogDate.setGeometry(QRect(480, 210, 256, 192))
        self.sleepStartLogTime = QTimeEdit(self.centralwidget)
        self.sleepStartLogTime.setObjectName(u"sleepStartLogTime")
        self.sleepStartLogTime.setGeometry(QRect(50, 160, 150, 30))
        self.sleepEndLogTime = QTimeEdit(self.centralwidget)
        self.sleepEndLogTime.setObjectName(u"sleepEndLogTime")
        self.sleepEndLogTime.setGeometry(QRect(480, 160, 150, 30))
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
        self.title.setText(QCoreApplication.translate("MainWindow", u"Enter Sleep Log", None))
        self.logSleep.setText(QCoreApplication.translate("MainWindow", u"Log Sleep", None))
        self.cancelLog.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.sleepStartTitle.setText(QCoreApplication.translate("MainWindow", u"Enter start time of sleep", None))
        self.sleepEndTitle.setText(QCoreApplication.translate("MainWindow", u"Enter end time of sleep", None))
        self.notif.setText("")
    # retranslateUi

