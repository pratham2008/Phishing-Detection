import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Step 1: Load dataset
data = pd.read_csv("data/phishing.csv")
print("Columns in dataset:", data.columns)

# Step 2: Features and Target
X = data.drop("class", axis=1)   # all columns except 'class'
y = data["class"]                # target column

# Step 3: Split into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Step 5: Evaluate model
y_pred = model.predict(X_test)
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 6: Save the trained model
joblib.dump(model, "models/phishing_model.pkl")
print("💾 Model saved as models/phishing_model.pkl")
