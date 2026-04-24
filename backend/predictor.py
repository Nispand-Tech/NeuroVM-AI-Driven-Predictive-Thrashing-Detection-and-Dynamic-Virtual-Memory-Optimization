import numpy as np
import joblib

class ThrashingPredictor:
    def __init__(self):
        self.model = joblib.load("thrashing_model.pkl")

    def predict(self, page_fault_rate, cpu_utilization, working_set_size):

        X = np.array([[page_fault_rate, cpu_utilization, working_set_size]])

        pred = self.model.predict(X)[0]
        proba = self.model.predict_proba(X)[0]

        risk_score = float(proba[pred])  

        states = {
            0: "NORMAL",
            1: "WARNING",
            2: "SEVERE_THRASHING"
        }

        return {
            "state": states[pred],
            "risk": round(risk_score, 3)
        }