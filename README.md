# ⚡ Power Consumption Prediction App

This project is a Machine Learning web application built using Streamlit to predict power consumption based on environmental and time-based features.

---

## 🚀 Project Overview

The main goal of this project is to predict total power consumption using historical environmental data and time-related features.

Two machine learning models were implemented and compared:
- Random Forest Regressor
- XGBoost Regressor

The model with the best performance was selected based on evaluation metrics.

---

## 📊 Features Used

- Temperature  
- Humidity  
- Wind Speed  
- General Diffuse Flows  
- Diffuse Flows  
- Hour  
- Day  
- Month  

---

## 🧠 Models Implemented

### 1. Random Forest Regressor
- Used as a baseline model
- Performs well on structured/tabular data
- Less prone to overfitting in this case

### 2. XGBoost Regressor
- Parameters used:
  - n_estimators = 300  
  - learning_rate = 0.05  
  - max_depth = 6  
  - subsample = 0.8  
  - colsample_bytree = 0.8  

---

## 📈 Model Evaluation

- Evaluation Metric: Root Mean Squared Error (RMSE)
- Both models were trained on the same dataset and evaluated on the same test set.

### Result:
- Random Forest achieved lower RMSE compared to XGBoost
- Hence, Random Forest was selected as the final model

---

## ⚙️ Workflow

1. Data preprocessing
2. Feature extraction (hour, day, month from datetime)
3. Train-test split
4. Model training (RF and XGBoost)
5. Model evaluation using RMSE
6. Model selection
7. Deployment using Streamlit

---
http://192.168.20.110:8501
