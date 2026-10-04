import joblib
import pandas as pd
import streamlit as st

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Car Price Prediction App", page_icon="🚗", layout="centered"
)

st.title(" Car Price Prediction App")
st.write(
    "Bu uygulama, araç özelliklerini kullanarak Random Forest modeli ile tahmini piyasa fiyatını hesaplar."
)

# Eğitilmiş modeli yükleme
@st.cache_resource
def load_model():
    return joblib.load("Car_Price_Prediction.pkl")


model = load_model()

# Kullanıcı Girdi Alanları (Sidebar veya Ana Ekran)
st.subheader("Araç Özelliklerini Giriniz:")

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox(
        "Marka (Brand)",
        ["Ford", "Audi", "Volkswagen", "Honda", "Chevrolet", "BMW", "Hyundai", "Kia", "Toyota", "Mercedes"],
    )
    model_name = st.text_input("Model", "Golf")
    year = st.number_input("Üretim Yılı (Year)", min_value=1990, max_value=2026, value=2020)
    engine_size = st.number_input("Motor Hacmi (Engine Size)", min_value=1.0, max_value=6.0, value=2.0)
    fuel_type = st.selectbox("Yakıt Tipi (Fuel Type)", ["Diesel", "Hybrid", "Electric", "Gasoline"])

with col2:
    transmission = st.selectbox("Vites Tipi (Transmission)", ["Manual", "Automatic", "Semi-Automatic"])
    mileage = st.number_input("Kilometre (Mileage)", min_value=0, max_value=500000, value=50000)
    doors = st.number_input("Kapı Sayısı (Doors)", min_value=2, max_value=5, value=4)
    owner_count = st.number_input("Önceki Sahip Sayısı (Owner Count)", min_value=1, max_value=5, value=1)

# Tahmin Butonu
if st.button("Fiyatı Tahmin Et ", type="primary"):
    # Girdileri DataFrame formatına getirme
    input_data = pd.DataFrame(
        {
            "Brand": [brand],
            "Model": [model_name],
            "Year": [year],
            "Engine_Size": [engine_size],
            "Fuel_Type": [fuel_type],
            "Transmission": [transmission],
            "Mileage": [mileage],
            "Doors": [doors],
            "Owner_Count": [owner_count],
        }
    )

    # Model ile tahmin yapma (Not: Not defterindeki preprocessor adımlarını buraya entegre edebilirsiniz)
    try:
        prediction = model.predict(input_data)
        st.success(f"Tahmin Edilen Araç Fiyatı: **${prediction[0]:,.2f}**")
    except Exception as e:
        st.error(
            f"Tahmin sırasında bir hata oluştu (Model sütun/scaler uyumu kontrol edilmeli): {e}"
        )