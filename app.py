import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE COMPLET (FORCE LE DARK MODE ET LA SIDEBAR) ---
st.markdown("""
    <style>
    /* Fond principal */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Force la Sidebar en sombre et texte blanc */
    [data-testid="stSidebar"] {
        background-color: #161b22 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Bouton Rouge Rugby */
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
    
    /* Boite d'excuse */
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
    
    /* Inputs et Sliders */
    .stSlider label, .stSelectbox label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Le 'Droit de Retrait' Rugby")
st.write("Générateur d'excuses pour Cléo - Hardis Group Edition.")

# --- FORMULAIRE DANS LA SIDEBAR ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    heure = st.slider("Il est quelle heure ?", 0, 23, 20)
    humeur_match = st.select_slider("Ambiance du match", options=["Cata", "Tendu", "Grosse Victoire"])
    transport = st.selectbox("Ton transport", ["RER A", "RER B", "Ligne 13", "Ligne 1", "Transilien L", "Bus de ville"])

# --- LE MOTEUR D'EXCUSES ENRICHI ---
def generer_excuse_blindee(h, res, t):
    # Catégorie : Solidarité / Pote en galère
    solidarite = [
        "Le talonneur s'est fait larguer hier par SMS, il est en larmes au club-house. On fait bloc autour de lui, je peux pas le laisser comme ça, c'est l'esprit du club.",
        "Un petit nouveau a pris un KO technique moral après sa boulette sur le terrain. Le capitaine a interdit à quiconque de partir avant qu'il ait retrouvé le sourire.",
        "Le deuxième ligne a perdu ses papiers et son tel dans le vestiaire, on vide tout pour l'aider. Il est en panique totale, je gère le truc.",
        "Réunion de crise : un des gars a de gros soucis perso, on fait un cercle de parole dans le vestiaire. C'est sacré, je bouge pas d'ici."
    ]
    
    # Catégorie : Débrief / Institution
    debrief = [
        f"Le coach a verrouillé la porte. Vu la prestation '{res}', il nous fait la leçon de morale du siècle. On ne sort que quand il aura fini de gueuler.",
        f"On est en plein débrief vidéo sauvage au bar. On analyse pourquoi on a été '{res}'. Si je pars maintenant, je perds ma place de titulaire mardi.",
        "C'est la remise des maillots pour la saison prochaine et le président fait un discours interminable. Obligé de rester pour la photo officielle.",
        "Tradition de club : on doit accueillir les nouveaux avec un chant. C'est mon tour, je suis coincé pour au moins une heure."
    ]
    
    # Catégorie : Transports Parisiens (Le classique)
    paris = [
        f"Incident voyageur sur le {t}. Trafic totalement interrompu. Je suis bloqué au milieu du tunnel, on attend que le train redémarre.",
        f"C'est le bordel sur le {t}, y'a un sac suspect sur le quai, la gare est évacuée. Je cherche une solution en bus mais c'est blindé.",
        f"Le {t} est en mode 'service réduit' à cause d'une panne de caténaire. Prochain passage dans 45 min, si j'ai de la chance.",
        f"Travaux imprévus sur le {t}, je dois faire un détour de 1h30 par une autre ligne. C'est l'enfer ce soir."
    ]

    # Logique de sélection
    if h < 17:
        pool = debrief
    elif h < 21:
        pool = solidarite
    else:
        pool = paris
        
    return random.choice(pool)

# --- AFFICHAGE ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE IMPARABLE"):
    excuse = generer_excuse_blindee(heure, humeur_match, transport)
    
    st.markdown("### 📱 Message prêt à envoyer :")
    st.markdown(f"<div class='excuse-box'>« {excuse} »</div>", unsafe_allow_html=True)
    
    st.warning("⚠️ **Règle d'or :** Ne réplique pas au message suivant. Le silence confirme l'urgence ou l'absence de réseau dans le métro.")

st.sidebar.markdown("---")
st.sidebar.info("Développé pour la 3ème mi-temps.")
