import cv2

stream = cv2.VideoCapture(0) # Change the 1 to a 0 on your system if it doesn't work

while True:
    ret, frame = stream.read()
    cv2.imshow('frame', frame)
    """
    1. get list of bounding box coordinates using detectMultiScale
    2. Loop through list of coordinates and draw bounding box and label
    3. Send data to servos/LEDs which will then actuate
    """

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows() 