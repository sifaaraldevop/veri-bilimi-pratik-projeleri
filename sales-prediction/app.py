import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Örnek veri oluşturma (gerçek verilerinizi burada kullanmalısınız)
data = {
    'Feature1': [1, 2, 3, 4, 5],
    'Feature2': [2, 3, 4, 5, 6],
    'Target': [1.5, 2.5, 3.5, 4.5, 5.5]
}

df = pd.DataFrame(data)
X = df[['Feature1', 'Feature2']]
y = df['Target']

# Veriyi eğitim ve test setlerine ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modeli oluştur ve eğit
model = LinearRegression()
model.fit(X_train, y_train)

# Modeli kaydet
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Modeli yükle
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit uygulaması
st.title("Lineer Regresyon Tahmin Uygulaması")

# Kullanıcıdan girdi al
st.sidebar.header("Girdi Verileri")
feature1 = st.sidebar.number_input("Özellik 1", min_value=0.0, max_value=10.0, value=5.0)
feature2 = st.sidebar.number_input("Özellik 2", min_value=0.0, max_value=10.0, value=5.0)

# Tahmin yapma
input_data = np.array([[feature1, feature2]])
if st.button("Tahmin Et"):
    prediction = model.predict(input_data)
    st.subheader("Tahmin Edilen Değer:")
    st.write(f"{prediction[0]:.2f}")