import cv2
capture = cv2.VideoCapture(0)
mode = "normal"  # state varible
while True:
    ret,frame=capture.read()
    if not ret:
        print("could not read the frame ")
        break

    key = cv2.waitKey(1) & 0xFF

    if key == ord('g') :
       mode = "gray"
       
    elif key == ord('n'):
        mode = "normal"
        print("normal")

    elif key == ord('b'):
        mode = "Gaussian"
        print("Gaussian Blur")
    
    elif key == ord('e'):
        mode = "Edge"

    elif key == ord('f'):
        mode = "flip"

  
    elif key == ord('q'):
        print("Quitting...")
        break
    

    # apply filter based on mode
    if mode == "gray":
        output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.putText(output,"grayscale mode is on",(90,20),cv2.FONT_HERSHEY_SIMPLEX,1,(90,89,21),1)
    
    elif mode == "Gaussian":
        output = cv2.GaussianBlur(frame,(21,21),0)
        cv2.putText(output,"Blur mode is on",(90,20),cv2.FONT_HERSHEY_SIMPLEX,1,(90,89,21),1)

    elif mode == "Edge":
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray,(21,21),0)
        output = cv2.Canny(blur,10,100)
        cv2.putText(output,"Edge Detection mode is on",(90,20),cv2.FONT_HERSHEY_SIMPLEX,1,(90,89,21),1)
    
    elif mode == "flip":
        output = cv2.flip(frame,1)  #horizontal_flip
        
    else:
        output = frame

    cv2.imshow("webcam",output)

capture.release()
cv2.destroyAllWindows()   