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
        "le pilier droit est en pleine détresse psychologique à cause du boulot, on essaie de lui changer les idées.",
        "on accompagne un des jeunes qui a eu une altercation pour s'assurer qu'il rentre calmement.",
        "le 9 est en plein burn-out, il a craqué sous la douche. On ne peut pas le laisser partir dans cet état.",
        "une légende du club est passée et elle est pas bien, on reste tous pour lui rendre hommage et l'écouter."
    ],
    "Santé": [
        "un de mes potes a pris un énorme choc. On attend le médecin du club, je reste à côté pour le surveiller.",
        "grosse blessure pour un coéquipier, on suspecte une fracture. Je l'accompagne aux urgences pour ne pas qu'il soit seul.",
        "le soigneur m'a demandé de surveiller un gars qui a fait un malaise après l'effort. Je reste tant qu'il n'est pas stable.",
        "un gars s'est ouvert l'arcade, c'est assez moche. On lui fait les premiers soins, je l'aide.",
        "le demi de mêlée est tombé dans les pommes, on attend de voir s'il faut appeler les pompiers.",
        "suspicion de commotion pour le 10, il est totalement désorienté. On a ordre de vérifier qu'il ne s'endort pas.",
        "un joueur s'est déboîté l'épaule, on attend l'ambulance, je reste pour le rassurer.",
        "réaction allergique d'un pote après le match, on surveille que son état ne s'aggrave pas.",
        "le 15 s'est tordu la cheville dans les escaliers du vestiaire, je l'aide à mettre de la glace et à marcher.",
        "on attend les pompiers pour un gars de l'équipe adverse qui a fait un arrêt respiratoire, je reste en soutien."
    ],
    "Transports": [
        "c'est la galère totale dans le métro, incident voyageur et tout est bloqué. Je suis coincé sur le quai.",
        "plus aucun métro ne circule sur ma ligne (colis suspect). Je cherche un bus mais c'est blindé.",
        "panne de signalisation majeure, les rames sont à l'arrêt en plein tunnel. Aucune idée de l'heure de reprise.",
        "grève surprise sur le réseau, trafic quasi nul. Je tente de trouver un Uber mais c'est hors de prix.",
        "tunnel fermé pour intervention de police, quartier bouclé, impossible d'accéder au métro.",
        "problème d'alimentation électrique, bloqué dans une rame entre deux stations. Interdiction de descendre.",
        "mon pass Navigo est passé en opposition, je galère avec le guichet qui est fermé.",
        "gros malaise voyageur dans mon wagon, le train est immobilisé à quai le temps que les secours arrivent.",
        "signal d'alarme tiré trois fois de suite, les conducteurs attendent la sécurité ferroviaire.",
        "une rame est tombée en panne devant nous, on doit reculer jusqu'à la station précédente, c'est l'enfer."
    ],
    "Club": [
        f"le coach a verrouillé la porte. Vu le match ({res}), débriefing musclé obligatoire. Personne ne sort.",
        "on est en plein débrief vidéo sauvage. Si je pars maintenant, je suis sanctionné mardi.",
        "le président fait un discours interminable pour les nouveaux sponsors. Obligé de rester pour la cohésion.",
        "tradition de club : je suis de corvée pour la réception de l'équipe adverse. Je ne peux pas m'esquiver.",
        "l'arbitre est resté boire un verre pour expliquer ses décisions, obligation d'être présent.",
        "réunion imprévue sur l'organisation du tournoi de fin d'année, ma présence est requise.",
        "on doit ranger tout le matériel et nettoyer le vestiaire, le capitaine bloque les sorties.",
        "le club fête l'anniversaire d'une légende locale, partir maintenant serait très mal vu.",
        "il y a un problème de licence pour le prochain match, on doit tous signer des papiers officiels ce soir.",
        "le staff nous retient pour une annonce importante concernant le voyage de fin de saison."
    ]
}

# --- AFFICHAGE ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    msg = random.choice(EXCUSES[cat])
    
    # Construction du message personnalisé
    prefixe = f"Je sais que je devais être là pour {h_prevu}h mais "
    
    st.markdown("### 📱 Message prêt à envoyer :")
    st.markdown(f"<div class='excuse-box'>« {prefixe}{msg} »</div>", unsafe_allow_html=True)
    
    st.info("💡 **Conseil :** Active le mode avion juste après l'envoi pour justifier le manque de réponse.")
