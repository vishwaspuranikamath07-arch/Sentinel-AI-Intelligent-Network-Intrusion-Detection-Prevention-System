# AI-Based Network Intrusion Detection System (AI-NIDS)

![Python Version](https://img.shields.io/badge/python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109.2-009688.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.4.1.svg-F7931E.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)

An industry-grade, real-time Machine Learning pipeline for Network Intrusion Detection. It captures live network packets, extracts features, predicts malicious activity using ensemble models, and alerts administrators via a dashboard.

## 🚀 Features

- **Real-Time Packet Capture**: Multi-threaded packet sniffing using Scapy (supports BPF filters).
- **ML Pipeline**: Automated NSL-KDD dataset downloader, robust data preprocessing, and multi-model training with K-Fold cross-validation (Random Forest, XGBoost, SVM, etc.).
- **Live Inference Engine**: Thread-safe lazy-loading predictor with millisecond latency.
- **REST API**: Built with FastAPI, Pydantic v2 schemas, and JWT authentication.
- **Persistent Storage**: SQLAlchemy 2.0 with SQLite WAL mode for high concurrency.
- **Interactive Dashboard**: Bootstrap 5 + Chart.js frontend visualizing real-time threats.
- **Production Ready**: Dockerized deployment, comprehensive logging, and custom exception handling.

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Machine Learning**: Scikit-learn, XGBoost, Pandas, Numpy, Joblib
- **Networking**: Scapy
- **Frontend**: HTML5, Bootstrap 5, Chart.js
- **Testing**: Pytest

## 📦 Installation & Setup

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/yourusername/ai-nids.git
cd ai-nids
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

*(Note: On Windows, install [Npcap](https://npcap.com/) for Scapy to capture packets.)*

### 2. Prepare Data & Train Model
```bash
# Download and prepare the NSL-KDD dataset
python scripts/download_dataset.py

# Train 5 different models, evaluate, and save the best one
python scripts/train.py
```

### 3. Run the Application
```bash
# Start the FastAPI server and live dashboard
python main.py
```
Visit http://127.0.0.1:8000 in your browser to view the dashboard.

## 🐳 Docker Deployment

```bash
docker-compose up --build
```

## 🧠 Architecture Overview

Please see `docs/ARCHITECTURE.md` for a detailed breakdown of the system components and data flow.
