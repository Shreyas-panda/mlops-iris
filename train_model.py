import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
pipe = make_pipeline(StandardScaler(), LogisticRegression(max_iter=200))
pipe.fit(X_train, y_train)
print("Train:", pipe.score(X_train, y_train), "Test:", pipe.score(X_test, y_test))
with open("model.pkl", "wb") as f:
    pickle.dump(pipe, f)
print("Saved model.pkl")