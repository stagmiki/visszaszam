import streamlit as st
from datetime import datetime
import time
import base64

st.set_page_config(page_title="Barcelonai utazás", layout="wide")

# ✅ Háttér beállítása helyben tárolt képből (base64)
def get_base64_of_bin_file(picture_path):
    with open(picture_path, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(picture_path):
    bin_str = get_base64_of_bin_file(picture_path)
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .block-container {{
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 1rem;
    }}
    h1, h2 {{
        color: white;
        text-align: center;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

# 🖼️ Háttér beállítása
set_background('barcelona.jpeg')

# 🏷️ Cím
st.markdown("<h1>Barcelonai utazás</h1>", unsafe_allow_html=True)

# 🎯 Cél dátum
target_date = datetime(2025, 6, 19, 0, 0, 0)
placeholder = st.empty()

# 🔁 Élő visszaszámlálás
while True:
    now = datetime.now()
    delta = target_date - now

    with placeholder.container():
        if delta.total_seconds() > 0:
            days = delta.days
            hours = delta.seconds // 3600
            minutes = (delta.seconds % 3600) // 60
            seconds = delta.seconds % 60

            st.markdown(
                f"<div class='block-container'><h2>Hátralévő idő: {days} nap, {hours} óra, {minutes} perc, {seconds} másodperc</h2></div>",
                unsafe_allow_html=True
            )
        else:
            st.markdown("<div class='block-container'><h2>Ez az utazás dátuma már elmúlt.</h2></div>", unsafe_allow_html=True)

    time.sleep(1)
    st.experimental_rerun()
