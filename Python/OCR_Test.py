import pyrealsense2 as rs
import numpy as np
import cv2
import pytesseract

# RealSense 카메라 구성
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 카메라 시작
pipeline.start(config)

try:
    while True:
        # 카메라로부터 프레임 얻기
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        # Numpy 배열로 이미지 변환
        color_image = np.asanyarray(color_frame.get_data())

        # 이미지에서 텍스트 인식
        text = pytesseract.image_to_string(color_image)
        print("인식된 텍스트:", text)

        # 이미지 표시 (옵션)
        cv2.imshow('RealSense', color_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # 종료
    pipeline.stop()