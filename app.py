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
        margin-top: 10dvh;
        margin-bottom: 3rem;
        color: white !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
    }

    .glass-box {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 2rem;
        margin: 2rem auto;
        max-width: 600px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        font-family: 'Segoe UI', sans-serif;
    }

    .glass-box h2 {
        font-size: 1.8rem;
        margin-bottom: 1.2rem;
        color: white;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
    }

    .glass-box p {
        font-size: 1.2rem;
        margin: 0.5rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.markdown("<h1 class='custom-title'>Barcelonai utazás</h1>", unsafe_allow_html=True)

# ⏳ Visszaszámláló – keretben
components.html(f"""
<div class="glass-box">
  <h2>Hátralévő idő:</h2>
  <div id="countdown" style="font-size: 1.6rem; font-weight: bold; text-shadow: 1px 1px 3px black;">Számolás...</div>
</div>

<script>
  const target = new Date("{target_date.strftime('%Y-%m-%dT%H:%M:%S')}");
  const countdown = document.getElementById("countdown");

  function updateCountdown() {{
    const now = new Date();
    const diff = target - now;

    if (diff <= 0) {{
      countdown.innerHTML = "🎉 Ma van az utazás napja vagy már elmúlt!";
      return;
    }}

    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / (1000 * 60)) % 60);
    const seconds = Math.floor((diff / 1000) % 60);

    countdown.innerHTML =
      `${{String(days).padStart(2, '0')}} nap, ` +
      `${{String(hours).padStart(2, '0')}} óra, ` +
      `${{String(minutes).padStart(2, '0')}} perc, ` +
      `${{String(seconds).padStart(2, '0')}} másodperc`;
  }}

  updateCountdown();
  setInterval(updateCountdown, 1000);
</script>
""", height=160)

# 🌍 Időjárás – lekérés
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
        <div class="glass-box">
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
