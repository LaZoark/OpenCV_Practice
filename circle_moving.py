import cv2
from sklearn.linear_model import GammaRegressor
# import numpy as np
# from matplotlib import pyplot as plt

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

color = (255, 120, 0)

x ,y = (300,200)
r = 50

import myfunction
from myfunction import apollo

def apollo(A, B):
    # A=6, B=8
    print("Hello")
    C = A + B
    D = A - B
    # print(C)
    return int(C), int(D), "apollo"

dd = apollo(6, 9)
print(dd)

while cap.isOpened():
    ret, frame = cap.read()
      
    if not ret:
    # if ret:
        print("end")
        break
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # gauss = cv2.GaussianBlur(gray, (5, 5), 0)
    # canny = cv2.Canny(gauss, 30, 150)
    # text = "({}, {}, {})".format(x, y, r)
    text = f"({x}, {y}, {r})"
    locate = (int(x+r/3), int(y-r/3))
    cv2.circle(frame , (x, y), abs(r), color, 3)
    cv2.putText(frame, text, locate, cv2.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1, cv2.LINE_AA)
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 27 or key == 113:
        break
    elif key == 43:
        r+=5
    elif key == 45:
        r-=5
    elif key == 119:
        y-=10
    elif key == 115:
        y+=10
    elif key == 97:
        x-=10
    elif key == 100:
        x+=10
        # 255 is what the console returns when there is no key press...
    elif key != 255:
        print(key)

# 釋放所有資源
cap.release()
cv2.destroyAllWindows()
