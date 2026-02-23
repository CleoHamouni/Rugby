import streamlit as st
import random

# Configuration optimisée mobile
st.set_page_config(page_title="Third Time", page_icon="🏉", layout="centered")

# --- STYLE CSS (MOBILE & CONTRASTES) ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: white; }
    label, .stMarkdown p, .stText, [data-testid="stHeader"], .stSelectbox label { color: white !important; }
    .stButton>button { 
        width: 100%; background-color: #d62828 !important; color: white !important; 
        border-radius: 12px; height: 4em; font-weight: bold; font-size: 1.2rem; margin-bottom: 10px;
    }
    .stTextInput input, .stNumberInput input { height: 3em; font-size: 1.1rem !important; }
    .excuse-box { 
        background-color: #1c2128; padding: 20px; border-radius: 10px; 
        border-left: 6px solid #d62828; color: #f0f6fc !important; font-style: italic; font-size: 1.1em; margin: 15px 0;
    }
    .finops-card { 
        background-color: #000; padding: 15px; border-radius: 12px; 
        border: 2px solid #d62828; text-align: center; margin-bottom: 20px; 
    }
    .metric-value { font-size: 2.5rem; font-weight: bold; color: #d62828 !important; display: block; }
    .proof-box { 
        background-color: #000000; border-radius: 15px; padding: 15px; 
        font-family: -apple-system, sans-serif; border: 1px solid #333; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR : DASHBOARD ---
with st.sidebar:
    st.header("📊 Dashboard")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    roi_score = max(0, 20 - (conso * 1.5) - (tension * 1.5))
    st.markdown(f"""<div class="finops-card"><small style="color:white;">SCORE DE RENTABILITÉ</small><span class="metric-value">{roi_score:.1f}/20</span></div>""", unsafe_allow_html=True)

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
    st.write(f"Sécurité active (>5 unités). Recopiez : **{phrase_cible}**")
    reponse = st.text_input("Vérification :", key="test_lucide")
    lucidite_ok = (reponse.strip().lower() == phrase_cible.lower()) if reponse else False

# --- GÉNÉRATION ---
st.divider()

if st.button("🚀 GÉNÉRER L'EXCUSE"):
    if conso > 5 and not lucidite_ok:
        st.warning("Action bloquée : Réussissez le test de lucidité.")
    else:
        # --- BASE DE DONNÉES ÉTENDUE ---
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé.", "Changement de programme."]
        }
        
        actions = {
            "Solidarité": [
                "un pote a un gros souci perso et on fait bloc", "le capitaine a un énorme coup de mou", 
                "le 9 est en plein burn-out moral", "un ancien est passé et ne va pas bien", 
                "un gars vient de se faire larguer au vestiaire", "on soutient le soigneur qui a un coup dur",
                "un coéquipier a perdu ses clés et on l'aide", "on discute avec le 7 qui est démoralisé"
            ],
            "Santé": [
                "on attend l'ambulance pour un coéquipier blessé", "un gars a fait un malaise après l'effort",
                "le soigneur me demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade",
                "suspicion de fracture pour mon binôme", "le 10 est totalement désorienté après un tampon",
                "un gars s'est déboîté l'épaule", "on attend les pompiers pour un gars d'en face"
            ],
            "Transports": [
                "le trafic est totalement interrompu sur ma ligne", "un incident voyageur bloque tout",
                "une panne de signalisation paralyse le réseau", "un colis suspect retient mon train à quai",
                "le bus de substitution est aussi en panne", "une porte est bloquée, le train ne part pas",
                "travaux de nuit commencés plus tôt que prévu", "incident technique majeur sur les voies"
            ],
            "Club": [
                "le coach nous retient pour un débriefing obligatoire", "le président fait un discours interminable",
                "on est de corvée de rangement pour l'équipe", "l'arbitre explique ses choix au bar",
                "on doit signer les licences de toute l'équipe", "le staff fait un point individuel",
                "on nettoie la buvette suite à une sanction", "le capitaine a verrouillé les sorties pour parler"
            ]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler.", "je rentre dès que ça s'apaise."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route, je reste à côté.", "on attend l'avis définitif du doc.", "je l'accompagne jusqu'à sa voiture."],
            "Transports": ["aucune info sur la reprise du trafic.", "je cherche désespérément un itinéraire bis.", "on nous demande de patienter sur le quai.", "je tente de finir le trajet à pied."],
            "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "c'est une obligation du président.", "faut finir ça avant de pouvoir partir."]
        }

        # Assemblage
        i = random.choice(intros[ton]).format(h=h_prevu)
        a = random.choice(actions[cat])
        c = random.choice(concls[cat])
        
        # Bonus Victoire
        if (cat == "Club" or cat == "Solidarité") and res == "Victoire":
            c = "on savoure cette gagne historique tous ensemble."

        st.markdown(f"<div class='excuse-box'>« {i} {a}, {c} »</div>", unsafe_allow_html=True)
        st.progress({"Transports": 20, "Club": 40, "Solidarité": 70, "Health": 90}.get(cat, 50) / 100)

if st.button("🖼️ GÉNÉRER UNE PREUVE"):
    if cat == "Transports":
        st.markdown('<div class="proof-box"><small style="color:#aaa">INFO TRAFIC • Maintenant</small><br><b style="color:white">⚠️ Trafic interrompu</b><br><small style="color:#ddd">Incident sur votre ligne. Reprise estimée : Inconnue.</small></div>', unsafe_allow_html=True)
    elif cat == "Club":
        st.markdown('<div class="proof-box"><small style="color:#aaa">WhatsApp • Groupe Rugby</small><br><b style="color:white">Coach 🏉</b><br><small style="color:#ddd">Réunion obligatoire au vestiaire. Personne ne sort avant la fin du débrief.</small></div>', unsafe_allow_html=True)
    else:
        st.info("Pas de preuve nécessaire pour cette catégorie.")
