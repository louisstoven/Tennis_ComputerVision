from ultralytics import YOLO
model = YOLO('yolov8x')
result = model.track('input_vidéo/input_video.mp4', conf=0.2, save=True)