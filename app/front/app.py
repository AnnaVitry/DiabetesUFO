import streamlit as st
import requests
# from dotenv import load_dotenv
import os


# Charger le modèle
# model = joblib.load("model/diabeast.pkl")

# load_dotenv()
API_URL = os.environ.get('API_URL')

# Page configuration
st.set_page_config(
    page_title="Prédiction du risque de diabète",
    page_icon="🩺",
    layout="centered"
)

st.title("Prédiction du risque de diabète")
st.markdown("### Évaluation personnalisée du risque de diabète")
st.info("Remplissez le formulaire ci-dessous pour obtenir une estimation du risque de diabète basée sur les informations du patient.")

# Liste des features avec descriptions
feature_labels = {
    "age": "Âge",
    "gender": "Genre",
    "polyuria": "Polyurie (urination excessive)",
    "polydipsia": "Polydipsie (soif excessive)",
    "sudden_weight_loss": "Perte de poids soudaine",
    "weakness": "Faiblesse générale",
    "polyphagia": "Polyphagie (faim excessive)",
    "obesity": "Obésité",
    "genital_thrush": "Mycose génitale",
    "visual_blurring": "Vision floue",
    "itching": "Démangeaisons",
    "irritability": "Irritabilité",
    "delayed_healing": "Cicatrisation retardée",
    "partial_paresis": "Parésie partielle",
    "muscle_stiffness": "Raideur musculaire",
    "alopecia": "Alopécie (perte de cheveux)"
}

# Créer le formulaire utilisateur
user_input = {}
with st.form("patient_form"):
    # Informations démographiques
    st.subheader("Informations démographiques")
    col1, col2 = st.columns(2)

    with col1:
        user_input["age"] = st.number_input(
            feature_labels["age"],
            min_value=0,
            max_value=120,
            value=40,
            help="Entrez l'âge du patient"
        )

    with col2:
        select = st.selectbox(
            feature_labels["gender"],
            ["Homme", "Femme"],
            help="Sélectionnez le genre du patient"
        )
        user_input["gender"] = 1 if select == "Homme" else 0

    st.divider()

    # Symptômes principaux
    st.subheader("Symptômes principaux")
    st.caption("Ces symptômes sont les indicateurs les plus courants du diabète")

    main_symptoms = ["polyuria", "polydipsia", "sudden_weight_loss", "weakness", "polyphagia", "obesity"]

    col1, col2 = st.columns(2)

    for idx, feature in enumerate(main_symptoms):
        with col1 if idx % 2 == 0 else col2:
            user_input[feature] = st.radio(
                feature_labels[feature],
                options=[0, 1],
                format_func=lambda x: "Non" if x == 0 else "Oui",
                horizontal=True,
                key=feature
            )

    st.divider()

    # Symptômes secondaires
    st.subheader("Symptômes secondaires")
    st.caption("Ces symptômes peuvent également indiquer un risque de diabète")

    secondary_symptoms = ["genital_thrush", "visual_blurring", "itching", "irritability",
                         "delayed_healing", "partial_paresis", "muscle_stiffness", "alopecia"]

    col1, col2 = st.columns(2)

    for idx, feature in enumerate(secondary_symptoms):
        with col1 if idx % 2 == 0 else col2:
            user_input[feature] = st.radio(
                feature_labels[feature],
                options=[0, 1],
                format_func=lambda x: "Non" if x == 0 else "Oui",
                horizontal=True,
                key=feature
            )

    st.divider()
    submitted = st.form_submit_button("Obtenir la prédiction", use_container_width=True, type="primary")

# Lorsque l'utilisateur clique
if submitted:
    st.divider()

    with st.spinner("Analyse en cours... Veuillez patienter"):
        response = requests.post(API_URL+"/predict", json=user_input)

        if response.status_code == 200:
            data = response.json()
            proba = data['probabilities']
            prediction = data['prediction']

            st.subheader("Résultat de l'analyse")

            # Create two columns for better layout
            col1, col2 = st.columns([2, 1])

            with col1:
                if prediction == 1:
                    st.error("### Risque de diabète détecté")
                    st.write(f"**Probabilité de présence de diabète:** {proba['positive']*100:.1f}%")
                    st.progress(proba['positive'])
                    st.warning("**Recommandation:** Consultez un professionnel de santé pour un diagnostic approfondi.")
                else:
                    st.success("### Aucun risque détecté")
                    st.write(f"**Probabilité d'absence de diabète:** {proba['negative']*100:.1f}%")
                    st.progress(proba['negative'])
                    st.info("**Conseil:** Maintenez un mode de vie sain avec une alimentation équilibrée et une activité physique régulière.")

            with col2:
                # Display metrics
                st.metric(
                    label="Confiance",
                    value=f"{max(proba['positive'], proba['negative'])*100:.1f}%"
                )

                if prediction == 1:
                    st.metric(
                        label="Risque",
                        value="Élevé",
                        delta=None
                    )
                else:
                    st.metric(
                        label="Risque",
                        value="Faible",
                        delta=None
                    )
        else:
            st.error(f"Erreur lors de la prédiction. Code: {response.status_code}")
            st.warning("Veuillez vérifier que l'API est accessible et réessayer.")
