 # 🛡️ Face Mask Detection using YOLOv5

This project implements a real-time face mask detection system using the YOLOv5 object detection framework. It classifies people into three categories:
- 😷 With Mask
- ❌ Without Mask
- 😕 Mask Worn Incorrectly

## 📁 Project Structure
```
AIProject/
├── archive/                # Original dataset in PASCAL VOC format (XML + images)
│   └── annotations/        # XML label files
├── dataset/                # YOLO formatted data (images + labels)
│   ├── images/
│   └── labels/
├── yolov5/                 # YOLOv5 cloned from Ultralytics repo
│   └── runs/train/         # Training outputs and logs
├── face_mask.yaml          # Custom dataset config file
└── README.md               # Project overview (this file)
```

## 🧠 Dataset
- 📦 Total Images: 853
- 🔄 Split: 682 Training / 171 Validation
- 📁 Format: PASCAL VOC → converted to YOLO format

## 🚀 Model and Training
- 🔍 Model: YOLOv5s (pre-trained on COCO)
- 🧠 Transfer Learning: Fine-tuned for 3-class mask detection
- ⚙️ Config: 50 epochs, batch size 16, image size 640x640
- 🖥️ Hardware: Trained using NVIDIA RTX 3070 GPU

## 📈 Results (after 50 epochs)
| Metric      | Value     |
|-------------|-----------|
| Precision   | 83.1%     |
| Recall      | 19.2%     |
| mAP@0.5     | 21.1%     |
| mAP@0.5:0.95| 8.5%      |

## 🎥 Live Inference
To run live webcam detection:
```bash
python detect.py --weights runs/train/mask_detector/weights/best.pt --source 0 --conf 0.4
```

To test on an image:
```bash
python detect.py --weights runs/train/mask_detector/weights/best.pt --source path/to/image.jpg --conf 0.4
```


## 📚 References
- [YOLOv5 by Ultralytics](https://github.com/ultralytics/yolov5)
- [Original Mask Dataset](https://www.kaggle.com/datasets/ashishjangra27/face-mask-detection)

---

> Created as part of an AI course project for real-time public health monitoring. Made with ❤️ using PyTorch and OpenCV.

