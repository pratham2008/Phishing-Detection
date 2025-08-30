# predict.py
import joblib
import sys
import pandas as pd
from features import extract_features

# Load the trained model
model = joblib.load("models/phishing_model.pkl")

def predict_url(url):
    """Predict if the given URL is phishing or legitimate"""
    features_dict = extract_features(url)  # Extract dictionary of features

    # Convert dict to DataFrame with same feature order as training
    features_df = pd.DataFrame([features_dict])

    prediction = model.predict(features_df)[0]

    if prediction == 1:
        return f"[SAFE] {url}"
    else:
        return f"[PHISHING] {url}"

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python predict.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    result = predict_url(url)
    print(result)
