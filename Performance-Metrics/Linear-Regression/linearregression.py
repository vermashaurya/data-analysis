import pandas as pd
import numpy as np

df = pd.read_csv('dataset.csv')
pd.set_option('display.width', None)

print("Original Dataset:")
print(df)

df = df.drop(columns=['Extracurricular Activities'])

X = df.drop(columns=['Performance Index']).values
y = df['Performance Index'].values

X = (X - np.mean(X, axis=0)) / np.std(X, axis=0)

X_b = np.c_[np.ones((len(X), 1)), X]

theta = np.random.randn(X_b.shape[1], 1)

learning_rate = 0.01
iterations = 1000
m = len(X)

y = y.reshape(-1, 1)

for iteration in range(iterations):
    gradients = (2/m) * X_b.T.dot(X_b.dot(theta) - y)
    theta -= learning_rate * gradients

predicted_values = X_b.dot(theta)

df['Predicted Performance Index'] = predicted_values

print("\nDataset with Predicted Performance Index:")
print(df[['Performance Index', 'Predicted Performance Index']].head())

# Calculate Mean Squared Error
mse = sum((y[i][0] - predicted_values[i][0]) ** 2 for i in range(len(y))) / len(y)
print(f"\nMean Squared Error (MSE): {mse}")
# Calculate Root Mean Squared Error
rmse = (sum((y[i][0] - predicted_values[i][0]) ** 2 for i in range(len(y))) / len(y)) ** 0.5
print(f"\nRoot Mean Squared Error (RMSE): {rmse}")
# Calculate Mean Absolute Error
mae = np.mean(np.abs(predicted_values - y))
print(f"\nMean Absolute Error (MAE): {mae}")
# Calculate R-squared
ss_total = np.sum((y - np.mean(y)) ** 2)
ss_residual = np.sum((y - predicted_values) ** 2)
r_squared = 1 - (ss_residual / ss_total)
print(f"\nR-squared: {r_squared}")
# Calculate Adjusted R-squared
n = len(y)  # Number of observations
p = X_b.shape[1] - 1  # Number of features (excluding the intercept)
adjusted_r_squared = 1 - (1 - r_squared) * (n - 1) / (n - p - 1)
print(f"\nAdjusted R-squared: {adjusted_r_squared}")
