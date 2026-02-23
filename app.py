import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (FIX COMPLET) ---
st.markdown("""
    <style>
    /* 1. THÈME GÉNÉRAL */
    .stApp { background-color: #f8f9fa; color: #000000; }
    
    /* MASQUAGE SIDEBAR ET FLÈCHE NATIVE */
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    /* 2. FORCE LE NOIR SUR TOUT LE TEXTE */
    label, p, span, h1, h2, h3, [data-testid="stWidgetLabel"] p {
        color: #000000 !important; font-weight: 700 !important;
    }
    
    /* 3. STYLE DU DASHBOARD (EX-SIDEBAR) */
    .streamlit-expanderHeader {
        background-color: #e9ecef !important;
        border: 2px solid #28a745 !important;
        border-radius: 10px !important;
    }

    /* 4. FIX SELECTBOX */
    div[data-baseweb="select"] > div {
        background-color: #28a745 !important;
        color: #ffffff !important;
        border: none !important;
    }
    div[data-testid="stSelectbox"] svg { fill: #ffffff !important; }

    /* 5. FIX DROPDOWN (LISTE OUVERTE) */
    div[data-baseweb="popover"], ul[role="listbox"] { background-color: #ffffff !important; }
    li[role="option"] { color: #000000 !important; background-color: #ffffff !important; }

    /* 6. BOUTONS VERTS */
    .stButton>button { 
        width: 100%; 
        background-color: #28a745 !important; 
        color: #ffffff !important; 
        border-radius: 12px; 
        height: 3.5em; 
        font-weight: bold; 
        border: none; 
        font-size: 1.1rem;
    }

    /* 7. BOXES D'EXCUSES */
    .excuse-box { 
        background-color: #ffffff; padding: 20px; border-radius: 10px; 
        border: 3px solid #28a745; color: #000000 !important; font-style: italic; font-size: 1.1rem;
    }
    .finops-card { 
        background-color: #ffffff; padding: 15px; border-radius: 12px; 
        border: 3px solid #000000; text-align: center; margin-bottom: 10px; 
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #28a745 !important; display: block; }
    
    /* STYLE POUR L'ANALYSE DU SCORE */
    .roi-analysis {
        font-weight: bold;
        text-align: center;
        padding: 10px;
        border-radius: 8px;
        margin-top: 5px;
    }
    .credibility-gauge {
        text-align: center;
        margin-top: 10px;
        font-weight: bold;
        color: #28a745;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CORPS DE L'APPLI ---
st.title("🏉 Générateur d'excuses by The Paddies")

# --- DASHBOARD (REMPLACE LA SIDEBAR) ---
with st.expander("📊 RÉGLAGES : RATIO FUN / RISQUE", expanded=False):
    col_db1, col_db2 = st.columns(2)
    with col_db1:
        conso = st.slider("Verres consommés", 0, 15, 2)
        tension = st.slider("Taux d'énervement de Madame", 1, 10, 1)
    with col_db2:
        roi_score = (conso * 5) - (tension * 3)
        st.markdown(f"""<div class="finops-card"><p style="color:black; margin-bottom:0;">ROI FUN / RISQUE</p><span class="metric-value">{roi_score}</span></div>""", unsafe_allow_html=True)
        
        # --- ANALYSE DU RATIO ---
        if roi_score > 31:
            st.markdown('<div class="roi-analysis" style="background-color:#ffd700; color:black;">🏆 SOIRÉE DE LÉGENDE : Ne rentre jamais !</div>', unsafe_allow_html=True)
        elif roi_score > 8:
            st.markdown('<div class="roi-analysis" style="background-color:#28a745; color:white;">✅ ÇA VAUT LE COUP : Le plaisir dépasse le risque.</div>', unsafe_allow_html=True)
        elif roi_score >= 0:
            st.markdown('<div class="roi-analysis" style="background-color:#ff9f43; color:black;">⚠️ ZONE GRISE : Sois prudent sur le prochain verre.</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="roi-analysis" style="background-color:#dc3545; color:white;">🛑 RENTRE MAINTENANT : Le retour va être complexe.</div>', unsafe_allow_html=True)

st.divider()

# --- FORMULAIRE ---
col1, col2 = st.columns(2)
with col1:
    # AJOUT DE LA CATÉGORIE VOITURE
    cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Voiture", "Club"])
    ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
with col2:
    h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
    res = st.selectbox("Résultat match :", ["Victoire", "Défaite", "Nul"])

# --- TEST DE LUCIDITÉ ---
lucidite_ok = True
if conso > 5:
    st.info(f"Vérification requise ({conso} verres).")
    phrase_cible = "Le ballon est ovale"
    reponse = st.text_input(f"Recopiez exactement : {phrase_cible}", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- MOTEUR COMPLET D'EXCUSES ---
st.divider()
if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.error("Action bloquée : Réussissez le test de lucidité.")
    else:
        intros = {
            "Mielleux": ["Désolé pour les {h}h,", "Toutes mes excuses,", "Je m'en veux pour les {h}h,", "Vraiment navré pour le retard de {h}h,", "Pardonne-moi, je rate le coche de {h}h,"],
            "Râleur": ["Ça me gonfle pour les {h}h,", "Encore un plan galère, je serai jamais là à {h}h,", "Marre d'être bloqué alors que je devais être là à {h}h,", "Toujours sur moi que ça tombe pour les {h}h,", "C'est n'importe quoi cette organisation pour {h}h,"],
            "Factuel": ["Bloqué pour {h}h.", "Retard confirmé pour l'heure de {h}h.", "Coincé, impossible pour {h}h.", "Imprévu technique pour {h}h.", "Contretemps pour l'heure de {h}h."]
        }
        
        actions = {
            "Solidarité": [
                "un pote a un gros souci et on fait bloc", "le capitaine a un énorme coup de mou post-match", 
                "le 9 est en plein burn-out moral", "un ancien ne va pas bien du tout",
                "on soutient le coach qui a un coup dur", "un gars vient de se faire larguer, on l'épaule",
                "on discute avec le petit nouveau qui est démoralisé", "le groupe est mobilisé pour un pote qui a un pépin familial",
                "on fait bloc autour d'un gars qui a une mauvaise nouvelle", "on attend la famille d'un joueur qui a un souci",
                "un coéquipier a perdu ses clés et toute l'équipe aide à chercher", "on accompagne un gars qui n'a pas le moral au vestiaire"
            ],
            "Santé": [
                "on attend l'ambulance pour un blessé", "un gars a fait un malaise après l'effort", 
                "le soigneur me demande de surveiller un gars KO", "suspicion de fracture pour mon binôme",
                "protocole commotion en cours pour un joueur", "on gère une grosse entorse pour notre pillier au vestiaire",
                "le médecin du club fait passer des tests de sécurité à notre 3e ligne", "on attend les pompiers pour un choc sévère sur notre ailier",
                "un joueur s'est ouvert l'arcade, on attend les points", "je reste avec un gars qui a une chute de tension",
                "on gère un traumatisme crânien léger pour notre centre, on est en train d'appeler le SAMU", "le doc veut vérifier l'état de tout le monde"
            ],
            "Transports": [
                "le trafic est totalement interrompu sur ma ligne", "incident voyageur majeur bloque les rames", 
                "panne de signalisation paralyse le réseau", "un colis suspect retient mon train",
                "travaux imprévus sur les voies", "accident sur la voie",
                "le bus de remplacement est en panne", "une porte est bloquée, le metro ne part pas",
                "incident technique majeur sur les voies", "plus aucune rame ne circule avant un moment",
                "on est évacués de la station pour une alerte fumée", "le parking est saturé et personne ne peut sortir"
            ],
            "Voiture": [
                "ma batterie est totalement à plat, j'attends des câbles", "j'ai un pneu dégonflé je m'occupe de ce soucis",
                "une voiture me bloque totalement sur le parking du stade", "j'ai perdu mes clés dans l'herbe du terrain",
                "il y a un accident majeur qui bloque la sortie du complexe",
                "le parking a été fermé à clé par erreur avec ma voiture dedans", "j'ai le voyant de la reserve qui vient de s'allumer, je passe faire le plein",
                 "les flics bloquent l'accès à la rue pour une intervention",
                 "j'ai prêté mes clés à un gars parti aux douches"
            ],
            "Club": [
                "le coach nous retient pour un débriefing", "le président fait un discours interminable", 
                "corvée de rangement des maillots et des sacs", "le staff fait un point individuel",
                "réunion sur le calendrier de la saison", "inventaire du matos",
                "débriefing tactique sur le bord du terrain", "le bureau nous retient pour signer les licences",
                "réunion de crise sur le prochain déplacement", "on range les poteaux mobiles et les filets",
                "l'arbitre fait un point sur les règles au vestiaire", "on nettoie le local suite à une sanction"
            ]
        }

        # --- SYSTÈME DE CONCLUSIONS ÉTENDU ---
        if (cat in ["Club", "Solidarité"]) and res == "Victoire":
            conclusions = [
                "on profite un peu de cette gagne ensemble, je ne décolle pas tout de suite mais je fais au plus vite.",
                "impossible de partir en plein milieu des discours de victoire, je te rejoins dès que possible.",
                "l'ambiance est top après cette gagne, je reste un peu soutenir le groupe et j'arrive.",
                "on savoure ce résultat, le groupe a besoin de ce moment, je ne traîne pas trop."
            ]
        else:
            conclusions = [
                "je fais au plus vite pour rentrer dès que possible.",
                "je m'arrache dès que la situation est débloquée.",
                "je saute dans le premier trajet disponible.",
                "je fais au maximum pour limiter le retard.",
                "je te tiens au courant dès que je bouge, promis."
            ]
        
        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(conclusions)
            
        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

        # --- CALCUL CRÉDIBILITÉ ---
        base_success = 85 if ton == "Mielleux" else 60
        if cat == "Santé": base_success += 10
        if cat == "Transports" or cat == "Voiture": base_success -= 15
        credibility = max(5, min(99, base_success - (conso * 3) - (tension * 2)))
        st.markdown(f"<div class='credibility-gauge'>📊 Probabilité de succès : {credibility}%</div>", unsafe_allow_html=True)

# --- MODE ROULETTE ---
st.divider()
st.subheader("🎰 Mode Roulette")
if st.button("🎲 TENTER LE ALL-IN"):
    flash_list = [
        f"Serrure du vestiaire bloquée depuis 1 heure, on attend les doubles.",
        f"Un des gars à sa voiture qui a était prise par la fourrière, on attends avec lui qui puisse rentrer.",
        f"Plus d'eau chaude, on essaie de relancer la chaudière du stade.",
        f"Sac de maillots égaré juste depuis 1h, on fait l'inventaire complet.",
        f"On aide un pote à retrouver ses clefs de moto qu'il à perdu à coté du terrain.",
        f"La grille du complexe fermée par erreur, on est coincés à l'intérieur.",
        f"Fuite d'eau dans le local matos, on sauve les ballons en urgence.",
        f"Débriefing tactique improvisé qui s'éternise depuis 1h.",
        f"Le parking est bloqué par un camion de livraison en panne depuis 1h.",
        f"On doit attendre que le coach recense toutes les blessures.",
        f"Un gars a oublié son sac avec ses clefs, on attend avec lui qu'on lui rapporte.",
        f"Le club d'en face a un souci de transport, on les dépanne logistiquement.",
        f"Inondation dans les douches, on aide à éponger avant de partir.",
        f"On aide un pote à retrouver son alliance sur le terrain.",
        f"Le capitaine a égaré les clés du local, on fouille les vestiaires."
    ]
    st.balloons()
    st.markdown(f"<div class='excuse-box' style='border-color:#ff9f43;'>« Grosse galère : {random.choice(flash_list)} »</div>", unsafe_allow_html=True)

# --- GÉNÉRATEUR DE PREUVE ---
st.divider()
st.subheader("🖼️ Justificatif")
if st.button("📸 GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown(f'<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">⚠️ INFO TRAFIC RATP/SNCF</b><br><small style="color:#333">Incident technique à {h_prevu}h. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    elif cat == "Voiture":
        st.markdown(f'<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">📍 WAZE / MAPS</b><br><small style="color:#333">Accident signalé. Route saturée (+45 min). Heure d\'arrivée estimée décalée.</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">WhatsApp • Rugby </b><br><small style="color:#333">Coach : Réunion de fin de match obligatoire à {h_prevu}h. Présence indispensable pour débrief technique.</small></div>', unsafe_allow_html=True)
