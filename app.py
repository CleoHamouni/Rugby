import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE FORCÉ ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; }
    [data-testid="stSidebar"] * { color: white !important; }
    .stButton>button { width: 100%; background-color: #d62828 !important; color: white !important; border-radius: 8px; font-weight: bold; border: none; height: 3em; }
    .excuse-box { background-color: #1c2128; padding: 20px; border-radius: 10px; border-left: 6px solid #d62828; color: #f0f6fc; font-style: italic; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Le 'Droit de Retrait' Rugby")

# --- SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    cat = st.selectbox("Type d'excuse", ["Solidarité", "Santé", "Transports", "Club"])
    h = st.slider("Heure", 0, 23, 20)
    res = st.select_slider("Match", options=["Défaite", "Nul", "Victoire"])

# --- LES EXCUSES (Format ultra-simple pour éviter les erreurs) ---
EXCUSES = {
    "Solidarité": [
        "Un petit nouveau craque après le match, on fait bloc pour lui remonter le moral, je peux pas le laisser comme ça.",
        "Le talonneur s'est fait larguer par SMS, il est en larmes. On fait une réunion de crise, c'est l'esprit du club.",
        "Le capitaine est vraiment pas bien moralement, on reste avec lui pour s'assurer qu'il rentre pas seul.",
        "Un des gars a de gros soucis perso, on fait un cercle de parole dans le vestiaire. C'est sacré."
    ],
    "Santé": [
        "Un de mes potes a pris un énorme choc. On attend le médecin du club, je reste à côté de lui pour le surveiller.",
        "Grosse blessure pour un coéquipier, on suspecte une fracture. Je l'accompagne aux urgences pour ne pas qu'il soit seul.",
        "Le soigneur m'a demandé de surveiller un gars qui a fait un malaise après l'effort. Je reste tant qu'il n'est pas stable.",
        "Un gars s'est ouvert l'arcade, c'est assez moche. On lui fait les premiers soins, je l'aide."
    ],
    "Transports": [
        "C'est la galère totale dans le métro, incident voyageur et tout est bloqué. Je suis coincé sur le quai.",
        "Plus aucun métro ne circule sur ma ligne (colis suspect). Je cherche un bus mais c'est blindé.",
        "Panne de signalisation majeure, les rames sont à l'arrêt en plein tunnel. Aucune idée de l'heure de reprise.",
        "Grève surprise sur le réseau, trafic quasi nul. Je fais au plus vite mais c'est l'enfer."
    ],
    "Club": [
        f"Le coach a verrouillé la porte. Vu le match ({res}), débriefing musclé obligatoire. Personne ne sort.",
        "On est en plein débrief vidéo sauvage. Si je pars maintenant, je suis sanctionné mardi.",
        "Le président fait un discours interminable pour les nouveaux équipements. Obligé de rester pour la cohésion.",
        "Tradition de club : je dois gérer la réception de l'équipe adverse. Je ne peux pas m'esquiver."
    ]
}

# --- AFFICHAGE ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    # On pioche dans la liste choisie
    liste_choisie = EXCUSES[cat]
    msg = random.choice(liste_choisie)
    
    st.markdown("### 📱 Message prêt à envoyer :")
    st.markdown(f"<div class='excuse-box'>« {msg} »</div>", unsafe_allow_html=True)
    st.info("💡 **Conseil :** Ne réponds plus aux messages après l'envoi pour simuler l'impossibilité de communiquer.")
