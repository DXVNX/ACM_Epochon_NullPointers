import React from 'react';

function ChargingInfo({ energyPrediction, chargingPrediction }) {
  return (
    <div>
      {energyPrediction && (
        <div>
          <h2>Energy Efficiency Prediction:</h2>
          <p>{energyPrediction}</p>
        </div>
      )}

      {chargingPrediction && (
        <div>
          <h2>Charging Schedule Prediction:</h2>
          <p>{chargingPrediction}</p>
        </div>
      )}
    </div>
  );
}

export default ChargingInfo;
