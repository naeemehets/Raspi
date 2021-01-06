import firebase_access
import TestofCamera
import uploadtest
# import save_from_camera

if __name__ == '__main__':
    serialnumber = input('Please insert serial number: ')
    UserID = input('which user?: ')
    MyDrive = uploadtest.Authentication()
    TestofCamera.Camera(serialnumber,UserID)
    # save_from_camera.SavePhotos(serialnumber,UserID)
    firebase_access.FirebaseAccess.Readforupload(serialnumber, UserID, MyDrive)