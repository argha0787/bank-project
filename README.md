# Bank Deposit Prediction MLOps

## Overview

This project is an end-to-end Machine Learning Operations (MLOps) application that predicts whether a customer is likely to subscribe to a bank term deposit based on demographic and banking-related information.

The application is built using a production-style workflow that includes model training, experiment tracking, API development, containerization, and cloud deployment.

---

## Features

* Data preprocessing and feature engineering
* Machine Learning model training and evaluation
* MLflow experiment tracking and model registry
* FastAPI REST API for predictions
* Docker containerization
* AWS EC2 deployment
* AWS CodeDeploy integration
* CI/CD using AWS CodePipeline
* Version-controlled with Git and GitHub

---

## Tech Stack

### Programming Language

* Python 3.x

### Machine Learning

* Scikit-learn
* Pandas
* NumPy

### Experiment Tracking

* MLflow

### API Framework

* FastAPI
* Uvicorn

### Containerization

* Docker

### Cloud Platform

* Amazon Web Services (AWS)

### DevOps

* Git
* GitHub
* AWS CodePipeline
* AWS CodeDeploy

---

## Project Structure

```text
Bank_Deposit_MLOps/
│
├── app/
│   ├── predictor.py
│   └── __init__.py
│
├── models/
│   └── model.pkl
│
├── notebooks/
│
├── scripts/
│   └── install_dependencies.sh
│
├── Main.py
├── requirements.txt
├── Dockerfile
├── appspec.yml
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone <repository-url>
cd Bank_Deposit_MLOps
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the FastAPI Application

```bash
uvicorn Main:app --reload
```

Open your browser:

```
http://127.0.0.1:8000/docs
```

---

## Docker

Build the Docker image

```bash
docker build -t bank_app-api .
```

Run the container

```bash
docker run -d -p 8000:8000 bank_app-api
```

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis
4. Feature Engineering
5. Model Training
6. Hyperparameter Tuning
7. Model Evaluation
8. Model Serialization
9. MLflow Experiment Tracking
10. API Development
11. Dockerization
12. AWS Deployment
13. CI/CD Automation

---

## API Endpoint

### Prediction

**POST**

```
/predict
```

Input: Customer information in JSON format

Output:

```json
{
  "prediction": 1
}
```

where:

* `1` = Customer is likely to subscribe
* `0` = Customer is not likely to subscribe

---

## Deployment

The application is deployed using:

* Docker
* AWS EC2
* AWS CodeDeploy
* AWS CodePipeline

Each push to the GitHub repository can automatically trigger the deployment pipeline.

---

## Future Improvements

* Model Monitoring
* Data Drift Detection
* Model Drift Detection
* Automatic Retraining Pipeline
* Kubernetes Deployment
* AWS CloudWatch Integration
* Prometheus & Grafana Monitoring

---

## Author

Developed as an MLOps learning project demonstrating the complete lifecycle of a machine learning application, from model development to automated cloud deployment.
