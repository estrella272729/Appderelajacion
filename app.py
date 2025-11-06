import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="Espacio Zen", page_icon="🌿", layout="wide")

# -------- BACKGROUND DYNAMIC STYLE --------
def set_bg(image_url):
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{image_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .title-box {{
        background: rgba(255,255,255,0.55);
        padding: 25px;
        border-radius: 18px;
        backdrop-filter: blur(4px);
        text-align:center;
        animation: fadein 1s ease;
    }}
    @keyframes fadein {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .control-box {{
        background: rgba(255,255,255,0.45);
        padding: 20px;
        border-radius: 16px;
        backdrop-filter: blur(5px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.15);
        animation: fadein 1s ease;
    }}
    .stButton>button {{
        background: #ffffffcc;
        border: none;
        padding: 14px 26px;
        border-radius: 14px;
        font-size: 18px;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        transform: scale(1.07);
        background: #ffffff;
    }}
    </style>
    """, unsafe_allow_html=True)

# -------- AMBIENTES --------
ambientes = {
    "🌴 Selva": {
        "bg":"https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "musica":"https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "luz":"Verde selva",
        "temperatura":"Fresca y húmeda",
        "humidificador":"Alto"
    },
    "🏜️ Desierto": {
        "bg":"https://images.unsplash.com/photo-1508264165352-258a6f039317",
        "musica":"https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "luz":"Ámbar dorado",
        "temperatura":"Cálida suave",
        "humidificador":"Bajo"
    },
    "🕯️ Zen Minimal": {
        "bg":"https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "musica":"https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "luz":"Blanco tenue",
        "temperatura":"Neutral",
        "humidificador":"Medio"
    }
}

# -------- SELECTOR --------
st.markdown("<div class='title-box'><h1>🌿 ESPACIO DE RELAJACIÓN</h1><p>Elige tu ambiente y respira.</p></div>", unsafe_allow_html=True)

ambiente = st.selectbox("Selecciona un ambiente:", list(ambientes.keys()))

data = ambientes[ambiente]
set_bg(data["bg"])

# -------- VISUAL DISPLAY --------
st.markdown(f"""
<div class="control-box">
<h2>{ambiente}</h2>
<p><b>Luz:</b> {data['luz']}</p>
<p><b>Temperatura:</b> {data['temperatura']}</p>
<p><b>Humidificador:</b> {data['humidificador']}</p>
</div>
""", unsafe_allow_html=True)

# -------- MUSIC PLAYER --------
st.subheader("🎧 Paisaje Sonoro")
st_player(data["musica"])

# -------- PERSONAL CONTROL --------
st.markdown("<h2>🎨 Ajuste Personalizado</h2>", unsafe_allow_html=True)

luz = st.color_picker("Color de la luz", "#81c784")
temp = st.slider("Temperatura (°C)", 15, 35, 22)
hum = st.selectbox("Nivel de humidificador:", ["Apagado", "Bajo", "Medio", "Alto"])

st.markdown(f"""
<div class="control-box">
<h3>Estado Actual</h3>
<p><b>Luz:</b> {luz}</p>
<p><b>Temperatura:</b> {temp}°C</p>
<p><b>Humidificador:</b> {hum}</p>
<p style="opacity:0.6;">Listo para sincronizar con Arduino / Maqueta.</p>
</div>
""", unsafe_allow_html=True)
