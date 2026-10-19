import streamlit as st
import pickle
import pandas as pd
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components

# Modeli yükleme fonksiyonu
def load_model():
    with open('prophet_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Streamlit uygulaması
st.title("Hava Durumu Tahmini - Prophet Modeli")

# Modeli yükle
model = load_model()

# Kullanıcıdan tarih aralığı girişi
periods = st.number_input("Gelecek gün sayısını girin:", min_value=1, max_value=365, value=30)

# Gelecek verileri oluştur
future = model.make_future_dataframe(periods=periods)
predictions = model.predict(future)

# Tahminleri göster
st.subheader("Tahmin Sonuçları")
st.write(predictions[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])

# Tahmin sonuçlarını çiz
st.subheader("Tahmin Grafiği")
fig = plot_plotly(model, predictions)
st.plotly_chart(fig)

# Bileşen grafiğini çiz (matplotlib kullanarak)
st.subheader("Bileşen Grafiği")
components_fig = plot_components(model, predictions)
st.pyplot(components_fig)