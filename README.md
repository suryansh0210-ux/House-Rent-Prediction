 🏠 House Rent Prediction using Machine Learning

 📄 Project Overview
This project predicts the monthly rent of a house based on key features like area (in sqft), number of bedrooms, and city rating (locality quality).  
The model helps estimate rent prices for different cities and property sizes — similar to how real estate portals give price estimates.

## 🎯 Objective
To understand the end-to-end ML workflow: data creation, preprocessing, model training, prediction, and evaluation.

## 🧠 Technologies Used
- Python  
- Pandas, NumPy  
- scikit-learn (Linear Regression)  
- Matplotlib (for visualization)

## 📊 Dataset Details
A small custom dataset was created with columns:
- `Area_sqft` – Size of the house in square feet  
- `Bedrooms` – Number of bedrooms  
- `City_Rating` – Rating of the locality (1–10 scale)  
- `Rent_per_month` – Monthly rent in ₹ (used as target variable)

City_Rating represents the quality and demand of the area** —  
for example, Gurugram = 9, Dwarka = 8, Rohini = 6.

## ⚙️ Model Description
- Used Linear Regression from scikit-learn.  
- Trained model on the dataset to find the relationship between rent and input features.  
- The model then predicts rent for new data.

## 📈 Output Sample
Below is a sample comparison between Actual and Predicted rent values:

| Area_sqft | Bedrooms | City_Rating | Actual Rent | Predicted Rent |
|------------|-----------|--------------|--------------|----------------|
| 900 | 2 | 8 | ₹15,000 | ₹14,800 |
| 1100 | 3 | 9 | ₹22,000 | ₹21,900 |


