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

st.title("🏉 Third Time - Mode Légende")

# --- FORMULAIRE ---
st.subheader("1. Configuration")
cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
res = st.selectbox("Résultat du match :", ["Victoire", "Défaite", "Nul"])

# --- LE MOTEUR DE BRIQUES ---
def generer_phrase(categorie, ton_choisi, resultat, heure):
    
    # 1. LES INTROS (Selon le ton)
    intros = {
        "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Je fais au plus vite mais pour {h}h c'est mort,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
        "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,", "Je vais encore arriver une plombe après {h}h,"],
        "Factuel": ["Bloqué.", "Retard prévu.", "Je ne serai pas là pour {h}h.", "Coincé au club.", "Changement de programme."]
    }

    # 2. LES ACTIONS (Selon la catégorie)
    actions = {
        "Solidarité": ["un petit nouveau est en larmes au vestiaire", "le talonneur vient de se faire larguer", "le capitaine a un énorme coup de mou", "un gars a de gros soucis perso et on fait bloc", "le 9 est en plein burn-out moral"],
        "Santé": ["un pote a pris un énorme choc sur le terrain", "un coéquipier a fait un malaise après l'effort", "on attend l'ambulance pour le pilier", "le soigneur me demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade et je l'aide"],
        "Transports": ["le métro est totalement à l'arrêt", "il y a un colis suspect dans ma rame", "une panne de signalisation bloque tout", "un incident voyageur paralyse la ligne", "le trafic est nul à cause d'une grève surprise"],
        "Club": ["le coach nous a enfermés pour un débrief musclé", "le président fait un discours interminable", "on est de corvée de rangement pour l'équipe", "l'arbitre explique ses choix au bar", "on est bloqués pour une réunion administrative"]
    }

    # 3. LES COMPLÉMENTS (Selon le résultat ou aléatoire)
    complements = [
        "on ne peut vraiment pas le laisser seul.",
        "tout le groupe est obligé de rester.",
        "on fait bloc, c'est l'esprit de l'équipe.",
        "je rentre dès que la situation se débloque.",
        "le staff interdit à tout le monde de partir."
    ]
    
    if resultat == "Victoire":
        complements.append("faut dire que la gagne a fait monter l'émotion.")
        complements.append("on doit rester pour la remise des récompenses.")
    elif resultat == "Défaite":
        complements.append("vu le score, l'ambiance est vraiment pesante.")
        complements.append("le coach veut une mise au point immédiate.")

    # ASSEMBLAGE ALÉATOIRE
    i = random.choice(intros[ton_choisi]).format(h=heure)
    a = random.choice(actions[categorie])
    c = random.choice(complements)

    return f"{i} {a}, {c}"

# --- BOUTON ---
st.markdown("---")
if st.button("🚀 GÉNÉRER UNE EXCUSE PARMI 1000+"):
    message_final = generer_phrase(cat, ton, res, h_prevu)
    
    st.markdown("### 📱 Message prêt :")
    st.markdown(f"<div class='excuse-box'>« {message_final} »</div>", unsafe_allow_html=True)
    st.info("💡 Le moteur mélange les briques pour que chaque message soit unique.")
