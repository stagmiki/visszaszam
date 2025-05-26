import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# 🎯 Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# 🎨 Háttér + stílus
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .box {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 1.5rem;
        margin-top: 2rem;
        font-size: 1.5rem;
        color: white;
        text-align: center;
        box-shadow: 0 0 25px rgba(0,0,0,0.4);
        backdrop-filter: blur(3px);
    }

    h1 {
        text-align: center;
        color: white;
    }

    #counter {
        font-weight: bold;
        font-size: 2rem;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Cím
st.title("Barcelonai utazás")

# HTML + JS a számlálóhoz
st.markdown(f"""
<div class="box">
  <div>Hátralévő idő:</div>
  <div id="counter">Számolás...</div>
</div>

<script>
const target = new Date("{target_date.strftime('%Y-%m-%dT%H:%M:%S')}");
const counter = document.getElementById("counter");

function updateCountdown() {{
  const now = new Date();
  const diff = target - now;

  if (diff <= 0) {{
    counter.innerHTML = "🎉 Ma van az utazás napja vagy már elmúlt!";
    return;
  }}

  const days = Math.floor(diff / (1000 * 60 * 60 * 24));
  const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
  const minutes = Math.floor((diff / (1000 * 60)) % 60);
  const seconds = Math.floor((diff / 1000) % 60);

  counter.innerHTML = `${{days.toString().padStart(2,'0')}} nap, ${{hours.toString().padStart(2,'0')}} óra, ${{minutes.toString().padStart(2,'0')}} perc, ${{seconds.toString().padStart(2,'0')}} másodperc`;
}}

updateCountdown();
setInterval(updateCountdown, 1000);
</script>
""", unsafe_allow_html=True)
