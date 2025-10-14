import streamlit as st
import numpy as np
import joblib
import requests

# Charger le modèle
model = joblib.load("model/diabeast.pkl")

st.title("🧬 Prédiction du risque de diabète")
st.write("Remplis le formulaire ci-dessous pour estimer le risque de diabète.")

# Liste des features
features = [
    "age", "gender", "polyuria", "polydipsia", "sudden_weight_loss", "weakness",
    "polyphagia", "genital_thrush", "visual_blurring", "itching", "irritability",
    "delayed_healing", "partial_paresis", "muscle_stiffness", "alopecia", "obesity"
]

# Créer le formulaire utilisateur
user_input = {}
with st.form("patient_form"):
    for feature in features:
        if feature == "age":
            user_input[feature] = st.number_input("Âge", min_value=0, max_value=120, value=40)
        elif feature == "gender":
            user_input[feature] = st.selectbox("Genre", {"Homme": 1, "Femme": 0})
        else:
            user_input[feature] = st.radio(f"{feature.replace('_', ' ').capitalize()} ?", [0, 1])
    
    submitted = st.form_submit_button("🔮 Prédire")

# Lorsque l'utilisateur clique
if submitted:
    X = np.array([[v for v in user_input.values()]])
    prediction = model.predict(X)[0]
    proba = model.predict_proba(X)[0]

    st.subheader("Résultat :")
    if prediction == 1:
        st.error(f"⚠️ Risque de diabète détecté avec une probabilité de {proba[1]*100:.1f}%")
    else:
        st.success(f"✅ Aucun risque détecté ({proba[0]*100:.1f}% de probabilité)")

    st.progress(proba[1])
