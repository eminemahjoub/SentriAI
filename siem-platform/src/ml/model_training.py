from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
import pandas as pd
import joblib

class ModelTrainer:
    def __init__(self, data_path, model_path):
        self.data_path = data_path
        self.model_path = model_path
        self.model = IsolationForest(contamination=0.1)

    def load_data(self):
        data = pd.read_csv(self.data_path)
        return data

    def preprocess_data(self, data):
        # Assuming the data needs to be normalized or transformed
        # This is a placeholder for actual preprocessing logic
        return data

    def train_model(self, data):
        X = data.drop(columns=['label'], errors='ignore')  # Drop label if it exists
        self.model.fit(X)

    def save_model(self):
        joblib.dump(self.model, self.model_path)

    def run(self):
        data = self.load_data()
        processed_data = self.preprocess_data(data)
        self.train_model(processed_data)
        self.save_model()

if __name__ == "__main__":
    trainer = ModelTrainer(data_path='../models/training/training_data.csv', model_path='../models/saved/anomaly_model.pkl')
    trainer.run()