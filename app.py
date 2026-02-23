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
        "un joueur a une crampe géante qui ne passe pas.", "on surveille un gars qui a eu un coup de chaleur.",
        "un pote s'est cassé le nez, on éponge le sang.", "on attend les secours pour une luxation du genou.",
        "le soigneur fait un pansement compressif à un gars.", "un coéquipier a une forte fièvre après l'effort.",
        "le 1 s'est arraché un ongle, c'est très douloureux.", "on aide un blessé à se changer sans le bouger.",
        "le médecin vérifie une suspicion de trauma crânien.", "on attend l'arrivée de la famille d'un blessé grave.",
        "le 14 a une grosse contusion, on l'aide à glacer.", "le doc du club fait un test de lucidité au capitaine."
    ],
    "Transports": [
        "galère totale dans le métro, incident voyageur.", "plus aucun métro (colis suspect), bus blindé.",
        "panne de signalisation, rames à l'arrêt en tunnel.", "grève surprise, trafic nul, Uber hors de prix.",
        "tunnel fermé par la police, métro inaccessible.", "problème électrique, bloqué dans une rame.",
        "mon pass Navigo est en opposition, guichet fermé.", "gros malaise voyageur dans mon wagon, à l'arrêt.",
        "signal d'alarme tiré, on attend la sécurité.", "rame en panne devant, on doit reculer.",
        "accident de personne à la station suivante, bloqué.", "plus d'électricité sur toute la ligne, arrêt.",
        "bagage abandonné, station évacuée par les militaires.", "le métro est resté coincé entre deux arrêts.",
        "rupture de caténaire, aucun train ne circule.", "infiltration d'eau sur les voies, trafic coupé.",
        "agression dans la rame, le conducteur s'est arrêté.", "le bus de substitution est tombé en panne aussi.",
        "on nous fait descendre sur les voies pour évacuer.", "le chauffeur de bus a fini son service, on attend.",
        "les accès au métro sont saturés, police sur place.", "travaux de nuit commencés plus tôt, ligne fermée.",
        "dévers de rails, le métro roule au pas, c'est long.", "feu à proximité des voies, pompiers sur place.",
        "plus de taxis ni de Uber dispo, j'attends le bus.", "le RER est détourné par une autre gare, perdu.",
        "vols de câbles sur la ligne, trafic paralysé.", "objet tombé sur les voies, on attend le retrait.",
        "une porte ne ferme plus, le train ne peut pas partir.", "le métro ne s'arrête plus à ma station, détour."
    ],
    "Club": [
        f"le coach a verrouillé la porte. Vu la {res}, débrief.", "débrief vidéo sauvage. Si je pars, je saute.",
        "le président fait un discours pour les sponsors.", "corvée de réception de l'équipe adverse.",
        "l'arbitre explique ses choix, obligation d'être là.", "réunion imprévue sur le tournoi de fin d'année.",
        "on doit tout ranger, le capitaine bloque les sorties.", "le club fête une légende, partir serait mal vu.",
        "problème de licence pour mardi, signatures.", "staff nous retient pour le voyage de fin d'année.",
        "inventaire des maillots obligatoire ce soir, bloqué.", "réunion de sécurité pour le prochain gros match.",
        "le président offre le champagne pour la {res}.", "corvée de nettoyage de la buvette, punition.",
        "le capitaine nous fait une mise au point musclée.", "remise des récompenses pour le joueur du match.",
        "on doit gonfler tous les ballons pour l'école de rugby.", "le club organise un apéro d'honneur imprévu.",
        "le coach nous présente le nouveau schéma tactique.", "on attend le trésorier pour les remboursements.",
        "séance de photos officielles pour le calendrier.", "discussion sur le changement de sponsor maillot.",
        "on prépare les colis pour l'association du club.", "le staff fait un point individuel avec chaque joueur.",
        "le coach de la B nous retient pour un coup de main.", "on aide à installer le chapiteau pour demain.",
        "réunion sur la discipline après les cartons de ce jour.", "on attend le kiné pour les soins de mardi.",
        "le secrétaire du club a besoin d'un coup de main administratif.", "tradition : le dernier doit laver les chasubles."
    ]
}

# --- LOGIQUE D'ASSEMBLAGE ---
def assembler(t, h, excuse):
    if t == "Mielleux":
        return f"Mon amour, je m'en veux tellement... Je devais être là pour {h}h mais là c'est compliqué : {excuse} Je rentre le plus vite possible, je t'aime."
    elif t == "Râleur":
        return f"Franchement j'en ai marre, je pensais être rentré pour {h}h mais y'a encore une tuile : {excuse} Journée de l'enfer. À tout de suite."
    else: # Factuel
        return f"Bloqué. Je devais rentrer pour {h}h mais {excuse} Je fais au plus vite."

# --- BOUTON ---
st.markdown("---")
if st.button("🚀 GÉNÉRER L'EXCUSE"):
    excuse_base = random.choice(E[cat])
    msg = assembler(ton, h_prevu, excuse_base)
    st.markdown("### 📱 Message prêt :")
    st.markdown(f"<div class='excuse-box'>« {msg} »</div>", unsafe_allow_html=True)
    st.info("💡 Copie et passe en mode avion !")
