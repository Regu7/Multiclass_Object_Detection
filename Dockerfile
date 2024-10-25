FROM python:3.9-slim

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

# Set environment variable to make Streamlit accessible externally
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app.py"]