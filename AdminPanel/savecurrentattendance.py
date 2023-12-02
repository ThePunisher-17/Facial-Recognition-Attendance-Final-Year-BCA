import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

from datetime import datetime
import os
import time


class SaveCurrentAttendance(object):
    def __init__(self):
        super().__init__()
        path = os.getcwd()

        cred = credentials.Certificate(f'{path}\Core\\Database Key\\serviceAccountKey.json')
        project_id = cred.project_id

        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
                'storageBucket': "employeeattendancerealtime.appspot.com"
            })

        # Get a reference to the database service
        self.month = time.strftime("%Y-%m")
        self.month = str.split(self.month, "-")
        self.year = self.month[0]
        self.month = self.month[1]
        self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

        print(f"Employee/{self.year}/{self.monthList[int(self.month)-2]}")
        self.db_ref = db.reference(f"Employee/{self.year}/{self.monthList[int(self.month)-2]}")


        # Get the data
        data = self.db_ref.get()

        df = pd.DataFrame.from_dict(data, orient='index')

        # Save the DataFrame to an Excel file
        df.to_excel(
            f"C:\\Users\\prati\\Downloads\\{datetime.today().strftime('%Y-%m-%d')}.xlsx")


if __name__ == '__main__':
    SaveCurrentAttendance()
