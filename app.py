import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (STRATÉGIE DE CONTRASTE INVERSÉE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* On force les labels des sliders en BLANC pour être sûr qu'ils ressortent sur le fond noir de l'appli */
    .stSlider label, [data-testid="stWidgetLabel"] p {
        color: white !important;
        font-weight: bold !important;
    }

    /* Dashboard ROI : On met un fond sombre ROUGE/NOIR pour que le texte BLANC soit lisible */
    .finops-card { 
        background-color: #2a0505; /* Rouge très sombre */
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #d62828; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    
    .metric-value { 
        font-size: 2.5rem; 
        font-weight: bold; 
        color: #ff4b4b !important; /* Rouge clair pour le score */
        display: block; 
    }

    /* Boutons larges pour mobile */
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4em; font-weight: bold; margin-top: 10px;
    }
    
    .excuse-box { 
        background-color: #1c2128; padding: 20px; border-radius: 10px; 
        border-left: 6px solid #d62828; color: #f0f6fc !important; font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ---
with st.sidebar:
    st.header("📊 Dashboard")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    roi_score = max(0, 20 - (conso * 1.5) - (tension * 1.5))
    
    # Ici, même si le texte est blanc, le fond #2a0505 le rendra lisible
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:white; margin-bottom:0; font-weight:bold;">ROI DE LA SOIRÉE</p>
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
            "Mielleux": ["Je suis navré pour les {h}h,", "Toutes mes excuses,", "Pardonne-moi,"],
            "Râleur": ["Ça me gonfle,", "Encore une galère,", "Marre d'être bloqué,"],
            "Factuel": ["Bloqué.", "Retard prévu.", "Coincé."]
        }
        actions = {
            "Solidarité": ["un pote a un gros souci perso", "le capitaine a un coup de mou", "le 9 est en burn-out moral"],
            "Santé": ["on attend l'ambulance pour un blessé", "un gars a fait un malaise", "le soigneur me demande de surveiller un gars KO"],
            "Transports": ["le trafic est interrompu", "un incident voyageur bloque tout", "panne de signalisation"],
            "Club": ["le coach nous retient pour un débriefing", "le président fait un discours", "corvée de rangement obligatoire"]
        }
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc.", "on reste pour l'épauler."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "on attend l'avis du doc."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis."],
            "Club": ["personne ne sort avant la fin.", "sinon sanction mardi."]
        }

        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne ensemble."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Incident sur votre ligne.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">Coach 🏉</b><br><small style="color:#ddd">Débrief obligatoire. Personne ne sort.</small></div>', unsafe_allow_html=True)
