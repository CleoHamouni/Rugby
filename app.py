import streamlit as st
import random

st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉")

# --- STYLE ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0d17; color: white; }
    .stButton>button { width: 100%; background-color: #d62828; color: white; border-radius: 8px; height: 3em; font-size: 18px; font-weight: bold; border: none; }
    .excuse-box { background-color: #1a1c24; padding: 20px; border-radius: 10px; border-left: 6px solid #d62828; color: #e0e0e0; font-style: italic; font-size: 1.1em; }
    h1, h2, h3, p, label { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏉 Le 'Droit de Retrait' Rugby")
st.write("Générateur d'excuses socialement inattaquables.")

# --- FORMULAIRE ---
with st.sidebar:
    st.header("⚙️ Paramètres")
    heure = st.slider("Il est quelle heure (en théorie) ?", 0, 23, 20)
    humeur_match = st.select_slider("Résultat du match", options=["Déroute", "Moyen", "Victoire !"])
    transport = st.selectbox("Ton transport", ["RER A", "RER B", "Ligne 13", "Ligne 1", "Transilien"])

# --- LE MOTEUR D'EXCUSES ---
def generer_excuse_blindee(h, res, t):
    solidarite = [
        "Un petit nouveau est en train de craquer complètement après le match, on ne peut pas le laisser partir seul, on essaie de lui remonter le moral.",
        "Le talonneur s'est fait larguer violemment hier, il est au fond du trou. On fait une réunion de crise pour l'entourer, je me vois mal le lâcher maintenant.",
        "Le capitaine a pris un énorme tampon, il est un peu sonné, on surveille qu'il récupère bien ses esprits avant de le laisser rentrer."
    ]
    
    debrief = [
        f"Le coach est hors de lui après cette {res}, on est bloqués au vestiaire pour une séance débrief improvisée, personne ne sort.",
        f"Vu le match {res}, on est obligés de faire un débrief à froid pour mettre les choses à plat de suite, sinon ça va exploser au club.",
        "On refait le match action par action avec les gars d'en face, c'est une question de respect et d'image pour le club, je suis coincé."
    ]
    
    paris = [
        f"C'est la cata sur le {t}, colis suspect à Châtelet, tout est figé. Je cherche un itinéraire bis mais ça va mettre une éternité.",
        f"Le {t} est en panne de signalisation totale, je suis bloqué sur le quai avec la moitié de l'équipe. On attend le prochain train 'éventuel'.",
        f"Grève surprise sur le {t}, je vais essayer de gratter un trajet en Uber avec deux gars de l'équipe mais les prix sont délirants là."
    ]

    if h < 17:
        msg = random.choice(debrief)
    elif h < 21:
        msg = random.choice(solidarite)
    else:
        msg = random.choice(paris)
        
    return msg

# --- AFFICHAGE ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE IMPARABLE"):
    excuse = generer_excuse_blindee(heure, humeur_match, transport)
    
    st.markdown("### 📱 Message prêt à l'envoi :")
    st.markdown(f"<div class='excuse-box'>« {excuse} »</div>", unsafe_allow_html=True)
    
    st.info("💡 **Conseil stratégique :** Une fois envoyé, ne réponds plus au prochain message pour simuler 'le tunnel' ou 'la batterie faible'.")
