import pyrealsense2 as rs
import numpy as np
import cv2

# Setup:
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)  # RGB stream


# Start streaming:
pipeline.start(config)

mouse_x, mouse_y = 0, 0
def mouse_event(event, x, y, flags, param):
    global mouse_x, mouse_y
    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x, mouse_y = x, y
try:
    while True:
        # Get frameset of color and depth
        frames = pipeline.wait_for_frames()

        # Get depth and color frame
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()  # RGB frame

        # Colorize depth frame to jet colormap
        depth_color_frame = rs.colorizer().colorize(depth_frame)
        
        # Convert depth_frame and color_frame to numpy array to render image in opencv
        depth_color_image = np.asanyarray(depth_color_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # get distance
        distance = depth_frame.get_distance(mouse_x, mouse_y)
        distance_text = f"Distance at pixel ({mouse_x}, {mouse_y}): {distance:.2f} meters"
        
        cv2.rectangle(depth_color_image, (100,100), (300,300), (5,5,255),2)

        # put text on image
        cv2.putText(depth_color_image, distance_text, (mouse_x, mouse_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(color_image, distance_text, (mouse_x, mouse_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


        cv2.namedWindow('Depth Stream', cv2.WINDOW_AUTOSIZE)
        cv2.namedWindow('Color Stream', cv2.WINDOW_AUTOSIZE)
        cv2.setMouseCallback('Depth Stream', mouse_event)

        # Render image in opencv window
        cv2.imshow("Depth Stream", depth_color_image)
        cv2.imshow("Color Stream", color_image)
        key = cv2.waitKey(1)

        # if pressed escape exit program
        if key == 27:
            cv2.destroyAllWindows()
            break

finally:
    pipeline.stop()