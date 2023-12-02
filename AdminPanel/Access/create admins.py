from firebase_admin import credentials, db
import os
import cv2
import time
import firebase_admin

path = os.getcwd()
cred = credentials.Certificate(f"{path}\\Core\\Database Key\\serviceAccountKey.json")


firebase_admin.initialize_app(cred, {
            "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
            'storageBucket': "employeeattendancerealtime.appspot.com"
        })


ref = db.reference("administrators/")
data = {}
data[101] = {"Prat0691": "PratikD111"}
i = 0
try:
    
    for i in range(10):
            id = 101 + i
            values = {"ID" : f"Prat069{i}", "Password": f"PratikD{1}"}
            data[id] = values

    for id, data in data.items():
            ref.child(str(id)).set(data)

except Exception as e:
    print(e)

