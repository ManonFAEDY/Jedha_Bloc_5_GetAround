import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Rentale analysis",
    layout="wide"
)

st.title("📊 Impact of time delta between rentals")

# --- 1. GÉnÉration de DonnÉes d'Exemple ---
# Remplacez cette section par la lecture de vos propres données (ex: pd.read_csv('votre_fichier.csv'))

data_delay = pd.read_excel('get_around_delay_analysis.xlsx', sheet_name=['rentals_data', 'Documentation'])
df = data_delay['rentals_data']

# Affichage des premières lignes de données
if st.checkbox('Display raw data', False):
    st.subheader('Raw data')
    st.dataframe(df)

# --- 2. CRÉation du Filtre Interactif ---
st.sidebar.header("Reservation delay implementation")

# Filtre par Intervalle (Slider pour une colonne numérique)
min_val = float(df['time_delta_with_previous_rental_in_minutes'].min())
max_val = float(df['time_delta_with_previous_rental_in_minutes'].max())
valeur_range = st.sidebar.slider(
    "Select delay to implement to see impact on rentals :",
    min_value=min_val,
    max_value=max_val,
    value=(min_val, max_val), # Intervalle par défaut
    step=15.0
)

# --- 3. APPLICATION DU FILTRE ---
df_filtre = df.loc[
    (df['time_delta_with_previous_rental_in_minutes'] >= valeur_range[0]) & 
    (df['time_delta_with_previous_rental_in_minutes'] <= valeur_range[1])
]
df_notfollow = df[df['time_delta_with_previous_rental_in_minutes'].isna()]


# --- 4. CRÉation et Affichage de l'Histogramme ---
if not df_filtre.empty:
    st.subheader("Impact of Time Delta Between Rentals")
    
    # Message d'état
    st.info(f"Number of rentals concerned by delay implementation : **{len(df)-len(df_notfollow) - len(df_filtre)}** sur **{len(df)-len(df_notfollow)}**")
    st.info(f"Rentals which are not followed by an other rental are already filtered ({len(df_notfollow)})")


    # Création de l'histogramme avec Plotly Express
    fig = px.histogram(
        df_filtre, 
        x="time_delta_with_previous_rental_in_minutes",
        title="Distribution of Time Delta Between Rentals"     
    )

    # Mise à jour du layout pour une meilleure lisibilité
    fig.update_layout(
        xaxis_title="time_delta_with_previous_rental_in_minutes",
        yaxis_title="Fréquence (Nombre d'Observations)",
        hovermode="x unified",
        xaxis=dict(
            range=[0, 720])
    )
    
    # Affichage de la figure Plotly dans Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("⚠️ Aucune donnée ne correspond aux filtres sélectionnés. Veuillez ajuster les critères.")