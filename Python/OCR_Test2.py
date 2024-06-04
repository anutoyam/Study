import pyrealsense2 as rs
import numpy as np
import cv2
import pytesseract
import os

# RealSense 카메라 구성
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 저장할 경로 설정
save_path = "C:\\Users\\MH\\Desktop\\STD\\Study\\Python\\OCR_Capture"

# 폴더가 없으면 생성
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 카메라 시작
pipeline.start(config)

captured_images = 0  # 캡처된 이미지 수
text_length = 18     # 인식할 문자의 목표 길이

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

        # 목표 문자 길이에 도달했는지 확인
        if len(text) == text_length and captured_images < 3:
            print("인식된 텍스트:", text)
            image_filename = os.path.join(save_path, f'captured_image_{captured_images + 1}.png')
            cv2.imwrite(image_filename, color_image)
            captured_images += 1

        # 이미지 3장 캡처 후 종료
        if captured_images >= 3:
            break

finally:
    # 종료
    pipeline.stop()

# 캡처된 이미지들에서 텍스트 추출 및 출력
for i in range(1, 4):
    image_path = os.path.join(save_path, f'captured_image_{i}.png')
    image = cv2.imread(image_path)
    text = pytesseract.image_to_string(image)
    print(f"Image {i}의 인식된 텍스트:", text)