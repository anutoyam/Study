import cv2
import numpy as np
import pyrealsense2 as rs
import pytesseract

# Load template image
template = cv2.imread('C:/Users/MH/Desktop/STD/Study/Python/img1.jpg', 0)
w, h = template.shape[::-1]

# Setup Realsense
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # RGB stream
pipeline.start(config)

while True:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    frame = np.asanyarray(frames.get_color_frame().get_data())
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply OCR
    text = pytesseract.image_to_string(gray_frame)
    print("Recognized text:", text)

    # Apply template Matching
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # If the match is good enough
    if max_val >= 0.8:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw rectangle on matching area
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)

    cv2.imshow('frame', frame)
    

    k = cv2.waitKey(60) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
pipeline.stop()
