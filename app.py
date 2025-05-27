import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import requests

# 🎯 Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# 📄 Oldal beállítás
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🎨 Háttér + középre igazított cím stílus
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .custom-title {
        text-align: center;
        font-size: 3.5rem;
        margin-top: 25vh;
        margin-bottom: 2rem;
        color: white !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
    }

    .box {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        margin: 2rem auto;
        font-size: 1.2rem;
        color: white;
        text-align: center;
        max-width: 500px;
        box-shadow: 0 0 20px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        font-family: 'Segoe UI', sans-serif;
    }

    .box h2 {
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.markdown("<h1 class='custom-title'>Barcelonai utazás</h1>", unsafe_allow_html=True)

# ⏳ Visszaszámláló – hagyományos jól működő
placeholder = st.empty()

# Visszaszámlálás (JS helyett frissülő blokk)
now = datetime.now()
delta = target_date - now

if delta.total_seconds() > 0:
    days = delta.days
    hours = delta.seconds // 3600
    minutes = (delta.seconds % 3600) // 60
    seconds = delta.seconds % 60

    with placeholder.container():
        st.markdown(
            f"<div class='box'><h2>Hátralévő idő:</h2>{days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</div>",
            unsafe_allow_html=True
        )
else:
    st.markdown("<div class='box'>🎉 Ez az utazás dátuma már elmúlt!</div>", unsafe_allow_html=True)

# 🌍 Időjárás – külön dobozban
API_KEY = "7f6722e92808e9cb374d127f5d154122"
CITY_ID = "3128760"
URL = f"https://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric&lang=hu"

try:
    response = requests.get(URL)
    data = response.json()

    if data.get("cod") == 200:
        weather = data["weather"][0]["description"].capitalize()
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        st.markdown(f"""
        <div class='box'>
            <h2>🌤️ Aktuális időjárás Barcelonában</h2>
            <img src="http://openweathermap.org/img/wn/{icon}@2x.png" width="80">
            <p><strong>Állapot:</strong> {weather}</p>
            <p><strong>Hőmérséklet:</strong> {temp}°C (érzetre: {feels_like}°C)</p>
            <p><strong>Páratartalom:</strong> {humidity}%</p>
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Nem sikerült lekérdezni az időjárást.")
except Exception as e:
    st.error(f"Hiba történt az időjárás lekérésekor: {e}")
