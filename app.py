import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE FORCÉ (DARK MODE & SIDEBAR LISIBLE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 8px; 
        height: 3em; 
        font-size: 18px; 
        font-weight: bold; 
        border: none;
    }
    .excuse-box { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #d62828; 
        color: #f0f6fc; 
        font-style: italic; 
        font-size: 1.1em;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Le 'Droit de Retrait' Rugby")
st.write("Générateur d'excuses de terrain.")

# --- FORMULAIRE DANS LA SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    # Choix de la catégorie
    categorie = st.selectbox("Type d'excuse", [
        "Solidarité (Un pote va mal)", 
        "Santé / Blessure (Urgence)",
        "Transports (Métro/RER)", 
        "Débrief / Club (Obligation)"
    ])
    
    heure = st.slider("Heure prévue de retour", 0, 23, 20)
    
    match_statut = st.select_slider("Résultat du match", options=["Défaite", "Nul", "Victoire"])

# --- MOTEUR D'EXCUSES PAR CATÉGORIE ---
def generer_excuse(cat, h, res):
    
    if cat == "Solidarité (Un pote va mal)":
        excuses =
