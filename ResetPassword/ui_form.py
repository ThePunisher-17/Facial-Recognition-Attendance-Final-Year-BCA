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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)

class Ui_ResetPassword(object):
    def setupUi(self, ResetPassword):
        if not ResetPassword.objectName():
            ResetPassword.setObjectName(u"ResetPassword")
        ResetPassword.resize(798, 442)
        self.gridLayout = QGridLayout(ResetPassword)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.ResetWindow = QStackedWidget(ResetPassword)
        self.ResetWindow.setObjectName(u"ResetWindow")
        self.otpGenerate = QWidget()
        self.otpGenerate.setObjectName(u"otpGenerate")
        self.gridLayout_5 = QGridLayout(self.otpGenerate)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_3 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(122, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.coverFrameReset1 = QFrame(self.otpGenerate)
        self.coverFrameReset1.setObjectName(u"coverFrameReset1")
        self.coverFrameReset1.setFrameShape(QFrame.WinPanel)
        self.coverFrameReset1.setFrameShadow(QFrame.Sunken)
        self.gridLayout_4 = QGridLayout(self.coverFrameReset1)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(30, 30, 30, 30)
        self.MidFrameReset1 = QFrame(self.coverFrameReset1)
        self.MidFrameReset1.setObjectName(u"MidFrameReset1")
        self.MidFrameReset1.setFrameShape(QFrame.WinPanel)
        self.MidFrameReset1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.MidFrameReset1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(15, 15, 15, 15)
        self.label_2 = QLabel(self.MidFrameReset1)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.ResetFrameReset1 = QFrame(self.MidFrameReset1)
        self.ResetFrameReset1.setObjectName(u"ResetFrameReset1")
        self.ResetFrameReset1.setFrameShape(QFrame.WinPanel)
        self.ResetFrameReset1.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.ResetFrameReset1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label = QLabel(self.ResetFrameReset1)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(14)
        self.label.setFont(font1)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.UserID = QLineEdit(self.ResetFrameReset1)
        self.UserID.setObjectName(u"UserID")
        self.UserID.setMinimumSize(QSize(50, 0))

        self.gridLayout_2.addWidget(self.UserID, 0, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.sendOtp = QPushButton(self.ResetFrameReset1)
        self.sendOtp.setObjectName(u"sendOtp")
        self.sendOtp.setEnabled(True)
        self.sendOtp.setMinimumSize(QSize(150, 0))
        self.sendOtp.setCheckable(True)

        self.horizontalLayout.addWidget(self.sendOtp)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 2)

        self.label_4 = QLabel(self.ResetFrameReset1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_2.addWidget(self.label_4, 2, 0, 1, 1)

        self.otpBox = QLineEdit(self.ResetFrameReset1)
        self.otpBox.setObjectName(u"otpBox")

        self.gridLayout_2.addWidget(self.otpBox, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_10)

        self.verifyOtp = QPushButton(self.ResetFrameReset1)
        self.verifyOtp.setObjectName(u"verifyOtp")
        self.verifyOtp.setEnabled(False)
        self.verifyOtp.setMinimumSize(QSize(150, 0))
        self.verifyOtp.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.verifyOtp)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_9)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_11)

        self.ReturnToLogin = QPushButton(self.ResetFrameReset1)
        self.ReturnToLogin.setObjectName(u"ReturnToLogin")
        self.ReturnToLogin.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.ReturnToLogin)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 0, 1, 2)


        self.gridLayout_3.addWidget(self.ResetFrameReset1, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.MidFrameReset1, 0, 0, 1, 1)


        self.gridLayout_5.addWidget(self.coverFrameReset1, 1, 1, 1, 2)

        self.horizontalSpacer_4 = QSpacerItem(178, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 70, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.ResetWindow.addWidget(self.otpGenerate)
        self.resetPage = QWidget()
        self.resetPage.setObjectName(u"resetPage")
        self.gridLayout_9 = QGridLayout(self.resetPage)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_7 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_7, 1, 0, 1, 1)

        self.coverFrameReset2 = QFrame(self.resetPage)
        self.coverFrameReset2.setObjectName(u"coverFrameReset2")
        self.coverFrameReset2.setFrameShape(QFrame.WinPanel)
        self.coverFrameReset2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_6 = QGridLayout(self.coverFrameReset2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.MidFrameReset2 = QFrame(self.coverFrameReset2)
        self.MidFrameReset2.setObjectName(u"MidFrameReset2")
        self.MidFrameReset2.setFrameShape(QFrame.WinPanel)
        self.MidFrameReset2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.MidFrameReset2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(30, 15, 30, 30)
        self.ResetFrameReset2 = QFrame(self.MidFrameReset2)
        self.ResetFrameReset2.setObjectName(u"ResetFrameReset2")
        self.ResetFrameReset2.setFrameShape(QFrame.WinPanel)
        self.ResetFrameReset2.setFrameShadow(QFrame.Sunken)
        self.gridLayout_8 = QGridLayout(self.ResetFrameReset2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(15, 15, 15, 15)
        self.ResetPasswordButton = QPushButton(self.ResetFrameReset2)
        self.ResetPasswordButton.setObjectName(u"ResetPasswordButton")
        self.ResetPasswordButton.setCheckable(True)

        self.gridLayout_8.addWidget(self.ResetPasswordButton, 2, 0, 1, 1)

        self.newPass = QLineEdit(self.ResetFrameReset2)
        self.newPass.setObjectName(u"newPass")
        self.newPass.setMinimumSize(QSize(100, 0))
        self.newPass.setMouseTracking(True)
        self.newPass.setEchoMode(QLineEdit.Password)

        self.gridLayout_8.addWidget(self.newPass, 0, 0, 1, 1)

        self.confNewPass = QLineEdit(self.ResetFrameReset2)
        self.confNewPass.setObjectName(u"confNewPass")

        self.gridLayout_8.addWidget(self.confNewPass, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.ResetFrameReset2, 1, 0, 1, 1)

        self.label_3 = QLabel(self.MidFrameReset2)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setUnderline(True)
        self.label_3.setFont(font2)

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.MidFrameReset2, 1, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_6, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_6, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.coverFrameReset2, 1, 1, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(221, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_8, 1, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 55, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_8, 2, 2, 1, 1)

        self.ResetWindow.addWidget(self.resetPage)

        self.gridLayout.addWidget(self.ResetWindow, 0, 0, 1, 1)


        self.retranslateUi(ResetPassword)

        self.ResetWindow.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ResetPassword)
    # setupUi

    def retranslateUi(self, ResetPassword):
        ResetPassword.setWindowTitle(QCoreApplication.translate("ResetPassword", u"ResetPassword", None))
        self.label_2.setText(QCoreApplication.translate("ResetPassword", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Reset Password</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("ResetPassword", u"Enter Admin ID", None))
        self.UserID.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Enter your Admin ID", None))
        self.sendOtp.setText(QCoreApplication.translate("ResetPassword", u"Generate OTP", None))
        self.label_4.setText(QCoreApplication.translate("ResetPassword", u"Enter OTP Received", None))
        self.otpBox.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"OTP", None))
        self.verifyOtp.setText(QCoreApplication.translate("ResetPassword", u"Verify", None))
        self.ReturnToLogin.setText(QCoreApplication.translate("ResetPassword", u"Return To Login", None))
        self.ResetPasswordButton.setText(QCoreApplication.translate("ResetPassword", u"Reset Password", None))
        self.newPass.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Enter Password", None))
        self.confNewPass.setText("")
        self.confNewPass.setPlaceholderText(QCoreApplication.translate("ResetPassword", u"Confirm Password", None))
        self.label_3.setText(QCoreApplication.translate("ResetPassword", u"Reset Password", None))
    # retranslateUi

