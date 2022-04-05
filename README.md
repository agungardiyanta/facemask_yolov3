# mask_yolov3
This repo counts people and detects people using tiny YOLOv3 object detection with 3 object classes mask, nomask, person implemented on Raspberry Pi 4.
The results of the people counter will be sent to firebase. The data results will be displayed on the LCD and the android application.
while people don't use raspberry pi mask will trigger buzzer module.
if the total people is more than the capacity limit in the android app then firebase will send a warning notification
The main counter program in this repo is an adaptation of https://www.pyimagesearch.com/2018/08/13/opencv-people-counter/

screenshot from raspberry while processing video capture from module camera
![alt text](https://github.com/agungardiyanta/facemask_yolov3/blob/main/githubgambar.png)
screenshot alert notification in Dashboard android app
![alt text](https://github.com/agungardiyanta/facemask_yolov3/blob/main/githubgambar2.png)
repos for Dashboard app https://github.com/agungardiyanta/Dashboard
