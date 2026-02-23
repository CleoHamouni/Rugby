import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (LISIBILITÉ MAXIMALE NOIR SUR BLANC) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #000000; }
    label, p, span, div, h1, h2, h3, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important; font-weight: 700 !important;
    }
    [data-testid="stSidebar"] { background-color: #e9ecef !important; border-right: 1px solid #ddd; }
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 3.5em; font-weight: bold; border: none; margin-top: 10px;
    }
    div.stButton > button:first-child[kind="secondary"] {
        background-color: #1a1a1a !important; color: white !important;
    }
    .excuse-box { 
        background-color: #ffffff; padding: 20px; border-radius: 10px; 
        border: 3px solid #d62828; color: #000000 !important; font-style: italic; font-size: 1.1rem;
    }
    .finops-card { 
        background-color: #ffffff; padding: 15px; border-radius: 12px; 
        border: 3px solid #000000; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 3rem; font-weight: bold; color: #d62828 !important; display: block; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ROI ---
with st.sidebar:
    st.header("📊 Business Intel")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 1)
    roi_score = (conso * 5) - (tension * 3)
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:black; margin-bottom:0;">ROI FUN / RISQUE</p>
            <span class="metric-value">{roi_score}</span>
        </div>
    """, unsafe_allow_html=True)

# --- CORPS DE L'APPLI ---
st.title("🏉 Third Time")

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
            "Mielleux": ["Désolé pour les {h}h,", "Toutes mes excuses,", "Pardonne-moi,", "Je m'en veux pour les {h}h,", "Vraiment navré pour le retard,"],
            "Râleur": ["Ça me gonfle,", "Encore un plan galère,", "Marre d'être bloqué,", "Toujours sur moi que ça tombe,", "C'est n'importe quoi l'organisation,"],
            "Factuel": ["Bloqué.", "Retard confirmé.", "Coincé.", "Imprévu.", "Contretemps technique."]
        }
        actions = {
            "Solidarité": [
                "un pote a un gros souci et on fait bloc", "le capitaine a un énorme coup de mou", 
                "le 9 est en plein burn-out moral", "un ancien ne va pas bien du tout",
                "on soutient le soigneur qui a un coup dur", "on accompagne un gars qui n'a pas le moral",
                "un joueur a un souci familial urgent", "on fait une réunion de soutien pour le groupe"
            ],
            "Santé": [
                "on attend l'ambulance pour un blessé", "un gars a fait un malaise", 
                "le soigneur demande de surveiller un gars KO", "suspicion de fracture pour mon binôme",
                "protocole commotion en cours pour un joueur", "on gère une grosse entorse au vestiaire",
                "le médecin du club fait passer des tests de sécurité", "on attend les pompiers pour un choc sévère"
            ],
            "Transports": [
                "le trafic est totalement interrompu sur ma ligne", "incident voyageur majeur", 
                "panne de signalisation paralyse tout", "colis suspect retient mon train",
                "travaux de nuit imprévus sur les voies", "panne de secteur sur le réseau électrique",
                "le bus de remplacement est surchargé", "accident sur la voie express"
            ],
            "Club": [
                "le coach nous retient pour un débriefing", "le président fait un discours interminable", 
                "corvée de rangement des maillots et sacs", "le staff fait un point individuel",
                "réunion obligatoire sur le calendrier", "inventaire du matériel d'entraînement",
                "débriefing tactique sur le bord du terrain", "le bureau nous retient pour signer les licences"
            ]
        }
        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = "on savoure cette gagne ensemble." if (cat in ["Club", "Solidarité"] and res == "Victoire") else "je rentre dès que possible."
        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

# --- MODE ROULETTE ---
st.divider()
st.subheader("🎰 Mode Roulette (Excuse Flash)")

if st.button("🎲 TENTER LE ALL-IN", type="secondary"):
    flash_list = [
        "La serrure du vestiaire est bloquée, on attend le gars qui a les doubles.",
        "Le bus de l'équipe adverse est embourbé dans le parking, on aide à pousser.",
        "Plus d'eau chaude, la chaudière du club a sauté, on essaie de la relancer.",
        "Le sac de maillots a été égaré, on fait l'inventaire complet.",
        "On aide un coéquipier à retrouver son alliance perdue dans l'herbe.",
        "Le président a fermé la grille du complexe et il est parti avec les clés.",
        "Y'a une fuite d'eau géante dans le local matos, on sauve les ballons.",
        "Le coach a lancé un débriefing improvisé sur le bord du terrain.",
        "On attend que le parking se libère, un camion bloque la sortie.",
        "Le soigneur a oublié sa trousse sur le terrain annexe, on va la chercher.",
        "Un gars a oublié son sac dans ma voiture, je l'attends.",
        "On range les poteaux mobiles et le matos de l'école de rugby.",
        "Le club d'en face a un souci de transport, on les dépanne logistiquement."
    ]
    st.balloons()
    st.markdown(f"<div class='excuse-box' style='border-color:#ff9f43;'>« Grosse galère : {random.choice(flash_list)} »</div>", unsafe_allow_html=True)
