import streamlit as st
from transformers import MarianMTModel, MarianTokenizer
import torch  # Torch kütüphanesini içe aktar

# Model ve Tokenizer'ı yükleme
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

# Uygulama başlığı
st.title("İngilizce - Hintçe Çeviri Uygulaması")

# Kullanıcıdan girdi alma
input_sentence = st.text_area("İngilizce Cümle Girin:")

if st.button("Çevir"):
    # Tokenizasyon
    inputs = tokenizer(input_sentence, return_tensors="pt", max_length=128, truncation=True)
    
    # Model ile çeviri
    with torch.no_grad():
        translated = model.generate(**inputs)
    
    # Çeviriyi çözme
    output = tokenizer.decode(translated[0], skip_special_tokens=True)
    
    # Sonucu gösterme
    st.success(f"Hindice Çeviri: {output}")