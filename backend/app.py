from flask import Flask, request, jsonify
from models.energy_efficiency_model import train_energy_efficiency_model, predict_energy_efficiency
from models.charging_schedule_model import train_charging_schedule_model, predict_charging_schedule
from preprocess.preprocess_data import preprocess_data

app = Flask(__name__)

# Route for preprocessing data
@app.route('/preprocess', methods=['POST'])
def preprocess():
    preprocess_data()
    return jsonify({"message": "Data preprocessing completed successfully"}), 200

# Route for training models
@app.route('/train', methods=['POST'])
def train_models():
    energy_model = train_energy_efficiency_model()
    schedule_model = train_charging_schedule_model()
    return jsonify({"message": "Models trained successfully"}), 200

# Route for predicting energy efficiency

@app.route('/predict/energy_efficiency', methods=['POST'])
def predict_energy_efficiency_route():
    data = request.get_json()
    prediction = predict_energy_efficiency(data)
    return jsonify({"prediction": prediction}), 200

# Route for predicting charging schedule
@app.route('/predict/charging_schedule', methods=['POST'])
def predict_charging_schedule_route():
    data = request.get_json()
    prediction = predict_charging_schedule(data)
    return jsonify({"prediction": prediction}), 200

if __name__ == '__main__':
    app.run(debug=True)
