import cv2
import numpy as np

image = cv2.imread("rices.jpg")
grayLevel = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold = cv2.threshold(grayLevel, 200, 255, cv2.THRESH_BINARY)[1]
kernel = np.ones((3, 3), np.uint8)
threshold = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, kernel)
pointCounts, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

count = 0
for pointCount in pointCounts:
    area = cv2.contourArea(pointCount)
    if area > 100:
        count += 1

cv2.imwrite("esiklenmis.jpg", threshold)
print(f"Total Point: {count}")
