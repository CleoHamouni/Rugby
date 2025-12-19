import streamlit as st

# 1. Configuration
st.set_page_config(page_title="Rugby Score Pro", layout="wide")

# 2. CSS Simple
st.markdown("""
<style>
    .stApp { background-color: #0E1117; color: white; }
    [data-testid="stMetricValue"] { color: #FB923C !important; }
</style>
""", unsafe_allow_html=True)

# 3. Initialisation
for key in ['score_a', 'score_b', 'essais_a', 'essais_b']:
    if key not in st.session_state:
        st.session_state[key] = 0

# 4. Titre
st.title("🏉 SCOREBOARD PRO")

# 5. Interface
col1, col2 = st.columns(2)

with col1:
    st.header("DOMICILE")
    st.metric("Score", st.session_state.score_a)
    if st.button("ESSAI +5", key="btn_a1"):
        st.session_state.score_a += 5
        st.session_state.essais_a += 1
        st.rerun()
    if st.button("TRANSFO +2", key="btn_a2"):
        st.session_state.score_a += 2
        st.rerun()
    if st.button("PÉNALITÉ +3", key="btn_a3"):
        st.session_state.score_a += 3
        st.rerun()

with col2:
    st.header("EXTÉRIEUR")
    st.metric("Score", st.session_state.score_b)
    if st.button("ESSAI +5", key="btn_b1"):
        st.session_state.score_b += 5
        st.session_state.essais_b += 1
        st.rerun()
