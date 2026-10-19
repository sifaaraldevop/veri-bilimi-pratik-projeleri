import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# CSV dosyasını yükle
url = "https://raw.githubusercontent.com/amankharwal/Website-data/master/social.csv"
df = pd.read_csv(url)

# Uygulama başlığı
st.title("Sosyal Medya Satın Alma Tahmin Uygulaması")

# Veri çerçevesini göster
st.write("Veri Seti:")
st.dataframe(df)

# Hedef etiketler
st.write("Hedef Etiketler:", df["Purchased"].unique())

# Özellikleri ve etiketleri ayır
X = df[['Age', 'EstimatedSalary']]
y = df['Purchased']

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LogisticRegression()
model.fit(X_train, y_train)

# Kullanıcıdan girdi al
st.sidebar.header("Girdi Verileri")
age = st.sidebar.number_input("Yaş", min_value=18, max_value=100, value=30)
salary = st.sidebar.number_input("Tahmini Maaş", min_value=10000, max_value=150000, value=50000)

# Tahmin yapma
input_data = np.array([[age, salary]])
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Tahmin sonucunu göster
    st.subheader("Tahmin Edilen Sonuç:")
    st.write("Satın Alma Durumu:", "Evet" if prediction[0] == 1 else "Hayır")
    st.write("Tahmin Olma Olasılığı:", prediction_proba[0][1])