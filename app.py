import streamlit.components.v1 as components
from datetime import datetime

target_date = datetime(2025, 6, 19, 0, 0, 0)

components.html(f"""
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <style>
      body {{
        margin: 0;
        padding: 0;
      }}

      .center-wrapper {{
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
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        backdrop-filter: blur(4px);
        font-family: 'Segoe UI', sans-serif;
      }}

      .title {{
        font-size: 1.5rem;
        font-weight: 400;
        margin-bottom: 1rem;
        color: #ffffff;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
      }}

      #countdown {{
        font-size: 2.2rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.7);
      }}
    </style>
  </head>
  <body>
    <div class="center-wrapper">
      <div class="counter-box">
        <div class="title">Hátralévő idő:</div>
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
""", height=300)
