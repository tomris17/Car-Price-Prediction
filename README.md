#  Car Price Prediction Project

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains an end-to-end Machine Learning Regression project designed to predict car prices based on technical specifications and categorical attributes. The model achieves high predictive accuracy ($R^2$ score ~ 0.98) using a Random Forest Regressor.

---

##  Dataset Features
The model is trained on a structured dataset (`car_price_dataset.csv`) containing the following features:
* **Brand & Model**: Manufacturer and specific vehicle model[cite: 4].
* **Year**: Manufacturing year[cite: 4].
* **Engine_Size**: Engine displacement volume[cite: 4].
* **Fuel_Type**: Petrol, Diesel, Hybrid, or Electric[cite: 4].
* **Transmission**: Manual, Automatic, or Semi-Automatic[cite: 4].
* **Mileage**: Total distance driven[cite: 4].
* **Doors & Owner_Count**: Structural and ownership details[cite: 4].
* **Price**: Target variable (Car Market Price)[cite: 4].

---

##  Project Workflow
1. **Data Preprocessing**: Handling numerical scaling (`StandardScaler`) and categorical encoding (`OneHotEncoder`) via Scikit-Learn's `ColumnTransformer`.
2. **Model Training**: Fitting a `RandomForestRegressor` with optimized parameters (`random_state=42`)[cite: 4].
3. **Evaluation**: Assessing performance using Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and $R^2$ Score.
4. **Model Persistence**: Exporting the trained model using `joblib` into `Car_Price_Prediction.pkl`[cite: 4].
5. **Web Application**: Interactive deployment layout built using Streamlit.

---

##  Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/car-price-prediction.git](https://github.com/YOUR_USERNAME/car-price-prediction.git)
   cd car-price-prediction
