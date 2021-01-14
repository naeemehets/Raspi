import firebase_admin
from firebase_admin import credentials, db
import pyrebase
import uploadtest
import os


class FirebaseAccess:
    def __init__(self):
        self.registration_token = [
            "AAAAsxyhFrI:APA91bENuG0V_iU_iEHZuZqdiellhJQxaXlyLa7jeISO_YvOCqQvOSBGyJqGGSmLhizusZRgPyfXoyjKXr3iaom3Lyyz7UCfqEzRC4jEMwzspmKUJDfLop5i1mdLzpwvF6jfC6SeLwD9"]
        firebaseConfig = {
            "apiKey": "AIzaSyAvM_hZl5iIzRNZ_sJDHM9GfYFQslHN25M",
            "authDomain": "smilesymbol-53a69.firebaseapp.com",
            "databaseURL": "https://smilesymbol-53a69-default-rtdb.firebaseio.com/",
            "projectId": "smilesymbol-53a69",
            "storageBucket": "smilesymbol-53a69.appspot.com",
            "messagingSenderId": "769279465138",
            "appId": "1:769279465138:web:ca45f2b85605be6ee6dbab",
            "measurementId": "G-Q07G2WEYRV"
        }
        self.firebase = pyrebase.initialize_app(firebaseConfig)
        cred = credentials.Certificate("/home/developer/autodentistry-app/python/RaspberryPi/smilesymbol-53a69-firebase-adminsdk-pezxe-a81003685e.json")
        self.default_app = firebase_admin.initialize_app(cred)
        global ref
        ref = db.reference("smilesymbol-53a69-default-rtdb", url="https://smilesymbol-53a69-default-rtdb.firebaseio.com/")

    def CheckcameraFlag(Serial_number):
        return ref.child(Serial_number).child('CameraTurnOnflag').get()


    def set_database(self, imagename, Image_Address, Serial_number, UserId):
       # self.firebase.auth()
       ref.child(Serial_number).child(UserId).child('photos').push({
                                                    'Imagename' : imagename,
                                                    'Upload_Flag': 'false',
                                                    'Pi_Address': Image_Address
                                                   })

    def update_database(Imagename, ImageId, Serialnumber, UserId):
        ref.child(Serialnumber).child(UserId).child('Photo_Data').push({
                                                'Imagename' : Imagename,
                                                'GDrive_Id' : ImageId,
                                                'Image_Timestamp' : '11:30 Nov 02 2020',
                                                'PhotosTable_Id' : FirebaseAccess.GetphotoId(Serialnumber,UserId, Imagename)
                                                })

    def Readforupload(Serialnumber, Userid, Drive):
        falseItem = ref.child(Serialnumber).child(Userid).child('photos').get()
        FolderId = uploadtest.CreateFolder(Drive)
        for photo in falseItem :
            Upflag = ref.child(Serialnumber).child(Userid).child('photos').child(photo).child('Upload_Flag').get()
            if Upflag == 'false':
                currentname = ref.child(Serialnumber).child(Userid).child('photos').child(photo).child('Imagename').get()
                uploadtest.uploadGDrive(currentname, Serialnumber, Userid, FolderId, Drive)
                ref.child(Serialnumber).child(Userid).child('photos').child(photo).update({'Upload_Flag': 'true'})
                os.remove(os.path.join('/home/pi/images', currentname))
            else:
                print('Image is Uploaded')


    def GetphotoId(serialnumber, UserId, Imagename):
        for item in ref.child(serialnumber).child(UserId).child('photos').get():
            if ref.child(serialnumber).child(UserId).child('photos').child(item).child('Imagename').get() == Imagename:
                return item
