# YOLOv11n-Reproduction

This repository contains the code, configuration, and results for reproducing the evaluation of the **YOLOv11n (nano)** model as described in the paper:

> **YOLOv11: An Overview of the Key Architectural Enhancements**  
> [arXiv:2410.17725](https://arxiv.org/abs/2410.17725)

The objective of this project is to validate the reported performance of the YOLOv11n model on the **COCO 2017 validation set** using an input resolution of **640×640**.

---

## Steps to Run

### 1. Install the Ultralytics Package

Install the ultralytics package, including all requirements, in a Python>=3.8 environment with PyTorch>=1.8.

### 2. Download COCO val2017 Dataset

Download the following from the COCO website:

val2017.zip

annotations_trainval2017.zip

Unzip them and organize as:

datasets/coco/images/val2017/
datasets/coco/annotations/instances_val2017.json


### 3. Convert Annotations to YOLO Format