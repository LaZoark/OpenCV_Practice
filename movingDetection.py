import cv2
import numpy as np

cap = cv2.VideoCapture(1)
min_color_scale = 15

while cap.isOpened():
    img1 = cap.read()[1]
    img2 = cap.read()[1]
    # img1 = cv2.resize(img1,(640,480))
    # img2 = cv2.resize(img2,(640,480))
    # 彩色圖轉灰階圖
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    
    # 高斯模糊化處理
    blur1 = cv2.GaussianBlur(gray1,(5,5),0)
    blur2 = cv2.GaussianBlur(gray2,(5,5),0)
    
    result = cv2.absdiff(blur1, blur2)
    # 色階大於15的元素賦值255，色階小於15則賦值0
    ret, th = cv2.threshold(result, min_color_scale, 255, cv2.THRESH_BINARY)
    
    # 膨脹函數cv2.dilate把二值化後的圖片進行輪廓加強處理
    dilated = cv2.dilate(th, None, iterations=1)
    text = "min_color_scale = {}".format(min_color_scale)
    cv2.putText(result, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 1, cv2.LINE_AA)
    cv2.imshow("absdiff", result)
    cv2.imshow("threshold", th)
    cv2.imshow("dilate", dilated)
    
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27 or key == 113:
        break
    elif key == 43:
        min_color_scale+=5
    elif key == 45:
        min_color_scale-=5
        # 255 is what the console returns when there is no key press...
    elif key != 255:
        print(key)
        
cap.release()
cv2.destroyAllWindows()