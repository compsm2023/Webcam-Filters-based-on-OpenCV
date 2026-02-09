import cv2

read_img = cv2.imread("image.png")
if read_img is not None:
    saving = cv2.imwrite("output_naruto6.png",read_img,  [cv2.IMWRITE_PNG_COMPRESSION, 9]) #[cv2.IMWRITE_PNG_COMPRESSION, 9] use to save the image in to compressed format the range in 0-9
    if saving:
        print("Image saved succesfully as 'output_naruto.png'")
    else:
        print("Failed to save an image")
else:
    print("Error:Could not load image")
    