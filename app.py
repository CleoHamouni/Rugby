import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #000000; }
    label, p, span, div, h1, h2, h3, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important; font-weight: 700 !important;
    }
    [data-testid="stSidebar"] { background-color: #e9ecef !important; border-right: 1px solid #ddd; }
    .stButton>button { 
        width: 100%; background-color: #28a745 !important; color: #ffffff !important; 
        border-radius: 12px; height: 3.5em; font-weight: bold; border: none; margin-top: 10px; font-size: 1.1rem;
    }
    .excuse-box { 
        background-color: #ffffff; padding: 20px; border-radius: 10px; 
        border: 3px solid #28a745; color: #000000 !important; font-style: italic; font-size: 1.1rem;
    }
    .finops-card { 
        background-color: #ffffff; padding: 15px; border-radius: 12px; 
        border: 3px solid #000000; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 3rem; font-weight: bold; color: #28a745 !important; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ROI ---
with st.sidebar:
    st.header("📊 Ratio Fun / Risque")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 1)
    roi_score = (conso * 5) - (tension * 3)
    st.markdown(f"""<div class="finops-card"><p style="color:black; margin-bottom:0;">ROI FUN / RISQUE</p><span class="metric-value">{roi_score}</span></div>""", unsafe_allow_html=True)

# --- CORPS DE L'APPLI ---
st.title("🏉 Générateur d'excuses by The Paddies")
col1, col2 = st.columns(2)
with col1:
    cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
    ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
with col2:
    h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
    res = st.selectbox("Résultat match :", ["Victoire", "Défaite", "Nul"])

# --- TEST DE LUCIDITÉ ---
lucidite_ok = True
if conso > 5:
    st.divider()
    phrase_cible = "Le ballon est ovale"
    st.write(f"Vérification requise. Recopiez : **{phrase_cible}**")
    reponse = st.text_input("Saisie :", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- GÉNÉRATION CLASSIQUE ---
st.divider()
if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.error("Action bloquée : Réussissez le test de lucidité.")
    else:
        intros = {
            "Mielleux": ["Désolé pour les {h}h,", "Toutes mes excuses,", "Je m'en veux pour les {h}h,", "Vraiment navré pour le retard de {h}h,", "Pardonne-moi, je rate le coche de {h}h,"],
            "Râleur": ["Ça me gonfle pour les {h}h,", "Encore un plan galère, je serai jamais là à {h}h,", "Marre d'être bloqué alors que je devais être là à {h}h,", "Toujours sur moi que ça tombe pour les {h}h,", "C'est n'importe quoi cette organisation pour {h}h,"],
            "Factuel": ["Bloqué pour {h}h.", "Retard confirmé pour l'heure de {h}h.", "Coincé, impossible pour {h}h.", "Imprévu technique pour {h}h."]
        }
        actions = {
            "Solidarité": [
                "un pote a un gros souci et on fait bloc", "le capitaine a un énorme coup de mou post-match", 
                "le 9 est en plein burn-out moral", "un ancien ne va pas bien du tout",
                "on soutient le soigneur qui a un coup dur", "un gars vient de se faire larguer, on l'épaule",
                "on discute avec le petit nouveau qui est démoralisé", "le groupe est mobilisé pour un pote qui a un pépin familial",
                "on fait bloc autour d'un gars qui a une mauvaise nouvelle", "on attend la famille d'un joueur qui a un souci"
            ],
            "Santé": [
                "on attend l'ambulance pour un blessé sérieux", "un gars a fait un malaise après l'effort", 
                "le soigneur me demande de surveiller un gars KO", "suspicion de fracture pour mon binôme",
                "protocole commotion en cours pour un joueur", "on gère une grosse entorse au vestiaire",
                "le médecin du club fait passer des tests de sécurité", "on attend les pompiers pour un choc sévère",
                "un joueur s'est ouvert l'arcade, on attend les points", "je reste avec un gars qui a une chute de tension"
            ],
            "Transports": [
                "le trafic est totalement interrompu sur ma ligne", "incident voyageur majeur bloque les rames", 
                "panne de signalisation paralyse le réseau", "un colis suspect retient mon train",
                "travaux de nuit imprévus sur les voies", "accident sur la voie express",
                "le bus de remplacement est en panne", "une porte est bloquée, le train ne part pas",
                "incident technique majeur sur les voies SNCF", "plus aucune rame ne circule avant un moment"
            ],
            "Club": [
                "le coach nous retient pour un débriefing", "le président fait un discours interminable", 
                "corvée de rangement des maillots et des sacs", "le staff fait un point individuel",
                "réunion sur le calendrier de la saison", "inventaire du matos de l'école de rugby",
                "débriefing tactique sur le bord du terrain", "le bureau nous retient pour signer les licences",
                "réunion de crise sur le prochain déplacement", "on range les poteaux mobiles et les filets"
            ]
        }
        
        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        
        if (cat in ["Club", "Solidarité"]) and res == "Victoire":
            c = f"on savoure cette gagne ensemble, je ne décolle pas tout de suite."
        else:
            c = f"je fais au plus vite pour rentrer dès que possible après {h_prevu}h."
            
        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

# --- MODE ROULETTE ---
st.divider()
st.subheader("🎰 Mode Roulette")
if st.button("🎲 TENTER LE ALL-IN"):
    flash_list = [
        f"Serrure du vestiaire bloquée à {h_prevu}h, on attend les doubles.",
        f"Le bus adverse est embourbé, on aide à pousser pour libérer le parking.",
        f"Plus d'eau chaude, on essaie de relancer la chaudière du club avec le staff.",
        f"Sac de maillots égaré juste avant {h_prevu}h, on fait l'inventaire complet.",
        f"On aide un pote à retrouver son alliance sur le terrain à la frontale.",
        f"Grille du complexe fermée par erreur, on est coincés à l'intérieur.",
        f"Fuite d'eau dans le local matos, on sauve les ballons en urgence.",
        f"Débriefing tactique improvisé qui s'éternise depuis {h_prevu}h.",
        f"Le parking est bloqué par un camion de livraison en panne à {h_prevu}h.",
        f"On doit attendre que le soigneur valide la sortie de tout le monde.",
        f"Un gars a oublié son sac dans ma voiture, je l'attends pour lui rendre.",
        f"Le club d'en face a un souci de transport, on les dépanne logistiquement.",
        f"Inondation dans les douches, on aide à éponger avant de partir."
    ]
    st.balloons()
    st.markdown(f"<div class='excuse-box' style='border-color:#ff9f43;'>« Grosse galère : {random.choice(flash_list)} »</div>", unsafe_allow_html=True)

# --- GÉNÉRATEUR DE PREUVE ---
st.divider()
st.subheader("🖼️ Justificatif")
if st.button("📸 GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown(f'<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">⚠️ INFO TRAFIC</b><br><small style="color:#333">Incident technique à {h_prevu}h. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">WhatsApp • Rugby Loisir</b><br><small style="color:#333">Coach : Réunion de fin de match obligatoire à {h_prevu}h. Présence indispensable.</small></div>', unsafe_allow_html=True)
