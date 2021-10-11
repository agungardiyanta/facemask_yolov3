from firebase import firebase
import requests
import json
#,'fK49gDbiTruz6DYR5k7uEE:APA91bFRFETnSxSZZjyEY6N2GvyTWH_kO3ua_DyBGOGwIe55k-HOnTrYB5NYs6F3K_lGO8XxNHeHDhVkluoQEft7zop-tGoWPFLBnmFt2ZmnYq914R3H5WWuo0rHBowFxOMU4gy2mS1B'
fbcon = firebase.FirebaseApplication('https://test-python-8ba80.firebaseio.com/', None)
deviceToken = ['eX9ziyxDQVWr15rukPJDyK:APA91bGMD6KtWu1-Yg_WzlxPxRk5mBSZYzZWtJKa-5zp9r99_FUMZe3e12ECyKEk_ioRo6zBywUe7XRkw-Xt-3XmfSRi_hvhARDhqpQVZzklNg4xOv72phs1I-LWk3LOjqLDSdILL2mL','fK49gDbiTruz6DYR5k7uEE:APA91bFRFETnSxSZZjyEY6N2GvyTWH_kO3ua_DyBGOGwIe55k-HOnTrYB5NYs6F3K_lGO8XxNHeHDhVkluoQEft7zop-tGoWPFLBnmFt2ZmnYq914R3H5WWuo0rHBowFxOMU4gy2mS1B']
serverToken = 'AAAABBwr4zs:APA91bHkBPE2N8dveruc__fH4DgMqoGs1jx5xPd0kNRBONHxt04jcXhLZQJr4arpjP7hOVttEsVQZGOMBCgn-xsz412tUSeLKW1-TjaODIXJAQS0rphXINCzvdoUFsDa_xcEHgdvZTkc'

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
