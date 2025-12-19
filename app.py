import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Rugby Score Pro", page_icon="🏉", layout="wide")

# 2. Injection de CSS personnalisé pour le look unique
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Personnalisation des boutons */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #1F2937;
        color: #FB923C; /* Orange électrique */
        border: 1px solid #FB923C;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        background-color: #FB923C;
        color: #1F2937;
        box-shadow: 0 0 15px #FB923C;
    }

    /* Style des métriques de score */
    [data-testid="stMetricValue"] {
        font-size: 5rem !important;
        color: #FFFFFF !important;
        font-family: 'Courier New', Courier, monospace;
    }

    /* Style des titres de colonnes */
    h2 {
        color: #94A3B8 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }

    /* Masquer le menu Streamlit pour faire plus "App" */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Titre et Header
st.markdown("<h1 style='text-align: center; color: white;'>🏉 SCOREBOARD PRO</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #94A3B8;'>Gestion de match en temps réel</p>", unsafe_allow_html=True)

# 4. Initialisation du Score (Session State)
if 'score_a' not in st.session_state: st.session_state.score_a = 0
if 'score_b' not in st.session_state: st.session_state.score_b = 0
if 'essais_a' not in st.session_state: st.session_state.essais_a = 0
if 'essais_b' not in st.session_state: st.session_state.essais_b = 0

# 5. Mise en page principale
col1, mid_spacer, col2 = st.columns([2, 0.5, 2])

with col1:
    st.header("DOMICILE")
    st.metric("", st.session_state.score_a)
    
    # Boutons d'action
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("ESSAI +5", key="a1"):
            st.session_state.score_a += 5
            st.session_state.essais_a += 1
    with c2:
        if st.button("TR +2", key="a2"):
            st.session_state.score_a += 2
    with c3:
        if st.button("PÉN +3", key="a3"):
            st.session_state.score_a += 3

with col2:
    st.header("EXTÉRIEUR")
    st.metric("", st.session_state.score_b)
    
    c4, c5, c6 = st.columns(3)
    with c4:
        if st.button("ESSAI +5", key="b1"):
            st.session_state.score_b += 5
            st.session_state.essais_b += 1
    with c5:
        if st.button("TR +2", key="b2"):
            st.session_state.score_b += 2
    with c6:
        if st.button("PÉN +3", key="b3"):
            st.session_state.score_b += 3

st.divider()

# 6. Analyse des Bonus
st.markdown("<h3 style='color: #FB923C;'>🏆
