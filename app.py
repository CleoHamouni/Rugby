import streamlit as st
import random

# Configuration
st.set_page_config(page_title="Générateur d'excuse de 3e Mi-temps by THE PADDIES", page_icon="🏉", layout="centered")

# --- STYLE CSS (THÈME CLAIR & TEXTE NOIR) ---
st.markdown("""
    <style>
    /* Fond de l'application en clair */
    .stApp { 
        background-color: #f8f9fa; 
        color: #1a1a1a; 
    }
    
    /* TOUT LE TEXTE EN NOIR (Labels, titres, widgets) */
    label, p, span, div, h1, h2, h3, .stSelectbox label, .stNumberInput label, .stSlider label {
        color: #000000 !important;
        font-weight: 600 !important;
    }

    /* Sidebar en gris très clair pour contraste */
    [data-testid="stSidebar"] {
        background-color: #e9ecef !important;
    }

    /* Boutons en Rouge Rugby pour qu'ils restent visibles */
    .stButton>button { 
        width: 100%; 
        background-color: #d62828 !important; 
        color: white !important; 
        border-radius: 12px; 
        height: 4em; 
        font-weight: bold; 
        border: none;
        font-size: 1.1rem;
    }
    
    /* Boite d'excuse (Fond blanc cassé, texte noir) */
    .excuse-box { 
        background-color: #ffffff; 
        padding: 20px; 
        border-radius: 10px; 
        border: 2px solid #d62828; 
        color: #000000 !important; 
        font-style: italic;
        font-size: 1.1rem;
    }

    /* Dashboard ROI (Bordure noire) */
    .finops-card { 
        background-color: #ffffff; 
        padding: 15px; 
        border-radius: 12px; 
        border: 2px solid #000000; 
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

# --- SIDEBAR : DASHBOARD ROI ---
with st.sidebar:
    st.header("📊 Business Case")
    conso = st.slider("Unités consommées", 0, 15, 2)
    tension = st.slider("Indice de tension", 1, 10, 3)
    
    # ROI Plaisir vs Risque
    roi_score = (conso * 2) - (tension * 1.5)
    
    st.markdown(f"""
        <div class="finops-card">
            <p style="color:black; margin-bottom:0;">ROI PLAISIR / RISQUE</p>
            <span class="metric-value">{roi_score:.1f}</span>
        </div>
    """, unsafe_allow_html=True)
    
    if roi_score > 10: st.success("🔥 SOIRÉE LÉGENDAIRE")
    elif roi_score > 0: st.info("⚖️ RENTABILITÉ CORRECTE")
    else: st.warning("📉 DÉFICIT DE FUN")

# --- CORPS DE L'APPLI ---
st.title("Générateur d'excuse de 3e Mi-temps by THE PADDIES")

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
        st.error("Action bloquée : Réussissez le test de lucidité.")
    else:
        # Moteur d'excuses complet
        intros = {
            "Mielleux": ["Je suis vraiment navré pour les {h}h,", "Toutes mes excuses pour le retard,", "Je m'en veux terriblement,", "Pardonne-moi, je vais rater l'heure de {h}h,"],
            "Râleur": ["Franchement ça me gonfle,", "Encore un plan galère,", "C'est n'importe quoi cette journée,", "Marre d'être bloqué ici,"],
            "Factuel": ["Bloqué.", "Retard prévu pour {h}h.", "Coincé.", "Changement de programme."]
        }
        
        actions = {
            "Solidarité": ["un pote a un gros souci perso et on fait bloc", "le capitaine a un énorme coup de mou", "le 9 est en plein burn-out moral", "un ancien est passé et ne va pas bien", "un gars vient de se faire larguer au vestiaire", "on soutient le soigneur qui a un coup dur", "un coéquipier a perdu ses clés et on l'aide", "on discute avec le 7 qui est démoralisé"],
            "Santé": ["on attend l'ambulance pour un coéquipier blessé", "un gars a fait un malaise après l'effort", "le soigneur me demande de surveiller un gars KO", "un joueur s'est ouvert l'arcade", "suspicion de fracture pour mon binôme", "le 10 est totalement désorienté", "un gars s'est déboîté l'épaule", "on attend les pompiers pour un joueur"],
            "Transports": ["le trafic est totalement interrompu sur ma ligne", "un incident sur la voie bloque tout", "panne de signalisation paralyse le réseau", "un colis suspect retient mon train à quai", "le bus de substitution est aussi en panne", "une porte est bloquée, le train ne part pas", "travaux de nuit commencés plus tôt que prévu", "incident technique majeur sur les voies"],
            "Club": ["le coach nous retient pour un débriefing obligatoire", "le président fait un discours interminable", "on est de corvée de rangement pour l'équipe", "l'arbitre explique ses choix au bar", "on doit signer les licences de toute l'équipe", "le staff fait un point individuel", "on nettoie la buvette suite à une sanction", "le capitaine a verrouillé les sorties pour parler"]
        }
        
        concls = {
            "Solidarité": ["on ne peut pas le laisser seul.", "on fait bloc, c'est l'esprit.", "on reste pour l'épauler.", "je rentre dès que ça s'apaise."],
            "Santé": ["je reste tant qu'il n'est pas stable.", "le SAMU est en route, je reste à côté.", "on attend l'avis définitif du doc.", "je l'accompagne jusqu'à sa voiture."],
            "Transports": ["aucune info sur la reprise du trafic.", "je cherche désespérément un itinéraire bis.", "on nous demande de patienter sur le quai.", "je tente de finir le trajet à pied."],
            "Club": ["personne ne sort avant la fin.", "si je m'esquive, je suis sanctionné mardi.", "c'est une obligation du président.", "faut finir ça avant de pouvoir partir."]
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
