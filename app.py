# app.py - minimal Flask app that uses model.pkl
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def health():
    return "OK", 200

@app.route("/predict", methods=["POST"])
def predict():
    payload = request.get_json()
    # expect payload: {"instances": [[1,2,3], [4,5,6]]}
    instances = payload.get("instances")
    if not isinstance(instances, list):
        return jsonify({"error": "instances must be a list of lists"}), 400
    preds = model.predict(instances)
    return jsonify({"predictions": preds})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)