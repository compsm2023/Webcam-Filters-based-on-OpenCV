import cv2
image = cv2.imread("3Image_drawing_Function\image.png")
if image is None:
    print("Could not load image")
else:
    print("Image loaded Successfully!")
    text = "Naruto Uzumaki"
    org = (5,150)
    fontscale = 1

    cv2.putText(image,text,org,
                cv2.FONT_HERSHEY_COMPLEX,
                fontscale,(90,90,25),2)
    cv2.imshow("adding text",image)
    cv2.imwrite("added_Text.png",image)
    cv2.waitKey(0)
    cv2.destroyAllWindow()

    