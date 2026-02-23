import streamlit as st
import random
import time

# Configuration
st.set_page_config(page_title="Rugby Stealth Pro", page_icon="🏉", layout="wide")

# --- STYLE CSS (CORRECTION DES CONTRASTES) ---
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp { background-color: #0e1117; color: white; }
    
    /* Correction pour tous les labels (Vérification, Heure, etc.) */
    label, .stMarkdown p, .stText {
        color: white !important;
        font-weight: 500;
    }

    /* Correction spécifique pour la barre latérale */
    section[data-testid="stSidebar"] .stMarkdown p, 
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] label {
        color: white !important;
    }

    /* Boutons */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 8px; 
        height: 3.5em; 
        font-weight: bold; 
        border: none;
    }
    
    /* Boite d'excuse */
    .excuse-box { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #d62828; 
        color: #f0f6fc !important; 
        font-style: italic; 
        font-size: 1.2em;
    }

    /* FinOps Dashboard dans la sidebar */
    .finops-card { 
        background-color: #161b22; 
        padding: 20px; 
        border-radius: 12px; 
        border: 1px solid #30363d; 
        text-align: center; 
        margin-bottom: 20px; 
    }
    
    /* Texte "Score de rentabilité" forcé en blanc */
    .finops-card small {
        color: #8b949e !important;
        font-weight: bold;
    }
    
    .metric-value { 
        font-size: 32px; 
        font-weight: bold; 
        color: #d62828 !important; 
    }

    /* Simulateur de notification */
    .proof-box { 
        background-color: #000000; 
        border-radius: 15px; 
        padding: 15px; 
        font-family: sans-serif; 
        max-width: 300px; 
        margin: 10px auto; 
        border: 1px solid #333; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ANALYTIQUE ---
with st.sidebar:
    st.header("📊 Dashboard")
    st.write("Optimisation de la soirée")
    
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension (1-10)", 1, 10, 3)
    
    # Calcul du ROI
    roi_score = max(0, 20 - (conso * 1.2) - (tension * 1.5))
    
    st.markdown(f"""
        <div class="finops-card">
            <small>SCORE DE RENTABILITÉ (ROI)</small><br/>
            <span class="metric-value">{roi_score:.1f}/20</span>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 14:
        st.success("✅ OPTIMISÉ")
    elif roi_score > 8:
        st.warning("⚖️ BREAK-EVEN")
    else:
        st.error("🚨 DÉFICIT CRITIQUE")

# --- CORPS DE L'APPLICATION ---
st.title("🏉 Third Time - Master Edition")

col_left, col_right = st.columns([2, 1])

with col_left:
    st.subheader("1. Configuration")
    c1, c2 = st.columns(2)
    with c1:
        cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
        ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
    with c2:
        h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
        res = st.selectbox("Résultat match :", ["Victoire", "Défaite", "Nul"])

    # --- TEST DE LUCIDITÉ ---
    st.subheader("2. Check de Lucidité")
    phrase_secu = "L'intelligence artificielle optimise la gouvernance des données."
    st.caption(f"Recopiez exactement : **{phrase_secu}**")
    user_test = st.text_input("Vérification :")
    est_lucide = (user_test.strip() == phrase_secu)

    # MOTEUR DE GÉNÉRATION
    def generate_excuse(categorie, ton_choisi, resultat, heure, lucide):
        if not lucide and user_test != "":
            return f"Bloqué au club pour {categorie}. Je vais rater les {heure}h, je fais au plus vite."

        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses,", "Je m'en veux terriblement,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu.", "Coincé.", "Changement de programme."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso", "le capitaine a un coup de mou", "le 9 est en burn-out moral", "un ancien ne va pas bien", "on aide un gars sans voiture"],
            "Santé": ["un pote a pris un énorme choc", "un gars a fait un malaise", "on attend l'ambulance pour le 3", "le soigneur surveille un gars KO", "un joueur s'est ouvert l'arcade"],
            "Transports": ["métro totalement à l'arrêt", "colis suspect dans ma rame", "panne de signalisation", "incident voyageur", "grève surprise"],
            "Club": ["coach a verrouillé pour débrief", "président fait un discours", "corvée de rangement", "réunion administrative", "le staff fait un point individuel"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler."],
            "Santé": ["on attend les secours.", "on attend l'avis du doc.", "je reste tant qu'il n'est pas stable."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis.", "on patiente sur le quai."],
            "Club": ["personne ne sort.", "sinon sanction mardi.", "faut finir le débrief."]
        }

        i = random.choice(intros[ton_choisi]).format(h=heure)
        a = random.choice(actions[categorie])
        c = random.choice(concls[categorie])
        
        if categorie in ["Solidarité", "Club"] and resultat == "Victoire":
            c = "on savoure cette victoire ensemble."
            
        return f"{i} {a}, {c}"

    if st.button("🚀 GÉNÉRER"):
        if user_test == "" and ton != "Factuel":
            st.error("Prouvez votre lucidité pour les messages complexes.")
        else:
            msg = generate_excuse(cat, ton, res, h_prevu, est_lucide)
            st.markdown(f"<div class='excuse-box'>« {msg} »</div>", unsafe_allow_html=True)
            risks = {"Transports": 20, "Club": 50, "Solidarité": 75, "Santé": 95}
            st.progress(risks[cat]/100)
            st.caption(f"Indice de risque : {risks[cat]}%")

with col_right:
    st.subheader("🖼️ Preuve")
    if st.button("Générer Notif"):
        if cat == "Transports":
            st.markdown('<div class="proof-box"><small style="color:#aaa">RATP • Maintenant</small><br><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Colis suspect. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
        elif cat == "Club":
            st.markdown('<div class="proof-box"><small style="color:#aaa">WhatsApp • Rugby</small><br><b style="color:white">Coach 🏉</b><br><small style="color:#ddd">Réunion obligatoire au vestiaire tout de suite.</small></div>', unsafe_allow_html=True)
        else:
            st.info("Pas de preuve nécessaire.")
