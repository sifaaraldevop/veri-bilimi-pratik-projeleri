import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Modeli yükleme
model = tf.keras.models.load_model('model.keras')

# Sınıf isimleri
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
    'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot'
]

# Uygulama başlığı
st.title('Fashion MNIST Modeli ile Tahmin')

# Kullanıcıdan resim yükleme
uploaded_file = st.file_uploader("Bir resim yükleyin (28x28 boyutunda, gri tonlamalı)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Resmi yükleme ve ön işleme
    image = Image.open(uploaded_file).convert('L')  # Gri tonlamalı
    image = image.resize((28, 28))
    image_array = np.array(image)
    image_array = image_array.astype('float32') / 255.0
    image_array = image_array.reshape(1, 28, 28)  # Modelin beklediği şekil

    # Tahmin yapma
    predictions = model.predict(image_array)
    predicted_class = np.argmax(predictions, axis=1)

    # Sonuçları gösterme
    st.image(image, caption='Yüklenen Resim', use_column_width=True)
    st.write(f'Tahmin Edilen Sınıf: {class_names[predicted_class[0]]}')