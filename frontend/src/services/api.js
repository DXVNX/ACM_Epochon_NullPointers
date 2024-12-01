const API_URL = 'http://localhost:5000'; // Flask backend URL

export const getEnergyEfficiency = async (data) => {
  const response = await fetch(`${API_URL}/predict/energy_efficiency`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
};

export const getChargingSchedule = async (data) => {
  const response = await fetch(`${API_URL}/predict/charging_schedule`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  });
  return response.json();
};
