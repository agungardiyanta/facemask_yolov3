from firebase import firebase
import requests
import json

fbcon = firebase.FirebaseApplication('path database firebase', None)
deviceToken = ['devicetoken1','devicetoken2']
serverToken = 'servertoken'

class FirebaseFunc():
        
    def post_fb(totalUp,totalDown):
        print("Mengirim data ke firebase")
        fbcon.put('/yolov3/','pmasuk',totalUp)
        fbcon.put('/yolov3/','pkeluar',totalDown)
        print("Data terkirim")

    def get_fb():
        result = fbcon.get('/yolov3/','rCap')
        return result

    def fcm():
        for i in range(len(deviceToken)):

            headers =  {
            'Content-Type': 'application/json',
            'Authorization': 'key=' + serverToken,
            }
            body = {
            'notification': {'title': 'Peringatan',
            'body': 'Jumlah pengunjung melebihi batas kapasitas'
            },
            'to':
            deviceToken[i],
            'priority': 'high',
            #   'data': dataPayLoad,
            }
            response = requests.post("https://fcm.googleapis.com/fcm/send",headers = headers, data=json.dumps(body))
            print(response.status_code)

            print(response.json())
