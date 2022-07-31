import dlib
import cv2,sys

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

detector = dlib.get_frontal_face_detector()
while cap.isOpened():
    ret, frame = cap.read()
    face_rects, scores, idx = detector.run(frame, 0)
    for i, d in enumerate(face_rects):
      x1 = d.left()
      y1 = d.top()
      x2 = d.right()
      y2 = d.bottom()
      text = "%2.2f(%d)" % (scores[i], idx[i])
      result = frame[y1:y2, x1:x2]
      cv2.rectangle(frame, (x1, y1), (x2, y2), (80, 255, 11), 4, cv2.LINE_AA)
      cv2.putText(frame, text, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 
                  0.8, (255, 255, 255), 1, cv2.LINE_AA)
    
    cv2.imshow("FaceShow", frame)
    # print (result.size)
    try:
        gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
        canny = cv2.Canny(gray, 30, 150)
        cv2.imshow("square", canny)
    except:
        # sys.exc_info()[0] 就是用來取出except的錯誤訊息的方法
        print("Unexpected error:", sys.exc_info()[0])
        cap.release()
        cv2.destroyAllWindows()
    
    if cv2.waitKey(1) == ord('q'):
        break


    
# finally:
cap.release()
cv2.destroyAllWindows()