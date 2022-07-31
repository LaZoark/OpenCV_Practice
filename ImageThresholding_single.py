import cv2
import numpy as np

cap = cv2.VideoCapture(0)
titles = ['Original Image', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV', 
          'normal_cam'
          ]

while cap.isOpened():
   ret, img = cap.read()
   img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # 將圖片轉為灰階 
   img = cv2.resize(img, (640, 480))
   # 將小於閾值的灰度值設為0，其他值設為最大灰度值。>127 =255, <127 =0
   ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
   # 將大於閾值的灰度值設為0，其他值設為最大灰度值。>127 =0, <127 =255
   ret, th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
   # 將大於閾值的灰度值設為閾值，小於閾值的值保持不變。 >127 =127
   ret, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
   # 將小於閾值的灰度值設為0，大於閾值的值保持不變。 <127 =0
   ret, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
   # 將大於閾值的灰度值設為0，小於閾值的值保持不變。 >127 =0
   ret, th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
   images = [img, th1, th2, th3, th4, th5]
   for i in range(len(images)):
      cv2.imshow(titles[i], images[i])
      
   if cv2.waitKey(1) == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()