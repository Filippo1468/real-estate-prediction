import streamlit as st  
import pandas as pd  
import joblib  
import numpy as np


model1 = joblib.load("models/real_estate_model_features1.pkl")  
model2 = joblib.load("models/real_estate_model_features2.pkl")  

st.title("Predizione del prezzo degli immobili")

model_choice = st.radio(
    "Scegli il modello da utilizzare:",
    ("Età, distanza MRT, supermercati", "Latitudine e longitudine")
)

if model_choice == "Età, distanza MRT, supermercati":
    house_age = st.number_input("Età dello stabile (anni)", min_value=0.0, max_value=100.0, value=10.0, step=1.0)
    distance_mrt = st.number_input("Distanza alla MRT (metri)", min_value=0.0, max_value=10000.0, value=1000.0, step=100.0)
    num_convenience_stores = st.number_input("Numero di supermercati nelle vicinanze", min_value=0, max_value=15, value=3, step=1)

    house_age = float(house_age)  
    distance_mrt = float(distance_mrt)  
    num_convenience_stores = int(num_convenience_stores)

    if st.button("Predici prezzo"):
        input_data = np.array([[house_age, distance_mrt, num_convenience_stores]])
        prediction = model1.predict(input_data)[0]
        st.success(f"Il prezzo previsto per unità di area è: {prediction:.2f} al m^2")

else: 
    latitude = st.number_input("Latitudine", min_value=24.0, max_value=25.5, step=0.01)
    longitude = st.number_input("Longitudine", min_value=121.0, max_value=122.0, step=0.01)

    latitude = float(latitude) 
    longitude = float(longitude)

    if st.button("Predici prezzo"):
        input_data = np.array([[latitude, longitude]])
        prediction = model2.predict(input_data)[0]
        st.success(f"Il prezzo previsto per unità di area è: {prediction:.2f} al m^2")
