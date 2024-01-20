# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

import firebase_admin
from firebase_admin import credentials, db
from pathlib import Path
import os

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_LoginWindow

from LoginWindow.ui_form import Ui_LoginWindow

class LoginWindow(QWidget):
    a = 0
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)

        self.path = os.getcwd()

        # self.cred = credentials.Certificate(
        #      f"{self.path}\\Database Key\\serviceAccountKey.json")
        # self.cred = credentials.Certificate(
        #      f"{self.path}\\Database Key\\serviceAccountKey.json")
        # firebase_admin.initialize_app(self.cred, {
        #      "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
        #  })

        cred = credentials.Certificate(
           fr'{self.path}\LoginWindow\Database Key\serviceAccountKey.json')
        project_id = cred.project_id

        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
            })

        self.ref = db.reference("administrators/").get()


        self.ui.adminId.setValidator(QRegularExpressionValidator(
            QRegularExpression(r"^[A-Za-z]{4}+[0-9_]{4}$")))
        self.ui.adminPassword.setValidator(QRegularExpressionValidator(
            QRegularExpression(r"^[A-Za-z][A-Za-z0-9_!@#$%-]{4,40}$")))

        # self.ui.loginButton.toggled.connect(lambda: self.loginVerify())

        self.ui.showPassword.clicked.connect(self.showPassword)
        self.passwordVisible = False

    def getAdminData(self):
        if self.ui.adminId.text() == "" and self.ui.adminPassword.text() == "":
            if LoginWindow.a == 0:
                message = QMessageBox()
                message.setWindowTitle("Failed")
                message.setText("Please fill all the fields")
                message.exec()
                LoginWindow.a = 1
                return 0
        
        self.Id = self.ui.adminId.text()
        self.password = self.ui.adminPassword.text()

    def loginVerify(self):
        if self.getAdminData() == 0:
            return

        self.ref = db.reference("administrators/").get()

        flag = 0

        # print(self.ref)
        for Id, Key in self.ref.items():
            id = Id
            password = Key["Password"]
            if id == self.Id and password == self.password:
                flag = 1
                break

        if flag == 1:
            self.resetInputs()
            message = QMessageBox()
            message.setWindowTitle("Success")
            message.setText("Login Successful")
            message.exec()
            return True
        else:
            message = QMessageBox()
            message.setWindowTitle("Failed")
            message.setText("Invalid Credentials")
            self.resetInputs()
            message.exec()
            return False

    def resetInputs(self):
        self.ui.adminId.setText("")
        self.ui.adminPassword.setText("")

    def showPassword(self):
        if self.passwordVisible == False:
            self.ui.adminPassword.setEchoMode(QLineEdit.EchoMode.Normal)
            self.passwordVisible = True

        else:
            self.ui.adminPassword.setEchoMode(QLineEdit.EchoMode.Password)
            self.passwordVisible = False



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginWindow()
    with open("styleLogin.qss", "r") as f:
        widget.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())
