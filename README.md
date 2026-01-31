# CONSUMER-COMPLAINT-CLASSIFICATION-SYSTEM
![Status](https://img.shields.io/badge/status-complete-brightgreen.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)

An end-to-end Machine Learning application that classifies consumer complaints using an ensemble of NLP models. This project features a real-time web dashboard that communicates with a Python/Flask backend to provide live predictions and signal extraction.

The **Neural Audit Terminal** is designed for high-efficiency auditing. It uses three different AI engines to provide a consensus-based classification.

## Terminal IDLE 
- The initial state of the Neural Audit Terminal before a scan is initiated.
---
![Dashboard Idle](assets/dashboard_idle.png)
---

## IDLE: High Consensus
- When all active engines (Logistic Regression, SVM, and Naive Bayes) agree on the classification, the system flags a high-confidence consensus.
---
![High Consensus](assets/dashboard_consensus_high.png)
---

## IDLE: Low Consensus 
- In cases where the models disagree or return low probability scores, the terminal alerts the auditor to perform a manual review.
---
![Low Consensus](assets/dashboard_consensus_low.png)
---

## System Architecture
- The application follows a modular microservice-style architecture. The Frontend (HTML/JS) sends text data to a Flask API, which processes the text through pre-trained Scikit-Learn pipelines.
---
![Architecture Diagram](assets/Diagram.jpg)
---

##  Features
* **Ensemble Scoring:** Uses Logistic Regression, SVM, and Naive Bayes simultaneously.
* **Real-time Signal Extraction:** Identifies key "Impact Words" that triggered the AI's decision.
* **Consensus Engine:** Automatically flags results as "High Consensus" or "Low" based on model agreement.
* **Latency Tracking:** Measures backend processing time in milliseconds.

##  Project Structure
* **`app.py`**: The Flask server and prediction API that processes real-time requests.
* **`index.html`**: The Neural Audit Terminal UI, styled with Bootstrap and powered by vanilla JavaScript.
* **`Plotly.js`**: Provides logic for rendering live probability distributions and historical trends.
* **`Consumer complaint classification.ipynb`**: contains data cleaning, EDA and model training logic.
* **`*.pkl`**: Pre-trained Scikit-Learn pipelines and Label Encoders.

##  Installation & Usage
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd <repo-folder>
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