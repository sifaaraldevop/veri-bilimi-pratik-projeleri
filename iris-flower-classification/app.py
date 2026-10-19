import streamlit as st
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Iris veri setini yükle
iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['species'] = iris.target

# Hedef etiketleri göster
st.title("Iris Çiçeği Türü Tahmin Uygulaması")
st.write("Hedef Etiketler: ", df["species"].unique())

# Özellikleri ve etiketleri ayır
X = df[iris.feature_names]
y = df['species']

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Kullanıcıdan girdi al
st.sidebar.header("Girdi Verileri")
sepal_length = st.sidebar.number_input("Sepal Uzunluğu (cm)", min_value=4.0, max_value=8.0, value=5.0)
sepal_width = st.sidebar.number_input("Sepal Genişliği (cm)", min_value=2.0, max_value=5.0, value=3.0)
petal_length = st.sidebar.number_input("Petal Uzunluğu (cm)", min_value=1.0, max_value=7.0, value=1.5)
petal_width = st.sidebar.number_input("Petal Genişliği (cm)", min_value=0.1, max_value=2.5, value=0.2)

# Tahmin yapma
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    predicted_species = iris.target_names[prediction][0]

    # Tahmin sonucunu göster
    st.subheader("Tahmin Edilen Tür:")
    st.write(predicted_species)