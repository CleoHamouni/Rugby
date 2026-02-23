import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* FIX VISIBILITÉ SLIDERS : Texte noir sur bandeau blanc */
    div[data-testid="stWidgetLabel"] p, 
    .stSlider label {
        color: #000000 !important; 
        font-weight: 900 !important;
        background-color: #ffffff; 
        padding: 3px 12px;
        border-radius: 8px;
        display: inline-block;
        margin-bottom: 5px;
    }

    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4.5em; font-weight: bold; border: none;
    }
    
    .excuse-box { 
        background-color: #1c2128; padding: 20px; border-radius: 10px; 
        border-left: 6px solid #d62828; color: #f0f6fc !important; font-style: italic;
    }

    .finops-card { 
        background-color: #000; padding: 15px; border-radius: 12px; 
        border: 2px solid #d62828; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #d62828 !important; display: block; }
    .roi-detail { font-size: 0.8rem; color: #888; margin-top: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ROI PLAISIR ---
with st.sidebar:
    st.header("📊 Business Case")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    # Nouvelle Formule : Plaisir (Conso) vs Coût du Risque (Tension)
    # On multiplie la conso par 2 pour qu'elle pèse lourd dans le plaisir
    # On retire la tension au carré pour simuler une crise exponentielle
    roi_score = (conso * 2) - (tension * 1.5)
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:white; margin-bottom:0; font-weight:bold;">ROI PLAISIR / RISQUE</p>
            <span class="metric-value">{roi_score:.1f}</span>
            <p class="roi-detail">Objectif : Maximiser le plaisir sans exploser le risque.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 10:
        st.success("🔥 SOIRÉE LÉGENDAIRE")
    elif roi_score > 0:
        st.warning("⚖️ RENTABILITÉ CORRECTE")
    else:
        st.error("📉 DÉFICIT DE FUN / RISQUE TROP HAUT")

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

# --- MOTEUR D'EXCUSES ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.warning("Action bloquée : Réussissez le test de lucidité.")
    else:
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses,", "Je m'en veux terriblement,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso et on fait bloc", "le capitaine a un énorme coup de mou", "le 9 est en plein burn-out moral", "un ancien est passé et ne va pas bien", "on soutient le soigneur qui a un coup dur"],
            "Santé": ["on attend l'ambulance pour un coéquipier blessé", "un gars a fait un malaise après l'effort", "le soigneur demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade", "suspicion de fracture pour mon binôme"],
            "Transports": ["le trafic est totalement interrompu sur ma ligne", "un incident sur la voie bloque tout", "panne de signalisation", "un colis suspect retient mon train", "travaux de nuit commencés plus tôt"],
            "Club": ["le coach nous retient pour un débriefing obligatoire", "le président fait un discours interminable", "on est de corvée de rangement", "l'arbitre explique ses choix au bar", "le staff fait un point individuel"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route.", "on attend l'avis du doc."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis.", "je patiente sur le quai."],
            "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "faut finir ça."]
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
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">WhatsApp • Rugby</b><br><small style="color:#ddd">Coach : Débrief obligatoire. Personne ne sort.</small></div>', unsafe_allow_html=True)
