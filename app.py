from flask import Flask, request, jsonify
import pickle, numpy as np

app = Flask(__name__)

with open("model.pkl","rb") as f:
    model = pickle.load(f)

@app.route("/")
def root():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    X = np.array(data["instances"])
    preds = model.predict(X).tolist()
    return jsonify({"predictions": preds})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)