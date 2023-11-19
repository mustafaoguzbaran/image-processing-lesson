import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if not ret:
        break

    height, width, _ = frame.shape
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lowerRed = np.array([0, 120, 120])
    upperRed = np.array([10, 255, 255])
    filter = cv2.inRange(hsv, lowerRed, upperRed)

    result = cv2.bitwise_and(frame, frame, mask=filter)
    cv2.imshow('Original', frame)
    cv2.imshow('Red Filter Result', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
