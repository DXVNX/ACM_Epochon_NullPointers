import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def load_charging_data():
    return pd.read_csv('data/charging_behavior.csv')

def preprocess_charging_data(df):
    df['Charging Start Time'] = pd.to_datetime(df['Charging Start Time'])
    df['Charging End Time'] = pd.to_datetime(df['Charging End Time'])
    df['Charging Duration'] = (df['Charging End Time'] - df['Charging Start Time']).dt.total_seconds() / 3600
    df = df.drop(columns=['Vehicle Model', 'Vehicle Age', 'State of Charge (Start %)', 'State of Charge (End %)'])
    return df

def train_charging_schedule_model():
    df = load_charging_data()
    df = preprocess_charging_data(df)

    X = df[['Energy Consumed (kWh)', 'Charging Rate (kW)', 'Temperature (°C)', 'Distance Driven (since last charge) (km)', 'Time of Day', 'Day of Week']]
    y = df['Charging Duration']

    X = pd.get_dummies(X, columns=['Time of Day', 'Day of Week'], drop_first=True)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f'Mean Absolute Error for Charging Schedule Model: {mae}')

    return model

def predict_charging_schedule(input_data):
    model = train_charging_schedule_model()

    input_df = pd.DataFrame(input_data)
    input_df = pd.get_dummies(input_df, columns=['Time of Day', 'Day of Week'], drop_first=True)
    prediction = model.predict(input_df)
    return prediction.tolist()
