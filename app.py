import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Rugby Score Pro", page_icon="🏉", layout="wide")

# 2. Style CSS (Bloc simplifié)
st.markdown("""
<style>
    .stApp { background-color: #0E1117; }
    h2 { color: #94A3B8 !important; text-align: center; }
    h1 { color: white !important; text-align: center; }
    [data-testid="stMetricValue"] { font-size: 5rem !important; color: #FB923C !important; text-align: center; }
    div.stButton > button { 
        width: 100%; 
        border-radius: 10px; 
        background-color: #1F2937; 
        color: white; 
        border: 1px solid #FB923C;
    }
</style>
""", unsafe_allow_html=True)

# 3. Initialisation du Score
if 'score_a' not in st.session_state: st.session_state.score_a = 0
if 'score_b' not in st.session_state: st.session_state.score_b = 0
if 'essais_a' not in st.session_state: st.session_state.essais_a = 0
if 'essais_b' not in st.session_state: st.session_state.essais_b = 0

# 4. Titre
st.markdown("<h1>🏉 SCOREBOARD PRO</h1>", unsafe_allow_html=True)

# 5. Interface de match
col1, mid, col2 = st.columns([2, 0.5, 2])

with col1:
    st.markdown("<h2>DOMICILE</h2>", unsafe_allow_html=True)
    st.metric("", st.session_state.score_a)
    c1, c2, c3 = st.columns(3)
    if c
