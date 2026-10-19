import streamlit as st
import joblib
import pandas as pd
from autots import AutoTS

# Modeli yükle
model = joblib.load('autots_model.pkl')

# Verilerinizi yükleyin (CSV dosyasını kullanarak)
data = pd.read_csv('Dogecoin.csv', parse_dates=['Date'])

# Streamlit UI
st.title('DogeCoin Price Prediction with AutoTS')

# Tahmin yapmak için model kullan
if st.button('Tahmin Et'):
    prediction = model.predict()
    forecast = prediction.forecast

    # Tahmin sonuçlarını göster
    st.write("DogeCoin Price Prediction:")
    st.dataframe(forecast)