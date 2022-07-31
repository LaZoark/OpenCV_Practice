import cv2
 
cap = cv2.VideoCapture(1)

# 設定擷取影像的尺寸大小
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

thrh1 = 30

while cap.isOpened():
   ret, frame = cap.read()
 
   if not ret:
       print("end")
       break
   gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   blur = cv2.GaussianBlur(gray, (5, 5), 0)
#    canny = cv2.Canny(blur, 30, 150)
   canny = cv2.Canny(blur, thrh1, 150)
   cv2.imshow('frame', canny)
 
#    if cv2.waitKey(1) == ord('q'):
#        break
   key = cv2.waitKey(1) & 0xFF

   if key == 27 or key == 113:
       break
   elif key == ord('+'):
       thrh1 += 5
   elif key == ord('-'):
       thrh1 -= 5
#    elif key == 119:
#        y-=10
#    elif key == 115:
#        y+=10
#    elif key == 97:
#        x-=10
#    elif key == 100:
#        x+=10
       # 255 is what the console returns when there is no key press...
   elif key != 255:
       print(key)
# 釋放所有資源
cap.release()
cv2.destroyAllWindows()