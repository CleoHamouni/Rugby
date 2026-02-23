import streamlit as st
import random

# Configuration optimisée mobile
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (VISIBILITÉ & MOBILE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    
    /* FIX VISIBILITÉ : Force les labels des sliders en NOIR sur bandeau clair */
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

    /* Boutons larges pour usage tactile */
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4.5em; font-weight: bold; font-size: 1.1rem; margin-top: 10px;
        border: none;
    }
    
    /* Boîte d'excuse stylisée */
    .excuse-box { 
        background-color: #1c2128; padding: 20px; border-radius: 10px; 
        border-left: 6px solid #d62828; color: #f0f6fc !important; font-style: italic;
        font-size: 1.1rem; line-height: 1.5;
    }

    /* Dashboard ROI */
    .finops-card { 
        background-color: #000; padding: 15px; border-radius: 12px; 
        border: 2px solid #d62828; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { 
        font-size: 2.5rem; font-weight: bold; color: #d62828 !important; display: block; 
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ---
with st.sidebar:
    st.header("📊 Dashboard")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    roi_score = max(0, 20 - (conso * 1.5) - (tension * 1.5))
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:white; margin-bottom:0; font-weight:bold;">ROI DE LA SOIRÉE</p>
            <span class="metric-value">{roi_score:.1f}/20</span>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score < 7:
        st.error("🚨 Risque d'insolvabilité domestique élevé.")

# --- CORPS DE L'APPLI ---
st.title("🏉 Third Time")

# Paramètres de l'IA
cat = st.selectbox("Catégorie :", ["Solidarité", "Santé", "Transports", "Club"])
ton = st.selectbox("Ton :", ["Mielleux", "Râleur", "Factuel"])
h_prevu = st.number_input("Heure prévue :", 0, 23, 19)
res = st.selectbox("Résultat match :", ["Victoire", "Défaite", "Nul"])

# --- TEST DE LUCIDITÉ (SEUIL 5 VERRES) ---
lucidite_ok = True
if conso > 5:
    st.divider()
    st.subheader("🚨 Check de Lucidité")
    phrase_cible = "Le ballon est ovale"
    st.write(f"Sécurité active (>5 unités). Recopiez : **{phrase_cible}**")
    reponse = st.text_input("Vérification :", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- MOTEUR D'EXCUSES COMPLET ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.warning("Action bloquée : Réussissez le test de lucidité.")
    else:
        # Intros
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé.", "Changement de programme."]
        }
        
        # Actions (Moteur étendu)
        actions = {
            "Solidarité": [
                "un pote a un gros souci perso et on fait bloc", "le capitaine a un énorme coup de mou", 
                "le 9 est en plein burn-out moral", "un ancien est passé et ne va pas bien", 
                "un gars vient de se faire larguer au vestiaire", "on soutient le soigneur qui a un coup dur",
                "un coéquipier a perdu ses clés et on l'aide", "on discute avec le 7 qui est démoralisé",
                "on attend la famille d'un gars qui a un pépin", "le groupe est mobilisé pour un pote"
            ],
            "Santé": [
                "on attend l'ambulance pour un coéquipier blessé", "un gars a fait un malaise après l'effort",
                "le soigneur me demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade",
                "suspicion de fracture pour mon binôme", "le 10 est totalement désorienté après un tampon",
                "un gars s'est déboîté l'épaule", "on attend les pompiers pour un joueur",
                "le doc veut faire un check-up complet avant de libérer le gars", "protocole commotion en cours"
            ],
            "Transports": [
                "le trafic est totalement interrompu sur ma ligne", "un incident sur la voie bloque tout",
                "une panne de signalisation paralyse le réseau", "un colis suspect retient mon train à quai",
                "le bus de substitution est aussi en panne", "une porte est bloquée, le train ne part pas",
                "travaux de nuit commencés plus tôt que prévu", "incident technique majeur sur les voies",
                "on est évacués de la station là", "plus aucune rame ne circule"
            ],
            "Club": [
                "le coach nous retient pour un débriefing obligatoire", "le président fait un discours interminable",
                "on est de corvée de rangement pour l'équipe", "l'arbitre explique ses choix au bar",
                "on doit signer les licences de toute l'équipe", "le staff fait un point individuel",
                "on nettoie la buvette suite à une sanction", "le capitaine a verrouillé les sorties pour parler",
                "réunion de crise sur le calendrier", "inventaire du matos de l'école de rugby"
            ]
        }
        
        # Conclusions
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler.", "je rentre dès que ça s'apaise."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route, je reste à côté.", "on attend l'avis définitif du doc.", "je l'accompagne jusqu'à sa voiture."],
            "Transports": ["aucune info sur la reprise du trafic.", "je cherche un itinéraire bis.", "on nous demande de patienter sur le quai.", "je tente de finir le trajet à pied."],
            "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "c'est une obligation du président.", "faut finir ça avant de pouvoir partir."]
        }

        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        
        # Condition Victoire
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne tous ensemble, c'est sacré."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Incident sur votre ligne. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div style="background:#000; padding:15px; border-radius:10px; border:1px solid #333;"><b style="color:white">WhatsApp • Rugby</b><br><small style="color:#ddd">Coach : Débrief obligatoire au vestiaire. Personne ne sort.</small></div>', unsafe_allow_html=True)
    else:
        st.info("Pas de preuve nécessaire pour cette catégorie.")
