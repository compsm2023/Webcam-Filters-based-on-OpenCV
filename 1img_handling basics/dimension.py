import cv2
read_img=cv2.imread("1img_handling basics/`image.png" )
if read_img is not None:
    h1,w1,c1=read_img.shape
    print(f"Image Loaded:\n Height:{h1}\nWidth:{w1}\n Channels:{c1}")
else:
    print("COuld not load the img")