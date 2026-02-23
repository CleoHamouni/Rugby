import streamlit as st
import random

# Configuration de la page
st.set_page_config(page_title="Rugby Excuse Pro", page_icon="🏉", layout="centered")

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* Menus déroulants */
    div[data-baseweb="select"] > div {
        background-color: #262730 !important;
        color: white !important;
        border: 1px solid #d62828 !important;
    }
    div[data-testid="stSelectbox"] div div { color: white !important; }

    /* Boutons */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 8px; 
        height: 3.5em; 
        font-weight: bold; 
        border: none;
        font-size: 18px;
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
        margin-top: 10px;
    }

    /* Simulateur de notification (Preuve) */
    .proof-box {
        background-color: #000000;
        border: 1px solid #333;
        border-radius: 15px;
        padding: 15px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica;
        color: white;
        max-width: 320px;
        margin: 10px auto;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .notif-header { 
        font-size: 10px; 
        color: #aaa; 
        margin-bottom: 5px; 
        text-transform: uppercase; 
        letter-spacing: 0.5px;
        display: flex;
        justify-content: space-between;
    }
    .notif-title { font-weight: bold; font-size: 14px; color: #ffffff; margin-bottom: 2px; }
    .notif-body { font-size: 13px; color: #ddd; line-height: 1.3; }
    
    /* Jauge de risque */
    .risk-container { margin-top: 20px; }
    .risk-bar-bg { background-color: #333; height: 10px; width: 100%; border-radius: 5px; overflow: hidden; }
    .risk-bar-fill { height: 100%; border-radius: 5px; transition: width 0.5s ease-in-out; }
    
    label { color: #aaa !important; font-size: 14px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- TITRE ---
st.title("🏉 Third Time")
st.write("L'outil de précision pour les troisièmes mi-temps prolongées.")

# --- FORMULAIRE ---
st.subheader("1. Analyse de la situation")

cat = st.selectbox("Catégorie d'excuse :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton du message :", ["Mielleux", "Râleur", "Factuel"])

col1, col2 = st.columns(2)
with col1:
    h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
with col2:
    res = st.selectbox("Résultat du match :", ["Victoire", "Défaite", "Nul"])

# --- LOGIQUE DU MOTEUR ---
def generer_excuse(categorie, ton_choisi, resultat, heure):
    # INTROS (5 par ton)
    intros = {
        "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Je fais au plus vite mais pour {h}h c'est mort,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
        "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,", "Je vais encore arriver une plombe après {h}h,"],
        "Factuel": ["Bloqué.", "Retard prévu.", "Je ne serai pas là pour {h}h.", "Coincé.", "Changement de programme."]
    }

    # ACTIONS (15 par catégorie)
    actions = {
        "Solidarité": [
            "un petit nouveau est en larmes au vestiaire", "le talonneur vient de se faire larguer", "le capitaine a un énorme coup de mou", "un gars a de gros soucis perso et on fait bloc", "le 9 est en plein burn-out moral", "un ancien est passé et il ne va pas bien", "un coéquipier a perdu ses clés et son tel", "on soutient le soigneur qui a un coup dur", "le deuxième ligne a appris une mauvaise nouvelle", "un gars est en crise de nerfs après le match", "on entoure un joueur qui veut arrêter le rugby", "un pote est effondré suite à une erreur de jeu", "le groupe reste pour aider un gars sans voiture", "un coéquipier a des problèmes familiaux urgents", "on discute avec le 7 qui est totalement démoralisé"
        ],
        "Santé": [
            "un pote a pris un énorme choc sur le terrain", "un coéquipier a fait un malaise après l'effort", "on attend l'ambulance pour le pilier", "le soigneur me demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade", "suspicion de fracture pour mon binôme", "le 10 est totalement désorienté après un tampon", "un gars s'est déboîté l'épaule aux vestiaires", "on attend les pompiers pour un gars d'en face", "une blessure grave nous oblige à rester", "un joueur a une plaie qui ne s'arrête pas de saigner", "on aide le doc pour une suspicion de trauma", "le kiné a besoin de bras pour manipuler un blessé", "un gars est en hypothermie sous la douche", "on surveille un joueur qui respire mal"
        ],
        "Transports": [
            "le métro est totalement à l'arrêt", "il y a un colis suspect dans ma rame", "une panne de signalisation bloque tout", "un incident voyageur paralyse la ligne", "le trafic est nul à cause d'une grève surprise", "un bagage abandonné bloque la station", "un problème d'alimentation coupe le courant", "la rame est bloquée entre deux stations", "un malaise voyageur oblige le train à rester à quai", "le bus de substitution est aussi en panne", "une porte est bloquée, le train ne démarre pas", "travaux de nuit commencés plus tôt que prévu", "incident technique majeur sur les voies", "la sécurité ferroviaire évacue le quai", "le conducteur attend le feu vert du PC"
        ],
        "Club": [
            "le coach nous a enfermés pour un débrief musclé", "le président fait un discours interminable", "on est de corvée de rangement pour l'équipe", "l'arbitre explique ses choix au bar", "on est bloqués pour une réunion administrative", "on doit signer les licences pour mardi", "le staff fait un point individuel avec chacun", "on nettoie la buvette suite à une sanction", "on prépare les colis pour le tournoi", "le capitaine a verrouillé les sorties pour parler", "inventaire obligatoire de tout le matos", "on attend les sponsors pour la photo officielle", "réunion de crise sur la discipline du groupe", "le secrétaire a besoin d'un coup de main urgent", "le staff médical fait un point général obligatoire"
        ]
    }

    # CONCLUSIONS (10 par catégorie)
    conclusions = {
        "Solidarité": ["on ne peut vraiment pas le laisser seul.", "on fait bloc, c'est l'esprit de l'équipe.", "tout le groupe reste pour l'épauler.", "je rentre dès que la situation s'apaise.", "le staff demande qu'on reste ensemble.", "c'est sacré, on ne lâche personne ici.", "on attend que sa famille arrive pour partir.", "le capitaine insiste pour qu'on fasse cercle.", "on essaie de lui changer les idées au max.", "c'est un moment dur pour le groupe."],
        "Santé": ["je reste en soutien le temps que les secours arrivent.", "on attend l'avis définitif du médecin du club.", "je ne peux pas le lâcher tant qu'il n'est pas stable.", "le soigneur a besoin d'aide pour l'aider.", "on surveille que son état ne s'aggrave pas.", "le SAMU est en route, je reste à côté.", "on lui met de la glace en attendant l'infirmier.", "le doc veut que je reste pour témoigner du choc.", "on l'aide à s'habiller sans le bouger.", "je l'accompagne jusqu'à sa voiture plus tard."],
        "Transports": ["aucune info sur la reprise du trafic.", "je cherche désespérément un itinéraire bis.", "on nous demande de patienter sur le quai.", "c'est l'enfer pour trouver un taxi ou un Uber.", "je suis coincé à l'intérieur pour le moment.", "les haut-parleurs annoncent un retard indéterminé.", "je vais tenter de finir le trajet à pied.", "tout le quartier est bouclé par la police.", "le prochain train est dans une éternité.", "je suis bloqué au guichet pour mon pass."],
        "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "c'est une obligation directe du président.", "je fais au plus vite pour m'échapper.", "c'est le protocole habituel ici.", "le coach a pris les clés du vestiaire.", "on doit finir ça avant de pouvoir partir.", "c'est mal vu de bouger avant le staff.", "on est réquisitionnés pour la logistique.", "c'est le débriefing obligatoire de fin de match."]
    }

    # Bonus résultat
    if categorie in ["Solidarité", "Club"]:
        if resultat == "Victoire":
            conclusions[categorie].append("le président veut fêter ça dignement.")
        elif resultat == "Défaite":
            conclusions[categorie].append("l'ambiance est vraiment pesante suite au score.")

    intro = random.choice(intros[ton_choisi]).format(h=heure)
    action = random.choice(actions[categorie])
    concl = random.choice(conclusions[categorie])

    return f"{intro} {action}, {concl}"

# --- GÉNÉRATION ---
st.divider()

col_btn1, col_btn2 = st.columns(2)

if col_btn1.button("🚀 GÉNÉRER"):
    message = generer_excuse(cat, ton, res, h_prevu)
    st.markdown(f"<div class='excuse-box'>« {message} »</div>", unsafe_allow_html=True)
    
    # Jauge de risque
    risques = {"Transports": (20, "Faible", "limegreen"), "Club": (50, "Modéré", "orange"), 
               "Solidarité": (75, "Élevé", "orangered"), "Santé": (95, "Critique", "red")}
    val, lab, col = risques[cat]
    
    st.markdown(f"""
        <div class="risk-container">
            <small>Indice de risque : <b>{lab}</b></small>
            <div class="risk-bar-bg"><div class="risk-bar-fill" style="width: {val}%; background-color: {col};"></div></div>
        </div>
    """, unsafe_allow_html=True)

if col_btn2.button("🖼️ PREUVE"):
    st.write("Fais une capture d'écran du bloc ci-dessous :")
    if cat == "Transports":
        st.markdown(f"""
            <div class="proof-box">
                <div class="notif-header"><span>SNCF/RATP • Maintenant</span></div>
                <div class="notif-title">⚠️ Trafic interrompu</div>
                <div class="notif-body">Incident majeur sur la ligne. Les trains sont à l'arrêt. Reprise estimée dans 60 minutes. Merci de favoriser les bus.</div>
            </div>
        """, unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown(f"""
            <div class="proof-box">
                <div class="notif-header"><span>WhatsApp • Groupe Seniors</span></div>
                <div class="notif-title">Coach 🏉</div>
                <div class="notif-body">Personne ne quitte les vestiaires. On débriefe le match maintenant. Les retardataires seront sanctionnés mardi.</div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Pas de preuve visuelle nécessaire pour cette catégorie. Le texte suffit.")

st.divider()
st.caption("N'oublie pas de passer en mode avion après l'envoi ! 😉")
