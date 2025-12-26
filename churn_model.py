import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Load dataset
df = pd.read_excel("data/Telco_customer_churn.xlsx")
# -----------------------------
# Data cleaning (IMPORTANT)
# -----------------------------

# Fix Total Charges column properly
df["Total Charges"] = pd.to_numeric(df["Total Charges"], errors="coerce")

# Fill missing Total Charges with median
df["Total Charges"].fillna(df["Total Charges"].median(), inplace=True)

# Convert all categorical columns to string
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].astype(str)


# Convert all categorical columns to string
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = df[col].astype(str)


# Target variable
y = df["Churn Value"]

# Drop columns not useful for prediction
X = df.drop([
    "CustomerID",
    "Churn Label",
    "Churn Value",
    "Churn Reason"
], axis=1)

# Separate categorical and numerical columns
categorical_cols = X.select_dtypes(include=["object"]).columns
numerical_cols = X.select_dtypes(exclude=["object"]).columns

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

# Model
model = LogisticRegression(max_iter=1000)

# Pipeline
pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier", model)
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
pipeline.fit(X_train, y_train)

# Save model and columns
joblib.dump(pipeline, "churn_model.pkl")
joblib.dump(X.columns.tolist(), "model_columns.pkl")

print("✅ Model training complete.")
print("📁 Files saved: churn_model.pkl, model_columns.pkl")
