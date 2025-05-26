import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# Oldal beállítás
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# Háttér + stílus
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# Cím
st.title("Barcelonai utazás")

# 🔁 Komponens: JS-alapú visszaszámláló
components.html(f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      .counter-box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 1.5rem;
        color: white;
        text-align: center;
        box-shadow: 0 0 25px rgba(0,0,0,0.4);
        backdrop-filter: blur(3px);
        font-family: sans-serif;
      }}
      h2 {{
        color: white;
        margin-bottom: 1rem;
      }}
      #countdown {{
        font-size: 2rem;
        font-weight: bold;
      }}
    </style>
  </head>
  <body>
    <div class="counter-box">
      <h2>Hátralévő idő:</h2>
      <div id="countdown">Számolás...</div>
    </div>
    <script>
      const target = new Date("{target_date.strftime('%Y-%m-%dT%H:%M:%S')}");
      function updateCountdown() {{
        const now = new Date();
        const diff = target - now;

        if (diff <= 0) {{
          document.getElementById("countdown").innerHTML = "🎉 Ma van az utazás napja vagy már elmúlt!";
          return;
        }}

        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
        const minutes = Math.floor((diff / (1000 * 60)) % 60);
        const seconds = Math.floor((diff / 1000) % 60);

        document.getElementById("countdown").innerHTML =
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
""", height=300)
