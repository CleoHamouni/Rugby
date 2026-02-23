import streamlit as st
import random
import time

# Configuration de la page
st.set_page_config(page_title="Rugby Stealth Pro", page_icon="🏉", layout="wide")

# --- STYLE CSS MASTER ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* Boutons */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 8px; 
        height: 3.5em; 
        font-weight: bold; 
        border: none;
        font-size: 18px;
    }
    
    /* Boite d'excuse */
    .excuse-box { 
        background-color: #1c2128; 
        padding: 20px; 
        border-radius: 10px; 
        border-left: 6px solid #d62828; 
        color: #f0f6fc; 
        font-style: italic; 
        font-size: 1.2em;
    }

    /* FinOps Dashboard */
    .finops-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        text-align: center;
        margin-bottom: 20px;
    }
    .metric-value { font-size: 32px; font-weight: bold; color: #d62828; }
    
    /* Preuve Notification */
    .proof-box {
        background-color: #000000;
        border-radius: 15px;
        padding: 15px;
        font-family: -apple-system, sans-serif;
        max-width: 300px;
        margin: 10px auto;
        border: 1px solid #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD FINOPS (Hardis Tech Services Style) ---
with st.sidebar:
    st.header("📊 Dashboard FinOps")
    st.write("Optimisation du ROI de la 3ème mi-temps")
    
    consommation = st.slider("Unités consommées (bières)", 0, 15, 2)
    tension = st.slider("Tension domestique estimée (1-10)", 1, 10, 3)
    
    # Algorithme de ROI : Score sur 20
    # On dégrade le score selon la conso et la tension de départ
    roi_score = max(0, 20 - (consommation * 1.2) - (tension * 1.5))
    
    st.markdown(f"""
        <div class="finops-card">
            <small>SCORE DE RENTABILITÉ (ROI)</small><br/>
            <span class="metric-value">{roi_score:.1f}/20</span>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 14:
        st.success("✅ OPTIMISÉ : Continuez l'investissement.")
    elif roi_score > 8:
        st.warning("⚖️ BREAK-EVEN : Envisagez une sortie prochaine.")
    else:
        st.error("🚨 DÉFICIT : Risque de faillite personnelle. RENTREZ.")

# --- CORPS DE L'APPLI ---
st.title("🏉 Third Time - Master Edition")

col_main, col_proof = st.columns([2, 1])

with col_main:
    st.subheader("1. Paramètres de l'IA")
    c1, c2 = st.columns(2)
    with c1:
        cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
        ton = st.selectbox("Ton souhaité :", ["Mielleux", "Râleur", "Factuel"])
    with c2:
        h_prevu = st.number_input("Heure annoncée :", 0, 23, 19)
        res = st.selectbox("Résultat du match :", ["Victoire", "Défaite", "Nul"])

    # --- TEST DE LUCIDITÉ ---
    st.subheader("2. Check de Lucidité (Anti-Cramage)")
    phrase_secu = "L'intelligence artificielle optimise la gouvernance des données."
    st.caption(f"Pour débloquer les tons complexes, recopiez : **{phrase_secu}**")
    user_test = st.text_input("Vérification orthographique :")
    
    est_lucide = (user_test.strip() == phrase_secu)

    # --- MOTEUR DE GÉNÉRATION ---
    def generate_master_excuse(categorie, ton_choisi, resultat, heure, lucide):
        if not lucide and user_test != "":
            st.warning("⚠️ Echec du test. Mode 'Sécurité' activé : message neutre et court.")
            return f"Bloqué au club suite à un imprévu ({categorie}). Je vais rater les {heure}h, je fais au plus vite."

        # INTROS
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Je fais au plus vite mais pour {h}h c'est mort,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,", "Je vais encore arriver une plombe après {h}h,"],
            "Factuel": ["Bloqué.", "Retard prévu.", "Je ne serai pas là pour {h}h.", "Coincé.", "Changement de programme."]
        }
        
        # ACTIONS (15 par cat)
        actions_db = {
            "Solidarité": ["un petit nouveau est en larmes", "le talonneur s'est fait larguer", "le capitaine a un coup de mou", "un gars a de gros soucis perso", "le 9 est en burn-out moral", "un ancien est passé et ne va pas bien", "un pote a perdu ses clés", "on soutient le soigneur", "le 2ème ligne a une mauvaise nouvelle", "un gars est en crise de nerfs", "un joueur veut arrêter le rugby", "un pote est effondré par son match", "on aide un gars sans voiture", "un coéquipier a un drame familial", "on discute avec le 7 démoralisé"],
            "Santé": ["un pote a pris un énorme choc", "un gars a fait un malaise", "on attend l'ambulance pour le 3", "le soigneur surveille un gars KO", "un joueur s'est ouvert l'arcade", "suspicion de fracture pour le 10", "le 15 est désorienté", "épaule déboitée pour un gars", "on attend les pompiers", "blessure grave au vestiaire", "plaie qui ne s'arrête pas", "on aide pour un trauma", "le kiné a besoin d'aide", "hypothermie sous la douche", "un gars respire mal"],
            "Transports": ["métro totalement à l'arrêt", "colis suspect dans ma rame", "panne de signalisation", "incident voyageur", "grève surprise", "bagage abandonné", "coupure de courant", "bloqué entre deux stations", "malaise voyageur dans le train", "bus de substitution en panne", "porte bloquée en station", "travaux de nuit précoces", "incident technique voies", "évacuation du quai", "attente du feu vert PC"],
            "Club": ["coach a verrouillé pour débrief", "président fait un discours", "corvée de rangement", "arbitre explique ses choix au bar", "réunion administrative", "signature des licences", "point individuel avec le staff", "nettoyage buvette (sanction)", "préparation du tournoi", "capitaine bloque la sortie", "inventaire du matos", "attente sponsors photo", "réunion de crise discipline", "aide urgente au secrétaire", "point médical obligatoire"]
        }
        
        # CONCLUSIONS (10 par cat)
        concls_db = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler.", "je rentre dès que ça s'apaise.", "le staff demande qu'on reste.", "on ne lâche personne.", "on attend sa famille.", "le capitaine insiste.", "on essaie de le changer les idées.", "moment dur pour le groupe."],
            "Santé": ["on attend les secours.", "on attend l'avis du doc.", "je reste tant qu'il n'est pas stable.", "le soigneur a besoin d'aide.", "on surveille l'évolution.", "SAMU en route.", "on met de la glace.", "le doc veut un témoin du choc.", "on l'aide à s'habiller.", "je le ramène plus tard."],
            "Transports": ["aucune info sur la reprise.", "je cherche un itinéraire bis.", "on patiente sur le quai.", "pas de taxi ni Uber dispo.", "bloqué à l'intérieur.", "retard indéterminé.", "je tente de finir à pied.", "quartier bouclé par police.", "train dans une éternité.", "bloqué au guichet pass."],
            "Club": ["personne ne sort.", "sinon sanction mardi.", "obligation du président.", "je tente de m'échapper.", "protocole habituel.", "coach a les clés.", "faut finir le débrief.", "mal vu de bouger.", "réquisition logistique.", "débrief fin de match."]
        }

        # Assemblage
        i = random.choice(intros[ton_choisi]).format(h=heure)
        a = random.choice(actions_db[categorie])
        c = random.choice(concls_db[categorie])
        
        # Ajout résultat
        if categorie in ["Solidarité", "Club"] and resultat == "Victoire":
            c = "on savoure cette gagne tous ensemble."
            
        return f"{i} {a}, {c}"

    if st.button("🚀 GÉNÉRER L'EXCUSE MASTER"):
        if user_test == "" and ton != "Factuel":
            st.error("Prouve ta lucidité (Test de Lucidité) pour accéder aux messages complexes.")
        else:
            with st.spinner('Analyse des risques...'):
                time.sleep(1)
                final_msg = generate_master_excuse(cat, ton, res, h_prevu, est_lucide)
                st.markdown(f"<div class='excuse-box'>« {final_msg} »</div>", unsafe_allow_html=True)
                
                # Jauge de risque
                risks = {"Transports": 20, "Club": 50, "Solidarité": 75, "Santé": 95}
                st.progress(risks[cat]/100)
                st.caption(f"Indice de danger : {risks[cat]}% (Prudence conseillée)")

with col_proof:
    st.subheader("🖼️ Preuve Visuelle")
    if st.button("Générer Notification"):
        if cat == "Transports":
            st.markdown("""
                <div class="proof-box">
                    <div style="font-size:10px; color:#888;">INFO TRAFIC • Maintenant</div>
                    <div style="font-weight:bold; font-size:13px;">⚠️ Trafic Interrompu</div>
                    <div style="font-size:12px;">Colis suspect en gare. Reprise estimée : Inconnue.</div>
                </div>
            """, unsafe_allow_html=True)
        elif cat == "Club":
            st.markdown("""
                <div class="proof-box">
                    <div style="font-size:10px; color:#888;">WHATSAPP • Rugby Club</div>
                    <div style="font-weight:bold; font-size:13px;">Coach 🏉</div>
                    <div style="font-size:12px;">Réunion obligatoire au vestiaire tout de suite.</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Catégorie ne nécessitant pas de preuve visuelle.")

st.divider()
st.caption(f"Utilisateur : Cléo HAMOUNI | Mode : Hardis Stealth Pro")
