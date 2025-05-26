import streamlit as st
from datetime import datetime

st.title("Barcelonai utazás")

# Fix dátum: 2025. június 9.
target_date = datetime(2025, 6, 9)
now = datetime.now()
target_datetime = datetime.combine(target_date, datetime.min.time())
delta = target_datetime - now

if delta.total_seconds() > 0:
    st.success(f"Hátralévő idő: {delta.days} nap, {delta.seconds // 3600} óra")
else:
    st.warning("Ez az utazás dátuma már elmúlt.")
