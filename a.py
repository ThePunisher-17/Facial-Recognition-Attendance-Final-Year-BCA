
from firebase_admin import credentials, db
import os
import cv2
import time
import firebase_admin

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


for i in range(0,-11, -1 ):
    ref = db.reference(f"Employee/{currentYear-1}/{months[i]}")

    print(f"Employee/{currentYear-1}/{months[i]}")


    for month in months:
        data = {}
        for i in range(10):
            id = 10000 + i
            values = {"Name" : f"Pratik{i}", "Department": "AI","Profession": "AI Engineer", "Gender": "Male","Starting_Year": "2020", "total_attendance": 11+i, "Last_Attendance_time": "2023-01-01 00:00:00", "Experience": "0"}
            data[id] = values

        for id, data in data.items():
            ref.child(str(id)).set(data)


