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
    "le demi de mêlée est tombé dans les pommes, on attend les secours.",
    "suspicion de commotion pour le 10, il est totalement désorienté.",
    "un joueur s'est déboîté l'épaule, on attend l'ambulance ici.",
    "réaction allergique d'un pote, on surveille que ça n'empire pas.",
    "le 15 s'est tordu la cheville dans l'escalier, je l'aide.",
    "on attend les pompiers pour un gars de l'autre équipe, je reste."
]
E["Transports"] = [
    "c'est la galère totale dans le métro, incident voyageur bloqué.",
    "plus aucun métro (colis suspect). Je cherche un bus blindé.",
    "panne de signalisation majeure, rames à l'arrêt en tunnel.",
    "grève surprise sur le réseau, trafic nul. Uber est hors de prix.",
    "tunnel fermé par la police, quartier bouclé, métro inaccessible.",
    "problème électrique, bloqué dans une rame entre deux stations.",
    "mon pass Navigo est en opposition, je galère au guichet fermé.",
    "gros malaise voyageur dans mon wagon, le train est immobilisé.",
    "signal d'alarme tiré trois fois, on attend la sécurité.",
    "une rame est en panne devant, on doit reculer. C'est l'enfer."
]
E["Club"] = [
    f"le coach a verrouillé la porte. Vu la {res}, débrief obligatoire.",
    "on est en plein débrief vidéo sauvage. Si je pars, je saute mardi.",
    "le président fait un discours interminable pour les sponsors.",
    "corvée de réception de l'équipe adverse. Je peux pas m'esquiver.",
    "l'arbitre explique ses choix au bar, obligation d'être présent.",
    "réunion imprévue sur l'organisation du tournoi de fin d'année.",
    "on doit tout ranger et nettoyer, le capitaine bloque les sorties.",
    "le club fête une légende locale, partir serait très mal vu.",
    "problème de licence pour mardi, on doit signer des papiers.",
    "le staff nous retient pour une annonce sur le voyage de fin d'année."
]

# --- BOUTON GÉNÉRER ---
st.markdown("---")
if st.button("🚀 GÉNÉRER L'EXCUSE"):
    msg = random.choice(E[cat])
    pref = f"Je sais que je devais être là pour {h_prevu}h mais "
    st.markdown("### 📱 Message prêt :")
    st.markdown(f"<div class='excuse-box'>« {pref}{msg} »</div>", unsafe_allow_html=True)
    st.info("💡 Copie le texte et passe en mode avion !")
