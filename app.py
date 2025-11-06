import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="Espacio Zen Multimodal", page_icon="🌿", layout="wide")

def save_command(cmd):
    with open("comando.txt", "w") as f:
        f.write(cmd)

ambientes = {
    "🌴 Selva": {
        "bg": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "musica": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "comando": "#00AA55,20,Alto",  # Luz verde + temp fresca + humidificador ON
        "editable": False
    },
    "🏜️ Desierto": {
        "bg": "https://images.unsplash.com/photo-1508264165352-258a6f039317",
        "musica": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "comando": "#D29944,30,Bajo",  # Luz cálida + temp media + humidificador OFF
        "editable": False
    },
    "🕯️ Zen Personalizable": {
        "bg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "musica": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "editable": True
    }
}

st.title("🌿 ESPACIO DE RELAJACIÓN MULTIMODAL")

ambiente = st.selectbox("Selecciona un ambiente:", ambientes.keys())
data = ambientes[ambiente]

st_player(data["musica"])

if data["editable"] == False:
    st.subheader("Modo automático ✨")
    st.write("Este ambiente tiene una configuración ya diseñada 🌱")
    if st.button("✨ Activar Ambiente"):
        save_command(data["comando"])
        st.success("Ambiente enviado a la maqueta ✅")

else:
    st.subheader("Modo personalizable 🎨")
    luz = st.color_picker("Color de la luz", "#ffffff")
    temp = st.slider("Temperatura (°C)", 18, 35, 24)
    hum = st.selectbox("Humidificador (LED):", ["Apagado", "Alto"])

    if st.button("💾 Enviar a la Maqueta"):
        comando = f"{luz},{temp},{hum}"
        save_command(comando)
        st.success("Configuración enviada ✅")
