# Customer Churn Prediction

This project predicts whether a customer is likely to churn using machine learning techniques.
The model is trained on the Telco Customer Churn dataset and deployed using Streamlit.

---

## Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib
- OpenPyXL

---

Customer-churn-prediction/
│
├── app.py # Streamlit web application
├── churn_model.py # Model training and saving script
├── requirements.txt # Project dependencies
├── README.md # Project documentation
├── .gitignore # Files and folders to ignore in Git
│
├── data/
│ └── Telco_customer_churn.xlsx # Dataset used for training
│
├── notebooks/
│ └── churn_analysis.ipynb # Exploratory data analysis notebook


---

## Features
- Data preprocessing and cleaning
- Handling mixed data types and missing values
- Machine learning model training (Logistic Regression)
- One-hot encoding for categorical variables
- Customer churn prediction
- Interactive Streamlit-based user interface

---

## Model Training

The trained model files (`churn_model.pkl`, `model_columns.pkl`) are not included in this repository
due to GitHub file size limitations.

To generate the model files locally, run:
```bash
python churn_model.py
```
This will create:
churn_model.pkl

model_columns.pkl

## How to Run the Application
- install dependencies
  pip install -r requirements.txt
- Run the Streamlit app
 streamlit run app.py

## Dataset
The dataset used is the public Telco Customer Churn dataset, which contains customer demographic,
service usage, and billing information.

## Output
Churn = 1 → Customer is likely to churn

Churn = 0 → Customer is not likely to churn

## Author
Megha Gautam
