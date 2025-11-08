from sklearn.ensemble import IsolationForest
import pandas as pd
import numpy as np

class AnomalyDetector:
    def __init__(self, contamination=0.01):
        self.contamination = contamination
        self.model = IsolationForest(contamination=self.contamination)

    def fit(self, data):
        self.model.fit(data)

    def predict(self, data):
        predictions = self.model.predict(data)
        return np.where(predictions == -1, 1, 0)  # 1 for anomaly, 0 for normal

    def detect_anomalies(self, data):
        self.fit(data)
        return self.predict(data)

def preprocess_data(logs):
    # Convert logs to a DataFrame and perform necessary preprocessing
    df = pd.DataFrame(logs)
    # Example preprocessing: fill missing values, normalize, etc.
    df.fillna(0, inplace=True)
    return df

if __name__ == "__main__":
    # Example usage
    sample_logs = [
        {"feature1": 1, "feature2": 2},
        {"feature1": 2, "feature2": 3},
        {"feature1": 1, "feature2": 2},
        {"feature1": 100, "feature2": 200},  # Anomaly
    ]

    processed_data = preprocess_data(sample_logs)
    detector = AnomalyDetector(contamination=0.1)
    anomalies = detector.detect_anomalies(processed_data)

    print("Anomalies detected:", anomalies)