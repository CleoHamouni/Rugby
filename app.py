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

st.title("🏉 Third Time - Master")

# --- FORMULAIRE ---
cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
res = st.selectbox("Résultat :", ["Victoire", "Défaite", "Nul"])

def generer_phrase(categorie, ton_choisi, resultat, heure):
    # 1. INTROS (5 par ton)
    intros = {
        "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Je fais au plus vite mais pour {h}h c'est mort,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
        "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,", "Je vais encore arriver une plombe après {h}h,"],
        "Factuel": ["Bloqué.", "Retard prévu.", "Je ne serai pas là pour {h}h.", "Coincé.", "Changement de programme."]
    }

    # 2. ACTIONS (15 par catégorie)
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

    # 3. CONCLUSIONS (10 par catégorie + variantes résultats)
    concl = {
        "Solidarité": ["on ne peut vraiment pas le laisser seul.", "on fait bloc, c'est l'esprit de l'équipe.", "tout le groupe reste pour l'épauler.", "je rentre dès que la situation s'apaise.", "le staff demande qu'on reste ensemble.", "c'est sacré, on ne lâche personne ici.", "on attend que sa famille arrive pour partir.", "le capitaine insiste pour qu'on fasse cercle.", "on essaie de lui changer les idées au max.", "c'est un moment dur pour le groupe."],
        "Santé": ["je reste en soutien le temps que les secours arrivent.", "on attend l'avis définitif du médecin du club.", "je ne peux pas le lâcher tant qu'il n'est pas stable.", "le soigneur a besoin d'aide pour l'aider.", "on surveille que son état ne s'aggrave pas.", "le SAMU est en route, je reste à côté.", "on lui met de la glace en attendant l'infirmier.", "le doc veut que je reste pour témoigner du choc.", "on l'aide à s'habiller sans le bouger.", "je l'accompagne jusqu'à sa voiture plus tard."],
        "Transports": ["aucune info sur la reprise du trafic.", "je cherche désespérément un itinéraire bis.", "on nous demande de patienter sur le quai.", "c'est l'enfer pour trouver un taxi ou un Uber.", "je suis coincé à l'intérieur pour le moment.", "les haut-parleurs annoncent un retard indéterminé.", "je vais tenter de finir le trajet à pied.", "tout le quartier est bouclé par la police.", "le prochain train est dans une éternité.", "je suis bloqué au guichet pour mon pass."],
        "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "c'est une obligation directe du président.", "je fais au plus vite pour m'échapper.", "c'est le protocole habituel ici.", "le coach a pris les clés du vestiaire.", "on doit finir ça avant de pouvoir partir.", "c'est mal vu de bouger avant le staff.", "on est réquisitionnés pour la logistique.", "c'est le débriefing obligatoire de fin de match."]
    }

    # Ajout du sel selon le résultat
    if categorie in ["Solidarité", "Club"]:
        if resultat == "Victoire":
            concl[categorie].extend(["le président veut fêter ça dignement.", "c'est la folie pour la remise des prix.", "on savoure ce moment tous ensemble."])
        elif resultat == "Défaite":
            concl[categorie].extend(["le coach est hors de lui après ce score.", "ambiance de deuil, personne ne bouge.", "on se fait remonter les bretelles grave."])

    # ASSEMBLAGE
    i = random.choice(intros[ton_choisi]).format(h=heure)
    a = random.choice(actions[categorie])
    c = random.choice(concl[categorie])

    return f"{i} {a}, {c}"

# --- BOUTON ---
st.markdown("---")
if st.button("🚀 GÉNÉRER L'EXCUSE MAÎTRE"):
    msg = generer_phrase(cat, ton, res, h_prevu)
    st.markdown(f"<div class='excuse-box'>« {msg} »</div>", unsafe_allow_html=True)
    st.info("💡 Combo généré parmi plus de 3000 possibilités cohérentes.")
