import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    div[data-baseweb="select"] > div { background-color: #262730 !important; color: white !important; border: 1px solid #d62828 !important; }
    div[data-testid="stSelectbox"] div div { color: white !important; }
    .stButton>button { width: 100%; background-color: #d62828 !important; color: white !important; border-radius: 8px; height: 4em; font-weight: bold; border: none; font-size: 20px; }
    .excuse-box { background-color: #1c2128; padding: 20px; border-radius: 10px; border-left: 6px solid #d62828; color: #f0f6fc; font-style: italic; font-size: 1.1em; }
    label { color: white !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Third Time")

# --- FORMULAIRE ---
st.subheader("1. Configure ton excuse")
col_a, col_b = st.columns(2)
with col_a:
    cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
    ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
with col_b:
    h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
    res = st.selectbox("Ambiance :", ["Défaite", "Nul", "Victoire"])

# --- BASE DE DONNÉES (30 PAR CATÉGORIE) ---
E = {
    "Solidarité": [
        "un petit nouveau craque après le match, on fait bloc.", "le talonneur s'est fait larguer, il est en larmes.",
        "le capitaine est pas bien, on reste pour lui.", "un gars a de gros soucis perso, cercle de parole.",
        "le soigneur a une mauvaise nouvelle, on le soutient.", "un pote a perdu ses clés et son tel, on cherche.",
        "le pilier est en détresse, on lui change les idées.", "on accompagne un jeune qui a eu une altercation.",
        "le 9 est en plein burn-out, il a craqué.", "une légende du club est là et pas bien.",
        "le deuxième ligne a appris un décès, on l'entoure.", "un gars a peur de rentrer seul après sa boulette.",
        "on fait une haie d'honneur pour un départ imprévu.", "le kiné a besoin de bras pour porter un gars.",
        "le 15 est en crise de nerfs, on calme le jeu.", "on discute avec le petit nouveau qui veut arrêter.",
        "un ancien du club fait un malaise moral, on reste.", "le 13 a besoin de parler, il est au fond du trou.",
        "on soutient le coach qui est très marqué par le match.", "un coéquipier n'a plus de batterie et de voiture.",
        "le 7 est en plein doute sur son niveau, débrief.", "on gère un conflit qui a éclaté dans les douches.",
        "le 8 est coincé au club sans solution de retour.", "on reste pour soutenir le bénévole qui est seul.",
        "un gars est effondré suite à une mauvaise nouvelle perso.", "on fait le point avec le capitaine qui veut démissionner.",
        "le 11 a besoin qu'on l'écoute, il est pas bien du tout.", "on rassure un gars qui s'est fait chauffer dehors.",
        "le 6 est très secoué par son tampon, on surveille.", "on attend que le calme revienne pour un gars nerveux."
    ],
    "Santé": [
        "un pote a pris un choc. On attend le médecin.", "grosse blessure pour un pote, suspicion fracture.",
        "le soigneur me demande de surveiller un malaise.", "un gars s'est ouvert l'arcade, c'est moche.",
        "le demi de mêlée est tombé dans les pommes.", "suspicion de commotion pour le 10, désorienté.",
        "un joueur s'est déboîté l'épaule, ambulance.", "réaction allergique d'un pote, on surveille.",
        "le 15 s'est tordu la cheville dans l'escalier.", "on attend les pompiers pour un gars d'en face.",
        "un gars s'est fait mal au dos, on le bouge pas.", "le 12 a une grosse plaie qui ne s'arrête pas.",
        "un coéquipier respire mal, on attend le doc.", "grosse entorse pour le 2, on l'aide à béquiller.",
        "un gars s'est pris un doigt dans l'oeil, urgences.", "le 4 est sonné, on lui met de la glace.",
        "malaise vagal dans les douches pour un remplaçant.", "le 5 s'est bloqué les cervicales, on gère.",
        "un joueur a une crampe géante qui ne passe pas.", "on surveille un gars qui a eu
