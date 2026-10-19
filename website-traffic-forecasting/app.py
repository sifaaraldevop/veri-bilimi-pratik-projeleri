import streamlit as st
import joblib
import pandas as pd
import statsmodels.api as sm

# Modeli yükle
model = joblib.load('sarimax_model.pkl')

# Verilerinizi yükleyin (tarih sütunu adını doğru bir şekilde değiştirin)
data = pd.read_csv('Thecleverprogrammer.csv', parse_dates=['Date'], index_col='Date')

# Modelin özetini göster
st.title('SARIMAX Model Özeti')
st.write(model.summary())

# Tahmin yapmak için bir fonksiyon oluşturun
def predict_views(model, data, steps=5):
    last_date = data.index[-1]  # Son tarih
    print("Last Date:", last_date)  # Hata ayıklama için
    print("Type of Last Date:", type(last_date))  # Hata ayıklama için

    # Son tarihi doğru bir şekilde kullan
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=steps)
    
    # Tahminleri yap
    forecast = model.get_forecast(steps=steps)
    predicted_mean = forecast.predicted_mean
    return future_dates, predicted_mean

# Streamlit UI
steps = st.number_input('Tahmin edilecek adım sayısı', min_value=1, max_value=30, value=5)

if st.button('Tahmin Et'):
    future_dates, predictions = predict_views(model, data, steps)
    st.write('Tahmin Edilen Görüntü Sayısı:')
    for date, prediction in zip(future_dates, predictions):
        st.write(f"{date.date()}: {prediction:.2f}")