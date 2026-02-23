import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (THÈME CLAIR & TEXTE NOIR PROFOND) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; color: #000000; }
    
    /* FORCE LE NOIR PARTOUT */
    label, p, span, div, h1, h2, h3, .stSelectbox label, .stNumberInput label, .stSlider label, [data-testid="stWidgetLabel"] p {
        color: #000000 !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebar"] { background-color: #e9ecef !important; }

    /* Boutons Rugby */
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4em; font-weight: bold; border: none; font-size: 1.1rem;
    }
    
    /* Boite d'excuse */
    .excuse-box { 
        background-color: #ffffff; padding: 20px; border-radius: 10px; 
        border: 3px solid #d62828; color: #000000 !important; font-style: italic; font-size: 1.1rem;
    }

    /* Dashboard ROI */
    .finops-card { 
        background-color: #ffffff; padding: 15px; border-radius: 12px; 
        border: 3px solid #000000; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { 
        font-size: 3rem; font-weight: bold; color: #d62828 !important; display: block; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ROI "FUN MAX" ---
with st.sidebar:
    st.header("📊 Business Case")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 1)
    
    # NOUVELLE FORMULE : Le plaisir augmente vite, la tension casse la marge
    # Score de base = Conso * 5 (Chaque verre rapporte gros)
    # Malus = Tension * 3
    roi_score = (conso * 5) - (tension * 3)
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:black; margin-bottom:0; font-weight:bold;">ROI FUN / RISQUE</p>
            <span class="metric-value">{roi_score}</span>
            <p style="font-size:0.8rem; color:#555;">Marge brute basée sur le plaisir net.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 30: st.success("🔥 RENTABILITÉ HISTORIQUE")
    elif roi_score > 10: st.info("📈 BUSINESS SAIN")
    elif roi_score >= 0: st.warning("⚖️ SEUIL DE RENTABILITÉ")
    else: st.error("📉 DÉFICIT OPÉRATIONNEL")

# --- CORPS DE L'APPLI ---
st.title("🏉 Générateur d'excuses by The Paddies")

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
    phrase_cible = "Le football est un sport de gentleman" # On varie un peu pour tester
    st.write(f"Vérification de sécurité. Recopiez : **{phrase_cible}**")
    reponse = st.text_input("Saisie :", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- GÉNÉRATION ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.error("Action bloquée : Réussissez le test de lucidité.")
    else:
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses,", "Pardonne-moi,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso et on fait bloc", "le capitaine a un énorme coup de mou", "le 9 est en plein burn-out moral", "un ancien est passé et ne va pas bien", "on soutient le soigneur qui a un coup dur"],
            "Santé": ["on attend l'ambulance pour un blessé", "un gars a fait un malaise après l'effort", "le soigneur demande de surveiller un gars KO", "suspicion de fracture pour mon binôme"],
            "Transports": ["le trafic est totalement interrompu", "un incident sur la voie bloque tout", "panne de signalisation paralyse le réseau", "un colis suspect retient mon train"],
            "Club": ["le coach nous retient pour un débriefing", "le président fait un discours interminable", "on est de corvée de rangement", "le staff fait un point individuel"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc.", "on reste pour l'épauler."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route.", "on attend l'avis du doc."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis.", "je patiente sur le quai."],
            "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné.", "faut finir ça."]
        }

        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne tous ensemble, c'est sacré."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">⚠️ Trafic interrompu</b><br><small style="color:#333">Incident sur votre ligne. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div style="background:#fff; padding:15px; border-radius:10px; border:2px solid #000;"><b style="color:black">WhatsApp • Coach</b><br><small style="color:#333">Débrief obligatoire. Personne ne sort avant la fin.</small></div>', unsafe_allow_html=True)
