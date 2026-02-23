import streamlit as st
import random

# Configuration optimisée mobile
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (LE "MARTEAU-PIQUEUR" POUR LE BLANC) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* Ciblage ultra-précis des labels des sliders et autres widgets */
    div[data-testid="stWidgetLabel"] p, 
    .stSlider label, 
    .stSelectbox label, 
    .stNumberInput label,
    label { 
        color: white !important; 
        font-weight: bold !important;
        -webkit-text-fill-color: white !important; /* Pour certains navigateurs mobiles */
    }

    /* Boutons mobiles */
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4em; font-weight: bold; font-size: 1.2rem; margin-top: 10px;
    }
    
    /* Boîte d'excuse */
    .excuse-box { 
        background-color: #1c2128; padding: 20px; border-radius: 10px; 
        border-left: 6px solid #d62828; color: #f0f6fc !important; font-style: italic; font-size: 1.1em;
    }

    /* Dashboard ROI */
    .finops-card { 
        background-color: #000; padding: 15px; border-radius: 12px; 
        border: 2px solid #d62828; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #d62828 !important; display: block; }
    
    /* Arrière-plan des curseurs pour visibilité */
    .stSlider [data-baseweb="slider"] {
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ---
with st.sidebar:
    st.header("📊 Dashboard")
    # Les labels ici devraient maintenant être blancs
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    roi_score = max(0, 20 - (conso * 1.5) - (tension * 1.5))
    
    st.markdown(f"""
        <div class="finops-card">
            <small style="color:white;">ROI DE LA SOIRÉE</small>
            <span class="metric-value">{roi_score:.1f}/20</span>
        </div>
    """, unsafe_allow_html=True)

# --- CORPS DE L'APPLI ---
st.title("🏉 Third Time")

cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
res = st.selectbox("Résultat match :", ["Victoire", "Défaite", "Nul"])

# --- TEST DE LUCIDITÉ (> 5) ---
lucidite_ok = True
if conso > 5:
    st.divider()
    st.subheader("🚨 Check de Lucidité")
    phrase_cible = "Le ballon est ovale"
    st.write(f"Recopiez : **{phrase_cible}**")
    reponse = st.text_input("Vérification :", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- GÉNÉRATION ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.warning("Action bloquée : Réussissez le test de lucidité.")
    else:
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses,", "Je m'en veux terriblement,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso", "le capitaine a un coup de mou", "le 9 est en burn-out moral", "un gars vient de se faire larguer", "on soutient le soigneur qui a un coup dur"],
            "Santé": ["on attend l'ambulance pour un blessé", "un gars a fait un malaise", "le soigneur me demande de surveiller un gars KO", "suspicion de fracture pour mon binôme"],
            "Transports": ["le trafic est interrompu sur ma ligne", "un incident voyageur bloque tout", "panne de signalisation", "un colis suspect retient mon train"],
            "Club": ["le coach nous retient pour un débriefing", "le président fait un discours interminable", "corvée de rangement obligatoire", "le staff fait un point individuel"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route.", "on attend l'avis du doc."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis.", "je tente de finir à pied."],
            "Club": ["personne ne sort avant la fin.", "sinon sanction mardi.", "faut finir ça avant de partir."]
        }

        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne ensemble."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><small style="color:#aaa">INFO TRAFIC</small><br><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Incident sur votre ligne.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><small style="color:#aaa">WhatsApp</small><br><b style="color:white">Coach 🏉</b><br><small style="color:#ddd">Débrief obligatoire. Personne ne sort.</small></div>', unsafe_allow_html=True)
