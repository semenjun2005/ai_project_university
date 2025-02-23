import cv2
import numpy as np

img = cv2.imread('images/photo.jpg')
img = cv2.resize(img,(img.shape[1] // 2, img.shape[1] // 2))
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.Canny(img, 90, 90)
kernel = np.ones((5, 5),np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('Result', img)
cv2.waitKey(10000)
