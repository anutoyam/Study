import cv2
import numpy as np
import pyrealsense2 as rs

# Load template image
template = cv2.imread('C:/Users/MH/Desktop/STD/Study/Python/img1.jpg', 0)
w, h = template.shape[::-1]

# Setup Realsense
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)  # Depth stream
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # RGB stream
pipeline.start(config)

mouse_x, mouse_y = 0, 0
def mouse_event(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y

# def mouse_callback(event, x, y, flags, params):
#     # params[0] is the depth frame
#     depth_frame = params[0]
    
#     if event == cv2.EVENT_MOUSEMOVE:
#         distance = depth_frame.get_distance(x, y)
#         distance_text = "{:.2f}m".format(distance)
        
#         # Display text on frame
#         frame_with_text = cv2.putText(frame.copy(), distance_text, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 
#                                       1, (255, 255, 255), 2, cv2.LINE_AA)
#         cv2.imshow('frame', frame_with_text)

while True:
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    frame = np.asanyarray(frames.get_color_frame().get_data())
    
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply template Matching
    res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    
    # If the match is good enough
    if max_val >= 0.8:
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)

        # Draw rectangle on matching area
        cv2.rectangle(frame, top_left, bottom_right, 255, 2)

    distance = depth_frame.get_distance(mouse_x, mouse_y)
    distance_text = "{:.2f}m".format(distance)

    cv2.namedWindow('frame', cv2.WINDOW_AUTOSIZE)

    cv2.putText(frame, distance_text, (mouse_x, mouse_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    cv2.setMouseCallback('frame', mouse_event)

    cv2.imshow('frame', frame)

    k = cv2.waitKey(15) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()
pipeline.stop()