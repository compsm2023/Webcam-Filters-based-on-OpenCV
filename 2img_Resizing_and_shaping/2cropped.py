import cv2
image = cv2.imread("img_Resizing_and_shaping\image.png")
if image is not None:
    cropped = image[100:200,50:150] # there no anhi crop funtion for cropping the image , we use the slicing 
    
    cv2.imshow("original",image)
    cv2.imshow("Cropped",cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()