import streamlit as st
from streamlit_player import st_player

# ---------- CONFIGURACIÓN ----------
st.set_page_config(page_title="Espacio de Relajación", page_icon="🌿", layout="centered")

# ---------- ESTILOS PERSONALIZADOS ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #e8f5e9, #ffffff);
    font-family: 'Helvetica', sans-serif;
}
h1, h2, h3, h4 {
    font-weight: 600;
    color: #2e4d39;
}
.box {
    background: #ffffffdd;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 6px 20px #00000015;
    margin-top: 20px;
    text-align: center;
}
button[kind="secondary"] {
    background-color: #a5d6a7 !important;
}
.stButton>button {
    background: #81c784 !important;
    color: white !important;
    border-radius: 15px !important;
    padding: 12px 24px !important;
    border: none !important;
    font-size: 18px !important;
    transition: 0.3s;
}
.stButton>button:hover {
    transform: scale(1.05);
    background: #66bb6a !important;
}
</style>
""", unsafe_allow_html=True)

# ---------- INTERFAZ ----------
st.markdown("<h1 style='text-align:center;'>🌿 ESPACIO DE RELAJACIÓN</h1>", unsafe_allow_html=True)
st.write("<p style='text-align:center;'>Respira profundo, elige tu ambiente y deja que el espacio te acompañe.</p>", unsafe_allow_html=True)

# ---------- DEFINICIÓN DE AMBIENTES ----------
ambientes = {
    "Ambiente 1 — Naturaleza": {
        "luz": "Verde suave",
        "musica": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "temperatura": "Fresca",
        "humidificador": "Alto"
    },
    "Ambiente 2 — Calma Cálida": {
        "luz": "Ámbar cálido",
        "musica": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "temperatura": "Templada",
        "humidificador": "Bajo"
    },
    "Ambiente 3 — Minimal Zen": {
        "luz": "Blanco tenue",
        "musica": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "temperatura": "Neutral",
        "humidificador": "Medio"
    }
}

# ---------- SELECCIÓN ----------
st.subheader("✨ Elige un Ambiente")

ambiente = st.selectbox("", list(ambientes.keys()))

data = ambientes[ambiente]

st.markdown(f"""
<div class="box">
<h3>🌸 {ambiente}</h3>
<p><b>Luz:</b> {data['luz']}</p>
<p><b>Temperatura:</b> {data['temperatura']}</p>
<p><b>Humidificador:</b> {data['humidificador']}</p>
</div>
""", unsafe_allow_html=True)

# ---------- MÚSICA ----------
st.subheader("🎧 Paisaje Sonoro")
st_player(data["musica"])

# ---------- CONTROL MANUAL ----------
st.markdown("<h2>🎨 Personaliza tu experiencia</h2>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        luz = st.color_picker("Color de la luz", "#81c784")
    with col2:
        temp = st.slider("Temperatura (°C)", 15, 35, 22)

hum = st.selectbox("Nivel del humidificador", ["Apagado", "Bajo", "Medio", "Alto"])

st.markdown(f"""
<div class="box">
<h3>🌬️ Estado Actual</h3>
<p><b>Luz actual:</b> {luz}</p>
<p><b>Temperatura configurada:</b> {temp} °C</p>
<p><b>Humidificador:</b> {hum}</p>
<p style="opacity:0.7">Esta configuración puede conectarse a Arduino / Wokwi después.</p>
</div>
""", unsafe_allow_html=True)
