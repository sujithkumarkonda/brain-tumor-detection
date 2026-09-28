from flask import Flask, request, render_template, jsonify
from ultralytics import YOLO
import cv2
import numpy as np
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load the model (update this path to where your model actually is)
model = YOLO("./brain_tumor_detector.pt")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    img = Image.open(file.stream)
    
    img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    
    # Run prediction
    results = model.predict(img_cv)
    
    # Process results
    result_img = results[0].plot()
    result_img_rgb = cv2.cvtColor(result_img, cv2.COLOR_BGR2RGB)
    
    # Convert to base64
    _, buffer = cv2.imencode('.jpg', result_img_rgb)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    
    # Get detection results
    boxes = results[0].boxes
    confidence = boxes.conf.max().item() if len(boxes) > 0 else None
    
    response = {
        'image': f'data:image/jpeg;base64,{img_base64}',
        'result': 'Tumor detected' if confidence else 'No tumor detected',
        'confidence': f'{confidence:.2f}' if confidence else None
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)