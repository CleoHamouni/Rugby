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
    h = st.slider("Heure de retour prévue", 0, 23, 20)
    res = st.select_slider("Ambiance Match", options=["Déroute", "Moyen", "Victoire"])

# --- LA MINE D'OR DES EXCUSES ---
EXCUSES = {
    "Solidarité": [
        "Le petit nouveau est en train de craquer complètement après le match, on fait bloc pour lui remonter le moral, je peux pas le laisser comme ça.",
        "Le talonneur s'est fait larguer par SMS juste avant le coup d'envoi, il est en larmes. On fait une réunion de crise, c'est l'esprit du club.",
        "Le capitaine est vraiment pas bien moralement après sa blessure, on reste avec lui pour s'assurer qu'il rentre pas seul.",
        "Un des gars a de gros soucis perso qui sont ressortis dans le vestiaire, on fait un cercle de parole. C'est sacré, je bouge pas.",
        "Le soigneur du club vient d'apprendre une mauvaise nouvelle, on reste tous avec lui pour le soutenir, il a beaucoup donné pour nous.",
        "Un coéquipier a perdu ses clés et son portefeuille sur le terrain ou dans les douches, on ratisse tout le complexe à 15 pour l'aider.",
        "Le pilier droit est en pleine détresse psychologique à cause du boulot, on essaie de lui changer les idées avant qu'il rentre.",
        "On accompagne un des jeunes qui a eu une altercation après le match pour s'assurer qu'il rentre calmement chez lui."
    ],
    "Santé": [
        "Un de mes potes a pris un énorme choc sur les cervicales. On attend le médecin du club, je reste à côté de lui pour le surveiller.",
        "Grosse blessure pour un coéquipier, on suspecte une fracture. Je l'accompagne aux urgences pour ne pas qu'il soit seul.",
        "Le soigneur m'a demandé de surveiller un gars qui a fait un malaise vagal après l'effort. Je reste tant qu'il n'est pas stable.",
        "Un gars s'est ouvert l'arcade, c'est assez moche. On lui fait les premiers soins en attendant les points, je lui tiens la compresse.",
        "Le demi de mêlée est tombé dans les pommes sous la douche, on attend de voir s'il faut appeler les pompiers, je reste en soutien.",
        "Suspicion de commotion pour le 10, il est totalement désorienté. On a ordre de rester avec lui pour vérifier qu'il ne s'endort pas.",
        "Un joueur s'est violemment déboîté l'épaule, on attend l'ambulance, je reste pour lui tenir le bras et le rassurer.",
        "Grosse réaction allergique d'un pote après le match (sans doute le gel douche du club), on surveille que son état ne s'aggrave pas."
    ],
    "Transports": [
        "C'est la galère totale dans le métro, incident voyageur et tout est bloqué. Je suis coincé sur le quai sans aucune info.",
        "Plus aucun métro ne circule sur ma ligne (colis suspect). Je cherche un bus de substitution mais la file d'attente fait 200 mètres.",
        "Panne de signalisation majeure sur le réseau, les rames sont à l'arrêt en plein tunnel. Aucune idée de l'heure de reprise.",
        "Grève surprise sur le réseau RATP, trafic quasi nul. Je tente de trouver un Uber mais les prix sont en mode x4.",
        "Le tunnel est fermé pour une intervention de police, tout le quartier est bouclé, on ne peut même pas accéder aux bouches de métro.",
        "Problème d'alimentation électrique, je suis bloqué dans une rame entre deux stations. On nous dit de ne pas descendre sur les voies.",
        "Mon pass Navigo est passé en opposition sans raison, je galère avec le guichet qui est fermé, je cherche une solution.",
        "Gros malaise voyageur dans mon wagon, le train est immobilisé à quai le temps que les secours arrivent."
    ],
    "Club": [
        f"Le coach a verrouillé la porte. Vu le match ({res}), débriefing musclé obligatoire de 2h. Personne ne sort sous peine de sanction.",
        "On est en plein débrief vidéo sauvage pour comprendre les erreurs. Si je pars maintenant, je suis écarté du groupe mardi.",
        "Le président fait un discours interminable pour les nouveaux sponsors. Obligé de rester pour la cohésion et la photo.",
        "Tradition de club : je suis de corvée pour la réception de l'équipe adverse. Je ne peux pas m'esquiver avant qu'ils partent.",
        "L'arbitre est resté boire un verre avec nous pour expliquer ses décisions, le staff nous oblige à être présents pour l'image du club.",
        "Réunion imprévue sur l'organisation du tournoi de fin d'année, ma présence est requise pour représenter les joueurs.",
        "On doit ranger tout le matériel et nettoyer le vestiaire suite à une dégradation, le capitaine a dit que personne ne partait avant que ce soit nickel.",
        "Le club fête l'anniversaire d'une légende du rugby local qui est passée nous voir, partir maintenant serait très mal vu."
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
    
    st.info("💡 **Conseil de 3ème mi-temps :** N'oublie pas de baisser la luminosité de ton téléphone, ça fait 'plus de batterie'.")
