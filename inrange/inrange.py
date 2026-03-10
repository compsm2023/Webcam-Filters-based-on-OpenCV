'''
💡 Simple Meaning:

👉 It checks which pixels fall inside a given color range
👉 It creates a mask (black & white image)

White = color detected
Black = color not detected

🧠 Think Like This:

You say:

“Give me only blue color from this image.”

OpenCV replies:

“Okay, I’ll make blue parts white and everything else black.”

Syntax:
"mask = cv2.inRange(hsv_image, lower_color, upper_color)"
'''
import cv2
import numpy as np

img = cv2.imread("inrange\image.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue = np.array([100,150,50])
upper_blue = np.array([140,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)
cv2.imshow("Mask",mask)
cv2.imshow("real",img)
cv2.waitKey(0)
cv2.destroyAllWindows()