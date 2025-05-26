import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components

# Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)

# Oldal beállítása
st.set_page_config(page_title="Barcelonai utazás", layout="centered")

# Háttér és alapstílus
st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url("https://i.imgur.com/hbWis1E.jpeg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: bold;
        color: white;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.8);
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Cím
st.markdown("<div class='main-title'>Barcelonai utazás</div>", unsafe_allow_html=True)

# JS-es visszaszámláló, új dizájnnal
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
        height: 50vh;
      }}
      .counter-box {{
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 1rem;
        padding: 2rem 3rem;
        font-size: 1.8rem;
        color: white;
        text-align: center;
        box-shadow: 0 8px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(5px);
        font-family: 'Segoe UI', sans-serif;
      }}
      .counter-title {{
        font-size: 1.5rem;
        margin-bottom: 1rem;
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
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
