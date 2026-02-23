import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE FORCÉ (DARK MODE & TEXTE SÉLECTIONNÉ VISIBLE) ---
st.markdown("""
    <style>
    /* Fond principal */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Correction Sidebar : Fond sombre et texte blanc */
    [data-testid="stSidebar"] { background-color: #161b22 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    
    /* FORCE LA VISIBILITÉ DU TEXTE DANS LE SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #d62828 !important;
    }

    /* Force la couleur du texte à l'intérieur de la boîte quand c'est sélectionné */
    div[data-testid="stSelectbox"] div div {
        color: white !important;
    }

    /* Style des options quand on clique */
    ul[role="listbox"] li {
        color: black !important;
        background-color: white !important;
    }
    
    /* Bouton Rouge Rugby */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 8px; 
        height: 3em; 
        font-weight: bold; 
        border: none; 
    }
    
    /* Boite d'excuse */
    .excuse-box { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #d62828; 
        color: #f0f6fc; 
        font-style: italic; 
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Le 'Droit de Retrait' Rugby")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    # Utilisation de l'index pour s'assurer que l'état reste propre
    cat = st.selectbox("Type d'excuse", ["Solidarité", "Santé", "Transports", "Club"])
    h_prevu = st.slider("Heure de retour annoncée", 0, 23, 19)
    res = st.select_slider("Ambiance Match", options=["Déroute", "Moyen", "Victoire"])

# --- LA MINE D'OR DES EXCUSES (10 par catégorie) ---
EXCUSES = {
    "Solidarité": [
        "un petit nouveau craque après le match, on fait bloc pour lui remonter le moral, je peux pas le laisser comme ça.",
        "le talonneur s'est fait larguer par SMS, il est en larmes. On fait une réunion de crise, c'est l'esprit du club.",
        "le capitaine est vraiment pas bien moralement, on reste avec lui pour s'assurer qu'il ne rentre pas seul.",
        "un des gars a de gros soucis perso, on fait un cercle de parole dans le vestiaire. C'est sacré.",
        "le soigneur du club vient d'apprendre une mauvaise nouvelle, on reste tous avec lui pour le soutenir.",
        "un coéquipier a perdu ses clés et son portefeuille, on ratisse tout le complexe à 15 pour l'aider.",
        "le pilier droit est en pleine dé
