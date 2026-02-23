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
st.subheader("1. Ton angle d'attaque")
cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton souhaité :", ["Mielleux", "Râleur", "Factuel"])
h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)

# --- MÉGA BASE DE DONNÉES ---
E = {cat: {t: [] for t in ["Mielleux", "Râleur", "Factuel"]} for cat in ["Solidarité", "Santé", "Transports", "Club"]}

# --- CATEGORIE : SOLIDARITÉ ---
E["Solidarité"]["Mielleux"] = [
    f"Je suis vraiment désolé pour les {h_prevu}h mais un petit nouveau est en larmes au vestiaire, je ne peux pas le laisser seul.",
    f"Je m'en veux de rater {h_prevu}h mais le talonneur vient de se faire larguer, on fait bloc pour lui remonter le moral.",
    f"Je fais au plus vite pour te rejoindre, mais le capitaine a un gros coup de mou, on reste tous pour l'entourer un peu.",
    f"Mille excuses, je vais avoir du retard sur les {h_prevu}h car un pote a de gros soucis et on fait une réunion de soutien.",
    f"Je suis navré, je fais le maximum mais le 9 est en plein burn-out, je ne peux pas l'abandonner dans cet état."
]
E["Solidarité"]["Râleur"] = [
    f"Franchement ça me gonfle, je pensais être là pour {h_prevu}h mais le coach nous force à rester pour un gars qui craque.",
    f"Encore un plan galère, le talonneur fait une crise de nerfs, tout le monde est bloqué au club. Pas là à {h_prevu}h.",
    f"C'est n'importe quoi, on ne peut pas partir car un gars a perdu ses clés et on doit ratisser tout le terrain à 15.",
    f"Journée de l'enfer, je vais rater {h_prevu}h parce que le 15 fait encore son cinéma et le staff veut qu'on l'écoute.",
    f"Marre de ce club, le président nous retient pour faire un 'cercle de parole' suite à une embrouille. À plus."
]
E["Solidarité"]["Factuel"] = [
    f"Bloqué au club. Un pote va mal, on reste en équipe pour lui. Désolé pour les {h_prevu}h.",
    f"Retard prévu. Problème perso pour un coéquipier, on fait bloc. Je rentre dès que possible.",
    f"Je ne serai pas là pour {h_prevu}h. Situation compliquée avec un joueur, on gère la crise collectivement.",
    f"Coincé au vestiaire. Soutien moral obligatoire pour un gars. Je te tiens au courant.",
    f"Pas de départ possible pour {h_prevu}h. Cohésion d'équipe nécessaire suite à un coup dur pour le soigneur."
]

# --- CATEGORIE : SANTÉ ---
E["Santé"]["Mielleux"] = [
    f"Je suis navré pour {h_prevu}h mais un pote a pris un énorme choc et je reste avec lui pour le surveiller un peu.",
    f"Vraiment désolé, je suis aux urgences avec le 10 qui a une commotion, je ne pouvais pas le laisser seul ici.",
    f"Je m'en veux pour {h_prevu}h, mais un coéquipier a fait un gros malaise, je l'aide le temps que ça aille mieux.",
    f"Pardonne-moi, on attend l'ambulance pour le pilier, je reste à ses côtés pour le rassurer. Je fais au plus vite.",
    f"Je vais avoir du retard, j'aide le soigneur avec un gars qui s'est ouvert l'arcade. Je rentre dès que possible."
]
E["Santé"]["Râleur"] = [
    f"C'est la poisse, je rate {h_prevu}h car je dois accompagner un blessé. Pourquoi ça tombe toujours sur moi ?",
    f"Génial, encore un gars qui se blesse et je suis de corvée pour attendre les pompiers. Pas là pour {h_prevu}h.",
    f"Franchement marre, le 15 s'est tordu la cheville et je dois l'aider à bouger. Journée de merde.",
    f"Pas de bol, le médecin du club me demande de surveiller un gars qui a fait un malaise. Je rate {h_prevu}h.",
    f"Sérieux, le 12 s'est cassé le nez et je dois aider le staff en attendant les secours. Je vais être en retard."
]
E["Santé"]["Factuel"] = [
    f"Urgence médicale au club. Je reste en soutien. Je ne serai pas là pour {h_prevu}h.",
    f"Retard important. Un joueur s'est déboîté l'épaule, on attend l'arrivée de l'ambulance.",
    f"Bloqué. Surveillance d'un coéquipier sonné par un tampon. Je fais au plus vite.",
    f"Coincé aux soins. Suspicion de fracture pour un pote, je l'aide. À tout de suite.",
    f"Pas là pour {h_prevu}h. Le soigneur a besoin d'aide pour stabiliser un gars après le match."
]

# --- CATEGORIE : TRANSPORTS ---
E["Transports"]["Mielleux"] = [
    f"Je suis désolé, le métro est totalement bloqué... Je ne serai malheureusement pas là pour {h_prevu}h.",
    f"Vraiment navré, colis suspect dans ma rame, on est évacués. C'est très compliqué pour rentrer.",
    f"Je m'en veux, panne de signalisation majeure. Je rêve de rentrer mais je suis coincé sur le quai.",
    f"Toutes mes excuses, la ligne est coupée. Je cherche une solution alternative pour te rejoindre au plus vite.",
    f"Je suis à l'arrêt en plein tunnel. Je fais le maximum pour arriver, mais le trafic est paralysé."
]
E["Transports"]["Râleur"] = [
    f"Sérieux, c'est quoi cette ville ? Métro bloqué, incident voyageur. Je rate {h_prevu}h, ça me saoule.",
    f"Encore une grève surprise ! Aucun train. Je vais mettre 2h à rentrer. Journée pourrie.",
    f"Marre de la RATP. Panne électrique, bloqué entre deux stations. Ne m'attends pas pour {h_prevu}h.",
    f"Franchement j'en peux plus, colis suspect à Châtelet, tout est figé. C'est le bordel complet.",
    f"Génial, le bus de substitution est aussi en panne. Je vais arriver une plombe après {h_prevu}h."
]
E["Transports"]["Factuel"] = [
    f"Métro bloqué. Incident voyageur majeur. Je vais rater l'heure de {h_prevu}h.",
    f"Retard SNCF/RATP. Panne de signalisation. Trafic totalement interrompu pour le moment.",
    f"Coincé dans la rame. On attend l'évacuation suite à un problème électrique sur les voies.",
    f"Ligne coupée (colis suspect). Je cherche un itinéraire bis. À plus tard.",
    f"Trafic nul sur tout le réseau. Je fais au plus vite mais la progression est très lente."
]

# --- CATEGORIE : CLUB ---
E["Club"]["Mielleux"] = [
    f"Je suis navré, le coach a verrouillé les vestiaires pour un débrief. Je m'en veux de rater {h_prevu}h.",
    f"Désolé, le président nous retient pour un discours obligatoire. Je rentre dès que la séance finit.",
    f"Vraiment navré, on fête l'anniversaire d'une légende du club, je ne peux pas m'éclipser par respect.",
    f"Je fais au plus vite pour te retrouver, mais on a une corvée de rangement imprévue pour l'équipe.",
    f"Je m'en veux pour {h_prevu}h, mais l'arbitre explique ses choix au bar et tout le groupe doit être là."
]
E["Club"]["Râleur"] = [
    f"Le coach fait son tyran, débriefing vidéo obligatoire. Je serai pas là pour {h_prevu}h, c'est chiant.",
    f"Encore une réunion de merde pour le tournoi de fin d'année. Je suis coincé au club.",
    f"Sérieux, je dois nettoyer les vestiaires à cause des petits. Corvée de dernière minute. Marre.",
    f"Le président fait un discours interminable pour ses sponsors de merde. Je rate {h_prevu}h.",
    f"Génial, l'arbitre reste boire un coup et on est obligés de faire de la figuration par principe. À plus."
]
E["Club"]["Factuel"] = [
    f"Retenu au club. Débriefing obligatoire suite au match. Désolé pour {h_prevu}h.",
    f"Coincé. Réunion administrative imprévue pour les licences. Je rentre juste après.",
    f"Obligation de présence pour la réception de l'équipe adverse. Retard à prévoir.",
    f"Corvée de rangement décidée au dernier moment par le staff. Je fais au plus vite.",
    f"Réunion tactique pour le match de mardi prochain. Pas là pour {h_prevu}h."
]

# --- BOUTON GÉNÉRER ---
st.markdown("---")
if st.button("🚀 GÉNÉRER L'EXCUSE UNIQUE"):
    liste_options = E[cat][ton]
    if not liste_options:
        st.error("Désolé, pas d'excuse dispo pour ce combo.")
    else:
        message_final = random.choice(liste_options)
        st.markdown("### 📱 Message prêt :")
        st.markdown(f"<div class='excuse-box'>« {message_final} »</div>", unsafe_allow_html=True)
        st.info("💡 Copie le texte et passe en mode avion !")
