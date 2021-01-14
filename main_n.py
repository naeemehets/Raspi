import firebase_access
import TestofCamera
import uploadtest
import os
import json
import save_from_camera

if __name__ == '__main__':

    serialnumber = '00000000d474f1ea'
    UserID = input('which user?: ')
    while firebase_access.FirebaseAccess.CheckcameraFlag(serialnumber) == 1:
        # TestofCamera.Camera(serialnumber,UserID)
        save_from_camera.SavePhotos(serialnumber,UserID)
    if firebase_access.FirebaseAccess.CheckcameraFlag(serialnumber) == 0 & len(os.listdir('/home/pi/images') ) != 0 :
        MyDrive = uploadtest.Authentication()
        firebase_access.FirebaseAccess.Readforupload(serialnumber, UserID, MyDrive)
    else:
        print('the camerat is off')











    """
    with open('Newjsonfile.json', 'r') as json_file:
        Newdata = json.load(json_file)
        #S = Newdata[0]
        for x in Newdata:
            A = x['naeemeh']['photo_data']['Image001']['Image_Id']
            print(A)


    with open('Exportjsonfile.json') as export_json_file:
        old_data = json.load(export_json_file)
        for Y in old_data:
            Y['Image002']['Image_Id']=A
            print(A)
        # D = str(old_data).join(A)
        #D.join(A)
        #F = json(D)
        #print(D)
"""