import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not opened")
    exit()

prev_x = None
prev_y = None
canvas = None

while True:
    ret, frame = cap.read()
    if not ret:
        print("Something went wrong")
        break

    flip = cv2.flip(frame, 1)

    # Create canvas only once
    if canvas is None:
        canvas = np.zeros_like(flip)

    hsv = cv2.cvtColor(flip, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100,150,50])
    upper_blue = np.array([140,255,255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Remove noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest_contour = max(contours, key=cv2.contourArea)

        M = cv2.moments(largest_contour)

        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            # Draw pointer circle
            cv2.circle(flip, (cx, cy), 5, (255,255,255), -1)

            # Draw line on canvas
            if prev_x is not None and prev_y is not None:
                cv2.line(canvas, (prev_x, prev_y), (cx, cy), (0,255,0), 3)

            prev_x = cx
            prev_y = cy
    else:
        prev_x = None
        prev_y = None

    # Combine frame and canvas
    output = cv2.add(flip, canvas)

    # Title text
    cv2.putText(output,
                "Virtual Drawing App",
                (10,50),
                cv2.FONT_HERSHEY_COMPLEX,
                1.2,
                (250,90,25),
                2)

    # UI rectangle
    cv2.rectangle(output,
                  (20,70),
                  (460,120),
                  (200,250,200),
                  3)

    cv2.putText(output,
                "Use Blue pen TO DRAW |Press C to Clear | Q to Quit",
                (30,105),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255,255,255),
                1)

    cv2.imshow("Virtual Drawing", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        canvas = np.zeros_like(flip)
        prev_x = None
        prev_y = None

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()