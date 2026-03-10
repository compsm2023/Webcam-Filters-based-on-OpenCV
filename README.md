# Basics-of-OpenCV

This repository contains basic OpenCV examples and small projects that you used to **learn step‑by‑step computer vision with Python**.

## What You Will Learn

By going through the folders in order, you learn:

- **Image basics**: how to read, display, save images and understand image size, channels and color formats.
- **Geometric transforms**: how to resize, crop, rotate and flip images.
- **Drawing on images**: how to draw lines, rectangles, circles and write text on images.
- **Working with video**: how to capture frames from a webcam and save video to a file.
- **Image filtering**: how to blur images (Gaussian, median) and sharpen them.
- **Edge detection & thresholding**: how to detect strong edges and create binary (black & white) images.
- **Contours & shapes**: how to find object outlines and detect basic shapes like rectangles and triangles.
- **Face & feature detection**: how to use Haar cascade models to detect faces, eyes and smiles.
- **Mini projects**: how to combine these skills into small, practical OpenCV projects.

## Folder Structure (and what each folder teaches)

- `1img_handling basics/`  
  You learn how to:
  - Read images from disk with `cv2.imread`
  - Display images using `cv2.imshow` and window controls
  - Save processed images using `cv2.imwrite`
  - Check image dimensions (height, width, channels) and convert to grayscale

- `2img_Resizing_and_shaping/`  
  You learn how to:
  - Resize images to different widths/heights using `cv2.resize`
  - Crop parts of an image using NumPy slicing
  - Rotate images by angles
  - Flip images horizontally/vertically

- `3Image_drawing_Function/`  
  You learn how to:
  - Draw lines, rectangles and circles on images (`cv2.line`, `cv2.rectangle`, `cv2.circle`)
  - Add text to images with `cv2.putText` (font, size, color, thickness)

- `4VideoFunctions/`  
  You learn how to:
  - Capture video from a webcam using `cv2.VideoCapture`
  - Read frames in a loop and display them in real time
  - Save video to a file using `cv2.VideoWriter`

- `5Filter and Bluring/`  
  You learn how to:
  - Apply Gaussian blur (`cv2.GaussianBlur`)
  - Apply median blur (`cv2.medianBlur`)
  - Sharpen images using kernels and filtering

- `6Edge_dectection/`  
  You learn how to:
  - Apply different thresholding methods to create binary images
  - Detect edges using the Canny edge detector (`cv2.Canny`)
  - Use bitwise operations to combine or mask images

- `7Contour & Shape Detection/`  
  You learn how to:
  - Find contours in images (`cv2.findContours`)
  - Draw contours on images
  - Approximate contours and identify basic shapes (like rectangles and triangles)

- `8Face and Oject detection/`  
  You learn how to:
  - Load Haar cascade XML files for faces, eyes and smiles
  - Detect faces and facial features in images or video
  - Draw bounding boxes around detected regions

- `Assingments/`  
  You practice the above concepts in small tasks and exercises.

- `projects/`  
  You build small OpenCV-based projects by combining multiple concepts together, such as:
  - **Webcam Filters** – apply real‑time filters (gray, blur, edges, flip, etc.) to a webcam feed.
  - **Virtual Drawing** – use color/object tracking to draw on the screen in real time using hand or object movement.

> Note: The local helper script `webcam_filters1.py` is **not** tracked or pushed to this repository, as requested.

## Requirements

- Python 3.x
- OpenCV (`cv2`) library

Install OpenCV with:

```bash
pip install opencv-python
```

## How to Use This Repository

1. Clone the repository:

```bash
git clone https://github.com/compsm2023/Basics-of-OpenCV.git
cd Basics-of-OpenCV
```

2. Follow the folders in order (`1img_handling basics` → `2img_Resizing_and_shaping` → …) like a mini course.

3. Run any example script, for example:

```bash
python "1img_handling basics/reading_img.py"
```

4. After you understand the basics, explore the `projects/` folder and try to modify or create your own mini projects.

## Author

compsm2023

## License

This project is open source and intended for learning and educational purposes.
