import firebase_access
import os
from distutils.dir_util import copy_tree

base = firebase_access.FirebaseAccess()
def Camera(Serial_number, UserId):
    path1 = r"/home/developer/autodentistry-app/python/RaspberryPi/Cameratest"
    path2 = r"/home/developer/autodentistry-app/python/RaspberryPi/images"
    for X in os.listdir(path1):
        Image_address = os.path.join(path2, X)
        copy_tree(path1, path2)
        base.set_database(X,Image_address, Serial_number, UserId)