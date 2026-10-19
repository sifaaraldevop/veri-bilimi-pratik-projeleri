import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go

# Uygulama başlığı
st.title("TV Reklamı ve Satış Analizi")

# Veriyi yükle
data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/Advertising.csv")

# İlk 5 satırı göster
st.subheader("Veri Seti")
st.write(data.head())

# X ve y değerlerini ayır
x = data["TV"].values.reshape(-1, 1)
y = data["Sales"]

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(x, y)

# Tahminler için aralık oluştur
x_range = np.linspace(x.min(), x.max(), 100)
y_range = model.predict(x_range.reshape(-1, 1))

# Grafiği oluştur
fig = px.scatter(data, x='TV', y='Sales', opacity=0.65)
fig.add_traces(go.Scatter(x=x_range, y=y_range, name='Linear Regresyon', mode='lines'))

# Grafiği göster
st.subheader("TV Reklamı ve Satış İlişkisi")
st.plotly_chart(fig)