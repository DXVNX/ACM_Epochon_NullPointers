# AI-Powered Electric Vehicle (EV) Charging Networks

This project leverages AI to optimize energy efficiency in EV charging networks. It includes two key AI models:

1. *Energy Efficiency for the Charging Grid*: Optimizing the energy supply to the grid, improving efficiency, and reducing energy loss during the transfer.
2. *Charging Schedule Based on Driver Behavior*: Predicting personalized charging schedules and routes based on user behavior to minimize energy consumption and cost.

The backend is built using *Flask* for serving the machine learning models, while the frontend is built with *React* for an interactive user interface.


## Key Features

- *Energy Efficiency Prediction*: Predicts energy consumption, efficiency, and grid load based on real-time data from charging stations.
- *Charging Schedule Prediction*: Customizes charging schedules based on user data, such as time of day, charging rate, and energy consumed.
- *Dynamic Charging Scheduling*: Optimizes charging times based on grid demand, renewable energy availability, and user behavior.
- *Carbon Footprint Optimization*: Minimizes carbon emissions by optimizing charging times when renewable energy is abundant.

## Tech Stack

- *Backend*: Python, Flask
- *Frontend*: React.js
- *Machine Learning*: scikit-learn, TensorFlow (for deep learning models)
- *Database*: No database is used for this project; it uses CSV files for data input.
- *Other Tools*: Node.js, npm
## Installation

### Backend Setup (Flask)

1. Clone the repository:
    bash
    git clone <repository-url>
    cd <repository-folder>
    

2. Create a virtual environment and install dependencies:
    bash
    python -m venv venv
    source venv/bin/activate  # For Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    

3. Run the Flask backend:
    bash
    python app.py
    

4. The backend will be accessible at http://127.0.0.1:5000/.
### Frontend Setup (React)

1. Navigate to the frontend directory:
    bash
    cd frontend
    

2. Install the required packages:
    bash
    npm install
    

3. Start the React development server:
    bash
    npm start
    

4. The frontend will be accessible at http://localhost:3000/.

### Credits
-**Kaggle** for datasets.

-**ChatGPT** for assistance with code, project structure, and documentation.

-Acknowledged other tools such as **TensorFlow**, **Flask** and **React.js**.





