import cv2
import objects
# https://github.com/trane293/Palm-Fist-Gesture-Recognition - open_palm.xml
# https://github.com/Aravindlivewire/Opencv/tree/master/haarcascade - fist.xml
# https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml - face.xml

x = objects.Item("empty", 0, 0, 0, 0)
objects.trash.append(x)

centerx = 0
centery = 0

imcap = cv2.VideoCapture(1)

imcap.set(3, 640) # width = 640
imcap.set(4, 480) # height = 480

fistCascade = cv2.CascadeClassifier("fist.xml")
handCascade = cv2.CascadeClassifier("open_palm.xml")
faceCascade = cv2.CascadeClassifier("face.xml")

while True:
    # captures image
    success, img = imcap.read() 
   
    # grayscales image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plastic = fistCascade.detectMultiScale(imgGray, 1.5, 5)
    paper = handCascade.detectMultiScale(imgGray, 1.3, 5)
    garbage = faceCascade.detectMultiScale(imgGray, 1.5, 5)

    # puts boxes
    for (x, y, w, h) in paper: 
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
        objects.AddTrash("paper", x, y, w, h)
        print("Paper detected")

    for (x, y, w, h) in plastic: 
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
        objects.AddTrash("plastic", x, y, w, h)
        print("Plastic detected")

    for (x, y, w, h) in garbage:
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        objects.AddTrash("garbage", x, y, w, h)
        print("Garbage detected")

    objects.Sort()

    # displays image with boxes
    cv2.imshow('ObjectDetection', img)

    # space key to close
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break

imcap.release()
cv2.destroyAllWindows()