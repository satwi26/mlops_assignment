import os
import joblib
import numpy as np
from flask import Flask, request, jsonify

# Path to saved model
MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'model.pkl')

# Create Flask app
app = Flask(__name__)

# Load model once when app starts
try:
    model = joblib.load(MODEL_PATH)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'ok'})


@app.route('/predict', methods=['POST'])
def predict():
    """Make predictions using the trained model."""
    if model is None:
        return jsonify({'error': 'Model not loaded'}), 500

    data = request.get_json(force=True)
    instances = data.get('instances')
    if instances is None:
        return jsonify({'error': 'No instances in request'}), 400

    X = np.array(instances)
    preds = model.predict(X).tolist()
    return jsonify({'predictions': preds})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
