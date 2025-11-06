import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="Espacio Zen Multimodal", page_icon="🌿", layout="wide")

def save_command(cmd):
    with open("comando.txt", "w") as f:
        f.write(cmd)

# ------- DEFINICIÓN DE AMBIENTES -------
# Formato del comando es: color_hex,temperatura,humidificador
ambientes = {
    "🌴 Selva (Automático)": {
        "bg": "https://images.unsplash.com/photo-1501785888041-af3ef285b470",
        "musica": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "comando": "#00AA55,20,Alto",  # Luz verde, temp fresca, humidificador ON
        "editable": False
    },
    "🏜️ Desierto (Automático)": {
        "bg": "https://images.unsplash.com/photo-1508264165352-258a6f039317",
        "musica": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "comando": "#D29944,30,Bajo",  # Luz ámbar, temp cálida, humidificador OFF
        "editable": False
    },
    "🕯️ Zen Personalizable": {
        "bg": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e",
        "musica": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "editable": True
    }
}

# ------- UI PRINCIPAL -------
st.title("🌿 ESPACIO DE RELAJACIÓN MULTIMODAL")
st.write("Selecciona el ambiente que deseas experimentar:")

ambiente = st.selectbox("", ambientes.keys())
data = ambientes[ambiente]

# Música dinámica según ambiente
st_player(data["musica"])

# Fondo dinámico
st.markdown(f"""
<style>
.stApp {{
    background-image: url("{data['bg']}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}
</style>
""", unsafe_allow_html=True)

# ------- SI EL AMBIENTE ES AUTOMÁTICO -------
if not data["editable"]:
    st.subheader("🌱 Ambiente Automático")
    
    color, temperatura, humidificador = data["comando"].split(",")

    st.markdown(f"""
    **Luz:** {color}  
    **Temperatura:** {temperatura} °C  
    **Humidificador:** {humidificador}
    """)

    st.write("Esta configuración está diseñada para mantener la atmósfera original.")

    if st.button("✨ Activar Ambiente"):
        save_command(data["comando"])
        st.success("Ambiente enviado a la maqueta ✅")

# ------- SI ES PERSONALIZABLE -------
else:
    st.subheader("🎨 Personalizar Ambiente Zen")

    luz = st.color_picker("Color de la luz ambiente", "#ffffff")
    temp = st.slider("Temperatura (°C)", 18, 35, 24)
    hum = st.selectbox("Humidificador (LED):", ["Apagado", "Alto"])

    if st.button("💾 Enviar a la Maqueta"):
        comando = f"{luz},{temp},{hum}"
        save_command(comando)
        st.success("Configuración enviada ✅")
