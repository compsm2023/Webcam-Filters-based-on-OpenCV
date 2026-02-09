import cv2
read_img=cv2.imread("image.png",0 )
if read_img is not None:
    cv2.imshow("naruto_img",read_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("could not load the img") 