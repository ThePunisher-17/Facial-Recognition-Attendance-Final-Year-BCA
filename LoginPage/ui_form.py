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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(831, 601)
        self.gridLayout_4 = QGridLayout(LoginPage)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 76, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 3, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(218, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.coverFrame = QFrame(LoginPage)
        self.coverFrame.setObjectName(u"coverFrame")
        self.coverFrame.setStyleSheet(u"#frame_5{\n"
"background-color: rgba(255,255,255,1);\n"
"}")
        self.coverFrame.setFrameShape(QFrame.WinPanel)
        self.coverFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.coverFrame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.coverFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, -1)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.goToSignUp = QPushButton(self.frame_3)
        self.goToSignUp.setObjectName(u"goToSignUp")

        self.gridLayout_3.addWidget(self.goToSignUp, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_2.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line, 0, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 3, 0, 1, 1)

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

        self.verticalLayout_2.addWidget(self.loginButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.Logo = QPushButton(self.frame)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setFont(font)
        icon1 = QIcon()
        icon1.addFile(u"../../../../Downloads/favicon_io/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon1)
        self.Logo.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.Logo, 1, 0, 1, 1)


        self.gridLayout_5.addWidget(self.frame, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(51, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)


        self.gridLayout_4.addWidget(self.coverFrame, 1, 2, 2, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 1, 1, 1)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"LoginPage", None))
        self.goToSignUp.setText(QCoreApplication.translate("LoginPage", u"Don't have an account? Sing-Up", None))
        self.pushButton_3.setText(QCoreApplication.translate("LoginPage", u"Forgotten Your Password ", None))
        self.adminId.setPlaceholderText(QCoreApplication.translate("LoginPage", u"User ID", None))
        self.adminPassword.setInputMask("")
        self.adminPassword.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.loginButton.setText(QCoreApplication.translate("LoginPage", u"Login", None))
        self.Logo.setText(QCoreApplication.translate("LoginPage", u"@ptk", None))
    # retranslateUi

