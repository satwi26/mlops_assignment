import joblib
import os
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Define directories
ROOT = os.path.dirname(__file__)
MODEL_DIR = os.path.join(ROOT, '..', 'models')
os.makedirs(MODEL_DIR, exist_ok=True)
MODEL_PATH = os.path.join(MODEL_DIR, 'model.pkl')

def train_and_save(random_state=42):
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_state)

    # Create a simple pipeline (scaling + model)
    pipe = Pipeline([
        ('scaler', StandardScaler()),
        ('clf', RandomForestClassifier(n_estimators=100, random_state=random_state))
    ])

    # Train the model
    pipe.fit(X_train, y_train)

    # Evaluate accuracy
    preds = pipe.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.4f}")

    # Save model to models folder
    joblib.dump(pipe, MODEL_PATH)
    print(f"Saved model to {MODEL_PATH}")

    return MODEL_PATH

if __name__ == '__main__':
    train_and_save()
