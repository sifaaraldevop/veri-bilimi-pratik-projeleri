import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Modeli yükle
model = tf.keras.models.load_model('my_model.h5')

# Uygulama başlığı
st.title("İşaret Dili İşaret Tanıma")

# Kullanıcıdan görüntü yükleme
uploaded_file = st.file_uploader("Bir işaret dili resmini yükleyin...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Resmi yükle ve ön işleme yap
    image = Image.open(uploaded_file).convert('L')  # Gri tonlamaya dönüştür
    image = image.resize((28, 28))  # Boyutu ayarla (modelin beklediği boyut)
    image = np.array(image) / 255.0  # Normalize et
    image = image.reshape(1, 28, 28, 1)  # Model girişi için şekillendir

    # Tahmin yap
    predictions = model.predict(image)
    predicted_class = np.argmax(predictions)

    # Sonucu göster
    st.write(f'Tahmin Edilen İşaret: {predicted_class}')  # Sınıf numarasını göster