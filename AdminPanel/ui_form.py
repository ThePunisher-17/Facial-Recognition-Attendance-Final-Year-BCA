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
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        if not AdminPanel.objectName():
            AdminPanel.setObjectName(u"AdminPanel")
        AdminPanel.resize(898, 604)
        self.gridLayout_4 = QGridLayout(AdminPanel)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.IconAndNameContainer = QWidget(AdminPanel)
        self.IconAndNameContainer.setObjectName(u"IconAndNameContainer")
        self.IconAndNameContainer.setMinimumSize(QSize(200, 0))
        self.gridLayout_2 = QGridLayout(self.IconAndNameContainer)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.goToReportsLabeled = QPushButton(self.IconAndNameContainer)
        self.goToReportsLabeled.setObjectName(u"goToReportsLabeled")
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(14)
        self.goToReportsLabeled.setFont(font)
        icon = QIcon()
        icon.addFile(u"icons/reports.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToReportsLabeled.setIcon(icon)
        self.goToReportsLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToReportsLabeled, 6, 0, 1, 1)

        self.Exit_2 = QPushButton(self.IconAndNameContainer)
        self.Exit_2.setObjectName(u"Exit_2")
        self.Exit_2.setFont(font)
        self.Exit_2.setMouseTracking(False)
        self.Exit_2.setLayoutDirection(Qt.LeftToRight)
        self.Exit_2.setAutoFillBackground(True)
        icon1 = QIcon()
        icon1.addFile(u"icons/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.Exit_2.setIcon(icon1)
        self.Exit_2.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.Exit_2, 9, 0, 1, 1)

        self.goToAddEmployeeLabeled = QPushButton(self.IconAndNameContainer)
        self.goToAddEmployeeLabeled.setObjectName(u"goToAddEmployeeLabeled")
        self.goToAddEmployeeLabeled.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u"icons/add.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToAddEmployeeLabeled.setIcon(icon2)
        self.goToAddEmployeeLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToAddEmployeeLabeled, 3, 0, 1, 1)

        self.MainLogo = QPushButton(self.IconAndNameContainer)
        self.MainLogo.setObjectName(u"MainLogo")
        self.MainLogo.setEnabled(False)
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(16)
        self.MainLogo.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u"icons/favicon_io/favicon.ico", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"icons/favicon_io/favicon.ico", QSize(), QIcon.Disabled, QIcon.Off)
        self.MainLogo.setIcon(icon3)
        self.MainLogo.setIconSize(QSize(50, 50))

        self.gridLayout_2.addWidget(self.MainLogo, 0, 0, 1, 1)

        self.goToListOfEmployeeLabeled = QPushButton(self.IconAndNameContainer)
        self.goToListOfEmployeeLabeled.setObjectName(u"goToListOfEmployeeLabeled")
        self.goToListOfEmployeeLabeled.setFont(font)
        icon4 = QIcon()
        icon4.addFile(u"icons/list.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToListOfEmployeeLabeled.setIcon(icon4)
        self.goToListOfEmployeeLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToListOfEmployeeLabeled, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 8, 0, 1, 1)

        self.goToAttendanceLabeled = QPushButton(self.IconAndNameContainer)
        self.goToAttendanceLabeled.setObjectName(u"goToAttendanceLabeled")
        self.goToAttendanceLabeled.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u"icons/attendance.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToAttendanceLabeled.setIcon(icon5)
        self.goToAttendanceLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToAttendanceLabeled, 5, 0, 1, 1)

        self.launchAnAttenderLabeled = QPushButton(self.IconAndNameContainer)
        self.launchAnAttenderLabeled.setObjectName(u"launchAnAttenderLabeled")
        self.launchAnAttenderLabeled.setEnabled(True)
        self.launchAnAttenderLabeled.setFont(font)
        icon6 = QIcon()
        icon6.addFile(u"icons/attender.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.launchAnAttenderLabeled.setIcon(icon6)
        self.launchAnAttenderLabeled.setIconSize(QSize(25, 25))
        self.launchAnAttenderLabeled.setCheckable(True)

        self.gridLayout_2.addWidget(self.launchAnAttenderLabeled, 4, 0, 1, 1)

        self.goToDashboardLabeled = QPushButton(self.IconAndNameContainer)
        self.goToDashboardLabeled.setObjectName(u"goToDashboardLabeled")
        self.goToDashboardLabeled.setFont(font)
        icon7 = QIcon()
        icon7.addFile(u"icons/dashboard.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.goToDashboardLabeled.setIcon(icon7)
        self.goToDashboardLabeled.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.goToDashboardLabeled, 1, 0, 1, 1)

        self.remove_emp_label = QPushButton(self.IconAndNameContainer)
        self.remove_emp_label.setObjectName(u"remove_emp_label")
        self.remove_emp_label.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u"icons/trash.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.remove_emp_label.setIcon(icon8)
        self.remove_emp_label.setIconSize(QSize(25, 25))

        self.gridLayout_2.addWidget(self.remove_emp_label, 7, 0, 1, 1)


        self.gridLayout_4.addWidget(self.IconAndNameContainer, 0, 1, 2, 1)

        self.StatusBar = QWidget(AdminPanel)
        self.StatusBar.setObjectName(u"StatusBar")
        self.gridLayout_5 = QGridLayout(self.StatusBar)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.StatusBar)
        self.menuButton.setObjectName(u"menuButton")
        icon9 = QIcon()
        icon9.addFile(u"icons/drawer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon9)
        self.menuButton.setIconSize(QSize(25, 25))
        self.menuButton.setCheckable(True)

        self.gridLayout_5.addWidget(self.menuButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout_4.addWidget(self.StatusBar, 0, 2, 1, 1)

        self.IconContainer = QWidget(AdminPanel)
        self.IconContainer.setObjectName(u"IconContainer")
        self.gridLayout = QGridLayout(self.IconContainer)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.launchAnAttender = QPushButton(self.IconContainer)
        self.launchAnAttender.setObjectName(u"launchAnAttender")
        self.launchAnAttender.setEnabled(True)
        self.launchAnAttender.setIcon(icon6)
        self.launchAnAttender.setIconSize(QSize(25, 25))
        self.launchAnAttender.setCheckable(True)

        self.gridLayout.addWidget(self.launchAnAttender, 4, 0, 1, 1)

        self.goToAddEmployee = QPushButton(self.IconContainer)
        self.goToAddEmployee.setObjectName(u"goToAddEmployee")
        self.goToAddEmployee.setIcon(icon2)
        self.goToAddEmployee.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToAddEmployee, 3, 0, 1, 1)

        self.goToDashboard = QPushButton(self.IconContainer)
        self.goToDashboard.setObjectName(u"goToDashboard")
        self.goToDashboard.setIcon(icon7)
        self.goToDashboard.setIconSize(QSize(30, 30))

        self.gridLayout.addWidget(self.goToDashboard, 1, 0, 1, 1)

        self.goToAttendance = QPushButton(self.IconContainer)
        self.goToAttendance.setObjectName(u"goToAttendance")
        self.goToAttendance.setIcon(icon5)
        self.goToAttendance.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToAttendance, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.Exit = QPushButton(self.IconContainer)
        self.Exit.setObjectName(u"Exit")
        self.Exit.setIcon(icon1)
        self.Exit.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.Exit, 9, 0, 1, 1)

        self.goToReports = QPushButton(self.IconContainer)
        self.goToReports.setObjectName(u"goToReports")
        self.goToReports.setIcon(icon)
        self.goToReports.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToReports, 6, 0, 1, 1)

        self.IconLogo = QPushButton(self.IconContainer)
        self.IconLogo.setObjectName(u"IconLogo")
        self.IconLogo.setEnabled(False)
        self.IconLogo.setIcon(icon3)
        self.IconLogo.setIconSize(QSize(25, 30))

        self.gridLayout.addWidget(self.IconLogo, 0, 0, 1, 1)

        self.goToListOfEmployee = QPushButton(self.IconContainer)
        self.goToListOfEmployee.setObjectName(u"goToListOfEmployee")
        self.goToListOfEmployee.setIcon(icon4)
        self.goToListOfEmployee.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.goToListOfEmployee, 2, 0, 1, 1)

        self.remove_emp = QPushButton(self.IconContainer)
        self.remove_emp.setObjectName(u"remove_emp")
        self.remove_emp.setIcon(icon8)
        self.remove_emp.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.remove_emp, 7, 0, 1, 1)


        self.gridLayout_4.addWidget(self.IconContainer, 0, 0, 2, 1)

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
        self.gridLayout_23 = QGridLayout(self.page)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.dashboardLabel = QLabel(self.page)
        self.dashboardLabel.setObjectName(u"dashboardLabel")
        font2 = QFont()
        font2.setFamilies([u"Rockwell Condensed"])
        self.dashboardLabel.setFont(font2)

        self.gridLayout_23.addWidget(self.dashboardLabel, 0, 0, 1, 1)

        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_22 = QGridLayout(self.frame_9)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.frame_8 = QFrame(self.frame_9)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_8)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.verticalSpacer_5 = QSpacerItem(20, 136, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.empFrame = QFrame(self.frame_8)
        self.empFrame.setObjectName(u"empFrame")
        self.empFrame.setFrameShape(QFrame.WinPanel)
        self.empFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_24 = QGridLayout(self.empFrame)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.totalEmpLabel = QLabel(self.empFrame)
        self.totalEmpLabel.setObjectName(u"totalEmpLabel")
        font3 = QFont()
        font3.setFamilies([u"Elephant"])
        self.totalEmpLabel.setFont(font3)
        self.totalEmpLabel.setFrameShape(QFrame.WinPanel)
        self.totalEmpLabel.setFrameShadow(QFrame.Raised)

        self.gridLayout_24.addWidget(self.totalEmpLabel, 0, 0, 1, 1)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")

        self.gridLayout_24.addLayout(self.horizontalLayout_23, 3, 0, 1, 1)

        self.frame_10 = QFrame(self.empFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Sunken)
        self.gridLayout_19 = QGridLayout(self.frame_10)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.totalEmpValue = QLabel(self.frame_10)
        self.totalEmpValue.setObjectName(u"totalEmpValue")
        self.totalEmpValue.setFont(font)
        self.totalEmpValue.setIndent(0)

        self.gridLayout_19.addWidget(self.totalEmpValue, 0, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_32, 0, 0, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_33, 0, 2, 1, 1)


        self.gridLayout_24.addWidget(self.frame_10, 2, 0, 1, 1)

        self.line = QFrame(self.empFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_24.addWidget(self.line, 1, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.empFrame)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_19)

        self.adminFrame = QFrame(self.frame_8)
        self.adminFrame.setObjectName(u"adminFrame")
        self.adminFrame.setFrameShape(QFrame.WinPanel)
        self.adminFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_25 = QGridLayout(self.adminFrame)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.totalAdminLabel = QLabel(self.adminFrame)
        self.totalAdminLabel.setObjectName(u"totalAdminLabel")
        self.totalAdminLabel.setFont(font3)
        self.totalAdminLabel.setFrameShape(QFrame.WinPanel)
        self.totalAdminLabel.setFrameShadow(QFrame.Raised)

        self.gridLayout_25.addWidget(self.totalAdminLabel, 0, 0, 1, 1)

        self.frame_11 = QFrame(self.adminFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_20 = QGridLayout(self.frame_11)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_36)

        self.totalAdminValue = QLabel(self.frame_11)
        self.totalAdminValue.setObjectName(u"totalAdminValue")
        self.totalAdminValue.setFont(font)

        self.horizontalLayout_24.addWidget(self.totalAdminValue)

        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_37)


        self.gridLayout_20.addLayout(self.horizontalLayout_24, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.frame_11, 2, 0, 1, 1)

        self.line_2 = QFrame(self.adminFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_25.addWidget(self.line_2, 1, 0, 1, 1)


        self.horizontalLayout_15.addWidget(self.adminFrame)


        self.horizontalLayout_16.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_29 = QSpacerItem(64, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_29)


        self.gridLayout_21.addLayout(self.horizontalLayout_16, 0, 0, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_30, 0, 1, 1, 1)


        self.gridLayout_22.addWidget(self.frame_8, 0, 0, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_22.addItem(self.horizontalSpacer_20, 0, 1, 1, 1)


        self.gridLayout_23.addWidget(self.frame_9, 1, 0, 1, 2)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_23.addItem(self.horizontalSpacer_31, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_23.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_13 = QGridLayout(self.page_2)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.AttendanceList = QLabel(self.page_2)
        self.AttendanceList.setObjectName(u"AttendanceList")
        self.AttendanceList.setFont(font2)

        self.horizontalLayout_13.addWidget(self.AttendanceList)

        self.horizontalSpacer_28 = QSpacerItem(640, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_28)


        self.gridLayout_13.addLayout(self.horizontalLayout_13, 0, 0, 1, 1)

        self.empListFrame = QFrame(self.page_2)
        self.empListFrame.setObjectName(u"empListFrame")
        self.empListFrame.setFrameShape(QFrame.StyledPanel)
        self.empListFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.empListFrame)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.currentMonthAndYear = QLabel(self.empListFrame)
        self.currentMonthAndYear.setObjectName(u"currentMonthAndYear")
        font4 = QFont()
        font4.setFamilies([u"Rockwell Condensed"])
        font4.setPointSize(20)
        self.currentMonthAndYear.setFont(font4)
        self.currentMonthAndYear.setStyleSheet(u"")
        self.currentMonthAndYear.setFrameShape(QFrame.WinPanel)
        self.currentMonthAndYear.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.currentMonthAndYear, 0, 0, 1, 1)

        self.attendanceTableDetailed = QTableWidget(self.empListFrame)
        self.attendanceTableDetailed.setObjectName(u"attendanceTableDetailed")
        self.attendanceTableDetailed.setFrameShape(QFrame.WinPanel)
        self.attendanceTableDetailed.setFrameShadow(QFrame.Sunken)
        self.attendanceTableDetailed.setAlternatingRowColors(False)
        self.attendanceTableDetailed.setSortingEnabled(True)
        self.attendanceTableDetailed.horizontalHeader().setCascadingSectionResizes(True)
        self.attendanceTableDetailed.horizontalHeader().setProperty("showSortIndicator", True)
        self.attendanceTableDetailed.horizontalHeader().setStretchLastSection(True)
        self.attendanceTableDetailed.verticalHeader().setCascadingSectionResizes(True)
        self.attendanceTableDetailed.verticalHeader().setProperty("showSortIndicator", False)
        self.attendanceTableDetailed.verticalHeader().setStretchLastSection(False)

        self.gridLayout_7.addWidget(self.attendanceTableDetailed, 1, 0, 1, 1)


        self.gridLayout_13.addWidget(self.empListFrame, 1, 0, 1, 1)

        self.downloadCurrentAttendance = QPushButton(self.page_2)
        self.downloadCurrentAttendance.setObjectName(u"downloadCurrentAttendance")

        self.gridLayout_13.addWidget(self.downloadCurrentAttendance, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_26 = QGridLayout(self.page_3)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_9 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_9)

        self.coverFrame = QFrame(self.page_3)
        self.coverFrame.setObjectName(u"coverFrame")
        self.coverFrame.setFrameShape(QFrame.StyledPanel)
        self.coverFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.coverFrame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(15, 15, 15, 15)
        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_34, 0, 0, 1, 1)

        self.AddEmpFrame = QFrame(self.coverFrame)
        self.AddEmpFrame.setObjectName(u"AddEmpFrame")
        self.AddEmpFrame.setFrameShape(QFrame.WinPanel)
        self.AddEmpFrame.setFrameShadow(QFrame.Sunken)
        self.gridLayout_3 = QGridLayout(self.AddEmpFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.AddEmpBox = QVBoxLayout()
        self.AddEmpBox.setObjectName(u"AddEmpBox")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.empDetailsFrame = QFrame(self.AddEmpFrame)
        self.empDetailsFrame.setObjectName(u"empDetailsFrame")
        self.empDetailsFrame.setFrameShape(QFrame.Box)
        self.empDetailsFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.empDetailsFrame)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.empDetailsFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(1)
        self.gridLayout_9 = QGridLayout(self.frame_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.submitEmpDetails = QPushButton(self.frame_2)
        self.submitEmpDetails.setObjectName(u"submitEmpDetails")
        self.submitEmpDetails.setEnabled(True)
        self.submitEmpDetails.setFont(font3)

        self.horizontalLayout_10.addWidget(self.submitEmpDetails)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.gridLayout_9.addLayout(self.horizontalLayout_10, 0, 0, 2, 2)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_12, 2, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_2, 1, 0, 1, 1)

        self.widget = QWidget(self.empDetailsFrame)
        self.widget.setObjectName(u"widget")
        self.gridLayout_8 = QGridLayout(self.widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_38, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.empIdLabel = QLabel(self.widget)
        self.empIdLabel.setObjectName(u"empIdLabel")
        font5 = QFont()
        font5.setFamilies([u"Elephant"])
        font5.setPointSize(12)
        self.empIdLabel.setFont(font5)

        self.horizontalLayout_5.addWidget(self.empIdLabel)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_23)

        self.empId = QLineEdit(self.widget)
        self.empId.setObjectName(u"empId")
        self.empId.setAutoFillBackground(False)
        self.empId.setClearButtonEnabled(False)

        self.horizontalLayout_5.addWidget(self.empId)


        self.gridLayout_8.addLayout(self.horizontalLayout_5, 0, 1, 1, 2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.empNameLabel = QLabel(self.widget)
        self.empNameLabel.setObjectName(u"empNameLabel")
        self.empNameLabel.setFont(font3)

        self.horizontalLayout_6.addWidget(self.empNameLabel)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_25)

        self.empName = QLineEdit(self.widget)
        self.empName.setObjectName(u"empName")

        self.horizontalLayout_6.addWidget(self.empName)


        self.gridLayout_8.addLayout(self.horizontalLayout_6, 0, 3, 1, 1)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_39, 0, 4, 1, 1)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setFamilies([u"Elephant"])
        font6.setPointSize(8)
        self.label_7.setFont(font6)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_22)

        self.empProfession = QLineEdit(self.widget)
        self.empProfession.setObjectName(u"empProfession")

        self.horizontalLayout_7.addWidget(self.empProfession)


        self.gridLayout_8.addLayout(self.horizontalLayout_7, 1, 1, 1, 2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.horizontalLayout_14.addWidget(self.label_6)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_26)

        self.empDepartment = QLineEdit(self.widget)
        self.empDepartment.setObjectName(u"empDepartment")

        self.horizontalLayout_14.addWidget(self.empDepartment)


        self.gridLayout_8.addLayout(self.horizontalLayout_14, 1, 3, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.horizontalLayout_9.addWidget(self.label_8)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_24)

        self.empJoiningYear = QLineEdit(self.widget)
        self.empJoiningYear.setObjectName(u"empJoiningYear")

        self.horizontalLayout_9.addWidget(self.empJoiningYear)


        self.gridLayout_8.addLayout(self.horizontalLayout_9, 2, 1, 1, 2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font3)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_27)

        self.empExperience = QLineEdit(self.widget)
        self.empExperience.setObjectName(u"empExperience")

        self.horizontalLayout_8.addWidget(self.empExperience)


        self.gridLayout_8.addLayout(self.horizontalLayout_8, 2, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.gridLayout_8.addWidget(self.label, 3, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.male = QRadioButton(self.widget)
        self.male.setObjectName(u"male")

        self.verticalLayout.addWidget(self.male)

        self.female = QRadioButton(self.widget)
        self.female.setObjectName(u"female")

        self.verticalLayout.addWidget(self.female)


        self.gridLayout_8.addLayout(self.verticalLayout, 3, 2, 1, 1)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_42, 3, 3, 1, 1)


        self.gridLayout_10.addWidget(self.widget, 0, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.empDetailsFrame)

        self.empPhotoFrame = QFrame(self.AddEmpFrame)
        self.empPhotoFrame.setObjectName(u"empPhotoFrame")
        self.empPhotoFrame.setFrameShape(QFrame.Box)
        self.empPhotoFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.empPhotoFrame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.frame_4 = QFrame(self.empPhotoFrame)
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

        self.imageSelectionButton = QPushButton(self.empPhotoFrame)
        self.imageSelectionButton.setObjectName(u"imageSelectionButton")
        self.imageSelectionButton.setEnabled(False)
        self.imageSelectionButton.setFont(font3)
        icon10 = QIcon()
        icon10.addFile(u"../../../../Downloads/pencil.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.imageSelectionButton.setIcon(icon10)
        self.imageSelectionButton.setIconSize(QSize(25, 25))
        self.imageSelectionButton.setCheckable(True)

        self.horizontalLayout.addWidget(self.imageSelectionButton)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)


        self.gridLayout_11.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.horizontalLayout_3.addWidget(self.empPhotoFrame)


        self.AddEmpBox.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.RegisterEmp = QPushButton(self.AddEmpFrame)
        self.RegisterEmp.setObjectName(u"RegisterEmp")
        self.RegisterEmp.setEnabled(False)
        self.RegisterEmp.setFont(font3)
        self.RegisterEmp.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.RegisterEmp)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_12)


        self.AddEmpBox.addLayout(self.horizontalLayout_2)


        self.gridLayout_3.addLayout(self.AddEmpBox, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.AddEmpFrame, 0, 1, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)


        self.horizontalLayout_17.addWidget(self.coverFrame)

        self.horizontalSpacer_35 = QSpacerItem(22, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_35)


        self.gridLayout_26.addLayout(self.horizontalLayout_17, 1, 0, 1, 2)

        self.verticalSpacer_10 = QSpacerItem(20, 92, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_26.addItem(self.verticalSpacer_10, 2, 1, 1, 1)

        self.addEmployeeLabel = QLabel(self.page_3)
        self.addEmployeeLabel.setObjectName(u"addEmployeeLabel")
        self.addEmployeeLabel.setFont(font2)
        self.addEmployeeLabel.setFrameShape(QFrame.NoFrame)

        self.gridLayout_26.addWidget(self.addEmployeeLabel, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_28 = QGridLayout(self.page_4)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.attendanceSheet = QLabel(self.page_4)
        self.attendanceSheet.setObjectName(u"attendanceSheet")
        font7 = QFont()
        font7.setFamilies([u"Rockwell"])
        self.attendanceSheet.setFont(font7)

        self.gridLayout_28.addWidget(self.attendanceSheet, 0, 0, 1, 1)

        self.empListShortFrame = QFrame(self.page_4)
        self.empListShortFrame.setObjectName(u"empListShortFrame")
        self.empListShortFrame.setFrameShape(QFrame.StyledPanel)
        self.empListShortFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_14 = QGridLayout(self.empListShortFrame)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(15, 15, 15, 15)
        self.thisMonthAttendance = QTableWidget(self.empListShortFrame)
        self.thisMonthAttendance.setObjectName(u"thisMonthAttendance")
        self.thisMonthAttendance.setGridStyle(Qt.DotLine)
        self.thisMonthAttendance.setSortingEnabled(True)
        self.thisMonthAttendance.horizontalHeader().setCascadingSectionResizes(True)
        self.thisMonthAttendance.horizontalHeader().setProperty("showSortIndicator", True)
        self.thisMonthAttendance.horizontalHeader().setStretchLastSection(True)
        self.thisMonthAttendance.verticalHeader().setCascadingSectionResizes(True)

        self.gridLayout_14.addWidget(self.thisMonthAttendance, 0, 0, 1, 1)


        self.gridLayout_28.addWidget(self.empListShortFrame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_27 = QGridLayout(self.page_5)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.widget_2 = QWidget(self.page_5)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_18 = QGridLayout(self.widget_2)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_18.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.reportsLabel = QLabel(self.widget_2)
        self.reportsLabel.setObjectName(u"reportsLabel")
        self.reportsLabel.setFont(font2)

        self.gridLayout_18.addWidget(self.reportsLabel, 0, 0, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_18.addItem(self.horizontalSpacer_17, 0, 1, 1, 1)


        self.gridLayout_27.addWidget(self.widget_2, 0, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(239, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_15, 1, 0, 1, 1)

        self.coverFrameReports = QFrame(self.page_5)
        self.coverFrameReports.setObjectName(u"coverFrameReports")
        self.coverFrameReports.setFrameShape(QFrame.StyledPanel)
        self.coverFrameReports.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.coverFrameReports)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.verticalSpacer_7 = QSpacerItem(20, 23, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.horizontalSpacer_40 = QSpacerItem(12, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_40, 1, 0, 1, 1)

        self.ReportsFrame = QFrame(self.coverFrameReports)
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

        self.horizontalSpacer_41 = QSpacerItem(12, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_41, 1, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_11, 2, 1, 1, 1)


        self.gridLayout_27.addWidget(self.coverFrameReports, 1, 1, 2, 2)

        self.horizontalSpacer_16 = QSpacerItem(238, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_16, 2, 3, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 157, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_27.addItem(self.verticalSpacer_9, 3, 2, 1, 1)

        self.stackedWidget.addWidget(self.page_5)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 2, 1, 1)


        self.retranslateUi(AdminPanel)
        self.menuButton.toggled.connect(self.IconAndNameContainer.setHidden)
        self.menuButton.toggled.connect(self.IconContainer.setVisible)
        self.submitEmpDetails.clicked["bool"].connect(self.imageSelectionButton.setDisabled)
        self.imageSelectionButton.clicked["bool"].connect(self.RegisterEmp.setEnabled)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(AdminPanel)
    # setupUi

    def retranslateUi(self, AdminPanel):
        AdminPanel.setWindowTitle(QCoreApplication.translate("AdminPanel", u"AdminPanel", None))
#if QT_CONFIG(tooltip)
        self.goToReportsLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.goToReportsLabeled.setText(QCoreApplication.translate("AdminPanel", u"Reports", None))
        self.Exit_2.setText(QCoreApplication.translate("AdminPanel", u"Logout", None))
#if QT_CONFIG(tooltip)
        self.goToAddEmployeeLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Add Employee", None))
#endif // QT_CONFIG(tooltip)
        self.goToAddEmployeeLabeled.setText(QCoreApplication.translate("AdminPanel", u"Add Employee", None))
        self.MainLogo.setText(QCoreApplication.translate("AdminPanel", u"@PTK", None))
#if QT_CONFIG(tooltip)
        self.goToListOfEmployeeLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Employee List", None))
#endif // QT_CONFIG(tooltip)
        self.goToListOfEmployeeLabeled.setText(QCoreApplication.translate("AdminPanel", u"Employee List", None))
#if QT_CONFIG(tooltip)
        self.goToAttendanceLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Attendance", None))
#endif // QT_CONFIG(tooltip)
        self.goToAttendanceLabeled.setText(QCoreApplication.translate("AdminPanel", u"Attendance", None))
#if QT_CONFIG(tooltip)
        self.launchAnAttenderLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Launch Attender", None))
#endif // QT_CONFIG(tooltip)
        self.launchAnAttenderLabeled.setText(QCoreApplication.translate("AdminPanel", u"Launch Attender", None))
#if QT_CONFIG(shortcut)
        self.launchAnAttenderLabeled.setShortcut("")
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.goToDashboardLabeled.setToolTip(QCoreApplication.translate("AdminPanel", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.goToDashboardLabeled.setText(QCoreApplication.translate("AdminPanel", u"Dashboard", None))
#if QT_CONFIG(tooltip)
        self.remove_emp_label.setToolTip(QCoreApplication.translate("AdminPanel", u"Remove Employee", None))
#endif // QT_CONFIG(tooltip)
        self.remove_emp_label.setText(QCoreApplication.translate("AdminPanel", u"Remove Employee", None))
        self.menuButton.setText("")
#if QT_CONFIG(tooltip)
        self.launchAnAttender.setToolTip(QCoreApplication.translate("AdminPanel", u"Launch Attender", None))
#endif // QT_CONFIG(tooltip)
        self.launchAnAttender.setText("")
#if QT_CONFIG(tooltip)
        self.goToAddEmployee.setToolTip(QCoreApplication.translate("AdminPanel", u"Add Employee", None))
#endif // QT_CONFIG(tooltip)
        self.goToAddEmployee.setText("")
#if QT_CONFIG(tooltip)
        self.goToDashboard.setToolTip(QCoreApplication.translate("AdminPanel", u"Dashboard", None))
#endif // QT_CONFIG(tooltip)
        self.goToDashboard.setText("")
#if QT_CONFIG(tooltip)
        self.goToAttendance.setToolTip(QCoreApplication.translate("AdminPanel", u"Attendance", None))
#endif // QT_CONFIG(tooltip)
        self.goToAttendance.setText("")
        self.Exit.setText("")
#if QT_CONFIG(tooltip)
        self.goToReports.setToolTip(QCoreApplication.translate("AdminPanel", u"Reports", None))
#endif // QT_CONFIG(tooltip)
        self.goToReports.setText("")
        self.IconLogo.setText("")
#if QT_CONFIG(tooltip)
        self.goToListOfEmployee.setToolTip(QCoreApplication.translate("AdminPanel", u"Employee List", None))
#endif // QT_CONFIG(tooltip)
        self.goToListOfEmployee.setText("")
#if QT_CONFIG(tooltip)
        self.remove_emp.setToolTip(QCoreApplication.translate("AdminPanel", u"Remove Employee", None))
#endif // QT_CONFIG(tooltip)
        self.remove_emp.setText("")
        self.dashboardLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Dashboard</span></p></body></html>", None))
        self.totalEmpLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Total Employees </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Registered</span></p></body></html>", None))
        self.totalEmpValue.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">0</span></p></body></html>", None))
        self.totalAdminLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Total  Admin </span></p><p align=\"center\"><span style=\" font-size:11pt;\">Registered</span></p></body></html>", None))
        self.totalAdminValue.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">0</span></p></body></html>", None))
        self.AttendanceList.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Employee List:    </span></p></body></html>", None))
        self.currentMonthAndYear.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p align=\"center\"> fdsfafasd</p></body></html>", None))
        self.downloadCurrentAttendance.setText(QCoreApplication.translate("AdminPanel", u"Download Current Attendance", None))
        self.submitEmpDetails.setText(QCoreApplication.translate("AdminPanel", u"Submit", None))
        self.empIdLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:8pt;\">Employee Id</span></p></body></html>", None))
        self.empId.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Employee ID", None))
        self.empNameLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Employee Name</p></body></html>", None))
        self.empName.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Employee Name", None))
        self.label_7.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:9pt;\">Profession   </span></p></body></html>", None))
        self.empProfession.setText("")
        self.empProfession.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Porfession", None))
        self.label_6.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Department </p></body></html>", None))
        self.empDepartment.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Department", None))
        self.label_8.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Joining Year</p></body></html>", None))
        self.empJoiningYear.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Joining Year", None))
        self.label_10.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p>Experience </p></body></html>", None))
        self.empExperience.setPlaceholderText(QCoreApplication.translate("AdminPanel", u"Total Experience", None))
        self.label.setText(QCoreApplication.translate("AdminPanel", u"Gender", None))
        self.male.setText(QCoreApplication.translate("AdminPanel", u"Male", None))
        self.female.setText(QCoreApplication.translate("AdminPanel", u"Female", None))
        self.imageFrame.setText("")
        self.imageSelectionButton.setText(QCoreApplication.translate("AdminPanel", u"Select Image", None))
        self.RegisterEmp.setText(QCoreApplication.translate("AdminPanel", u"Register", None))
        self.addEmployeeLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Add Employee</span></p></body></html>", None))
        self.attendanceSheet.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Attendance Sheet</span></p></body></html>", None))
        self.reportsLabel.setText(QCoreApplication.translate("AdminPanel", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:700; text-decoration: underline;\">Reports</span></p></body></html>", None))
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

