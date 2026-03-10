'''
Simple Meaning:

👉 It helps you find the center of an object

It gives mathematical values from which we calculate:

Center X

Center Y

🧠 Think Like This:

You detected a blue object.

Now you want to know:

“Where exactly is it on the screen?”

moments() helps find that location.

Why We Use cv2.moments() ?

Now we detected the object.

But we still don’t know:

👉 Where exactly is it on the screen?

That’s where moments() helps.

✅ Syntax
M = cv2.moments(contour)
Then calculate center:

cx = int(M["m10"] / M["m00"])
cy = int(M["m01"] / M["m00"])
'''
import cv2
import numpy as np

img = cv2.imread("inrange\image.png")
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue = np.array([100,150,50])
upper_blue = np.array([140,255,255])

mask = cv2.inRange(hsv,lower_blue,upper_blue)

mask = cv2.erode(mask,None,iterations = 2)
mask = cv2.dilate(mask,None,iterations = 2)
contour,_ = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

if contour:
    largest = max(contour, key=cv2.contourArea)
    M = cv2.moments(largest)

    if M["m00"] != 0:
        # centroid(cx,cy)
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])
        print("Center:", cx, cy)

print("Number of contours:", len(contour))
# cv2.imshow("Mask",mask)
# cv2.imshow("real",img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()