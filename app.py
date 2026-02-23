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

st.title("🏉 Third Time - Expert")

# --- FORMULAIRE ---
st.subheader("1. Analyse du terrain")
cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton souhaité :", ["Mielleux", "Râleur", "Factuel"])

col1, col2 = st.columns(2)
with col1:
    h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
with col2:
    res = st.selectbox("Résultat du match :", ["Victoire", "Défaite", "Nul"])

# --- MÉGA BASE DE DONNÉES (Extraits pour la structure) ---
E = {c: {t: [] for t in ["Mielleux", "Râleur", "Factuel", "Victoire", "Défaite", "Nul"]} for c in ["Solidarité", "Santé", "Transports", "Club"]}

# --- SOLIDARITÉ ---
E["Solidarité"]["Mielleux"] = [f"Je suis navré pour les {h_prevu}h mais un petit nouveau est en larmes, je ne peux pas le laisser seul.", f"Je m'en veux de rater {h_prevu}h mais le talonneur vient de se faire larguer, on fait bloc.", f"Je fais au plus vite, mais le capitaine a un gros coup de mou, on reste tous pour l'entourer.", f"Mille excuses, retard sur les {h_prevu}h car un pote a de gros soucis et on fait une réunion de soutien.", f"Je suis navré, je fais le maximum mais le 9 est en plein burn-out, je ne peux pas l'abandonner."]
E["Solidarité"]["Râleur"] = [f"Ça me gonfle, je pensais être là pour {h_prevu}h mais le coach nous force à rester pour un gars qui craque.", f"Encore un plan galère, le talonneur fait sa crise, tout le monde est bloqué. Pas là à {h_prevu}h.", f"C'est n'importe quoi, on doit ratisser tout le terrain car un gars a perdu ses clés de bagnole.", f"Journée de l'enfer, je vais rater {h_prevu}h parce que le 15 fait encore son cinéma au vestiaire.", f"Marre de ce club, le président nous retient pour un 'cercle de parole' après une embrouille."]
E["Solidarité"]["Factuel"] = [f"Bloqué au club. Un pote va mal, on reste en équipe. Désolé pour les {h_prevu}h.", f"Retard prévu. Problème perso pour un coéquipier, on fait bloc. Je rentre dès que possible.", f"Je ne serai pas là pour {h_prevu}h. Situation compliquée avec un joueur, on gère la crise.", f"Coincé au vestiaire. Soutien moral obligatoire pour un gars. Je te tiens au courant.", f"Pas de départ possible pour {h_prevu}h. Cohésion d'équipe nécessaire suite à un coup dur."]
E["Solidarité"]["Victoire"] = [f"C'est la folie ici après la victoire, un des gars a craqué sous l'émotion, on reste l'épauler.", f"On ne peut pas laisser le capitaine seul, il est trop monté en pression avec la gagne, on le calme.", f"Victoire historique mais un gars est resté prostré, on fait bloc autour de lui avant de partir."]
E["Solidarité"]["Défaite"] = [f"Vu la défaite, l'ambiance est tragique. On reste pour éviter qu'un des jeunes ne fasse une bêtise.", f"Tout le monde est effondré, on fait une réunion de crise pour ne pas laisser les gars partir dans cet état.", f"C'est dur ce soir, je reste pour soutenir le 10 qui s'en veut terriblement pour le score."]

# --- SANTÉ ---
E["Santé"]["Mielleux"] = [f"Désolé pour {h_prevu}h mais un pote a pris un énorme choc et je reste avec lui.", f"Je suis aux urgences avec le 10 qui a une commotion, je ne pouvais pas le laisser seul.", f"Je m'en veux pour {h_prevu}h, mais un coéquipier a fait un gros malaise, je l'aide un peu.", f"Pardonne-moi, on attend l'ambulance pour le pilier, je reste à ses côtés. Je fais au plus vite.", f"Je vais avoir du retard, j'aide le soigneur avec un gars qui s'est ouvert l'arcade."]
E["Santé"]["Râleur"] = [f"La poisse, je rate {h_prevu}h car je dois accompagner un blessé. Pourquoi ça tombe sur moi ?", f"Génial, encore un gars blessé et je suis de corvée pour attendre les pompiers. Pas là à {h_prevu}h.", f"Franchement marre, le 15 s'est tordu la cheville et je dois l'aider. Journée de merde.", f"Pas de bol, le doc me demande de surveiller un gars qui a fait un malaise. Je rate {h_prevu}h.", f"Sérieux, le 12 s'est cassé le nez et je dois aider en attendant les secours. Retard prévu."]
E["Santé"]["Factuel"] = [f"Urgence médicale au club. Je reste en soutien. Je ne serai pas là pour {h_prevu}h.", f"Retard important. Un joueur s'est déboîté l'épaule, on attend l'ambulance.", f"Bloqué. Surveillance d'un coéquipier sonné par un tampon. Je fais au plus vite.", f"Coincé aux soins. Suspicion de fracture pour un pote, je l'aide. À tout de suite.", f"Pas là pour {h_prevu}h. Le soigneur a besoin d'aide pour stabiliser un gars."]
E["Santé"]["Victoire"] = [f"On a gagné mais le 8 s'est sacrifié sur le dernier plaquage, on attend le doc avec lui.", f"La victoire coûte cher : suspicion de fracture pour mon binôme, je l'accompagne aux radios.", f"Grosse gagne mais un gars a fait un malaise d'épuisement juste après, je reste en surveillance."]
E["Santé"]["Défaite"] = [f"On perd le match et mon pote se pète le bras sur la dernière action, je reste avec lui.", f"Sale journée, défaite et blessure grave pour le petit nouveau, je l'aide pour les soins.", f"Le score est naze et j'aide le soigneur pour un gars qui a pris un KO, je rentre après."]

# --- TRANSPORTS --- (Les résultats impactent peu le métro, on garde les tons)
E["Transports"]["Mielleux"] = [f"Je suis désolé, le métro est bloqué... Je ne serai pas là pour {h_prevu}h.", f"Vraiment navré, colis suspect dans ma rame, on est évacués. C'est compliqué.", f"Je m'en veux, panne de signalisation majeure. Je rêve de rentrer mais je suis coincé.", f"Toutes mes excuses, la ligne est coupée. Je cherche une solution pour te rejoindre.", f"Je suis à l'arrêt en plein tunnel. Je fais le maximum, mais le trafic est paralysé."]
E["Transports"]["Râleur"] = [f"C'est quoi cette ville ? Métro bloqué, incident voyageur. Je rate {h_prevu}h, ça me saoule.", f"Encore une grève surprise ! Aucun train. Je vais mettre 2h. Journée pourrie.", f"Marre de la RATP. Panne électrique, bloqué entre deux stations. Ne m'attends pas.", f"Franchement j'en peux plus, colis suspect à Châtelet, tout est figé. Bordel complet.", f"Génial, le bus de substitution est aussi en panne. Une plombe de retard."]
E["Transports"]["Factuel"] = [f"Métro bloqué. Incident voyageur majeur. Je vais rater l'heure de {h_prevu}h.", f"Retard RATP. Panne de signalisation. Trafic totalement interrompu.", f"Coincé dans la rame. On attend l'évacuation suite à un problème électrique.", f"Ligne coupée (colis suspect). Je cherche un itinéraire bis.", f"Trafic nul sur le réseau. Je fais au plus vite mais c'est très lent."]
E["Transports"]["Victoire"] = [f"Même avec la victoire, les transports s'y mettent : ligne coupée pour incident.", f"Je voulais fêter ça vite avec toi mais le métro est en panne totale. Bloqué.", f"La ligne est saturée à cause d'un colis suspect, je vais rater {h_prevu}h malgré la gagne."]

# --- CLUB ---
E["Club"]["Mielleux"] = [f"Je suis navré, le coach a verrouillé les vestiaires pour un débrief après le match.", f"Désolé, le président nous retient pour un discours. Je rentre dès que ça finit.", f"Vraiment navré, on fête l'anniversaire d'une légende du club, je reste par respect.", f"Je fais au plus vite, mais on a une corvée de rangement imprévue ce soir.", f"Je m'en veux pour {h_prevu}h, mais l'arbitre explique ses choix et on doit être là."]
E["Club"]["Râleur"] = [f"Le coach fait son tyran, débriefing vidéo obligatoire. Je serai pas là pour {h_prevu}h.", f"Encore une réunion de merde pour le tournoi. Je suis coincé au club.", f"Sérieux, je dois nettoyer les vestiaires. Corvée de dernière minute. Marre.", f"Le président fait un discours interminable pour ses sponsors. Je rate {h_prevu}h.", f"Génial, l'arbitre reste boire un coup et on est obligés de rester par principe."]
E["Club"]["Factuel"] = [f"Retenu au club. Débriefing obligatoire suite au match. Désolé pour {h_prevu}h.", f"Coincé. Réunion administrative imprévue pour les licences. Je rentre juste après.", f"Obligation de présence pour la réception de l'équipe adverse. Retard prévu.", f"Corvée de rangement décidée au dernier moment par le staff.", f"Réunion tactique pour le match de mardi prochain. Pas là pour {h_prevu}h."]
E["Club"]["Victoire"] = [f"Le président a verrouillé les portes pour fêter la victoire, impossible de sortir.", f"Vu qu'on a gagné, remise des récompenses officielle, je suis obligé de rester.", f"Le coach veut marquer le coup pour la victoire, débriefing 'festif' obligatoire."]
E["Club"]["Défaite"] = [f"Le coach est hors de lui après la défaite, il nous interdit de partir avant d'avoir tout rangé.", f"Vu le score, le président fait une descente au vestiaire pour une mise au point.", f"Ambiance de deuil, on est bloqués pour un débriefing de crise après ce naufrage."]

# --- BOUTON GÉNÉRER ---
st.markdown("---")
if st.button("🚀 GÉNÉRER L'EXCUSE UNIQUE"):
    # On mixe les excuses du Ton et du Résultat pour avoir de la variété
    pool = E[cat][ton] + E[cat][res]
    # On filtre les listes vides au cas où
    pool = [x for x in pool if x]
    
    if not pool:
        st.error("Désolé, pas d'excuse dispo.")
    else:
        message_final = random.choice(pool)
        st.markdown("### 📱 Message prêt :")
        st.markdown(f"<div class='excuse-box'>« {message_final} »</div>", unsafe_allow_html=True)
        st.info("💡 Copie le texte et passe en mode avion !")
