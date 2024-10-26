FROM python:3.9-slim

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

# Set working directory
WORKDIR /app

# Create necessary directories
RUN mkdir -p artifacts/custom_yolov8_model4

# Copy application files
COPY app.py .
COPY artifacts/custom_yolov8_model4/weights artifacts/custom_yolov8_model4/weights
COPY requirements.txt .

RUN pip install -r requirements.txt

# Expose port for Streamlit
EXPOSE 8501

# Set Streamlit configuration
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_PORT=8501

# Run Streamlit with specific flags
ENTRYPOINT ["streamlit", "run", "--server.address", "0.0.0.0", "--server.port", "8501", "app.py"]
