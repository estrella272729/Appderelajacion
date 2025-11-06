import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="Espacio Zen Multimodal", page_icon="🌿", layout="wide")

# --------- FONDOS PERSONALIZADOS ---------
def set_bg(url):
    st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
    }}
    h1, h2, h3, label {{ color: #ffffff; text-shadow: 0 0 10px #00000055; }}
    .glass {{
        background: rgba(255,255,255,0.18);
        padding: 28px;
        border-radius: 22px;
        backdrop-filter: blur(8px);
        box-shadow: 0 8px 25px rgba(0,0,0,0.30);
        margin-top: 20px;
        animation: fadein 0.8s ease;
    }}
    @keyframes fadein {{
      from {{ opacity: 0; transform: translateY(10px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}
    .stButton>button {{
        background: rgba(255,255,255,0.35) !important;
        backdrop-filter: blur(6px);
        border: none !important;
        font-size: 18px;
        border-radius: 18px;
        padding: 14px 30px;
        color: white !important;
        transition: 0.3s;
    }}
    .stButton>button:hover {{
        background: rgba(255,255,255,0.7) !important;
        color: #1b1b1b !important;
        transform: scale(1.05);
    }}
    </style>
    """, unsafe_allow_html=True)


# --------- AMBIENTES ---------
ambientes = {
    "🌴 Selva (Fijo)": {
        "bg": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "musica": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "info": "Luz verde, humedad alta, sonido fauna natural",
        "editable": False
    },
    "🏜️ Desierto (Fijo)": {
        "bg": "https://images.unsplash.com/photo-1508264165352-258a6f039317",
        "musica": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "info": "Luz ámbar cálida, calor suave, viento desértico",
        "editable": False
    },
    "🕯️ Zen (Personalizable)": {
        "bg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "musica": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "info": "Ambiente minimal relajante para personalizar",
        "editable": True
    }
}

# --------- UI PRINCIPAL ---------
st.markdown("<h1 style='text-align: center;'>🌿 ESPACIO DE RELAJACIÓN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Elige un ambiente para comenzar...</p>", unsafe_allow_html=True)

ambiente = st.selectbox("", list(ambientes.keys()))
data = ambientes[ambiente]
set_bg(data["bg"])

st.markdown(f"""
<div class="glass">
<h2>{ambiente}</h2>
<p>{data['info']}</p>
</div>
""", unsafe_allow_html=True)

# --- MUSIC PLAYER ---
st.subheader("🎧 Paisaje Sonoro")
st_player(data["musica"])


# ------- SOLO PERSONALIZACIÓN EN AMBIENTE 3 -------
if data["editable"]:
    st.markdown("<h2>🎨 Personalizar Ambiente Zen</h2>", unsafe_allow_html=True)

    luz = st.color_picker("Color de la luz", "#f7f5e7")
    temp = st.slider("Temperatura (°C)", 18, 35, 23)
    hum = st.selectbox("Nivel de humidificador", ["Apagado", "Bajo", "Medio", "Alto"])

    st.markdown("### 🎼 Elige tu música")
    musica_op = st.radio("Tipo de música:", ["YouTube", "Archivo (MP3/WAV)"])

    if musica_op == "YouTube":
        nueva_musica = st.text_input("Pega enlace de YouTube:")
        if nueva_musica:
            st_player(nueva_musica)

    else:
        archivo = st.file_uploader("Sube tu audio", type=["mp3", "wav"])
        if archivo:
            st.audio(archivo)

    st.markdown(f"""
    <div class="glass">
    <h3>🧘 Estado Actual</h3>
    <p><b>Luz:</b> {luz}</p>
    <p><b>Temperatura:</b> {temp} °C</p>
    <p><b>Humidificador:</b> {hum}</p>
    <p style="opacity:0.7;">Listo para conexión con Arduino / maqueta.</p>
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("<p style='opacity:0.8;'>🔒 Este ambiente está bloqueado para preservar su atmósfera original.</p>", unsafe_allow_html=True)
