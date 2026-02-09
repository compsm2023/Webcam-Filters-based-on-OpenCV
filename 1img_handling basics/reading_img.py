import cv2
read_img=cv2.imread("image.png")
if read_img is None:
    print("could not load the img")
else:
    print("Successfully load the img ")
