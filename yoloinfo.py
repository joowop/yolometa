# 추론
from ultralytics import YOLO

model = YOLO('runs/detect/train20/weights/best.pt')
results= model.predict(source='fish.jpg', show=False, save=True)


for result in results:
    boxes = result.boxes
    print(boxes)

print(boxes.xywh)
print(boxes.cls)
# 수정