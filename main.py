import cv2 as cv

cap = cv.VideoCapture(0)

while True:
    if cv.waitKey(1) == 27:
        break
    _, image = cap.read()
    cv.imshow('d',image)