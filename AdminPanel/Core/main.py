import cv2
import pickle
import os
import numpy as np
import face_recognition
import cvzone
import time

import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials
from firebase_admin import db

from PyQt5.QtWidgets import QWidget, QLabel
from PySide6.QtWidgets import QApplication
import sys


class Attender(object):
    def __init__(self):
        super().__init__()
        self.path = os.getcwd()

        cred = credentials.Certificate(
            f"{self.path}\\AdminPanel\\Core\\Database Key\\serviceAccountKey.json")
        project_id = cred.project_id

        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
                'storageBucket': "employeeattendancerealtime.appspot.com"
            })

        bucket = storage.bucket()

        self.month = time.strftime("%Y-%m")
        self.month = str.split(self.month, "-")
        self.year = self.month[0]
        self.month = self.month[1]
        self.monthList = ["January", "February", "March", "April", "May", "June",
                          "July", "August", "September", "October", "November", "December"]

        # 1
        cap = cv2.VideoCapture(1)

        # 2
        # setting up the size of video frame
        cap.set(3, 640)  # setting width
        cap.set(4, 480)  # setting height

        # 6
        imgBackground = cv2.imread(
            f"{self.path}\\AdminPanel\\Core\\Resources\\background.png")

        # 4
        # importing the modes in a list
        folderModePath = f"{self.path}\\AdminPanel\\Core\Resources\Modes"
        modePathList = os.listdir(folderModePath)
        imageModeList = []

        # 5
        for path in modePathList:
            # this list will contain the complete details of images of our background mode
            imageModeList.append(cv2.imread(
                os.path.join(folderModePath, path)))
        # print(len(imageModeList))

        # This part comes after completing the EncodeGenerator file

        # 8 Now we're loading the file which is created by EncodeGenerator
        # print("Loading Encoded File ...")
        file = open(f"{self.path}\\AdminPanel\\Core\\EncodedFile.p", "rb")
        encodeListKnownWithIds = pickle.load(file)
        file.close()
        encodeListKnown, employeeIds = encodeListKnownWithIds
        # print(employeeIds)
        # print("Encoded File Loaded")

        # 13 now creating mode and counter to display different modes in our face recognition panel
        modeType = 0
        counter = 0
        id = -1
        imageEmployee = []

        while True:
            # 3
            success, img = cap.read()

        # 8 resizing the image from the video for faster execution
            imgSmall = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)

        # 9 now taking faces in current frame and encodings them
            faceCurrentFrame = face_recognition.face_locations(imgSmall)
            # print(face_recognition.face_locations(imgSmall))

            encodeCurrentFrame = face_recognition.face_encodings(
                imgSmall, faceCurrentFrame)

        # 7
            # merging the Background and video
            imgBackground[158:158+480, 52:52+640] = img
            # adding the modes to our control panel
            imgBackground[44: 44+633, 808: 808+414] = imageModeList[modeType]

        # 10 now we've current frame encoding and registered encoding we're going to compare them with each other

            for encodFace, faceLocation in zip(encodeCurrentFrame, faceCurrentFrame):
                matches = face_recognition.compare_faces(
                    encodeListKnown, encodFace)
                faceDistance = face_recognition.face_distance(
                    encodeListKnown, encodFace)
                # print("matches", matches)
                # print("Face Distance", faceDistance)
        # 11 now we're finding the index of the closest match
                matchIndex = np.argmin(faceDistance)
                # print("Match Index", matchIndex)

        # 12 now we're getting the name of the closest match
                if matches[matchIndex]:
                    # showing the ids of employee
                    name = employeeIds[matchIndex].upper()
                    # print(name)
                    # this code will draw a rectangle around the face
                    y1, x2, y2, x1 = faceLocation
                    # as we've reduced the size of image we've to scale it again
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    bbox = 55+x1, 162+y1, x2-x1, y2-y1  # these're the coordinates of the rectangle

                    imgBackground = cvzone.cornerRect(
                        imgBackground, bbox=bbox, rt=0)

                    id = employeeIds[matchIndex]
                    if counter == 0:
                        counter = 1
                        modeType = 1

            if counter != 0:
                if counter == 1:
                    # here we're getting data about the employee
                    employeeInfo = db.reference(
                        f"Employee/{self.year}/{self.monthList[int(self.month)-2]}/{id}").get()
                    # print(employeeInfo)
                    # here we're getting image of employee from database
                    blob = bucket.blob(f"Core\Images/{id}.jpeg")
                    imageArray = np.frombuffer(
                        blob.download_as_string(), np.uint8)
                    imageEmployee = cv2.imdecode(imageArray, cv2.COLOR_BGR2RGB)
        # 14
                    # now we're going to update the database with the new attendance
                    ref = db.reference(
                        f"Employee/{self.year}/{self.monthList[int(self.month)-2]}/{id}")
                    employeeInfo["total_attendance"] += 1
                    ref.child("total_attendance").set(
                        employeeInfo["total_attendance"])

                # The following code is used to display the employee details
                cv2.putText(imgBackground, str(id), (1006, 493),
                            cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(employeeInfo["total_attendance"]), (
                    881, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(employeeInfo["Profession"]), (
                    1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                cv2.putText(imgBackground, str(employeeInfo["Department"]), (
                    910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgBackground, str(employeeInfo["Starting_Year"]), (
                    1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                cv2.putText(imgBackground, str(employeeInfo["Experience"]), (
                    1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                # The following line returns the width and height of the text which is used to set position of text
                (w, h), _ = cv2.getTextSize(
                    employeeInfo["Name"], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                offset = (414-w)//2
                cv2.putText(imgBackground, str(
                    employeeInfo["Name"]), (808+offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (250, 250, 250), 1)

                # Putting the image of employee on the background
                imgBackground[175: 175+216, 909: 909+216] = imageEmployee

                counter += 1

            # cv2.imshow("WebCam", img)

            cv2.imshow("Background", imgBackground)
            cv2.waitKey(1)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    Attender().run()
