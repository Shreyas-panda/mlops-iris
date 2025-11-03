# train_model.py
# Creates a tiny dummy model with a .predict() method and saves it as model.pkl
import pickle

class DummyModel:
    """
    Dummy classifier:
    - It returns class 0 if sum(features) < threshold
    - class 1 if sum(features) >= threshold but < 2*threshold
    - else class 2.
    This is just a stub to demonstrate pipeline behavior.
    """
    def __init__(self, threshold=5.0):
        self.threshold = threshold

    def predict(self, X):
        # X expected as list of list-like numeric features
        preds = []
        for row in X:
            s = sum(row)
            if s < self.threshold:
                preds.append(0)
            elif s < 2 * self.threshold:
                preds.append(1)
            else:
                preds.append(2)
        return preds

if __name__ == "__main__":
    model = DummyModel(threshold=5.0)
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("Dummy model saved to model.pkl")