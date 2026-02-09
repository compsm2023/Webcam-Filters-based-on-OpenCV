import cv2
# capture = cv2.VideoCapture("my_video.avi")
capture = cv2.VideoCapture(0)

# 0 is used for internal camera of the PC 
# 1 is use for external camera 
while True:
    ret, frame = capture.read() # ret=true/false frame=image
    if not ret:
        print("could not read frame")
        break
    cv2.imshow("Webcam Feed",frame)
    # capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    # capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
    # capture.get(cv2.CAP_PROP_FPS)
    # capture.get(cv2.CAP_PROP_FRAME_COUNT)
    w = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print (w,h)
    fps = capture.get(cv2.CAP_PROP_FPS)
    print(fps)
    delay = int(1000 / fps)
    print(delay)
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    print(total_frames)
    capture.set(cv2.CAP_PROP_BRIGHTNESS, 150)
    capture.set(cv2.CAP_PROP_CONTRAST, 50)


    if cv2.waitKey(1) & 0xFF ==ord('q'):
        print("Quitting...")
        break
capture.release() # use to close the camera
cv2.destroyAllWindows()