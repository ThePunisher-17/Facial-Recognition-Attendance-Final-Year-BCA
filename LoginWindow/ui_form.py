# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(800, 600)
        self.gridLayout_6 = QGridLayout(LoginWindow)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.coverFrame = QFrame(LoginWindow)
        self.coverFrame.setObjectName(u"coverFrame")
        self.coverFrame.setFrameShape(QFrame.StyledPanel)
        self.coverFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.coverFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.frame_4 = QFrame(self.coverFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_4)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.adminId = QLineEdit(self.frame)
        self.adminId.setObjectName(u"adminId")
        self.adminId.setEnabled(True)
        font = QFont()
        font.setFamilies([u"Rockwell Condensed"])
        font.setPointSize(14)
        self.adminId.setFont(font)

        self.verticalLayout_2.addWidget(self.adminId)

        self.adminPassword = QLineEdit(self.frame)
        self.adminPassword.setObjectName(u"adminPassword")
        self.adminPassword.setFont(font)
        self.adminPassword.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.adminPassword)

        self.loginButton = QPushButton(self.frame)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setFont(font)
        icon = QIcon()
        icon.addFile(u"../../../../Downloads/login.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.loginButton.setIcon(icon)
        self.loginButton.setIconSize(QSize(25, 25))
        self.loginButton.setCheckable(True)

        self.verticalLayout_2.addWidget(self.loginButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.Logo = QPushButton(self.frame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u"icons/favicon_io/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon1)
        self.Logo.setIconSize(QSize(50, 50))
        self.Logo.setCheckable(False)

        self.gridLayout.addWidget(self.Logo, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setCheckable(True)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.goToSignUp = QPushButton(self.frame_2)
        self.goToSignUp.setObjectName(u"goToSignUp")
        self.goToSignUp.setCheckable(True)

        self.verticalLayout.addWidget(self.goToSignUp)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame_4, 1, 1, 2, 2)

        self.horizontalSpacer_3 = QSpacerItem(51, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 2, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 3, 2, 1, 1)


        self.gridLayout_6.addWidget(self.coverFrame, 1, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 64, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 2, 2, 1, 1)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"LoginWindow", None))
        self.adminId.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"User ID", None))
        self.adminPassword.setInputMask("")
        self.adminPassword.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.Logo.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("LoginWindow", u"Forgotten Your Password ", None))
        self.goToSignUp.setText(QCoreApplication.translate("LoginWindow", u"Don't have an account? Sign-Up", None))
    # retranslateUi

