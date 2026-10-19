import streamlit as st
import pandas as pd
import numpy as np
from keras.models import load_model
from sklearn.preprocessing import StandardScaler

# Modeli yükle
model = load_model('model.keras')

# Özniteliklerin standardizasyonu için scaler'ı oluştur
scaler = StandardScaler()

# Uygulama başlığı
st.title("Deprem Büyüklüğü ve Derinliği Tahmin Uygulaması")

# Kullanıcıdan girdi al
st.sidebar.header("Girdi Verileri")
timestamp = st.sidebar.text_input("Timestamp (örn: 2023-10-31 11:57:10)")
latitude = st.sidebar.number_input("Enlem", -90.0, 90.0, 0.0)
longitude = st.sidebar.number_input("Boylam", -180.0, 180.0, 0.0)

# Girdi verilerini hazırlama
input_data = np.array([[timestamp, latitude, longitude]])

# Eğer timestamp'ı kullanmayacaksanız, onu çıkarmanız ve uygun bir formatta giriş yapmanız gerekebilir.
# Burada sadece latitude ve longitude kullanılıyor.
# input_data = np.array([[latitude, longitude]])

# Standardize et
input_data_scaled = scaler.fit_transform(input_data)

# Tahmin yapma
if st.button("Tahmin Et"):
    prediction = model.predict(input_data_scaled)
    magnitude, depth = prediction[0]
    st.subheader("Tahmin Edilen Büyüklük ve Derinlik:")
    st.write(f"Büyüklük: {magnitude:.2f}")
    st.write(f"Derinlik: {depth:.2f} km")