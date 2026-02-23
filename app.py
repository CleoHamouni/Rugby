import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (LISIBILITÉ MAXIMALE & COULEURS CORRIGÉES) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #000000; }
    
    /* FORCE LE NOIR SUR LES LABELS ET TEXTES */
    label, p, span, div, h1, h2, h3, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important; font-weight: 700 !important;
    }
    
    [data-testid="stSidebar"] { background-color: #e9ecef !important; border-right: 1px solid #ddd; }

    /* BOUTONS VERTS AVEC TEXTE BLANC */
    .stButton>button { 
        width: 100%; 
        background-color: #28a745 !important; /* VERT */
        color: #ffffff !important; /* BLANC */
        border-radius: 12px; 
        height: 3.5em; 
        font-weight: bold; 
        border: none; 
        margin-top: 10px;
        font-size: 1.1rem;
    }

    /* Boite d'excuse */
    .excuse-box { 
        background-color: #ffffff; padding: 20px; border-radius: 10px; 
        border: 3px solid #28a745; color: #000000 !important; font-style: italic; font-size: 1.1rem;
    }

    /* Dashboard ROI */
    .finops-card { 
        background-color: #ffffff; padding: 15px; border-radius: 12px; 
        border: 3px solid #000000; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 3rem; font-weight: bold; color: #28a745 !important; display: block; }
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
            "Solidarité": ["un pote a un gros souci et on fait bloc", "le capitaine a un énorme coup de mou", "le 9 est en plein burn-out moral", "un ancien ne va pas bien du tout", "on soutient le soigneur qui a un coup dur", "un joueur a un souci familial urgent"],
            "Santé": ["on attend l'ambulance pour un blessé", "un gars a fait un malaise", "le soigneur demande de surveiller un gars KO", "suspicion de fracture pour mon binôme", "protocole commotion en cours", "le doc fait passer des tests de sécurité"],
            "Transports": ["le trafic est interrompu", "incident voyageur majeur", "panne de signalisation", "colis suspect retient mon train", "travaux de nuit imprévus", "accident sur la voie express"],
            "Club": ["le coach nous retient pour un débriefing", "le président fait un discours interminable", "corvée de rangement des maillots", "le staff fait un point individuel", "réunion sur le calendrier", "inventaire du matos"]
        }
        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = "on savoure cette gagne ensemble." if (cat in ["Club", "Solidarité"] and res == "Victoire") else "je rentre dès que possible."
        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

# --- MODE ROULETTE ---
st.divider()
st.subheader("🎰 Mode Roulette")
if st.button("🎲 TENTER LE ALL-IN"):
    flash_list = [
        "La serrure du vestiaire est bloquée, on attend les doubles.",
        "Le bus adverse est embourbé, on aide à pousser.",
        "Plus d'eau chaude, on essaie de relancer la chaudière.",
        "Sac de maillots égaré, on fait l'inventaire complet.",
        "On aide un pote à retrouver son alliance sur le terrain.",
        "Grille du complexe fermée par erreur, on attend les clés.",
        "Fuite d'eau dans le local matos, on sauve les ballons.",
        "Débriefing improvisé sur le bord du terrain.",
        "Parking bloqué par un camion de livraison.",
        "Soigneur a oublié sa trousse sur le terrain annexe.",
        "Rangement des poteaux mobiles et du matos école de rugby.",
        "Souci de transport pour les adversaires, on dépanne."
    ]
    st.balloons()
    st.markdown(f"<div class='excuse-box' style='border-color:#ff9f43;'>« Grosse galère : {random.choice(flash_list)} »</div>", unsafe_allow_html=True)

# --- GÉNÉRATEUR DE PREUVE (RÉINTÉGRÉ) ---
st.divider()
st.subheader("🖼️ Justificatif")
if st.button("📸 GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">⚠️ INFO TRAFIC</b><br><small style="color:#333">Incident technique sur votre ligne. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">WhatsApp • Rugby Loisir</b><br><small style="color:#333">Coach : Réunion de fin de match obligatoire au vestiaire pour tout le monde. Personne ne sort.</small></div>', unsafe_allow_html=True)
