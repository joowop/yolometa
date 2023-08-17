import torch
#  nvidia-smi -> cuda 버전 확인하기 -> pytorch get started -> cuda 버전에 맞게 설정하여 설치
from ultralytics import YOLO
import ultralytics
print(torch.cuda.is_available())
print('====================')
print(ultralytics.checks())

if __name__ == '__main__':
    # 모델 학습
    model = YOLO('yolov8n.pt')
    # device 는 0일때 gpu??
    model.train(data='C:/Users/user/PycharmProjects/yolo8/Fish-44/data.yaml', imgsz=640, epochs = 30, batch=4, device=0)
