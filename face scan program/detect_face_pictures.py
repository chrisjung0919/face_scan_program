import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test3.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)

for (x, y, w, h) in faces:

    if w < 100 or h < 100:
        continue
    
    adjusted_height = int(h * 1.0)
    cv2.rectangle(img, (x, y), (x + w, y + adjusted_height), (255, 0, 0), 2)

cv2.imshow('img', img)
cv2.waitKey()