import cv2
image = cv2.imread("3Image_drawing_Function\image.png")
if image is None:
    print("Could not load image")
else:
    print("Image loaded Successfully!")
    
    center = (60,90)
    color = (0,0,255)
    radius = 17
    thickness = -1
    cv2.circle(image,center,radius,color,thickness)
    cv2.imshow("Image focusing circle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()