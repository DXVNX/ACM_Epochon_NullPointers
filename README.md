# EVChargerProject
The increasing adoption of EVs strains grid infrastructure and charging stations. AI-powered charging networks optimize schedules to align with grid availability and renewable energy, reducing congestion and carbon footprint.

Overview:
This project aims to create an AI-powered Electric Vehicle (EV) charging network that optimizes charging schedules and energy supply to reduce carbon emissions, lower energy costs, and improve grid stability. The system uses machine learning models to analyze grid conditions, renewable energy availability, and user driving behavior, ultimately providing personalized charging recommendations and ensuring energy-efficient operation.

Features:

Energy Supply Optimization: Aligns charging activities with grid availability and renewable energy supply (e.g., solar, wind).
Personalized Charging Schedules: AI analyzes user behavior to recommend optimal charging times based on driving habits and trip data.
Renewable Energy Integration: Prioritizes charging when renewable energy is abundant, reducing reliance on fossil fuels.
Cost Optimization: Recommends off-peak charging to minimize energy costs for users.
Grid Load Balancing: Predicts energy demand and balances it across different locations to prevent grid congestion.


Tech stack
Frontend: React.js

Backend: Flask for API

Machine learning: Python
Model 1: Grid load optimization (e.g., regression models or neural networks).
Model 2: Personalized charging schedules (e.g., clustering or recommendation algorithms).

Database: 
Two csv files: charging_behaviour.csv and energy_efficiency.csv

APIs: RESTful API built with Flask to handle real-time data exchange between frontend and machine learning models.



Models

Model 1: Energy Supply Optimization

Objective: Predict grid load and renewable energy supply to optimize when and where energy should be supplied to the charging network.
Data: Historical grid demand, renewable energy availability (solar/wind), and weather data.
Machine Learning Approach: Regression models.

Model 2: Personalized Charging Schedules

Objective: Predict optimal charging times based on user behavior, such as trip duration, parking duration, and driving patterns.
Data: User driving behavior, trip logs, parking habits.
Machine Learning Approach: Regression modelsw.
