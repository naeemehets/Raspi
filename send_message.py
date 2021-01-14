
## Install request module by running ->
#  pip3 install requests

# Replace the deviceToken key with the device Token for which you want to send push notification.
# Replace serverToken key with your serverKey from Firebase Console

# Run script by ->
# python3 fcm_python.py


import requests
import json

serverToken = 'AAAAsxyhFrI:APA91bENuG0V_iU_iEHZuZqdiellhJQxaXlyLa7jeISO_YvOCqQvOSBGyJqGGSmLhizusZRgPyfXoyjKXr3iaom3Lyyz7UCfqEzRC4jEMwzspmKUJDfLop5i1mdLzpwvF6jfC6SeLwD9'
deviceToken = 'device token here'

headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + serverToken,
      }

body = {
          'notification': {'title': 'Sending push form python script',
                            'body': 'New Message'
                            },
          'to':
              deviceToken,
          'priority': 'high',
        #   'data': dataPayLoad,
        }
response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
print(response.status_code)

print(response.json())