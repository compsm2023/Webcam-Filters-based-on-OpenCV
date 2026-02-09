import cv2
image = cv2.imread("Image_drawing_Function\image.png")
if image is None:
    print("Could not load image")
else:
    print("Image loaded Successfully!")
    pt1 = (50,50)
    pt2 = (20,20)
    color = (0,0,255)
    thickness = 3
    cv2.rectangle(image, pt1,pt2,color,thickness)
    cv2.imshow("Image focusing rectangle",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()