import cv2
import numpy as np
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 
          'normal_cam'
          ]


while cap.isOpened():
    ret, img = cap.read()
    ret2, img2 = cap2.read()
    img = cv2.resize(img, (640, 480))
    img2 = cv2.resize(img2, (640, 480))
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
    images = [img, th1, th2, th3, th4, th5, img2]
    for i in range(7):
       cv2.imshow(titles[i], images[i])
       
    if cv2.waitKey(1) == ord('q'):
       break




cap.release()
cap2.release()
cv2.destroyAllWindows()