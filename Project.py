# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint
from PySide6.QtGui import QIcon

from AdminPanel.adminpanel import AdminPanel
from LoginWindow.loginwindow import LoginWindow
from SignUpWindow.signupwindow import SignUpWindow
from ResetPassword.resetpassword import ResetPassword

import firebase_admin
from firebase_admin import credentials, db
import os
import types

from ui_form import Ui_Project


class Project(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.path = os.getcwd()
        self.cred = credentials.Certificate(
            f"{self.path}\\AdminPanel\\Core\\Database Key\\serviceAccountKey.json")

        firebase_admin.initialize_app(self.cred, {
            "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
            'storageBucket': "employeeattendancerealtime.appspot.com"
        })

        self.ui = Ui_Project()
        self.ui.setupUi(self)

        self.signup = SignUpWindow()
        self.login = LoginWindow()
        self.admin = AdminPanel()
        self.resetpassword = ResetPassword()

        self.ui.stackedWidget.addWidget(self.signup)
        self.ui.stackedWidget.addWidget(self.login)
        self.ui.stackedWidget.addWidget(self.admin)
        self.ui.stackedWidget.addWidget(self.resetpassword)

        self.ui.stackedWidget.setCurrentIndex(1)

        # Signup page actions
        self.signup.ui.adminSubmit.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(
            1) if self.signup.collectData() else self.ui.stackedWidget.setCurrentIndex(0))
        self.signup.ui.goToLogin.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # Login page actions
        self.login.ui.loginButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2) if self.login.loginVerify() else self.ui.stackedWidget.setCurrentIndex(1))
        self.login.ui.goToSignUp.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))
        
        self.login.ui.resetPassword.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(3))

        # Admin panel actions
        self.admin.ui.Exit.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1) if (QMessageBox.warning(self, "warning", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes) else self.ui.stackedWidget.setCurrentIndex(2))
            
        self.admin.ui.Exit_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1) if (QMessageBox.warning(self, "warning", "Are you sure you want to exit?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes) else self.ui.stackedWidget.setCurrentIndex(2))
        
        
        #Forgotten Password
        self.resetpassword.ui.ReturnToLogin.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))

        self.setWindowTitle("Pratik's Attender")
        self.setWindowIcon(QIcon("icons\\favicon_io\\favicon.ico"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Project()
    with open("style.qss") as f:
        widget.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())
