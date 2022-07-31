import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

cap = cv.VideoCapture(1)
threshold = 10

while cap.isOpened():
    ret, img = cap.read()
    img = cv.resize(img, (640,480))
    # Initiate FAST object with default values
    fast = cv.FastFeatureDetector_create()
    # find and draw the keypoints
    kp = fast.detect(img,None)
    img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
    fast.setThreshold(threshold)
    # Print all default params
    Threshold = "Threshold: {}".format(fast.getThreshold())
    nonmaxSuppression = "nonmaxSuppression:{}".format(fast.getNonmaxSuppression())
    neighborhood = "neighborhood: {}".format(fast.getType())
    Total = "Total Keypoints with nonmaxSuppression: {}".format(len(kp))
    cv.putText(img2, Threshold, (10, 40), cv.FONT_HERSHEY_SIMPLEX,
               1, (0, 255, 255), 1, cv.LINE_AA)
    cv.putText(img2, nonmaxSuppression, (10, 70), cv.FONT_HERSHEY_SIMPLEX,
               1, (0, 255, 255), 1, cv.LINE_AA)
    cv.putText(img2, neighborhood, (10, 100), cv.FONT_HERSHEY_SIMPLEX,
               1, (0, 255, 0), 1, cv.LINE_AA)
    cv.putText(img2, Total, (10, 130), cv.FONT_HERSHEY_SIMPLEX,
               0.5, (0, 0, 0), 1, cv.LINE_AA)
    cv.imshow('fast_true',img2)
    # Disable nonmaxSuppression
    fast.setNonmaxSuppression(0)
    kp = fast.detect(img,None)
    Total = "Total Keypoints without nonmaxSuppression: {}".format(len(kp))
    img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
    cv.putText(img3, Total, (10, 130), cv.FONT_HERSHEY_SIMPLEX,
               0.5, (0, 0, 0), 1, cv.LINE_AA)
    cv.imshow('fast_false',img3)
    
    key = cv.waitKey(1) & 0xFF
    
    if key == 27 or key == 113:
        break
    elif key == 43:
        threshold+=1
    elif key == 45:
        threshold-=1

cap.release()
cv.destroyAllWindows()