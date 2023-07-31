#merge photo in live video
import cv2
import numpy
cap=cv2.VideoCapture(0)
while True:
    status,photo=cap.read()
    photo1=photo[150:400,200:450]
    photo1_resized = cv2.resize(photo1, (200, 200))
    photo[0:200,0:200,:]=photo1_resized
    cv2.imshow("merge_photo",photo)
    if cv2.waitKey(100)==13:
        break
cv2.destroyAllWindows()
cap.release()
