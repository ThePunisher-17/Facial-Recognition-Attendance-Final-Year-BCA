
from firebase_admin import credentials, db
import os
import cv2
import time
import firebase_admin


def swapMonths(month_list, currentMonth):
        itr = (13-currentMonth)
        for i in range(itr):
            month_list.insert(0, month_list.pop())

        return month_list




path = os.getcwd()
cred = credentials.Certificate(f"{path}\\AdminPanel\\Core\\Database Key\\serviceAccountKey.json")


firebase_admin.initialize_app(cred, {
            "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
            'storageBucket': "employeeattendancerealtime.appspot.com"
        })

# ref = db.reference("September_2023/Employee").get()


months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

l = months

currentMonth = time.strftime("%m-%Y")
currentMonth = str.split(currentMonth, "-")

currentYear = (int)(currentMonth[1])
currentMonth = int(currentMonth[0])

sortedMonthList = swapMonths(month_list=months.copy(), currentMonth=currentMonth)

periodList = [-1, -3, -6, -9, -12]        
userSelection = 4


userSelection = periodList[userSelection]

for i in range(-1, userSelection -1, -1):
    if  "December" == sortedMonthList[i]:
        currentYear = currentYear 

    ref = db.reference(f"Employee/{currentYear}/January")

    print(f"Employee/{currentYear}/{sortedMonthList[i]}")


    for month in months:
        data = {}
        for i in range(7,10):
            id = 1000 + i
            values = {"Name" : f"Pratik{i}", "Department": "AI","Profession": "AI Engineer", "Gender": "Male","Starting_Year": "2020", "total_attendance": 11+i, "Last_Attendance_time": "2023-01-01 00:00:00", "Experience": "0"}
            data[id] = values

        for id, data in data.items():
            ref.child(str(id)).set(data)


