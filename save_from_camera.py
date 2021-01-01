import time
import picamera
import firebase_access
import os

def SavePhotos(self, Serial_number, UserId):
    counter = 0
    instance = firebase_access.FirebaseAccess()
    path = r"camera_test"
    with picamera.PiCamera() as camera:
        for each in range(5):
            counter = counter + 1
            camera.start_preview()
            time.sleep(5)
            #Image_Address = "/home/pi/camera_test",counter,".jpg"
            Image_address = os.path.join(path, counter)
            camera.capture(Image_address)
            instance.set_database(counter,Image_address,Serial_number, UserId)
            camera.stop_preview()