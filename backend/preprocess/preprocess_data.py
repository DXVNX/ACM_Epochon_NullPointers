import pandas as pd

def load_energy_data():
    return pd.read_csv('data/energy_efficiency.csv')

def load_charging_data():
    return pd.read_csv('data/charging_behavior.csv')

def preprocess_data():
    energy_df = load_energy_data()
    charging_df = load_charging_data()

    # Preprocess energy data
    energy_df['Date'] = pd.to_datetime(energy_df['Date'])
    energy_df = energy_df.drop(columns=['Charging Station ID'])

    # Preprocess charging behavior data
    charging_df['Charging Start Time'] = pd.to_datetime(charging_df['Charging Start Time'])
    charging_df['Charging End Time'] = pd.to_datetime(charging_df['Charging End Time'])
    charging_df['Charging Duration'] = (charging_df['Charging End Time'] - charging_df['Charging Start Time']).dt.total_seconds() / 3600
    charging_df = charging_df.drop(columns=['Vehicle Model', 'Vehicle Age', 'State of Charge (Start %)', 'State of Charge (End %)'])

    # Save processed data
    energy_df.to_csv('data/energy_efficiency_processed.csv', index=False)
    charging_df.to_csv('data/charging_behavior_processed.csv', index=False)
