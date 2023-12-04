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
    QWidget)

class Ui_SignUpWindow(object):
    def setupUi(self, SignUpWindow):
        if not SignUpWindow.objectName():
            SignUpWindow.setObjectName(u"SignUpWindow")
        SignUpWindow.resize(800, 600)
        self.gridLayout_5 = QGridLayout(SignUpWindow)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalSpacer_5 = QSpacerItem(20, 107, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 1, 0, 1, 1)

        self.coverFrame = QFrame(SignUpWindow)
        self.coverFrame.setObjectName(u"coverFrame")
        self.coverFrame.setFrameShape(QFrame.WinPanel)
        self.coverFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.coverFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.frame_4 = QFrame(self.coverFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.WinPanel)
        self.frame_4.setFrameShadow(QFrame.Sunken)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(15, 15, 15, 15)
        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_16)

        self.goToLogin = QPushButton(self.frame)
        self.goToLogin.setObjectName(u"goToLogin")

        self.horizontalLayout_9.addWidget(self.goToLogin)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_17)


        self.gridLayout.addLayout(self.horizontalLayout_9, 5, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_7 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_7)

        self.adminSubmit = QPushButton(self.frame)
        self.adminSubmit.setObjectName(u"adminSubmit")
        self.adminSubmit.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.adminSubmit)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_8)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_7, 3, 0, 1, 1)

        self.line = QFrame(self.frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.adminPass1 = QLineEdit(self.frame)
        self.adminPass1.setObjectName(u"adminPass1")
        self.adminPass1.setMinimumSize(QSize(150, 0))
        self.adminPass1.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_3.addWidget(self.adminPass1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.adminPass2 = QLineEdit(self.frame)
        self.adminPass2.setObjectName(u"adminPass2")
        self.adminPass2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.adminPass2)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_14)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adminName = QLineEdit(self.frame)
        self.adminName.setObjectName(u"adminName")
        self.adminName.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.adminName)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.adminMobileNo = QLineEdit(self.frame)
        self.adminMobileNo.setObjectName(u"adminMobileNo")
        self.adminMobileNo.setMinimumSize(QSize(150, 0))

        self.horizontalLayout.addWidget(self.adminMobileNo)


        self.horizontalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_13)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Logo = QPushButton(self.frame_2)
        self.Logo.setObjectName(u"Logo")
        font = QFont()
        font.setFamilies([u"Rockwell Condensed"])
        font.setPointSize(20)
        self.Logo.setFont(font)
        icon = QIcon()
        icon.addFile(u"icons/favicon_io/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Logo.setIcon(icon)
        self.Logo.setIconSize(QSize(50, 50))

        self.gridLayout_3.addWidget(self.Logo, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 1, 1, 1, 1)


        self.gridLayout_5.addWidget(self.coverFrame, 1, 1, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(82, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 1, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 106, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 2, 1, 1, 1)


        self.retranslateUi(SignUpWindow)

        QMetaObject.connectSlotsByName(SignUpWindow)
    # setupUi

    def retranslateUi(self, SignUpWindow):
        SignUpWindow.setWindowTitle(QCoreApplication.translate("SignUpWindow", u"SignUpWindow", None))
        self.goToLogin.setText(QCoreApplication.translate("SignUpWindow", u"Already have an account? Login", None))
        self.adminSubmit.setText(QCoreApplication.translate("SignUpWindow", u"Submit", None))
        self.adminPass1.setText("")
        self.adminPass1.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Create Password", None))
        self.adminPass2.setText("")
        self.adminPass2.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Confirm Password", None))
        self.adminName.setText("")
        self.adminName.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Enter Your Name", None))
        self.adminMobileNo.setText("")
        self.adminMobileNo.setPlaceholderText(QCoreApplication.translate("SignUpWindow", u"Enter Your Mobile No.", None))
        self.Logo.setText("")
    # retranslateUi

