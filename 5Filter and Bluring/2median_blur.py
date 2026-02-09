import cv2
image = cv2.imread("5Filter and Bluring/image.png")
blurred = cv2.medianBlur(image,5) # use to remove the salt and papper noise in the image
# Syntax : cv2.medianBlur(image,kernel_size)
# kernel_size must be odd
cv2.imshow("original",image)
cv2.imshow("blurred image",blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
