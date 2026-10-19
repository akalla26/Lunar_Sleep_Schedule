# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'override.ui'
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
    QTextEdit, QWidget)

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
        self.startCalendar = QCalendarWidget(self.centralwidget)
        self.startCalendar.setObjectName(u"startCalendar")
        self.startCalendar.setGeometry(QRect(50, 120, 256, 192))
        self.startLabel = QLabel(self.centralwidget)
        self.startLabel.setObjectName(u"startLabel")
        self.startLabel.setGeometry(QRect(50, 100, 120, 15))
        self.endLabel = QLabel(self.centralwidget)
        self.endLabel.setObjectName(u"endLabel")
        self.endLabel.setGeometry(QRect(50, 325, 115, 15))
        self.endCalendar = QCalendarWidget(self.centralwidget)
        self.endCalendar.setObjectName(u"endCalendar")
        self.endCalendar.setGeometry(QRect(50, 345, 256, 192))
        self.sleepStartShiftLabel = QLabel(self.centralwidget)
        self.sleepStartShiftLabel.setObjectName(u"sleepStartShiftLabel")
        self.sleepStartShiftLabel.setGeometry(QRect(360, 30, 200, 15))
        self.sleepEndShiftLabel = QLabel(self.centralwidget)
        self.sleepEndShiftLabel.setObjectName(u"sleepEndShiftLabel")
        self.sleepEndShiftLabel.setGeometry(QRect(360, 120, 200, 15))
        self.overrideConfirm = QPushButton(self.centralwidget)
        self.overrideConfirm.setObjectName(u"overrideConfirm")
        self.overrideConfirm.setGeometry(QRect(360, 450, 150, 30))
        palette = QPalette()
        brush = QBrush(QColor(19, 193, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        self.overrideConfirm.setPalette(palette)
        self.quit = QPushButton(self.centralwidget)
        self.quit.setObjectName(u"quit")
        self.quit.setGeometry(QRect(360, 500, 150, 30))
        palette1 = QPalette()
        brush1 = QBrush(QColor(240, 0, 4, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette1.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        self.quit.setPalette(palette1)
        self.sleepShiftStart = QTextEdit(self.centralwidget)
        self.sleepShiftStart.setObjectName(u"sleepShiftStart")
        self.sleepShiftStart.setGeometry(QRect(360, 60, 200, 30))
        self.sleepShiftEnd = QTextEdit(self.centralwidget)
        self.sleepShiftEnd.setObjectName(u"sleepShiftEnd")
        self.sleepShiftEnd.setGeometry(QRect(360, 150, 200, 30))
        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(360, 200, 351, 231))
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
        self.title.setText(QCoreApplication.translate("MainWindow", u"Override", None))
        self.startLabel.setText(QCoreApplication.translate("MainWindow", u"Enter Start Of Override", None))
        self.endLabel.setText(QCoreApplication.translate("MainWindow", u"Enter End Of Override", None))
        self.sleepStartShiftLabel.setText(QCoreApplication.translate("MainWindow", u"Sleep start override (time in minutes)", None))
        self.sleepEndShiftLabel.setText(QCoreApplication.translate("MainWindow", u"Sleep end override (time in minutes)", None))
        self.overrideConfirm.setText(QCoreApplication.translate("MainWindow", u"Override", None))
        self.quit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

