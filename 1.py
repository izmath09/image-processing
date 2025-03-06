import cv2
import matplotlib.pyplot as plt
img = cv2.imread('trees.jpeg')
h, w, channels = img.shape
half = w //2
half2 = h //2
quadrant1 = img[:half2, :half]
cv2.imshow('image1', quadrant1)
quadrant2 = img[half2:, half:]
cv2.imshow('image2', quadrant2)
quadrant3 = img[:half2, half:]
cv2.imshow('image3', quadrant3)
quadrant4 = img[half2:, :half]
cv2.imshow('image4', quadrant4)
cv2.waitKey(0)
plt.show()