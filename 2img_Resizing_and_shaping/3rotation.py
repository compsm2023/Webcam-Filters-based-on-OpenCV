import cv2
image = cv2.imread("img_Resizing_and_shaping\image.png")
if image is None:
    print("could not load image")
else:
    (h,w) = image.shape[:2] 
    #image.shape → (height, width, channels)
    # [:2] → take only height and width
    center = (w//2,h//2)
    m = cv2.getRotationMatrix2D(center,90,1.0)
    rotated = cv2.warpAffine(image,m,(w,h))
    cv2.imshow("Original",image)
    cv2.imshow("Rotated 90 degree",rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
