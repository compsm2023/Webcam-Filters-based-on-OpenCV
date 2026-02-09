import cv2
img = cv2.imread("6Edge_dectection/vicky.png",cv2.IMREAD_GRAYSCALE)
ret,threshold_img = cv2.threshold(img,120,255,cv2.THRESH_T)
# ret,threshold_img = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)

# the thresholding is used for converting a grayscale image into a binary image(0,1)(black and white)


cv2.imshow("original Image",img)
cv2.imshow("Threshold image",threshold_img)
cv2.waitKey(0)
cv2.destroyAllWindows() 