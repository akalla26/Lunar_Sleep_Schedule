# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'recommendations.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.title = QLabel(Dialog)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(50, 50, 300, 30))
        font = QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.returnHome = QPushButton(Dialog)
        self.returnHome.setObjectName(u"returnHome")
        self.returnHome.setGeometry(QRect(50, 520, 150, 30))
        self.recommendationLabel = QLabel(Dialog)
        self.recommendationLabel.setObjectName(u"recommendationLabel")
        self.recommendationLabel.setGeometry(QRect(50, 100, 700, 400))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.title.setText(QCoreApplication.translate("Dialog", u"Recommendations", None))
        self.returnHome.setText(QCoreApplication.translate("Dialog", u"PushButton", None))
        self.recommendationLabel.setText("")
    # retranslateUi

