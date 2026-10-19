import streamlit as st
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Modeli yükle
tfv = joblib.load('tfidf_model.pkl')

# Uygulama başlığı
st.title("Film Özeti TF-IDF Analizi")

# Kullanıcıdan giriş al
user_input = st.text_area("Bir film özeti girin:")

if st.button("Analiz Et"):
    if user_input:
        # Kullanıcının girdiği metni dönüştür
        user_tfidf = tfv.transform([user_input])
        
        # Sonuçları göster
        st.write("TF-IDF Matrisi:")
        st.write(user_tfidf.toarray())
    else:
        st.error("Lütfen bir film özeti girin.")