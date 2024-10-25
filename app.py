import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
from PIL import Image
import io


def load_model():
    """Load YOLO model"""
    model = YOLO(
        r"artifacts\custom_yolov8_model4\weights\best.pt"
    )  # you can change to your custom model path
    return model


def process_image(image, model):
    """
    Process image with YOLO model and draw bounding boxes
    Returns: Image with bounding boxes and list of detections
    """
    # Convert PIL Image to numpy array
    img_array = np.array(image)

    # Make prediction
    results = model(img_array)

    # Get the first result (assuming single image)
    result = results[0]

    # Create a copy of image for drawing
    img_with_boxes = img_array.copy()

    # List to store detection information
    detections = []

    # Draw bounding boxes and store detection info
    for box in result.boxes:
        # Get box coordinates
        x1, y1, x2, y2 = box.xyxy[0]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        # Get confidence and class
        conf = float(box.conf[0])
        class_id = int(box.cls[0])
        class_name = result.names[class_id]

        # Draw rectangle
        cv2.rectangle(img_with_boxes, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Add label
        label = f"{class_name} {conf:.2f}"
        cv2.putText(
            img_with_boxes,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )

        # Store detection
        detections.append(
            {"class": class_name, "confidence": conf, "bbox": [x1, y1, x2, y2]}
        )

    return Image.fromarray(img_with_boxes), detections


def main():
    st.title("YOLO Object Detection")

    # Load model
    model = load_model()

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Load and display original image
        image = Image.open(uploaded_file)
        st.subheader("Original Image")
        st.image(image)

        # Add predict button
        if st.button("Predict"):
            st.subheader("Detection Result")

            # Process image and get detections
            result_image, detections = process_image(image, model)

            # Display result image
            st.image(result_image)

            # Display detections
            st.subheader("Detections")
            for i, det in enumerate(detections, 1):
                st.write(f"Detection {i}:")
                st.write(f"- Class: {det['class']}")
                st.write(f"- Confidence: {det['confidence']:.2f}")
                st.write(f"- Bounding Box: {det['bbox']}")


if __name__ == "__main__":
    main()
