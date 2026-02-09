import cv2
image = cv2.imread("5Filter and Bluring/fruit.png")
blurred = cv2.GaussianBlur(image,(21,21 ),10)
# sytanx: cv2.GaussianBlur(image,(kernel_size_x, kernel_size_y),sigma)
# (kernel_size_x, kernel_size_y) must be odd i.e. 
# (3,3) lightblur
# (9,9) strong
# (21,21) super blur
# sigma = means the how much it will blur / intensity
# if sigma = 0 means the OpenCV decides the much to blur the image
cv2.imshow("Original",image)
cv2.imshow("blurred",blurred)
cv2.waitKey(0)
