import streamlit as st
import pandas as pd
import numpy as np  # NumPy kütüphanesini ekleyin
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Dummy data preparation (replace this with your actual data)
# music_data_cleaned = pd.read_csv('your_music_data.csv')
# For demonstration, create a dummy DataFrame
music_data_cleaned = pd.DataFrame({
    'Danceability': [0.5, 0.7, 0.6, 0.9, 0.3],
    'Energy': [0.8, 0.6, 0.7, 0.9, 0.4],
    'Loudness': [-5, -3, -4, -2, -6],
    'Acousticness': [0.1, 0.2, 0.3, 0.1, 0.4],
    'Valence': [0.5, 0.6, 0.7, 0.8, 0.5],
    'Explicit': [1, 0, 1, 0, 1],
    'Key': [0, 1, 2, 3, 4],
    'Mode': [1, 0, 1, 0, 1],
    'Speechiness': [0.05, 0.1, 0.07, 0.08, 0.06],
    'Instrumentalness': [0.0, 0.1, 0.0, 0.2, 0.0],
    'Tempo': [120, 130, 125, 135, 110],
    'Popularity': [50, 60, 55, 70, 30]
})

# Convert 'Explicit' boolean to numeric (0 or 1)
music_data_cleaned['Explicit'] = music_data_cleaned['Explicit'].astype(int)

# Model için özellikleri seç
features = ['Danceability', 'Energy', 'Loudness', 'Acousticness', 'Valence', 'Explicit', 'Key', 'Mode', 'Speechiness', 'Instrumentalness', 'Tempo']
X = music_data_cleaned[features]
y = music_data_cleaned['Popularity']

# Standardizing
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Veri setlerini eğitim için ayır
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Streamlit uygulaması
st.title("Müzik Popülaritesi Tahmin Uygulaması")

# Kullanıcıdan verileri al
st.sidebar.header("Girdi Verileri")
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.5)
loudness = st.sidebar.slider("Loudness (dB)", -60, 0, -5)
acousticness = st.sidebar.slider("Acousticness", 0.0, 1.0, 0.1)
valence = st.sidebar.slider("Valence", 0.0, 1.0, 0.5)
explicit = st.sidebar.selectbox("Explicit", [0, 1])
key = st.sidebar.slider("Key", 0, 11, 0)
mode = st.sidebar.selectbox("Mode", [0, 1])
speechiness = st.sidebar.slider("Speechiness", 0.0, 1.0, 0.05)
instrumentalness = st.sidebar.slider("Instrumentalness", 0.0, 1.0, 0.0)
tempo = st.sidebar.slider("Tempo (BPM)", 60, 200, 120)

# Tahmin için özellikleri hazırlama
input_features = np.array([[danceability, energy, loudness, acousticness, valence, explicit, key, mode, speechiness, instrumentalness, tempo]])

# Standardize et
input_features_scaled = scaler.transform(input_features)

# Tahmin yapma
if st.button("Tahmin Et"):
    prediction = model.predict(input_features_scaled)
    st.subheader("Tahmin Edilen Popülarite:")
    st.write(f"{prediction[0]:.2f}")

# Katsayıları göster
st.subheader("Model Katsayıları:")
coefficients = pd.Series(model.coef_, index=features)
st.bar_chart(coefficients)