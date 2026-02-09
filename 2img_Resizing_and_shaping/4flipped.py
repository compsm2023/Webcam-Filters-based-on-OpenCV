# 0 = vertically top to bottom
# 1 = horizontally left to right
# -1 horizontally and vertically
import cv2
image = cv2.imread("img_Resizing_and_shaping\image.png")
 
if image is None:
    print("Could not load image")

else:
    flipped_horizontally = cv2.flip(image,1)
    flipped_vertically = cv2.flip(image,0)
    flipped_both = cv2.flip(image,-1)
    
    cv2.imshow("Original",image)
    cv2.imshow("flipped Horizontally",flipped_horizontally)
    cv2.imshow("flipped Vertically", flipped_vertically)
    cv2.imshow("flipped Both", flipped_both)
    cv2.waitKey(0)
    cv2.destroyAllWindows()