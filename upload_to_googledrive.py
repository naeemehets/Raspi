import json
import requests
import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import datetime


def CreateFolder():
    now = datetime.datetime.now()
    folder_name = now.strftime("%Y-%m-%d %H:%M:%S")
    drive = GoogleDrive(GoogleAuth())
    folder = drive.CreateFile({'title' : folder_name, 'mimeType' : 'application/vnd.google-apps.folder'})
    folder.Upload()
    FId=folder.get('id')
    return FId

def Uploadimages():
    entry = os.scandir('/home/developer/autodentistry-app/python/RaspberryPi/images')
    DirectoryAddress = CreateFolder()
    counter = 0
    for X in entry:
        print(X)
        counter = counter+1
        headers = {"Authorization": "Bearer ya29.a0AfH6SMANJfFAsx3Gvuyza-DoNtPW970YWJLJ7UAZfDVvvAmruP7Fdd21yjB0nMfX7Bi6ZsFLOZFwP-bUU_GzcQV-Z5O1my3Ch91nYLoz4UE_LGbsc75Jr0YtvZy5u2a00TIenYPLjOqHiPctpHyOWYvDS3uHCHBYQKK68L-a730"}
        para = {
            "name": [counter],  # change the name
            "parents": [DirectoryAddress]  # create specific folder
        }
        files = {
            'data': ('metadata', json.dumps(para), 'application/json; charset=UTF-8'),
            'file': open(X, "rb")
        }
        r = requests.post(
            "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
            headers=headers,
            files=files
        )



        print(r.text)

