# 🧠 YOLOv11n COCO Reproduction

This repository contains the code, configuration, and results for reproducing the evaluation of the **YOLOv11n (nano)** model as described in the paper:

> **YOLOv11: An Overview of the Key Architectural Enhancements**
> [arXiv:2410.17725](https://arxiv.org/abs/2410.17725)

The objective of this project is to validate the reported performance of the YOLOv11n model on the **COCO 2017 validation set** using an input resolution of **640×640**.

---

## 📆 Repository Structure

```bash
YOLOv11n-Reproduction/
├── datasets/
│   └── coco/
│       ├── images/
│       │   ├── train2017/
│       │   └── val2017/
│       ├── labels/
│       │   ├── train2017/
│       │   └── val2017/
│       └── annotations/
│           ├── instances_train2017.json
│           └── instances_val2017.json
├── coco.yaml
├── main.py
├── README.md
└── runs/  # YOLO output directory
```

---

## 🚀 How to Run

### 1. Clone the Ultralytics YOLOv11 Repository

```bash
git clone https://github.com/ultralytics/ultralytics.git
cd ultralytics
pip install -e .
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download COCO val2017 Dataset

Download the following from the [COCO website](https://cocodataset.org/#download):

* `val2017.zip`
* `annotations_trainval2017.zip`

Unzip and organize them as:

```
datasets/coco/images/val2017/
datasets/coco/annotations/instances_val2017.json
```

### 4. Convert Annotations to YOLO Format

Use a conversion script like `general_json2yolo.py` to generate YOLO-format `.txt` files under `datasets/coco/labels/val2017/`.

### 5. Evaluate YOLOv11n

```bash
yolo val model=yolo11n.pt data=coco.yaml imgsz=640
```

---

## 📊 Results

| Metric          | Value      |
| --------------- | ---------- |
| mAP\@0.5        | 67.4%      |
| mAP\@0.5:0.95   | 40.8%      |
| Inference Speed | 6.2 ms/img |
| Preprocessing   | 0.3 ms/img |
| Postprocessing  | 2.0 ms/img |

> *Note: Paper-reported latency (\~2 ms) was obtained using TensorRT 10 on T4 GPU with FP16 precision. This repo uses PyTorch FP32 inference on a GTX 1650.*

---

## 📌 Reference

* YOLOv11 Paper: [arXiv:2410.17725](https://arxiv.org/abs/2410.17725)
* Official Implementation: [Ultralytics GitHub](https://github.com/ultralytics/ultralytics)
* COCO Dataset: [cocodataset.org](https://cocodataset.org/#home)

---

## 📃 License

This project uses the AGPLv3 License as per the Ultralytics repo.

---

## 🤛️ Author

Aryan Tandon
\[Your GitHub or LinkedIn if applicable]
