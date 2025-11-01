import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    'Area_sqft': [450, 550, 600, 720, 850, 950, 1100, 1300, 1500, 1600, 1750, 1900],
    'Bedrooms':  [1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4],
    'City_Rating': [6, 7, 6, 8, 7, 7, 8, 9, 8, 9, 9, 10],
    'Rent_per_month': [6500, 7200, 8000, 9500, 11000, 12500, 14500, 16000, 18000, 19000, 21000, 23000]
}
df = pd.DataFrame(data)

X = df[['Area_sqft', 'Bedrooms', 'City_Rating']]
y = df['Rent_per_month']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

# Combine features + actual + predicted for clarity
result = X_test.copy()
result['Actual_Rent'] = y_test.values
result['Predicted_Rent'] = y_pred.round(0)
print("\n🏘️  Test Data with Actual & Predicted Rent (₹):\n")
print(result.to_string(index=False))

# Predict for new unseen house
sample = pd.DataFrame({'Area_sqft':[1200], 'Bedrooms':[3], 'City_Rating':[8]})
predicted_rent = model.predict(sample)[0]
print(f"\n💡 Predicted Rent for NEW house (1200 sqft, 3BHK, Rating 8): ₹{int(predicted_rent)} per month")
