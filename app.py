import streamlit as st

# -------------------------
# CONFIG
# -------------------------
st.set_page_config(
    page_title="Portafolio",
    page_icon="✨",
    layout="wide"
)

# -------------------------
# CSS
# -------------------------
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# -------------------------
# SIDEBAR
# -------------------------
st.sidebar.title("✨ Mi mundo")

menu = st.sidebar.radio(
    "",
    ["Inicio", "Proyectos", "Proceso", "Galería", "Contacto"]
)

st.sidebar.markdown("---")
st.sidebar.write("Hecho con amor 💖")

# -------------------------
# HERO
# -------------------------
def hero():
    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("# ✨ Mi Portafolio")
        st.markdown("### Diseño, emoción y proceso")
        st.write("""
        Este espacio reúne mis proyectos, exploraciones visuales
        y procesos creativos.
        """)

    with col2:
        st.image("assets/portada.png", use_container_width=True)

# -------------------------
# INICIO
# -------------------------
if menu == "Inicio":
    hero()

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🎨 Creatividad")
        st.write("Exploración visual y emocional.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 💻 Proyectos")
        st.write("Interfaces, ideas y soluciones.")
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🧠 Proceso")
        st.write("Pensamiento detrás del diseño.")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# PROYECTOS
# -------------------------
elif menu == "Proyectos":
    st.markdown("## 💻 Proyectos destacados")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("assets/proyecto1.png", use_container_width=True)
        st.markdown("### Proyecto 1")
        st.write("Descripción breve del proyecto.")
        st.link_button("Ver más", "https://tu-link.com")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.image("assets/proyecto2.png", use_container_width=True)
        st.markdown("### Proyecto 2")
        st.write("Descripción breve del proyecto.")
        st.link_button("Ver más", "https://tu-link.com")
        st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# PROCESO
# -------------------------
elif menu == "Proceso":
    st.markdown("## 🎨 Proceso creativo")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("assets/proceso1.png", use_container_width=True)
    st.write("""
    Aquí muestro cómo evolucionan mis ideas:
    desde bocetos hasta resultados finales.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------
# GALERÍA
# -------------------------
elif menu == "Galería":
    st.markdown("## 🖼️ Galería visual")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("assets/img1.png", use_container_width=True)
        st.image("assets/img2.png", use_container_width=True)

    with col2:
        st.image("assets/img3.png", use_container_width=True)
        st.image("assets/img4.png", use_container_width=True)

    with col3:
        st.image("assets/img5.png", use_container_width=True)
        st.image("assets/img6.png", use_container_width=True)

# -------------------------
# CONTACTO
# -------------------------
elif menu == "Contacto":
    st.markdown("## 📩 Contacto")

    st.write("Puedes encontrarme aquí:")

    col1, col2 = st.columns(2)

    with col1:
        st.link_button("Instagram", "https://instagram.com")

    with col2:
        st.link_button("Correo", "mailto:tuemail@gmail.com")
