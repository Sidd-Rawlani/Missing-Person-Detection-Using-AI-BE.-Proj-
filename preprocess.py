# preprocess.py

import cv2
import numpy as np

def preprocess_frame(frame):
    # Resize the frame to match your model input size
    frame = cv2.resize(frame, (64, 64))
    # Normalize pixel values to the range [0, 1]
    frame = frame / 255.0
    # Expand dimensions to match model input shape
    frame = np.expand_dims(frame, axis=0)
 
    processed_frame = frame  # Replace this line with your processing logic
    return processed_frame
