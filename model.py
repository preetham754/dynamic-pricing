import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load sample dataset
df = pd.read_csv("data/salesdata.csv")

# Features and target
X = df[["demand", "competitor_price"]]
y = df["price"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "pricing_model.pkl")

print("Model trained and saved!")
