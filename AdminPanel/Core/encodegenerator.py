import cv2
import face_recognition
import pickle
import os

# 7 importing the database storage details and credentials to upload registered images to database
import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials


class EncodeGenerator(object):
    def __init__(self):

        self.path = os.getcwd()

        cred = credentials.Certificate(f"{self.path}\\AdminPanel\\Core\\Database Key\\serviceAccountKey.json")
        # cred = credentials.Certificate(f"{path}\\Database Key\\serviceAccountKey.json")
        project_id = cred.project_id
        # firebase_admin.initialize_app(cred, {
        #     "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
        #     'storageBucket': "employeeattendancerealtime.appspot.com"
        # })
        try:
            firebase_admin.get_app(project_id)

        except ValueError:
            firebase_admin.initialize_app(credential=cred, name=project_id, options={
                "databaseURL": "https://employeeattendancerealtime-default-rtdb.firebaseio.com/",
                'storageBucket': "employeeattendancerealtime.appspot.com"
            })

        # 1
        # importing the images of employee

        folderPath = r"AdminPanel\Core\Images"
        # folderPath = "Images"
        pathList = os.listdir(folderPath)
        imageList = []
        # print(pathList)
        # 2 Extracting employee ids
        employeeIds = []

        for path in pathList:
            # this list will contain the complete details of images of our background mode
            imageList.append(cv2.imread(os.path.join(folderPath, path)))
            # extracting employee id from images
        # 3 listing ids in list
            employeeIds.append(os.path.splitext(path)[0])
        # print(employeeIds)
        # print(len(imageList))

        # 8 we're going to upload the images to database
            fileName = f'{folderPath}/{path}'
            bucket = storage.bucket()
            blob = bucket.blob(fileName)
            blob.upload_from_filename(fileName)

        # 4
        def findEncoding(imgList):
            '''
                This function first converts the default BGR image to standard RGB image
                Then Encodes the image and then sends the list containing the encoded images
            :param imgList:
            :return encodeList:
            '''
            encodeList = []
            for image in imgList:
                img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                encoding = face_recognition.face_encodings(img)[0]
                encodeList.append(encoding)

            return encodeList

        # 5 save the known employee images in encoded format
        try:
            encodeListKnown = findEncoding(imageList)
            encodeListKnownWithIds = [encodeListKnown, employeeIds]
            # print("Encoding Completed")
            # print(len(encodeListKnown))

            # 6 storing data in binary format in a pickle file with extension '.p'
            file = open(f"{self.path}\\AdminPanel\\Core\\EncodedFile.p", "wb")
            # Writing data to the file
            pickle.dump(encodeListKnownWithIds, file)
            file.close()
            # print("File saved")
        except Exception as e:
            print(e)


if __name__ == '__main__':
    EncodeGenerator()
