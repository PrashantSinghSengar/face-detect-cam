#importing openCV
import cv2
#importing faceclassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#using Video feature
cap = cv2.VideoCapture(0) #instead of 0 we can also use a video file name

while True:
    _, img = cap.read() #capturing all the frames
    # convering the image to Grayscale as the model only works on grayscale images
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # OpenCV works as BGR notation instead of RGB
    # detecting the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # drawing rectangels around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    #showing the image
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

#release the videoCapture object
cap.release()

