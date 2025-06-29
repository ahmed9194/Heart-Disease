import joblib
from sklearn.tree import DecisionTreeClassifier
import pandas as pd
import os

# Loading the data
df = pd.read_csv(r"C:\Users\user\Desktop\Project (1)intelligent prog\cleaned_data.csv")

# Splitting features from the target
X = df.drop(columns=["target"])
y = df["target"]

# Training the model
model = DecisionTreeClassifier()
model.fit(X, y)

# Create the folder if it doesn't exist
model_dir = r"C:\Users\user\AppData\Local\Microsoft\Windows\INetCache\IE\NP37CT3P\ml_model"
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Saving the model inside the folder
model_path = os.path.join(model_dir, "heart_disease_model.pkl")
joblib.dump(model, model_path)

print(f"✅ Model saved successfully at {model_path}")
