# app.py

import streamlit as st
import cv2
import numpy as np
import preprocess  # Import your preprocess.py module

def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        st.error("Error: Camera not found!")
        return
    
    capture_button_key = "capture_button"  # Unique key for the capture button
    
    # Add a text input for name or ID
    # search_input = st.text_input("Enter Name or ID of Missing Person")
    
    # Add a dropdown for filtering
    filter_option = st.selectbox("Filter by:", ["Gender", "Location"])
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            st.error("Error: Unable to capture frame.")
            break
        
        # Display the video feed directly using st.image
        st.image(frame, channels="BGR", use_column_width=True)  # Adjust display width as needed
        
        if st.button("Capture", key=capture_button_key):
            # Add code to save or process the captured image
            pass
        
        if st.button("Exit"):
            break
    
    cap.release()

if __name__ == "__main__":
    main()
