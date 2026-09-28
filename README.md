# 🧠 Brain Tumor Detection using YOLO

Detects and localizes brain tumors in MRI images using YOLO object detection (YOLOv8 / YOLOv9 / YOLOv11), with a simple Flask web app where you can upload an MRI image and see the result.

> ⚠️ **Disclaimer:** This is an educational/research project. It is **not** a medical device and must not be used for real diagnosis.

## 📌 Features
- Detects 3 tumor types: **glioma**, **meningioma**, **pituitary**
- Model training notebook (YOLOv8)
- Flask web app: upload an MRI → get the image with bounding boxes + confidence score
- Dataset prepared in YOLOv8, YOLOv9 and YOLOv11 formats

## 🗂️ Project Structure
```
brain-tumor-detection/
├── app.py                      # Flask web app
├── brain_tumor_detector.pt     # Trained YOLO model weights
├── requirements.txt            # Python packages needed
├── templates/index.html        # Web page
├── static/                     # CSS and JavaScript
├── notebooks/
│   └── brain-tumor-detection-with-yolov8.ipynb   # Training + evaluation
├── sample_images/              # A few example MRI images to test
├── docs/                       # Diagrams / screenshots
└── README.md
```

## 📊 Dataset
- Name: **Medical Image Dataset – Brain Tumor Detection** (Kaggle)
- Classes: `glioma`, `meningioma`, `pituitary`
- Split: 2145 train / 613 validation / 309 test images
- The dataset is **not included** in this repository because of its size.
  Download it from Kaggle (search the dataset name above), then place it in a folder called `BrainTumor/`.

## ⚙️ Installation
1. Install [Python 3.9+](https://www.python.org/downloads/)
2. Clone this repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/brain-tumor-detection.git
   cd brain-tumor-detection
   ```
3. (Recommended) Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate        # Windows
   source venv/bin/activate     # Mac / Linux
   ```
4. Install the packages:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the Web App
```bash
python app.py
```
Open **http://127.0.0.1:5000** in your browser, click **Upload MRI Image**, and choose an image (try one from `sample_images/`).

## 🏋️ Train the Model Yourself
1. Download the dataset (see above).
2. Open `notebooks/brain-tumor-detection-with-yolov8.ipynb` in Jupyter or Kaggle.
3. Update the `data.yaml` path in the training cell and run all cells.

## 📈 Results
_Add your results here from the notebook (e.g. mAP50, precision, recall) and a screenshot of a detection._

| Metric | Value |
|--------|-------|
| Precision | ... |
| Recall | ... |
| mAP@50 | ... |

## 🛠️ Tech Stack
Python · Ultralytics YOLO · Flask · OpenCV · NumPy · Pillow · HTML/CSS/JavaScript

## 🙏 Acknowledgements
- Dataset: Kaggle "Medical Image Dataset – Brain Tumor Detection"
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)

## 👤 Author
Your Name – [GitHub profile link]
