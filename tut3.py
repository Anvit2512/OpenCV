import cv2
import random

img = cv2.imread('asset/Lion.jpeg', -1)

tag = img[50:100, 100:150]
img[150:200, 150:200]=tag

cv2.imshow('Image', img)
cv2.waitKey(0)	
cv2.destroyAllWindows()