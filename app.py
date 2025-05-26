import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

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
        color: white;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.7);
        font-weight: bold;
        font-family: 'Segoe UI', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Középre helyezett cím
st.markdown("<h1 class='custom-title'>Barcelonai utazás</h1>", unsafe_allow_html=True)

# ⏳ JS-alapú visszaszámláló (mobilbarát felirat + rugalmas méretezés)
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
        padding: 2rem 1rem;
      }}

      .counter-box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 2.5rem 2rem;
        font-size: 1.8rem;
        color: white;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        font-family: 'Segoe UI', sans-serif;
        width: 100%;
        max-width: 500px;
      }}

      .counter-title {{
        font-size: 1.8rem;
        margin-bottom: 1.5rem;
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.9);
        font-weight: 600;
      }}

      #countdown {{
        font-size: 2.2rem;
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
