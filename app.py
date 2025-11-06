# app.py
import streamlit as st
from streamlit_player import st_player

st.set_page_config(page_title="Espacio de Relajación", page_icon="🌙", layout="wide")

# ---------- Estilos Amanecer y Glass UI ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300;400;500;600&display=swap');

* { font-family: 'Quicksand', sans-serif; }

.stApp {
    animation: gradient 12s ease infinite;
    background: linear-gradient(135deg, #f8cdd8, #f7e5d9, #fdebd3, #f4d5dd);
    background-size: 400% 400%;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

.glass {
    background: rgba(255,255,255,0.35);
    backdrop-filter: blur(12px);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.18);
    margin-top: 18px;
}

.stButton>button {
    background: rgba(255,255,255,0.55) !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 12px 28px !important;
    font-size: 16px !important;
    color: #4b3d45 !important;
    transition: 0.25s;
}
.stButton>button:hover {
    background: rgba(255,255,255,0.85) !important;
    transform: scale(1.04);
}

label, p, h3, h2, h1 { color: #4b3d45 !important; }
.small-muted { opacity: 0.75; font-size: 14px; }

.breathe-wrap {
  display:flex; gap:28px; align-items:center; justify-content:center; flex-wrap:wrap;
}

/* Circle + instruction base - these keyframes are generated dynamically */
.breathe-card {
  width: 420px;
  max-width: 92%;
  padding: 22px;
  border-radius: 16px;
  background: rgba(255,255,255,0.22);
  backdrop-filter: blur(8px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.12);
  text-align:center;
}

.breathe-circle {
  width: 220px;
  height: 220px;
  border-radius: 50%;
  margin: 0 auto 16px auto;
  display:flex;
  align-items:center;
  justify-content:center;
  background: radial-gradient(circle at 30% 30%, rgba(255,255,255,0.6), rgba(255,255,255,0.12));
  box-shadow: inset 0 6px 18px rgba(255,255,255,0.25), 0 8px 30px rgba(0,0,0,0.12);
}

/* Instruction styles */
.inst { font-size: 22px; font-weight:600; opacity:0; transition:opacity .3s ease; }
.counter { font-size:28px; font-weight:700; margin-top:8px; }

/* Small helper column for presets */
.presets {
  min-width:260px;
  max-width:320px;
  padding:16px;
  border-radius:12px;
  background: rgba(255,255,255,0.18);
  backdrop-filter: blur(8px);
}

/* mobile adjustments */
@media(max-width:760px){
  .breathe-wrap { flex-direction:column; }
  .breathe-card { width: 96%; }
  .breathe-circle { width:170px; height:170px; }
}
</style>
""", unsafe_allow_html=True)


# ---------- Ambientes ----------
ambientes = {
    "🌴 Selva (Fijo)": {
        "musica": "https://www.youtube.com/watch?v=OdIJ2x3nxzQ",
        "descripcion": "Ambiente húmedo, sonidos de fauna, sensación de bosque vivo.",
        "editable": False
    },
    "🏜️ Desierto (Fijo)": {
        "musica": "https://www.youtube.com/watch?v=2OEL4P1Rz04",
        "descripcion": "Calor suave, viento tibio, melodías cálidas.",
        "editable": False
    },
    "🕯️ Zen (Personalizable)": {
        "musica": "https://www.youtube.com/watch?v=lFcSrYw-ARY",
        "descripcion": "Espacio para personalizar tu bienestar.",
        "editable": True
    }
}

# ---------- Interfaz ----------
st.markdown("<h1 style='text-align:center;'>🌙 ESPACIO DE RELAJACIÓN</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Respira profundo. Elige el ambiente que te acompañará.</p>", unsafe_allow_html=True)

ambiente = st.selectbox("", list(ambientes.keys()))
data = ambientes[ambiente]

# ----- Tarjeta de descripción -----
st.markdown(f"""
<div class="glass">
  <h2 style="margin-bottom:6px;">{ambiente}</h2>
  <p class="small-muted" style="margin-top:0;">{data["descripcion"]}</p>
</div>
""", unsafe_allow_html=True)

# ---- Música ----
st.subheader("🎧 Paisaje Sonoro")
st_player(data["musica"])

# ---- Zona central: guía de respiración y presets ----
st.markdown("<h2 style='margin-top:18px;'>🧘 Guía de respiración</h2>", unsafe_allow_html=True)
st.markdown("<p class='small-muted'>Sigue el círculo: inhala → aguanta → exhala. Personaliza tiempos o usa un preset.</p>", unsafe_allow_html=True)

col1, col2 = st.columns([2,1])

with col1:
    # Duraciones personalizables
    st.markdown("<div class='glass'>", unsafe_allow_html=True)
    st.write("**Duraciones (segundos)**")
    inhale = st.number_input("Inhalar (s)", min_value=1, max_value=20, value=4, step=1, key="inhale")
    hold = st.number_input("Retener (s)", min_value=0, max_value=20, value=2, step=1, key="hold")
    exhale = st.number_input("Exhalar (s)", min_value=1, max_value=30, value=6, step=1, key="exhale")
    loop = st.checkbox("Repetir en bucle", value=True)
    bell = st.checkbox("Campana al inicio de cada ciclo", value=True)
    start = st.button("▶ Iniciar guía de respiración")
    st.markdown("</div>", unsafe_allow_html=True)

    # If user starts, render the animated block with CSS keyframes computed
    if start:
        total = inhale + hold + exhale
        # percent marks
        p1 = (inhale / total) * 100
        p2 = ((inhale + hold) / total) * 100

        # Generate dynamic CSS for the animation using computed percentages and total duration.
        # The overall animation-duration must equal total (in seconds).
        dynamic_css = f"""
        <style>
        /* circle scaling */
        @keyframes breatheScale {{
          0% {{ transform: scale(0.72); }}
          {p1:.3f}% {{ transform: scale(1.12); }}
          {p2:.3f}% {{ transform: scale(1.12); }}
          100% {{ transform: scale(0.72); }}
        }}
        .breathe-circle {{
          animation: breatheScale {total}s ease-in-out {'infinite' if loop else '1'}; 
        }}

        /* instruction visibility */
        @keyframes instInhale {{ 0% {{opacity:0}}; {p1:.3f}% {{opacity:1}}; {p2:.3f}% {{opacity:0}}; 100%{{opacity:0}} }}
        @keyframes instHold {{ 0% {{opacity:0}}; {p1:.3f}% {{opacity:0}}; {p2:.3f}% {{opacity:1}}; 100%{{opacity:0}} }}
        @keyframes instExhale {{ 0% {{opacity:0}}; {p2:.3f}% {{opacity:0}}; 100%{{opacity:1}} }}

        .inst-inhale {{"animation": "instInhale {total}s linear {'infinite' if loop else '1'};"}}
        .inst-hold {{"animation": "instHold {total}s linear {'infinite' if loop else '1'};"}}
        .inst-exhale {{"animation": "instExhale {total}s linear {'infinite' if loop else '1'};"}}

        /* simple fading for counters to match each phase */
        </style>
        """

        # Build HTML block: circle + instructions + optional audio bell (small beep)
        bell_audio_html = ""
        if bell:
            # small subtle bell using base64 short beep? We'll use an embedded tiny sine via data URI is complex.
            # Instead include a short external mp3 bell from a permissive CDN (if network available).
            # Fallback: not play if blocked. Provide link to bell sound.
            bell_audio_html = """
            <audio id="breathe-bell" src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg"></audio>
            <script>
            // play bell at loop start using CSS animation iteration event not available; use setInterval fallback
            const total = %d * 1000;
            function playBell(){ 
              const a = document.getElementById('breathe-bell'); 
              if(a){ a.currentTime = 0; a.play().catch(()=>{}); }
            }
            // play immediately first time
            playBell();
            // schedule repeats each cycle
            const bellTimer = setInterval(playBell, total);
            // if not looping, clear after one iteration
            if(%s === false){
              setTimeout(()=> clearInterval(bellTimer), total + 200);
            }
            </script>
            """ % (total, 'true' if loop else 'false')

        # Instruction HTML: three spans that show/hide courtesy CSS animations
        breathe_html = f"""
        {dynamic_css}
        <div class="breathe-wrap">
          <div class="breathe-card">
            <div class="breathe-circle" id="breatheCircle"></div>
            <div class="inst inst-inhale">INHALA</div>
            <div class="inst inst-hold">SOSTÉN</div>
            <div class="inst inst-exhale">EXHALA</div>
            <div class="counter small-muted">Ciclo: {inhale}s • {hold}s • {exhale}s</div>
          </div>
        </div>
        {bell_audio_html}
        """

        st.components.v1.html(breathe_html, height=420, scrolling=False)

with col2:
    st.markdown("<div class='presets'>", unsafe_allow_html=True)
    st.markdown("**Presets rápidos**")
    if st.button("🟣 4-2-6 (Relajación clásica)"):
        st.experimental_rerun()  # to refresh inputs, we'll set via query state below
    if st.button("🔵 3-3-6 (Equilibrio)"):
        st.experimental_rerun()
    if st.button("🟢 5-2-5 (Profunda)"):
        st.experimental_rerun()

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("**Consejos**")
    st.markdown("<ul><li class='small-muted'>Siéntate cómodo/a.</li><li class='small-muted'>Usa auriculares si puedes.</li><li class='small-muted'>Sigue el ritmo del círculo.</li></ul>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ---- Personalizable Zen (música/file uploader) ----
if data["editable"]:
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("<h2>🎨 Personalizar Ambiente Zen</h2>", unsafe_allow_html=True)

    luz = st.color_picker("Color de luz ambiente", "#f8efe6")
    temp = st.slider("Temperatura (°C)", 16, 34, 23)
    hum = st.selectbox("Nivel de humidificador", ["Apagado", "Bajo", "Medio", "Alto"])

    st.markdown("### 🎼 Música Personalizada")
    tipo_musica = st.radio("Elige cómo reproducir tu sonido:", ["YouTube", "Archivo MP3/WAV"])

    if tipo_musica == "YouTube":
        link = st.text_input("Pega enlace de YouTube aquí:")
        if link:
            st_player(link)
    else:
        archivo = st.file_uploader("Sube tu audio", type=["mp3", "wav"])
        if archivo:
            st.audio(archivo)

    st.markdown(f"""
    <div class="glass" style="margin-top:14px;">
    <h3>🧘 Estado Actual</h3>
    <p class="small-muted"><b>Luz:</b> {luz}</p>
    <p class="small-muted"><b>Temperatura:</b> {temp} °C</p>
    <p class="small-muted"><b>Humidificador:</b> {hum}</p>
    <p class="small-muted">Listo para sincronizar con la maqueta o Arduino.</p>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("<p style='opacity:0.8;'>🔒 Este ambiente es fijo para mantener su esencia.</p>", unsafe_allow_html=True)

