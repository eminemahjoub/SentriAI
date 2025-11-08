import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def load_data(file_path):
    return pd.read_csv(file_path)

def preprocess_data(data):
    # Assuming the last column is the target variable
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    return X, y

def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def save_model(model, model_path):
    joblib.dump(model, model_path)

if __name__ == "__main__":
    data_file = '../models/training/training_data.csv'
    model_file = '../models/saved/anomaly_model.pkl'
    
    data = load_data(data_file)
    X, y = preprocess_data(data)
    model = train_model(X, y)
    save_model(model, model_file)
    print("Model trained and saved successfully.")