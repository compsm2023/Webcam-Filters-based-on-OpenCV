import cv2
img = cv2.imread("6Edge_dectection/vicky.png",cv2.IMREAD_GRAYSCALE)
adaptive = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
_, otsu = cv2.threshold(
    img, 0, 255,
    cv2.THRESH_BINARY + cv2.THRESH_OTSU
)
cv2.imshow("Otsu's",otsu)
cv2.imshow("adaptive",adaptive)
cv2.waitKey(0)
cv2.destroyAllWindows()
