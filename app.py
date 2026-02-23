import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (LE "BLANCO" TOTAL) ---
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp { background-color: #0e1117; color: white; }
    
    /* 1. FORCE LE BLANC SUR TOUT LE TEXTE (Labels, Sélecteurs, Chiffres) */
    label, p, span, div, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stWidgetLabel"] p {
        color: white !important;
        font-weight: bold !important;
        -webkit-text-fill-color: white !important;
    }

    /* 2. EXCEPTION POUR LES SLIDERS (On les garde en noir sur fond blanc comme tu aimais) */
    .stSlider label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        background-color: #ffffff;
        padding: 3px 12px;
        border-radius: 8px;
        -webkit-text-fill-color: #000000 !important;
    }

    /* 3. STYLE DES BOUTONS */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 12px; 
        height: 4.5em; 
        font-weight: bold; 
        border: none;
        font-size: 1.1rem;
    }
    
    /* 4. BOITE D'EXCUSE */
    .excuse-box { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #d62828; 
        color: #f0f6fc !important; 
        font-style: italic;
    }

    /* 5. DASHBOARD ROI */
    .finops-card { 
        background-color: #000; 
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #d62828; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    .metric-value { 
        font-size: 2.5rem; 
        font-weight: bold; 
        color: #d62828 !important; 
        display: block; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ROI PLAISIR ---
with st.sidebar:
    st.header("📊 Business Case")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    # ROI Plaisir vs Risque
    roi_score = (conso * 2) - (tension * 1.5)
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:white; margin-bottom:0; font-weight:bold;">ROI PLAISIR / RISQUE</p>
            <span class="metric-value">{roi_score:.1f}</span>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 10: st.success("🔥 SOIRÉE LÉGENDAIRE")
    elif roi_score > 0: st.warning("⚖️ RENTABILITÉ CORRECTE")
    else: st.error("📉 DÉFICIT DE FUN")

# --- CORPS DE L'APPLI ---
st.title("🏉 Third Time")

# Section 1 : Paramètres (Désormais bien blancs)
st.subheader("1. Paramètres")
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
        # Base de données d'excuses (Moteur complet)
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses,", "Je m'en veux terriblement,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso", "le capitaine a un coup de mou", "le 9 est en plein burn-out moral", "on soutient le soigneur qui a un coup dur"],
            "Santé": ["on attend l'ambulance pour un blessé", "un gars a fait un malaise", "le soigneur me demande de surveiller un gars KO"],
            "Transports": ["le trafic est interrompu sur ma ligne", "un incident voyageur bloque tout", "panne de signalisation"],
            "Club": ["le coach nous retient pour un débriefing", "le président fait un discours interminable", "corvée de rangement obligatoire"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis."],
            "Club": ["personne ne sort avant la fin.", "sinon sanction mardi."]
        }

        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne tous ensemble, c'est sacré."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Incident sur votre ligne.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">WhatsApp • Coach</b><br><small style="color:#ddd">Débrief obligatoire. Personne ne sort.</small></div>', unsafe_allow_html=True)
