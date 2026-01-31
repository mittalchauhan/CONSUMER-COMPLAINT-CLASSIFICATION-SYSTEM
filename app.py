from flask import Flask, request, render_template, jsonify
import joblib
import numpy as np
from scipy.special import softmax

app = Flask(__name__)

# - Asset Loading
models = {
    "Logistic Regression": joblib.load("complaint_pipeline.pkl"),
    "SVM Engine": joblib.load("svm_pipeline.pkl"),
    "Naive Bayes": joblib.load("nb_pipeline.pkl")
}
encoder = joblib.load("label_encoder.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    text = data.get('complaint', '')
    requested_models = data.get('active_models', list(models.keys()))
    
    predictions, confidences, final_models = [], [], []
    
    for name in requested_models:
        if name in models:
            pipeline = models[name]
            try:
                probs = pipeline.predict_proba([text])[0]
            except AttributeError:
                # Handle LinearSVC decision function
                probs = softmax(pipeline.decision_function([text])[0])
            
            pred_idx = np.argmax(probs)
            predictions.append(encoder.classes_[pred_idx])
            confidences.append(round(float(np.max(probs)) * 100, 2))
            final_models.append(name)

    # Signal Extraction
    tfidf = models["Logistic Regression"].named_steps['tfidf']
    vec = tfidf.transform([text]).toarray()[0]
    top_idx = vec.argsort()[::-1][:8]
    features = [{"word": tfidf.get_feature_names_out()[i].upper()} for i in top_idx if vec[i] > 0]

    return jsonify({
        "models": final_models,
        "predictions": predictions,
        "confidences": confidences,
        "consensus": "HIGH" if len(set(predictions)) == 1 else "LOW/DISPUTED",
        "features": features
    })

if __name__ == '__main__':
    app.run(debug=True)