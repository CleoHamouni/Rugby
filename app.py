import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE FORCÉ (DARK MODE & TEXTE LISIBLE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* Force la visibilité du texte dans les menus déroulants sur mobile */
    div[data-baseweb="select"] > div {
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #d62828 !important;
    }
    
    /* Texte des options */
    div[data-testid="stSelectbox"] div div { color: white !important; }

    .stButton>button { 
        width: 100%; background-color: #d62828 !important; 
        color: white !important; border-radius: 8px; 
        height: 4em; font-weight: bold; border: none; font-size: 20px;
    }
    .excuse-box { 
        background-color: #1c2128; padding: 20px; 
        border-radius: 10px; border-left: 6px solid #d62828; 
        color: #f0f6fc; font-style: italic; font-size: 1.2em;
    }
    label { color: white !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Third Time")
st.write("Générateur d'excuses spécial Rugby.")

# --- FORMULAIRE DIRECTEMENT SUR LA PAGE ---
st.subheader("1. Choisis ton angle d'attaque")
cat = st.selectbox("Catégorie d'excuse :", ["Solidarité", "Santé", "Transports", "Club"])

col1, col2 = st.columns(2)
with col1:
    h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
with col2:
    res = st.selectbox("Ambiance :", ["Défaite", "Nul", "Victoire"])

# --- LES EXCUSES ---
E = {}
E["Solidarité"] = [
    "un petit nouveau craque, on fait bloc pour lui remonter le moral.",
    "le talonneur s'est fait larguer par SMS, il est en larmes au club.",
    "le capitaine est pas bien, on reste pour qu'il ne rentre pas seul.",
    "un des gars a de gros soucis perso, on fait un cercle de parole.",
    "le soigneur a une mauvaise nouvelle, on reste tous avec lui.",
    "un pote a perdu ses clés et son tel, on ratisse tout le complexe.",
    "le pilier est en détresse à cause du boulot, on lui change les idées.",
    "on accompagne un jeune qui a eu une altercation après le match.",
    "le 9 est en plein burn-out, il a craqué. On ne le laisse pas seul.",
    "une légende du club est là et pas bien, on reste pour l'écouter."
]
E["Santé"] = [
    "un pote a pris un énorme choc. On attend le médecin du club.",
    "grosse blessure pour un pote, on suspecte une fracture. J'aide.",
    "le soigneur me demande de surveiller un gars après un malaise.",
    "un gars s'est ouvert l'arcade, c'est moche. Je l'aide aux soins.",
    "le demi de mêlée est tombé dans les pommes, on attend les
