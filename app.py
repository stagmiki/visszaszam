import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import requests
import random

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
        font-size: 3.2rem;
        margin-top: 20dvh;
        margin-bottom: 1rem;
        color: white !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Cím
st.markdown("<h1 class='custom-title'>Barcelonai utazás</h1>", unsafe_allow_html=True)

# ⏳ JS-alapú visszaszámláló
components.html(f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body {{
        margin: 0;
        padding: 0;
        background: transparent;
      }}

      .counter-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0;
        margin-bottom: 0;
      }}

      .counter-box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem 1rem;
        font-size: 1.6rem;
        color: white;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        font-family: 'Segoe UI', sans-serif;
        width: 100%;
        max-width: 600px;
      }}

      .counter-title {{
        font-size: 1.6rem;
        margin-bottom: 1rem;
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
        font-weight: 600;
      }}

      #countdown {{
        font-size: 2rem;
        font-weight: bold;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.7);
      }}
    </style>
  </head>
  <body>
    <div class="counter-container">
      <div class="counter-box">
        <div class="counter-title">Hátralévő idő:</div>
        <div id="countdown">Számolás...</div>
      </div>
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
  </body>
</html>
""", height=400)

# 🌍 Időjárás API
API_KEY = "7f6722e92808e9cb374d127f5d154122"
CITY_ID = "3128760"
URL = f"https://api.openweathermap.org/data/2.5/weather?id={CITY_ID}&appid={API_KEY}&units=metric&lang=hu"

# 🌦️ Időjárás megjelenítése
try:
    response = requests.get(URL)
    data = response.json()

    if data.get("cod") == 200:
        weather = data["weather"][0]["description"].capitalize()
        icon = data["weather"][0]["icon"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        st.markdown("<div style='margin-top: -10rem'></div>", unsafe_allow_html=True)
        st.markdown(f"""
            <div style='
                background-color: rgba(0, 0, 0, 0.6);
                padding: 1.5rem;
                border-radius: 1rem;
                color: white;
                text-align: center;
                max-width: 600px;
                margin: 0rem auto;
                box-shadow: 0 4px 20px rgba(0,0,0,0.5);
                backdrop-filter: blur(4px);
                font-family: "Segoe UI", sans-serif;
            '>
                <h3 style='margin-bottom: 1rem;'>🌤️<br>Aktuális időjárás Barcelonában</br></h3>
                <img src="http://openweathermap.org/img/wn/{icon}@2x.png" width="80">
                <p><strong>Állapot:</strong> {weather}</p>
                <p><strong>Hőmérséklet:</strong> {temp}°C <br>(hőérzet: {feels_like}°C)</br></p>
                <p><strong>Páratartalom:</strong> {humidity}%</p>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("Nem sikerült lekérdezni az időjárást.")
except Exception as e:
    st.error(f"Hiba történt az időjárás lekérésekor: {e}")

# 💬 Barcelonai idézet doboz – sötétebben, kisebb margóval
barcelona_facts = [
    "„Barcelona több, mint város – ez egy életérzés.”",
    "A Sagrada Família templomot 1882-ben kezdték építeni – még mindig épül!",
    "Antoni Gaudí haláláig csak egy tornyot fejezett be a Sagrada Famílián.",
    "A barcelonai strandokat csak 1992-ben, az olimpia előtt építették ki!",
    "Barcelona az egyetlen város, aminek kilenc UNESCO világörökségi helyszíne van!",
    "A tapas nem étel, hanem étkezési stílus – kis adagok megosztásra.",
    "Barcelona lakói hivatalosan katalánnak vallják magukat – nem spanyolnak!",
    "A Rambla nem egy utca, hanem öt egybefolyó utca.",
    "„A tenger és a hegy között születtem – így lettem Barcelonai.” – ismeretlen",
    "Barcelonában található Európa legöregebb fedett piacainak egyike: La Boqueria."
]

random_fact = random.choice(barcelona_facts)

st.markdown(f"""
    <div style='
        background-color: rgba(0, 0, 0, 0.65);
        padding: 1.2rem;
        border-radius: 1rem;
        color: white;
        font-style: italic;
        text-align: center;
        max-width: 600px;
        margin: 1.2rem auto;
        box-shadow: 0 0 12px rgba(0,0,0,0.4);
        font-family: "Segoe UI", sans-serif;
        backdrop-filter: blur(4px);
    '>
        🌟 <em>{random_fact}</em>
    </div>
""", unsafe_allow_html=True)
