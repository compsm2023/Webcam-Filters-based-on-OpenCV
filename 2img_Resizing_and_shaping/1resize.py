import cv2
image = cv2.imread("2img_Resizing_and_shaping\image.png5")
if image is None:
    print("image not found")
else:
    print("image loaded")
    resized = cv2.resize(image,(400,300)) # width=400 and height=300
    cv2.imshow("Original Image", image)
    cv2.imshow("Resized Image", resized)
    cv2.imwrite("resized_img.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()