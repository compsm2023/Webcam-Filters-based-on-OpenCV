import cv2
img = cv2.imread("6Edge_dectection/vicky.png",cv2.IMREAD_GRAYSCALE)
# blur = cv2.GaussianBlur(img,(5,5),1)
# use the GausianBlur() to blur the img 
# Without blur → too many noisy edges
# With blur → clean edges
edges = cv2.Canny(img, 50,150)
# syntax => cv2.Canny(image,threshold1, threshold2)
# threshold1 value must be low
# threshold2 value must be high
# threshold1<threshold2
cv2.imshow("original Image",img)
cv2.imshow("edge",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()