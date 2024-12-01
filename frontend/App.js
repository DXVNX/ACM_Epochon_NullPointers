import React, { useState } from 'react';
import { getEnergyEfficiency, getChargingSchedule } from './services/api';
import ChargingInfo from './components/ChargingInfo';

function App() {
  const [energyPrediction, setEnergyPrediction] = useState(null);
  const [chargingPrediction, setChargingPrediction] = useState(null);

  const handleEnergyEfficiency = async () => {
    const data = {
      "Peak Power Demand (kW)": [36.5],
      "Avg Power Demand (kW)": [26.0],
      "Power Loss During Transfer (%)": [4.5],
      "Avg Charging Rate (kW)": [23.0]
    };
    const response = await getEnergyEfficiency(data);
    setEnergyPrediction(response.prediction);
  };

  const handleChargingSchedule = async () => {
    const data = {
      "Energy Consumed (kWh)": [60.7],
      "Charging Rate (kW)": [36.4],
      "Temperature (°C)": [28.0],
      "Distance Driven (since last charge) (km)": [295.6],
      "Time of Day": ['Evening'],
      "Day of Week": ['Tuesday']
    };
    const response = await getChargingSchedule(data);
    setChargingPrediction(response.prediction);
  };

  return (
    <div className="App">
      <h1>Energy Efficiency & Charging Schedule Predictions</h1>
      <button onClick={handleEnergyEfficiency}>Get Energy Efficiency</button>
      <button onClick={handleChargingSchedule}>Get Charging Schedule</button>
      <ChargingInfo energyPrediction={energyPrediction} chargingPrediction={chargingPrediction} />
    </div>
  );
}

export default App;
