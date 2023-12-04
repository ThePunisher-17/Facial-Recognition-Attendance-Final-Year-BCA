# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QRegularExpressionValidator
from PySide6.QtCore import QRegularExpression

import firebase_admin
from firebase_admin import credentials, db
import os
from pathlib import Path

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_SignUpWindow
from SignUpWindow.ui_form import Ui_SignUpWindow

class SignUpWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SignUpWindow()
        self.ui.setupUi(self)

        self.path = os.getcwd()

        # self.cred = credentials.Certificate(
        #     f"{self.path}\\Database Key\\serviceAccountKey.json")
        # firebase_admin.initialize_app(self.cred, {
        #     "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
        # })

        cred = credentials.Certificate(
            f'{self.path}\\AdminPanel\\Core\\Database Key\\serviceAccountKey.json')
        project_id = cred.project_id

        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
            })

        self.ref = db.reference("administrators")

        #

        self.ui.adminName.setValidator(QRegularExpressionValidator(
            QRegularExpression(r"[A-Za-z]+[\s]{1}+[A-Za-z_]{4,100}$")))
        self.ui.adminMobileNo.setValidator(
            QRegularExpressionValidator(QRegularExpression(r"^[0-9]{10}$")))

        self.changePage = False

        '''
            collection data from admin
            Start
        '''
        self.ui.adminSubmit.clicked.connect(self.collectData)
        '''
            End
        '''

    def collectData(self):
        data = {}
        name = self.ui.adminName.text()
        no = self.ui.adminMobileNo.text()
        id = name[:4]+no[-4:]
        if self.ui.adminPass1.text() == self.ui.adminPass2.text():
            password = self.ui.adminPass1.text()
            rawdata = {"Name": name, "No": no, "Password": password}
            data[id] = rawdata

            for key, value in data.items():
                self.ref.child(str(key)).set(value)

            return self.launchPopUpAndLogin()

        else:
            message = QMessageBox()
            message.setWindowTitle("Error")
            message.setText("Password Mismatch")
            message.setIcon(QMessageBox.Critical)
            message.setStandardButtons(QMessageBox.Ok)
            message.exec()
            self.clearInp()

            return False

    def launchPopUpAndLogin(self):
        message = QMessageBox()
        message.setWindowTitle("Success")
        message.setText("Sign Up Successful\nRememver: \nYour ID is first 4 latters of your name + last 4 digits of your mobile number.\n\n\nExample: \n If Name: 'Ravi' and Mobile No.: '1234567890'\n Then your ID will be: 'Ravi7890'")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        self.clearInp()
        message.exec()
        return True

    def clearInp(self):
        self.ui.adminName.setText("")
        self.ui.adminMobileNo.setText("")
        self.ui.adminPass1.setText("")
        self.ui.adminPass2.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = SignUpWindow()
    with open("styleSignUp.qss", "r") as style:
        app.setStyleSheet(style.read())
    widget.show()
    sys.exit(app.exec())
