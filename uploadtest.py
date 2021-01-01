from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import firebase_access
import datetime
import os

def Authentication():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def CreateFolder(drive):
    now = datetime.datetime.now()
    folder_name = now.strftime("%Y-%m-%d %H:%M:%S")
    # drive = GoogleDrive(GoogleAuth())
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    FId=folder.get('id')
    return FId

def uploadGDrive(Imagename, Serialnumber, UserId, folderId, drive):


    path = r"camera_test"
    for x in os.listdir(path):
        if x == Imagename :
            folder_metadata = {
                'title': x,
                'parents': [{"kind": "drive#fileLink", "id": folderId}],
                # 'Authorization': 'Bearer ya29.a0AfH6SMANJfFAsx3Gvuyza-DoNtPW970YWJLJ7UAZfDVvvAmruP7Fdd21yjB0nMfX7Bi6ZsFLOZFwP-bUU_GzcQV-Z5O1my3Ch91nYLoz4UE_LGbsc75Jr0YtvZy5u2a00TIenYPLjOqHiPctpHyOWYvDS3uHCHBYQKK68L-a730'
            }
            f = drive.CreateFile(folder_metadata)
            C = os.path.join(path, x)
            f.SetContentFile(C)
            f.Upload()
            FileID = f.get('id')
            firebase_access.FirebaseAccess.update_database(x,FileID,Serialnumber,UserId)
            f = None
        else:
            print('Image not found!')


