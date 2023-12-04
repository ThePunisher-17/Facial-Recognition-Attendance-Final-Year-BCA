# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
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

        self.regex = QRegularExpression(r"^[A-Za-z][A-Za-z0-9_!@#$%-]{4,40}$")
        self.validator = QRegularExpressionValidator(self.regex)

        self.ui.adminId.setValidator(QRegularExpressionValidator(
            QRegularExpression(r"^[A-Za-z][A-Za-z0-9_]{4,8}$")))
        self.ui.adminPassword.setValidator(QRegularExpressionValidator(
            QRegularExpression(r"^[A-Za-z][A-Za-z0-9_!@#$%-]{4,40}$")))

        self.ui.loginButton.clicked.connect(lambda: self.loginVerify())

    def getAdminData(self):

        self.Id = self.ui.adminId.text()
        self.password = self.ui.adminPassword.text()

    def loginVerify(self):
        self.getAdminData()
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = LoginWindow()
    with open("styleLogin.qss", "r") as f:
        widget.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())
