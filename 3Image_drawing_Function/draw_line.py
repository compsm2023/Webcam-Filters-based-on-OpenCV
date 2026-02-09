import cv2
image = cv2.imread("3Image_drawing_Function\image.png")
if image is None:
    print("Oops! Your image is not working")

else:
    print("Image loaded successfully!")

    pt1 = (300,0)
    pt2 = (0 ,100)
    color = (255,0,0)
    thickness = 4
    cv2.line(image,pt1,pt2,color,thickness)
    cv2.imshow("Line drawing",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
     