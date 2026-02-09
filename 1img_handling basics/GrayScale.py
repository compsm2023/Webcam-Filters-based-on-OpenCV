import cv2
read_img=cv2.imread("1img_handling basics/image.png" )
if read_img is not None:
    gray=cv2.cvtColor(read_img,cv2.COLOR_BGR2GRAY)
    cv2.imshow("grayscale",gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not load the img")