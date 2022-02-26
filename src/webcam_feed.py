import cv2

stream = cv2.VideoCapture(1)

while True:
    ret, frame = stream.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

stream.release()
cv2.destroyAllWindows()