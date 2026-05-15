# 🏡 Airbnb Price Prediction and Insights

## 📌 Overview
Pricing an Airbnb listing effectively is crucial for maximizing revenue while staying competitive.
This project builds a machine learning regression model to predict Airbnb listing prices based on
property features, host attributes, location, and customer engagement metrics.

## 🎯 Problem Statement
The goal is to predict the price of an Airbnb listing using features such as:
- Property type
- Room type
- Location
- Number of reviews
- Amenities and host characteristics

Additionally, the project provides actionable insights to help hosts optimize pricing strategies.

## 📂 Dataset
- Dataset Name: Airbnb_data
- Records: ~74,000 listings
- Features: 29 attributes including pricing, location, reviews, and property details

## 🛠 Tools & Technologies
- Python (Pandas, NumPy)
- Scikit-learn
- Matplotlib & Seaborn
- Jupyter Notebook
- Random Forest Regressor

## 🔍 Data Preprocessing
- Handled missing values using median imputation
- Removed extreme price outliers (99th percentile)
- Encoded categorical features using Label Encoding
- Dropped irrelevant text-heavy columns

## 🤖 Model Development
Two regression models were trained:
- Linear Regression
- Random Forest Regressor

## 📊 Model Evaluation
| Model | MAE | RMSE | R² |
|------|-----|------|----|
| Linear Regression | 0.35 | 0.46 | 0.54 |
| Random Forest | 0.28 | 0.38 | 0.69 |

➡️ Random Forest outperformed Linear Regression and was selected as the final model.

## 🔑 Key Insights
- Property type and room type significantly influence pricing
- Listings with higher review scores tend to command higher prices
- Location-based features (latitude & longitude) strongly impact price
- Accommodates, bedrooms, and cleaning fee are major price drivers

## 💡 Business Recommendations
- Hosts should optimize amenities and listing quality to improve reviews
- Pricing strategies should be location-sensitive
- Entire home listings can be priced higher compared to shared rooms

## 🚀 Conclusion
This project demonstrates an end-to-end machine learning workflow from data cleaning
to model deployment readiness, delivering actionable insights for Airbnb hosts.

## 🎥 Project Walkthrough Video
[Watch the Project Explanation](https://drive.google.com/file/d/1qaBleDCP1iMjMNbUPTf-wII0f6kw66g1/view)

## Project Deployment (Hugging Face)
[Watch the Project Live Demo](https://huggingface.co/spaces/VedantJadhav9/Airbnb-Price-Predictor)

