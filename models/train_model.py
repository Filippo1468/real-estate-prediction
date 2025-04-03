import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

df = pd.read_excel("data/Real estate valuation data set.xlsx")

feature_sets = {
    "features1": ['X2 house age', 'X3 distance to the nearest MRT station', 'X4 number of convenience stores'],
    "features2": ['X5 latitude', 'X6 longitude']
}

y = df['Y house price of unit area']

for key, features in feature_sets.items():
    X = df[features]

    if key == "features2":
        scaler = StandardScaler()
        X[['X5 latitude', 'X6 longitude']] = scaler.fit_transform(X[['X5 latitude', 'X6 longitude']])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    model_filename = f"models/real_estate_model_{key}.pkl"
    joblib.dump(model, model_filename)
    print(f"Modello {key} addestrato e salvato come {model_filename}")

print("Entrambi i modelli sono stati addestrati e salvati con successo.")
