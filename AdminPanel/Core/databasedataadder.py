import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import datetime
import time
import os


class DatabaseDataAdder(object):
    def __init__(self):

        path = os.getcwd()

        cred = credentials.Certificate(
            f"{path}\\Core\\Database Key\\serviceAccountKey.json")
        project_id = cred.project_id

        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
                'storageBucket': "employeeattendancerealtime.appspot.com"
            })

        # above line is provided by google firebase database admin panel

        # creating the employee reference directory in database

        self.month = time.strftime("%Y-%m")
        self.month = str.split(self.month, "-")
        self.year = self.month[0]
        self.month = self.month[1]
        self.monthList = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]

        self.ref = db.reference(
            f"Employee/{self.year}/{self.monthList[int(self.month)-1]}")

    def send_data(self, data):
        # Sending data to database
        for key, value in data.items():
            self.ref.child(str(key)).set(value)


if __name__ == "__main__":
    DatabaseDataAdder()
