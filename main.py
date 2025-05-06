from ultralytics import YOLO

# Load a model
model = YOLO("yolo11n.pt")  # load an official model
validation_results = model.val(data="coco.yaml", imgsz=640, device="cuda")

