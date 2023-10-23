import cv2
img = cv2.imread('asset/Lion.jpeg', -1)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('Images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


