import cv2

face_cascade = cv2.CascadeClassifier("8Face and Oject detection/haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 

    face = face_cascade.detectMultiScale(gray,1.1,5)

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        """
        x,y = topleft corner
        (x+w,y+h)
        face 
        x=how far from left
        y=how far from top
        w=width of face
        h= heightof face

        """
    cv2.imshow("weBcam,face detection",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
