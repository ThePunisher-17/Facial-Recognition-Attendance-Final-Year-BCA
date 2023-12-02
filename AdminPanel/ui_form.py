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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        if not AdminPanel.objectName():
            AdminPanel.setObjectName(u"AdminPanel")
        AdminPanel.resize(1002, 602)
        self.gridLayout_4 = QGridLayout(AdminPanel)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.IconContainer = QWidget(AdminPanel)
        self.IconContainer.setObjectName(u"IconContainer")
        self.gridLayout = QGridLayout(self.IconContainer)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 7, 0, 1, 1)

        self.goToReports = QPushButton(self.IconContainer)
        self.goToReports.setObjectName(u"goToReports")
        icon = QIcon()
        icon.addFile(u"icons/reports.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToReports.setIcon(icon)
        self.goToReports.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToReports, 6, 0, 1, 1)

        self.goToDashboard = QPushButton(self.IconContainer)
        self.goToDashboard.setObjectName(u"goToDashboard")
        icon1 = QIcon()
        icon1.addFile(u"icons/dashboard.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToDashboard.setIcon(icon1)
        self.goToDashboard.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.goToDashboard, 1, 0, 1, 1)

        self.goToListOfEmployee = QPushButton(self.IconContainer)
        self.goToListOfEmployee.setObjectName(u"goToListOfEmployee")
        icon2 = QIcon()
        icon2.addFile(u"icons/list.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToListOfEmployee.setIcon(icon2)
        self.goToListOfEmployee.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToListOfEmployee, 2, 0, 1, 1)

        self.goToAttendance = QPushButton(self.IconContainer)
        self.goToAttendance.setObjectName(u"goToAttendance")
        icon3 = QIcon()
        icon3.addFile(u"icons/attendance.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToAttendance.setIcon(icon3)
        self.goToAttendance.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToAttendance, 5, 0, 1, 1)

        self.goToAddEmployee = QPushButton(self.IconContainer)
        self.goToAddEmployee.setObjectName(u"goToAddEmployee")
        icon4 = QIcon()
        icon4.addFile(u"icons/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToAddEmployee.setIcon(icon4)
        self.goToAddEmployee.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToAddEmployee, 3, 0, 1, 1)

        self.launchAnAttender = QPushButton(self.IconContainer)
        self.launchAnAttender.setObjectName(u"launchAnAttender")
        self.launchAnAttender.setEnabled(True)
        icon5 = QIcon()
        icon5.addFile(u"icons/attender.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.launchAnAttender.setIcon(icon5)
        self.launchAnAttender.setIconSize(QSize(25, 25))
        self.launchAnAttender.setCheckable(True)

        self.gridLayout.addWidget(self.launchAnAttender, 4, 0, 1, 1)

        self.IconLogo = QPushButton(self.IconContainer)
        self.IconLogo.setObjectName(u"IconLogo")
        icon6 = QIcon()
        icon6.addFile(u"icons/favicon_io/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.IconLogo.setIcon(icon6)
        self.IconLogo.setIconSize(QSize(25, 30))

        self.gridLayout.addWidget(self.IconLogo, 0, 0, 1, 1)

        self.Exit = QPushButton(self.IconContainer)
        self.Exit.setObjectName(u"Exit")
        icon7 = QIcon()
        icon7.addFile(u"icons/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit.setIcon(icon7)
        self.Exit.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.Exit, 8, 0, 1, 1)


        self.gridLayout_4.addWidget(self.IconContainer, 0, 0, 2, 1)

        self.IconAndNameContainer = QWidget(AdminPanel)
        self.IconAndNameContainer.setObjectName(u"IconAndNameContainer")
        self.gridLayout_2 = QGridLayout(self.IconAndNameContainer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.goToDashboardLabeled = QPushButton(self.IconAndNameContainer)
        self.goToDashboardLabeled.setObjectName(u"goToDashboardLabeled")
        self.goToDashboardLabeled.setIcon(icon1)
        self.goToDashboardLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToDashboardLabeled, 1, 0, 1, 1)

        self.goToListOfEmployeeLabeled = QPushButton(self.IconAndNameContainer)
        self.goToListOfEmployeeLabeled.setObjectName(u"goToListOfEmployeeLabeled")
        self.goToListOfEmployeeLabeled.setIcon(icon2)
        self.goToListOfEmployeeLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToListOfEmployeeLabeled, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 7, 0, 1, 1)

        self.goToReportsLabeled = QPushButton(self.IconAndNameContainer)
        self.goToReportsLabeled.setObjectName(u"goToReportsLabeled")
        self.goToReportsLabeled.setIcon(icon)
        self.goToReportsLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToReportsLabeled, 6, 0, 1, 1)

        self.launchAnAttenderLabeled = QPushButton(self.IconAndNameContainer)
        self.launchAnAttenderLabeled.setObjectName(u"launchAnAttenderLabeled")
        self.launchAnAttenderLabeled.setEnabled(True)
        self.launchAnAttenderLabeled.setIcon(icon5)
        self.launchAnAttenderLabeled.setIconSize(QSize(25, 25))
        self.launchAnAttenderLabeled.setCheckable(True)

        self.gridLayout_2.addWidget(self.launchAnAttenderLabeled, 4, 0, 1, 1)

        self.goToAttendanceLabeled = QPushButton(self.IconAndNameContainer)
        self.goToAttendanceLabeled.setObjectName(u"goToAttendanceLabeled")
        self.goToAttendanceLabeled.setIcon(icon3)
        self.goToAttendanceLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToAttendanceLabeled, 5, 0, 1, 1)

        self.MainLogo = QPushButton(self.IconAndNameContainer)
        self.MainLogo.setObjectName(u"MainLogo")
        self.MainLogo.setIcon(icon6)
        self.MainLogo.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.MainLogo, 0, 0, 1, 1)

        self.goToAddEmployeeLabeled = QPushButton(self.IconAndNameContainer)
        self.goToAddEmployeeLabeled.setObjectName(u"goToAddEmployeeLabeled")
        self.goToAddEmployeeLabeled.setIcon(icon4)
        self.goToAddEmployeeLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToAddEmployeeLabeled, 3, 0, 1, 1)

        self.Exit_2 = QPushButton(self.IconAndNameContainer)
        self.Exit_2.setObjectName(u"Exit_2")
        self.Exit_2.setIcon(icon7)
        self.Exit_2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.Exit_2, 8, 0, 1, 1)


        self.gridLayout_4.addWidget(self.IconAndNameContainer, 0, 1, 2, 1)

        self.StatusBar = QWidget(AdminPanel)
        self.StatusBar.setObjectName(u"StatusBar")
        self.gridLayout_5 = QGridLayout(self.StatusBar)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.StatusBar)
        self.menuButton.setObjectName(u"menuButton")
        icon8 = QIcon()
        icon8.addFile(u"icons/drawer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon8)
        self.menuButton.setIconSize(QSize(25, 25))
        self.menuButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.menuButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.StatusBar, 0, 2, 1, 1)

        self.stackedWidget = QStackedWidget(AdminPanel)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush6 = QBrush(QColor(127, 127, 127, 127))
        brush6.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush6)
#endif
        self.stackedWidget.setPalette(palette)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_22 = QGridLayout(self.page)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_14 = QLabel(self.page)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setFamilies([u"Rockwell Condensed"])
        self.label_14.setFont(font)

        self.gridLayout_22.addWidget(self.label_14, 0, 0, 1, 2)

        self.frame_8 = QFrame(self.page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.empFrame = QFrame(self.frame_8)
        self.empFrame.setObjectName(u"empFrame")
        self.empFrame.setFrameShape(QFrame.WinPanel)
        self.empFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_19 = QGridLayout(self.empFrame)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.totalEmpLabel = QLabel(self.empFrame)
        self.totalEmpLabel.setObjectName(u"totalEmpLabel")
        font1 = QFont()
        font1.setFamilies([u"Elephant"])
        self.totalEmpLabel.setFont(font1)
        self.totalEmpLabel.setFrameShape(QFrame.WinPanel)
        self.totalEmpLabel.setFrameShadow(QFrame.Sunken)

        self.gridLayout_19.addWidget(self.totalEmpLabel, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_34)

        self.totalEmpValue = QLabel(self.empFrame)
        self.totalEmpValue.setObjectName(u"totalEmpValue")
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(14)
        self.totalEmpValue.setFont(font2)
        self.totalEmpValue.setIndent(0)

        self.horizontalLayout_23.addWidget(self.totalEmpValue)

        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_35)


        self.gridLayout_19.addLayout(self.horizontalLayout_23, 1, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.empFrame)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.adminFrame = QFrame(self.frame_8)
        self.adminFrame.setObjectName(u"adminFrame")
        self.adminFrame.setFrameShape(QFrame.WinPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.adminFrame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.totalAdminLabel = QLabel(self.adminFrame)
        self.totalAdminLabel.setObjectName(u"totalAdminLabel")
        self.totalAdminLabel.setFont(font1)
        self.totalAdminLabel.setFrameShape(QFrame.WinPanel)
        self.totalAdminLabel.setFrameShadow(QFrame.Sunken)

        self.gridLayout_20.addWidget(self.totalAdminLabel, 0, 0, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_36)

        self.totalAdminValue = QLabel(self.adminFrame)
        self.totalAdminValue.setObjectName(u"totalAdminValue")
        self.totalAdminValue.setFont(font2)

        self.horizontalLayout_24.addWidget(self.totalAdminValue)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_37)


        self.gridLayout_20.addLayout(self.horizontalLayout_24, 1, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.adminFrame)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_29 = QSpacerItem(64, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_29)


        self.gridLayout_21.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 136, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_5, 1, 0, 1, 1)


        self.gridLayout_22.addWidget(self.frame_8, 1, 1, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 250, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_22.addItem(self.verticalSpacer_7, 2, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(416, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_30, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_13 = QGridLayout(self.page_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.AttendanceList = QLabel(self.page_2)
        self.AttendanceList.setObjectName(u"AttendanceList")
        self.AttendanceList.setFont(font)

        self.horizontalLayout_13.addWidget(self.AttendanceList)

        self.horizontalSpacer_28 = QSpacerItem(640, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_28)


        self.gridLayout_13.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.currentMonthAndYear = QLabel(self.frame_5)
        self.currentMonthAndYear.setObjectName(u"currentMonthAndYear")
        font3 = QFont()
        font3.setFamilies([u"Rockwell Condensed"])
        font3.setPointSize(20)
        self.currentMonthAndYear.setFont(font3)
        self.currentMonthAndYear.setStyleSheet(u"")
        self.currentMonthAndYear.setFrameShape(QFrame.WinPanel)
        self.currentMonthAndYear.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.currentMonthAndYear, 0, 0, 1, 1)

        self.attendanceTableDetailed = QTableWidget(self.frame_5)
        self.attendanceTableDetailed.setObjectName(u"attendanceTableDetailed")
        self.attendanceTableDetailed.setFrameShape(QFrame.WinPanel)
        self.attendanceTableDetailed.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.attendanceTableDetailed, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_5, 1, 0, 1, 1)

        self.downloadCurrentAttendance = QPushButton(self.page_2)
        self.downloadCurrentAttendance.setObjectName(u"downloadCurrentAttendance")

        self.gridLayout_13.addWidget(self.downloadCurrentAttendance, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_6 = QGridLayout(self.page_3)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.AddEmpFrame = QFrame(self.page_3)
        self.AddEmpFrame.setObjectName(u"AddEmpFrame")
        self.AddEmpFrame.setFrameShape(QFrame.WinPanel)
        self.AddEmpFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.AddEmpFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.AddEmpBox = QVBoxLayout()
        self.AddEmpBox.setObjectName(u"AddEmpBox")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame = QFrame(self.AddEmpFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_14.addWidget(self.label_6)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)

        self.empDepartment = QLineEdit(self.widget)
        self.empDepartment.setObjectName(u"empDepartment")

        self.horizontalLayout_14.addWidget(self.empDepartment)


        self.gridLayout_8.addLayout(self.horizontalLayout_14, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.empIdLabel = QLabel(self.widget)
        self.empIdLabel.setObjectName(u"empIdLabel")
        self.empIdLabel.setFont(font1)

        self.horizontalLayout_5.addWidget(self.empIdLabel)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_23)

        self.empId = QLineEdit(self.widget)
        self.empId.setObjectName(u"empId")
        self.empId.setAutoFillBackground(False)
        self.empId.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.empId)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font4 = QFont()
        font4.setFamilies([u"Elephant"])
        font4.setPointSize(8)
        self.label_7.setFont(font4)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)

        self.empProfession = QLineEdit(self.widget)
        self.empProfession.setObjectName(u"empProfession")

        self.horizontalLayout_7.addWidget(self.empProfession)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.empNameLabel = QLabel(self.widget)
        self.empNameLabel.setObjectName(u"empNameLabel")
        self.empNameLabel.setFont(font1)

        self.horizontalLayout_6.addWidget(self.empNameLabel)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_25)

        self.empName = QLineEdit(self.widget)
        self.empName.setObjectName(u"empName")

        self.horizontalLayout_6.addWidget(self.empName)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_24)

        self.empJoiningYear = QLineEdit(self.widget)
        self.empJoiningYear.setObjectName(u"empJoiningYear")

        self.horizontalLayout_9.addWidget(self.empJoiningYear)


        self.gridLayout_8.addLayout(self.horizontalLayout_9, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_27)

        self.empExperience = QLineEdit(self.widget)
        self.empExperience.setObjectName(u"empExperience")

        self.horizontalLayout_8.addWidget(self.empExperience)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 2, 1, 1, 1)


        self.gridLayout_10.addWidget(self.widget, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.submitEmpDetails = QPushButton(self.frame_2)
        self.submitEmpDetails.setObjectName(u"submitEmpDetails")
        self.submitEmpDetails.setEnabled(True)
        self.submitEmpDetails.setFont(font1)

        self.horizontalLayout_10.addWidget(self.submitEmpDetails)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout_9.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_2, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_10.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame)

        self.frame_3 = QFrame(self.AddEmpFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_3)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_4)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(33, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_6, 0, 0, 1, 1)

        self.imageFrame = QLabel(self.frame_4)
        self.imageFrame.setObjectName(u"imageFrame")
        self.imageFrame.setEnabled(True)
        self.imageFrame.setMinimumSize(QSize(216, 216))
        self.imageFrame.setMaximumSize(QSize(216, 216))
        self.imageFrame.setAutoFillBackground(True)
        self.imageFrame.setFrameShape(QFrame.StyledPanel)
        self.imageFrame.setFrameShadow(QFrame.Sunken)
        self.imageFrame.setPixmap(QPixmap(u"icons/person Icon.ico"))
        self.imageFrame.setScaledContents(True)
        self.imageFrame.setWordWrap(True)

        self.gridLayout_12.addWidget(self.imageFrame, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(33, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 0, 2, 1, 1)


        self.gridLayout_11.addWidget(self.frame_4, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.imageSelectionButton = QPushButton(self.frame_3)
        self.imageSelectionButton.setObjectName(u"imageSelectionButton")
        self.imageSelectionButton.setEnabled(False)
        self.imageSelectionButton.setFont(font1)
        icon9 = QIcon()
        icon9.addFile(u"../../../../Downloads/pencil.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.imageSelectionButton.setIcon(icon9)
        self.imageSelectionButton.setIconSize(QSize(25, 25))
        self.imageSelectionButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.imageSelectionButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_11.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.frame_3)


        self.AddEmpBox.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.RegisterEmp = QPushButton(self.AddEmpFrame)
        self.RegisterEmp.setObjectName(u"RegisterEmp")
        self.RegisterEmp.setEnabled(False)
        self.RegisterEmp.setFont(font1)
        self.RegisterEmp.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.RegisterEmp)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)


        self.AddEmpBox.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.AddEmpBox, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.AddEmpFrame, 1, 1, 2, 2)

        self.verticalSpacer_11 = QSpacerItem(20, 124, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_11, 3, 2, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_9, 1, 3, 1, 1)

        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QFrame.NoFrame)

        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 4)

        self.horizontalSpacer_8 = QSpacerItem(4, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_14 = QGridLayout(self.page_4)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.thisMonthAttendance = QTableWidget(self.page_4)
        self.thisMonthAttendance.setObjectName(u"thisMonthAttendance")
        self.thisMonthAttendance.setFrameShape(QFrame.WinPanel)
        self.thisMonthAttendance.setFrameShadow(QFrame.Sunken)
        self.thisMonthAttendance.setGridStyle(Qt.DashDotDotLine)
        self.thisMonthAttendance.setSortingEnabled(True)

        self.gridLayout_14.addWidget(self.thisMonthAttendance, 1, 0, 1, 1)

        self.label_3 = QLabel(self.page_4)
        self.label_3.setObjectName(u"label_3")
        font5 = QFont()
        font5.setFamilies([u"Rockwell"])
        self.label_3.setFont(font5)

        self.gridLayout_14.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_15 = QGridLayout(self.page_5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalSpacer_15 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)

        self.widget_2 = QWidget(self.page_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_18 = QGridLayout(self.widget_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout_18.addWidget(self.label_11, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)


        self.gridLayout_15.addWidget(self.widget_2, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_9, 2, 1, 1, 1)

        self.ReportsFrame = QFrame(self.page_5)
        self.ReportsFrame.setObjectName(u"ReportsFrame")
        self.ReportsFrame.setFrameShape(QFrame.WinPanel)
        self.ReportsFrame.setFrameShadow(QFrame.Plain)
        self.ReportsFrame.setLineWidth(9)
        self.ReportsFrame.setMidLineWidth(11)
        self.gridLayout_16 = QGridLayout(self.ReportsFrame)
        self.gridLayout_16.setSpacing(0)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.MainReportLayout = QGridLayout()
        self.MainReportLayout.setSpacing(0)
        self.MainReportLayout.setObjectName(u"MainReportLayout")
        self.frame_6 = QFrame(self.ReportsFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_21)

        self.getReportButton = QPushButton(self.frame_6)
        self.getReportButton.setObjectName(u"getReportButton")

        self.horizontalLayout_4.addWidget(self.getReportButton)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)


        self.MainReportLayout.addWidget(self.frame_6, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.ReportsFrame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_11.addWidget(self.label_4)

        self.period = QComboBox(self.frame_7)
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.addItem("")
        self.period.setObjectName(u"period")

        self.horizontalLayout_11.addWidget(self.period)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_13)


        self.MainReportLayout.addWidget(self.frame_7, 1, 0, 1, 1)

        self.AdminReports = QFrame(self.ReportsFrame)
        self.AdminReports.setObjectName(u"AdminReports")
        self.AdminReports.setFrameShape(QFrame.StyledPanel)
        self.AdminReports.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.AdminReports)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(9, 9, -1, -1)
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_18)

        self.label_5 = QLabel(self.AdminReports)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_12.addWidget(self.label_5)

        self.pushButton_2 = QPushButton(self.AdminReports)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_12.addWidget(self.pushButton_2)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_14)


        self.gridLayout_17.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.MainReportLayout.addWidget(self.AdminReports, 3, 0, 1, 1)

        self.reportLabel = QLabel(self.ReportsFrame)
        self.reportLabel.setObjectName(u"reportLabel")

        self.MainReportLayout.addWidget(self.reportLabel, 0, 0, 1, 1)


        self.gridLayout_16.addLayout(self.MainReportLayout, 0, 0, 1, 1)


        self.gridLayout_15.addWidget(self.ReportsFrame, 1, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_16, 1, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 2, 1, 1)


        self.retranslateUi(AdminPanel)
        self.menuButton.toggled.connect(self.IconAndNameContainer.setHidden)
        self.menuButton.toggled.connect(self.IconContainer.setVisible)
        self.submitEmpDetails.clicked["bool"].connect(self.imageSelectionButton.setDisabled)
        self.imageSelectionButton.clicked["bool"].connect(self.RegisterEmp.setEnabled)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminPanel)
    # setupUi

    def retranslateUi(self, AdminPanel):
        AdminPanel.setWindowTitle(QCoreApplication.translate("AdminPanel", u"AdminPanel", None))
        self.goToReports.setText("")
        self.goToDashboard.setText("")
        self.goToListOfEmployee.setText("")
        self.goToAttendance.setText("")
        self.goToAddEmployee.setText("")
        self.launchAnAttender.setText("")
        self.IconLogo.setText("")
        self.Exit.setText("")
        self.goToDashboardLabeled.setText(QCoreApplication.translate("AdminPanel", u"Dashboard", None))
        self.goToListOfEmployeeLabeled.setText(QCoreApplication.translate("AdminPanel", u"Employee List", None))
        self.goToReportsLabeled.setText(QCoreApplication.translate("AdminPanel", u"Reports", None))
        self.launchAnAttenderLabeled.setText(QCoreApplication.translate("AdminPanel", u"Launch Attender", None))
        self.goToAttendanceLabeled.setText(QCoreApplication.translate("AdminPanel", u"Attendance", None))
        self.MainLogo.setText(QCoreApplication.translate("AdminPanel", u"@PTK", None))
        self.goToAddEmployeeLabeled.setText(QCoreApplication.translate("AdminPanel", u"Add Employee", None))
        self.Exit_2.setText(QCoreApplication.translate("AdminPanel", u"Logout", None))
        self.menuButton.setText("")
        self.label_14.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Dashboard</span></p></body></html>", None))
        self.totalEmpLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Total Employees </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Registered</span></p></body></html>", None))
        self.totalEmpValue.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">0</span></p></body></html>", None))
        self.totalAdminLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Total Admin </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Registered</span></p></body></html>", None))
        self.totalAdminValue.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">0</span></p></body></html>", None))
        self.AttendanceList.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Employee List:    </span></p></body></html>", None))
        self.currentMonthAndYear.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"> fdsfafasd</p></body></html>", None))
        self.downloadCurrentAttendance.setText(QCoreApplication.translate("AdminPanel", u"Download Current Attendance", None))
        self.label_6.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Department </p></body></html>", None))
        self.empDepartment.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Department", None))
        self.empIdLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:8pt;\">Employee Id</span></p></body></html>", None))
        self.empId.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Employee ID", None))
        self.label_7.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:9pt;\">Profession   </span></p></body></html>", None))
        self.empProfession.setText("")
        self.empProfession.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Porfession", None))
        self.empNameLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Employee Name</p></body></html>", None))
        self.empName.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Employee Name", None))
        self.label_8.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Joining Year</p></body></html>", None))
        self.empJoiningYear.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Joining Year", None))
        self.label_10.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Experience </p></body></html>", None))
        self.empExperience.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Total Experience", None))
        self.submitEmpDetails.setText(QCoreApplication.translate("AdminPanel", u"Submit", None))
        self.imageFrame.setText("")
        self.imageSelectionButton.setText(QCoreApplication.translate("AdminPanel", u"Select Image", None))
        self.RegisterEmp.setText(QCoreApplication.translate("AdminPanel", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Add Employee</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Attendance Sheet</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Reports</span></p></body></html>", None))
        self.getReportButton.setText(QCoreApplication.translate("AdminPanel", u"Generate Report", None))
        self.label_4.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Select The Report Duration</span></p></body></html>", None))
        self.period.setItemText(0, QCoreApplication.translate("AdminPanel", u"Last Month", None))
        self.period.setItemText(1, QCoreApplication.translate("AdminPanel", u"Last 3 Months", None))
        self.period.setItemText(2, QCoreApplication.translate("AdminPanel", u"Last 6 Months", None))
        self.period.setItemText(3, QCoreApplication.translate("AdminPanel", u"Last 9 Months", None))
        self.period.setItemText(4, QCoreApplication.translate("AdminPanel", u"Last 12 Months", None))

        self.label_5.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700;\">Get Admins</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("AdminPanel", u"Get", None))
        self.reportLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Reports</span></p></body></html>", None))
    # retranslateUi

