import streamlit as st
from datetime import datetime

st.title("Dátum visszaszámláló")

target_date = st.date_input("Cél dátum")
now = datetime.now()
target_datetime = datetime.combine(target_date, datetime.min.time())
delta = target_datetime - now

if delta.total_seconds() > 0:
    st.success(f"Hátralévő idő: {delta.days} nap, {delta.seconds // 3600} óra")
else:
    st.warning("Ez a dátum már elmúlt.")
