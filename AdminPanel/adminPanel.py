# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QMainWindow, QFileDialog, QWidget, QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QTimer

from firebase_admin import credentials, db
import os
import cv2
import time
import pandas as pd
import firebase_admin


# from Core.main import Attender
# from savecurrentattendance import SaveCurrentAttendance
# from Core.databasedataadder import DatabaseDataAdder
# from Core.encodegenerator import EncodeGenerator
# from ui_form import Ui_AdminPanel

from AdminPanel.Core.main import Attender
from AdminPanel.savecurrentattendance import SaveCurrentAttendance
from AdminPanel.Core.databasedataadder import DatabaseDataAdder
from AdminPanel.Core.encodegenerator import EncodeGenerator
from AdminPanel.ui_form import Ui_AdminPanel


class AdminPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self)

        self.path = os.getcwd()

        # self.cred = credentials.Certificate(f"{self.path}\\Core\\Database Key\\serviceAccountKey.json")

        # firebase_admin.initialize_app(self.cred, {
        #      "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
        #      'storageBucket': "employeeattendancerealtime.appspot.com"
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

        self.QMessageBoxs = QMessageBox()

        # Getting Current Month and Year
        self.month = time.strftime("%Y-%m-%d")
        self.month = str.split(self.month, "-")
        self.date = self.month[2]
        self.year = self.month[0]
        self.month = self.month[1]
        self.monthList = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]

        # print(f"Employee/{self.year}/{self.monthList[int(self.month)-1]}")
        # Get the database reference
        self.db_ref = db.reference(
            f"Employee/{self.year}/{self.monthList[int(self.month)-1]}")
        self.db_ref_admin = db.reference(f"administrators/")

        self.ui.IconContainer.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.goToDashboard.setChecked(True)

        if self.date == "01":
            self.itIsFirstDay()

        #
        self.ui.currentMonthAndYear.setText(
            f"{self.monthList[int(self.month)-1]} {self.year}")

        # Icon Buttons Event Binding
        self.ui.goToDashboard.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.goToListOfEmployee.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.goToAddEmployee.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.goToAttendance.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.goToReports.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(4))

        self.ui.launchAnAttender.clicked.connect(lambda: Attender())

        # Labeled Buttons Event Binding
        self.ui.goToDashboardLabeled.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.goToListOfEmployeeLabeled.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.goToAddEmployeeLabeled.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.goToAttendanceLabeled.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.goToReportsLabeled.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(4))

        self.ui.launchAnAttenderLabeled.clicked.connect(lambda: Attender())

        '''
            Sidebar Event Ends
        '''

        '''
            Download The Current Attendance Table
            Start
        '''
        self.ui.downloadCurrentAttendance.clicked.connect(
            lambda: SaveCurrentAttendance() and self.downloadCurrentAttendanceClose()
        )
        '''
            End
        '''

        '''
            attendanceTableDetailed  Table display and other functions
            Start
        '''
        self.ui.goToListOfEmployeeLabeled.clicked.connect(
            lambda: self.attendanceTableDetailedShow()
        )
        self.ui.goToListOfEmployeeLabeled.clicked.connect(
            lambda: self.ui.attendanceTableDetailed.show()
        )

        self.ui.goToListOfEmployee.clicked.connect(
            lambda: self.attendanceTableDetailedShow()
        )
        self.ui.goToListOfEmployee.clicked.connect(
            lambda: self.ui.attendanceTableDetailed.show()
        )

        '''
            End
        '''

        '''
            thisMonthAttendance Table display and other functions
            Start
        '''
        self.ui.goToAttendanceLabeled.clicked.connect(
            lambda: self.thisMonthAttendanceTableShow()
        )
        self.ui.goToAttendanceLabeled.clicked.connect(
            lambda: self.ui.thisMonthAttendance.show()
        )

        self.ui.goToAttendance.clicked.connect(
            lambda: self.ui.thisMonthAttendance.show()
        )
        self.ui.goToAttendance.clicked.connect(
            lambda: self.thisMonthAttendanceTableShow()
        )

        '''
            End
        '''

        '''
            imageSelectionButton Button Event 
            used to take image of employee when we add employee
            Start
        '''

        self.ui.imageSelectionButton.clicked.connect(
            lambda: self.openAndSaveImage()
        )
        '''
            End
        '''

        '''
            submitEmpDetails Button Event 
            used to update the details of an employee
            Start
        '''
        self.ui.submitEmpDetails.clicked.connect(
            lambda: self.updateEmpDetails()
        )

        '''
            End
        '''

        '''
            confirmRegistration Frame show and hide logic Event
            used to confirm registration of employee
            Start            
        '''

        self.ui.RegisterEmp.clicked.connect(
            lambda: self.confirmEmployeeRegistration())

        '''
            End
        '''

        '''
            Dashboard labels
            Start
        '''
        self.ui.totalEmpValue.setText(str(len(self.db_ref.get())))
        self.ui.totalAdminValue.setText(str(len(self.db_ref_admin.get())))
        '''
            End
        '''

        '''
            Reports page
            Start
        '''
        self.ui.getReportButton.clicked.connect(self.generateReprots)

        '''
            End
        '''

        '''
            Hidden Elements
            Start
        '''
        self.ui.AdminReports.setVisible(False)
        '''
            End
        '''

    def attendanceTableDetailedShow(self):
        # Retrieve data from Firebase

        data = self.db_ref.get()
        # Set the number of rows and columns
        self.ui.attendanceTableDetailed.setRowCount(len(data))
        self.ui.attendanceTableDetailed.setColumnCount(len(data["101"])-1)

        # Set the headers
        self.ui.attendanceTableDetailed.setHorizontalHeaderLabels(
            ['ID', 'Name', "Profession", "Department", "Experience", "Starting Year", "Total Attendance"])

        # Add data to the table
        for row, (table_name, table_data) in enumerate(data.items()):
            # Create table items for the table name and data
            empId = QTableWidgetItem(table_name)

            empName = QTableWidgetItem(str(table_data["Name"]))

            empProfession = QTableWidgetItem(str(table_data["Profession"]))

            empDepartment = QTableWidgetItem(str(table_data["Department"]))

            empExperience = QTableWidgetItem(str(table_data["Experience"]))

            empStartingYear = QTableWidgetItem(
                str(table_data["Starting_Year"]))

            empTotalAttendance = QTableWidgetItem(
                str(table_data["total_attendance"]))

            # Set the items in the table
            self.ui.attendanceTableDetailed.setItem(row, 0, empId)
            self.ui.attendanceTableDetailed.setItem(row, 1, empName)
            self.ui.attendanceTableDetailed.setItem(row, 2, empProfession)
            self.ui.attendanceTableDetailed.setItem(row, 3, empDepartment)
            self.ui.attendanceTableDetailed.setItem(row, 4, empExperience)
            self.ui.attendanceTableDetailed.setItem(row, 5, empStartingYear)
            self.ui.attendanceTableDetailed.setItem(row, 6, empTotalAttendance)

            self.ui.attendanceTableDetailed.setColumnWidth(0, 40)
            self.ui.attendanceTableDetailed.setColumnWidth(1, 200)
            self.ui.attendanceTableDetailed.setColumnWidth(2, 200)
            self.ui.attendanceTableDetailed.setColumnWidth(3, 200)
            self.ui.attendanceTableDetailed.setColumnWidth(4, 200)
            self.ui.attendanceTableDetailed.setColumnWidth(5, 200)
            self.ui.attendanceTableDetailed.setColumnWidth(6, 200)

            self.ui.attendanceTableDetailed.verticalHeader().setVisible(False)

            table_width = self.ui.attendanceTableDetailed.horizontalHeader().length()
            table_height = self.ui.attendanceTableDetailed.verticalHeader().length()

        self.ui.attendanceTableDetailed.show()

    def thisMonthAttendanceTableShow(self):
        # Retrieve data from Firebase
        data = self.db_ref.get()
        self.ui.thisMonthAttendance.setRowCount(len(data))
        self.ui.thisMonthAttendance.setColumnCount(3)
        # Set the headers
        self.ui.thisMonthAttendance.setHorizontalHeaderLabels(
            ['ID', 'Name', "Total Attendance"])

        for row, (table_name, table_data) in enumerate(data.items()):
            # Create table items for the table name and data
            empId = QTableWidgetItem(table_name)
            # empId.setFont(QFont('Times', 10, QFont.Bold))
            # empId.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            empName = QTableWidgetItem(str(table_data["Name"]))
            # empName.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            empTotalAttendance = QTableWidgetItem(
                str(table_data["total_attendance"]))
            # empTotalAttendance.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

            # Set the items in the table
            self.ui.thisMonthAttendance.setItem(row, 0, empId)
            self.ui.thisMonthAttendance.setItem(row, 1, empName)
            self.ui.thisMonthAttendance.setItem(row, 2, empTotalAttendance)

            self.ui.thisMonthAttendance.verticalHeader().setVisible(False)

            table_width = self.ui.thisMonthAttendance.horizontalHeader().length()
            table_height = self.ui.thisMonthAttendance.verticalHeader().length()

    def updateEmpDetails(self):
        dataAdder = DatabaseDataAdder()
        empIdAndData = {}

        self.id = self.ui.empId.text()
        details = {
            "Name": self.ui.empName.text(),
            "Profession": self.ui.empProfession.text(),
            "Department": self.ui.empDepartment.text(),
            "Starting_Year": self.ui.empJoiningYear.text(),
            "Experience": self.ui.empExperience.text(),
            "total_attendance": 0,
            "last_attendance_time": "2023-09-14 20:00:00"
        }
        # Adding Details of employee
        empIdAndData[self.id] = details

        # creating Backup
        with open(fr"{self.path}/Core/data.txt", "a") as f:
            f.write(f"{empIdAndData}\n")

        # Uploading to Database
        dataAdder.send_data(empIdAndData)
        self.ui.totalEmpValue.setText(str(len(self.db_ref.get())))

    def openAndSaveImage(self):
        self.image_path, _ = QFileDialog.getOpenFileName(
            self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")
        if self.image_path:
            # resizing and saving the image
            img = cv2.imread(self.image_path)
            img = cv2.resize(img, (216, 216))
            cv2.imwrite(f"{self.image_path}", img)

            # Opening and saving the image in our images folder
            self.ui.imageFrame.setPixmap(QPixmap(self.image_path))
            QPixmap(self.image_path).save(
                f"{self.path}\\Core\\Images\\{self.id}.jpeg")
            # Updating the images of employees
        EncodeGenerator()

    def confirmEmployeeRegistration(self):
        self.QMessageBoxs.setWindowTitle("Pop Up")
        self.QMessageBoxs.setText("Employee Registered")
        self.QMessageBoxs.setStandardButtons(QMessageBox.Ok)
        self.QMessageBoxs.show()
        self.ui.empId.setText("")
        self.ui.empName.setText("")
        self.ui.empProfession.setText("")
        self.ui.empDepartment.setText("")
        self.ui.empJoiningYear.setText("")
        self.ui.empExperience.setText("")
        self.ui.imageFrame.setPixmap(QPixmap("icons\person Icon.ico"))
        self.ui.imageFrame.setScaledContents(True)
        self.ui.imageSelectionButton.setEnabled(False)
        self.ui.RegisterEmp.setEnabled(False)

    def downloadCurrentAttendanceClose(self):
        message = QMessageBox()
        message.setWindowTitle("Sheet Downloaded")
        message.setText("File Downloaded Successfully")
        message.setStandardButtons(QMessageBox.Ok)
        message.setIcon(QMessageBox.Information)
        message.exec()

    def itIsFirstDay(self):

        data = db.reference(
            f"Employee/{self.year}/{self.monthList[int(self.month)-2]}/").get()

        for key, value in data.items():
            data[key]["total_attendance"] = 0

        if self.monthList[int(self.month)-2] != "December":
            ref = db.reference(
                f"Employee/{self.year}/{self.monthList[int(self.month)-1]}")
            for key, value in data.items():
                ref.child(str(key)).set(value)

        else:
            year = int(self.year)
            year -= 1
            year = str(year)

            ref = db.reference(
                f"Employee/{year}/{self.monthList[int(self.month)-1]}")

            for key, value in self.data1.items():
                ref.child(str(key)).set(value)

    def generateReprots(self):
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

        currentMonth = time.strftime("%m-%Y")
        currentMonth = str.split(currentMonth, "-")

        currentYear = (int)(currentMonth[1])
        currentMonth = int(currentMonth[0])

        sortedMonthList = self.swapMonths(months.copy(), currentMonth)

        periodList = [-1, -3, -6, -9, -12]
        userSelection = self.ui.period.currentIndex()

        userSelection = periodList[userSelection]

        df = pd.DataFrame()
        for i in range(-1, userSelection - 1, -1):
            if sortedMonthList[i] == "December":
                currentYear -= 1
            data = db.reference(
                f"Employee/{self.year}/{self.monthList[int(self.month)-2]}").get()
            # print(f"{sortedMonthList[i]}_{currentYear}")
            # print("\n\n")
            ids = list(data.keys())
            df.index = ids

            if i == -1:
                df["Name"] = [data[i]["Name"] for i in ids]

            df[f"{sortedMonthList[i]}_{currentYear}"] = [
                data[n]["total_attendance"] for n in ids]

            # print([data[n]["total_attendance"] for n in ids])

        message = QMessageBox()
        message.setWindowTitle("Report Downloaded")
        message.setText(
            f"File  Named report_on{time.strftime('%d-%m-%Y')} Downloaded Successfully")
        message.setStandardButtons(QMessageBox.Ok)
        message.setIcon(QMessageBox.Information)
        message.exec()

        df.to_excel(
            f"C:\\Users\\prati\\Downloads\\report_on_{time.strftime('%d-%m-%Y')}.xlsx")

    def swapMonths(self, month_list, currentMonth):
        itr = (13-currentMonth)
        for i in range(itr):
            month_list.insert(0, month_list.pop())

        return month_list


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = AdminPanel()

    with open("style.qss", "r") as style:
        app.setStyleSheet(style.read())

    widget.show()
    sys.exit(app.exec())
