import pandas as pd 
import numpy as np 

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor

from sklearn.metrics import  r2_score, mean_squared_error

import joblib

# Loading Data
path = "CaloriMate/Data/calorie_burned_data.csv"
df = pd.read_csv(path)

target_column = "Calories"
X = df.drop(columns=[target_column])
y = df[target_column]

# Feature Engineering
numeric_cols = X.select_dtypes(include=["int64","float64"]).columns.tolist()
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()

preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numeric_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Splitting the Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Build + Train model
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MSE:",mse)
print("R2 Score:", r2)

# Save Model

joblib.dump(model, "CaloriMate/Model/calorie_model.pkl")
print("Model saved.")