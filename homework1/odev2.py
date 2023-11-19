import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("apple.jpg", 0)
image_height = image.shape[0]
image_width = image.shape[1]
Histogram =np.zeros([256])

for i in range(0,image_height):
    for x in range(0,image_width):
        Histogram[image[i, x]] += 1

plt.plot(Histogram)
plt.title("Histogram Graph")
plt.show()