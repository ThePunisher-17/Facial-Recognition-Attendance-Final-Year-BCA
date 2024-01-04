# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtGui import QPixmap, QRegularExpressionValidator
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer, QRegularExpression

import firebase_admin
from firebase_admin import credentials, db
import numpy as np
import os
from twilio.rest import Client

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
# from ui_form import Ui_ResetPassword
from ResetPassword.ui_form import Ui_ResetPassword

class ResetPassword(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ResetPassword()
        self.ui.setupUi(self)

        self.path = os.getcwd()

        # cred = credentials.Certificate(f"{self.path}\\Database Key\\serviceAccountKey.json")
        # firebase_admin.initialize_app(cred, {
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
        self.ref1 = db.reference("administrators").get()

        self.ui.ResetWindow.setCurrentIndex(0)

        self.ui.UserID.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[A-Za-z]{4}+[0-9_]{4}$")))
        self.ui.otpBox.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[0-9_]{6}")))

        self.ui.newPass.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[A-Za-z][A-Za-z0-9_!@#$%-]{4,40}$")))
        self.ui.confNewPass.setValidator(QRegularExpressionValidator(QRegularExpression(r"^[A-Za-z][A-Za-z0-9_!@#$%-]{4,40}$")))

        self.ui.sendOtp.clicked.connect(self.isIdExits)

        self.ui.verifyOtp.clicked.connect(self.verifyOTP)

        self.ui.ReturnToLogin.clicked.connect(self.clears)

        self.ui.ResetPasswordButton.clicked.connect(self.verifyPasswords)



    def isIdExits(self):
        self.UserIdInp = self.ui.UserID.text()
        cntr = 0
        if self.UserIdInp == "" or len(self.UserIdInp) < 8:
            QMessageBox.warning(self, "Warning", "Please Enter a User Id")
            return
        
        for key, value in self.ref1.items():
            if self.UserIdInp == key:
                cntr+=1
                self.sendOTP(self.UserIdInp)

        if cntr == 0:
            QMessageBox.warning(self, "Warning", "User Id does not exist")
            self.ui.UserID.clear()


    def sendOTP(self, userId):
        # Define your account sid and auth token
        # You need to replace them with your own credentials
        # You can get them from https://www.twilio.com/console

        # account_sid = "ACa79ebb702f1c0617548604c4e347654d"
        # auth_token = "5a4ed0ea809a3cfc69fdfa7faef473c2"

        # Create a client object with your credentials

        # client = Client(account_sid, auth_token)

        # Define the phone number and the message you want to send
        # You need to replace them with your own values
        # You also need to use a valid twilio phone number

        # to_number = "+917588650"
        # from_number = "+14132895239"
        self.otp = np.random.randint(100000, 999999)
        # message = f"Your OTP is {self.otp}. Please Don't share it with anyone"

        # Send the message using the client object


        # message = client.messages.create(
        #     body=message,
        #     from_=from_number,
        #     to=to_number
        # )

        # Print the message sid
        print(self.otp)
        self.ui.verifyOtp.setEnabled(True)

    def verifyOTP(self):
        if self.ui.otpBox.text() == "":
            QMessageBox.warning(self, "Warning", "Please Enter OTP")
            return
        if self.otp == int(self.ui.otpBox.text()):
            QMessageBox.information(self, "Success", "OTP Verified")
            self.ui.ResetWindow.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Warning", "Wrong OTP")


    def verifyPasswords(self):
        if len(self.ui.confNewPass.text()) >= 10 or len(self.ui.newPass.text()) >= 10:
            if self.ui.newPass.text() == self.ui.confNewPass.text():
                for key, _ in self.ref1.items():
                    if self.UserIdInp == key:
                        self.ref.child(key).update({"Password": self.ui.newPass.text()})
                        QMessageBox.information(self, "Success", "Password Changed Successfully")
                        self.ui.UserID.clear()
                        self.ui.otpBox.clear()
                        self.ui.newPass.clear()
                        self.ui.confNewPass.clear()
                        self.ui.ReturnToLogin.click()
                        break
            else:
                QMessageBox.warning(self, "Warning", "Passwords do not match")

        else:
            QMessageBox.warning(self, "Warning", "Password length must be greater than 10")
            return 0
        
    def clears(self):
        self.ui.UserID.clear()
        self.ui.otpBox.clear()
        self.ui.newPass.clear()
        self.ui.confNewPass.clear()
        self.ui.ResetWindow.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ResetPassword()
    with open("style.qss") as f:
        widget.setStyleSheet(f.read())
    widget.show()
    sys.exit(app.exec())
