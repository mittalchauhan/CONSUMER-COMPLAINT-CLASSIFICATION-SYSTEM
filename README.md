# SFI-Neural-Audit-Terminal
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)

An end-to-end Machine Learning application that classifies consumer complaints using an ensemble of NLP models. This project features a real-time web dashboard that communicates with a Python/Flask backend to provide live predictions and signal extraction.

## Dashboard Overview
The **Neural Audit Terminal** is designed for high-efficiency auditing. It uses three different AI engines to provide a consensus-based classification.

| Idle State | High Consensus Result |
| :--- | :--- |
| ![Dashboard Idle](dashboard_idle.png) | ![High Consensus](dashboard_consensus_high.png) |

## System Architecture
The application follows a modular microservice-style architecture. The Frontend (HTML/JS) sends text data to a Flask API, which processes the text through pre-trained Scikit-Learn pipelines.

![Architecture Diagram](architecture_diagram.jpg)

##  Features
* **Ensemble Scoring:** Uses Logistic Regression, SVM, and Naive Bayes simultaneously.
* **Real-time Signal Extraction:** Identifies key "Impact Words" that triggered the AI's decision.
* **Consensus Engine:** Automatically flags results as "High Consensus" or "Low/Disputed" based on model agreement.
* **Latency Tracking:** Measures backend processing time in milliseconds.

##  Project Structure
* `app.py`: The Flask server and prediction API.
* `templates/index.html`: The Neural Audit Terminal UI.
* `model_training.ipynb`: The Jupyter Notebook containing data analysis and model training logic.
* `*.pkl`: Pre-trained model pipelines and encoders.

##  Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   ```
2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   python app.py
   
   # Access the Terminal: Open http://127.0.0.1:5000 in your browser.
   ```