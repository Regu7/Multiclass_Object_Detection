# Multiclass Object Detection with CI/CD Pipeline

## Project Overview

This project focuses on **multiclass object detection** using a custom-trained YOLOv8 model. We have developed and finetuned `custom_yolov8_model4` to accurately detect 20 distinct classes of objects. The model achieves a high average precision of 83% at an Intersection over Union (IoU) threshold of 0.5, demonstrating its robust performance in real-world scenarios.

To ensure efficient development and deployment, we have implemented a comprehensive CI/CD pipeline leveraging GitHub Actions and Docker. This pipeline automates the deployment process to AWS Elastic Container Registry (ECR), Elastic Container Service (ECS), and Elastic Compute Cloud (EC2), enabling seamless integration and continuous delivery of our object detection solution.

## Key Features

* **Custom YOLOv8 Model:** Utilizes a finetuned `custom_yolov8_model4` for superior object detection performance.
* **20-Class Detection:** Capable of identifying and localizing 20 different object classes.
* **High Accuracy:** Achieves an impressive 83% Average Precision (AP@0.5 IoU).
* **Automated CI/CD:** Streamlined deployment process using GitHub Actions.
* **Dockerized Deployment:** Containerized application for consistent environments across development and production.
* **AWS Integration:** Automated deployment to AWS ECR, ECS, and EC2 for scalable and reliable hosting.

## Project Structure

The repository is structured as follows:

Yes, I can provide the content for a downloadable README.md file. However, as an AI, I cannot directly create and provide a downloadable file to you.

Instead, I will give you the complete content of the README.md file. You can then copy and paste this content into a new file on your computer, and save it as README.md.

Markdown

# Multiclass Object Detection

## Project Overview

This project focuses on **multiclass object detection** using a custom-trained YOLOv8 model. We have developed and finetuned `custom_yolov8_model4` to accurately detect 20 distinct classes of objects. The model achieves a high average precision of 83% at an Intersection over Union (IoU) threshold of 0.5, demonstrating its robust performance in real-world scenarios.

To ensure efficient development and deployment, we have implemented a comprehensive CI/CD pipeline leveraging GitHub Actions and Docker. This pipeline automates the deployment process to AWS Elastic Container Registry (ECR), Elastic Container Service (ECS), and Elastic Compute Cloud (EC2), enabling seamless integration and continuous delivery of our object detection solution.

## Key Features

* **Custom YOLOv8 Model:** Utilizes a finetuned `custom_yolov8_model4` for superior object detection performance.
* **20-Class Detection:** Capable of identifying and localizing 20 different object classes.
* **High Accuracy:** Achieves an impressive 83% Average Precision (AP@0.5 IoU).
* **Automated CI/CD:** Streamlined deployment process using GitHub Actions.
* **Dockerized Deployment:** Containerized application for consistent environments across development and production.
* **AWS Integration:** Automated deployment to AWS ECR, ECS, and EC2 for scalable and reliable hosting.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.x
* Docker
* AWS CLI (configured for your AWS account if you plan to deploy)
* Git

### Local Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/Multiclass-Object-Detection.git](https://github.com/your-username/Multiclass-Object-Detection.git)
    cd Multiclass-Object-Detection
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application Locally

The `app.py` script is the main entry point for running the object detection model.

1.  **Ensure your model weights are accessible.** You might need to download `custom_yolov8_model4.pt` (or whatever the actual model file is named) and place it in a designated `artifacts/` folder, or modify `app.py` to fetch it.

2.  **Run the application:**
    ```bash
    python app.py
    # Follow any specific instructions printed by app.py for input/output
    ```

### Building and Running the Docker Image Locally

1.  **Build the Docker image:**
    ```bash
    docker build -t multiclass-object-detection .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:8000 multiclass-object-detection
    # Adjust port mapping (-p) if your app.py uses a different port
    ```

## CI/CD Pipeline (GitHub Actions)

The project incorporates a robust CI/CD pipeline using GitHub Actions to automate the build, test, and deployment process.

### Workflow Overview

The `.github/workflows/` directory contains the YAML files defining the CI/CD workflows. Typically, this includes:

* **Build & Test Workflow:** Triggered on pushes to `main` or pull requests, this workflow builds the Docker image, runs tests (if any are defined), and ensures code quality.
* **Deployment Workflow:** Triggered upon successful completion of the build and test, or on specific tag pushes, this workflow handles the deployment to AWS ECR, ECS, and EC2.

### Deployment Process

The automated deployment to AWS ECR, ECS, and EC2 follows these steps:

1.  **Image Build & Push to ECR:** The CI/CD pipeline builds the Docker image and pushes it to your designated AWS Elastic Container Registry (ECR) repository.
2.  **ECS Service Update:** The ECS service is updated to use the newly pushed Docker image from ECR.
3.  **EC2 Instance (Optional/Managed by ECS):** ECS will manage the deployment of the containerized application onto the provisioned EC2 instances.

**Note:** For the CI/CD pipeline to function correctly, ensure you have configured the necessary AWS credentials as GitHub Secrets in your repository (e.g., `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`).

## Model Details

* **Model Architecture:** YOLOv8 (specifically, `custom_yolov8_model4`)
* **Number of Classes:** 20
* **Performance:**
    * Average Precision (AP@0.5 IoU): 83%

The model was finetuned on a custom dataset tailored for the 20 target classes. Further details about the dataset and training process can be found in the `notebooks/` directory.
