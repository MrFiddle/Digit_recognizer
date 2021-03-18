import numpy as np
import cv2

original = cv2.imread("5.jpg")
gris = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
gauss = cv2.GaussianBlur(gris, (5,5), 0)
canny = cv2.Canny(gauss, 50, 150)
 
final = cv2.bitwise_not(canny)

cv2.imshow("canny", final)

 
cv2.waitKey(0)
