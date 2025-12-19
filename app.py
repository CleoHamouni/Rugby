import streamlit as st

# 1. Configuration de la page
st.set_page_config(page_title="Rugby Score Pro", page_icon="🏉", layout="wide")

# 2. Injection de CSS personnalisé pour un look "Stade de Nuit"
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Personnalisation des boutons */
    div.stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background-color: #1F2937;
        color: #FB923C !important; /* Orange électrique */
        border: 1px solid #FB923C !important;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    div.stButton > button:hover {
        background-color: #FB923C !important;
        color: #1F2937 !important;
        box-shadow: 0 0 15px #FB923C;
    }

    /* Style des métriques de score */
    [data-testid="stMetricValue"] {
        font-size: 5rem !important;
        color: #FFFFFF !important;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
    }

    /* Style des titres de colonnes */
    h2 {
        color: #94A3B8 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        text-align: center;
    }

    /* Masquer les éléments Streamlit superflus */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Style des boites de bonus */
    .status-box {
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #334155;
        background-color: #1E293B;
        text-align: center;
    }
    </style>
