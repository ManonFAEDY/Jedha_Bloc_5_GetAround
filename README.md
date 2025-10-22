C'est un excellent projet qui combine à la fois l'analyse de données et le déploiement de modèles \! Voici un `README.md` structuré pour présenter clairement ces deux aspects, comme demandé.

-----

# 🚗 GetAround: Optimisation du Temps de Location et Tarification

Ce projet, réalisé dans le cadre d'un partenariat avec GetAround (le "Airbnb de la voiture"), est divisé en deux parties :

1.  **Analyse de Données et Visualisation** : Création d'un tableau de bord pour aider la gestion produit à optimiser la logistique des locations.
2.  **Machine Learning et API** : Développement d'un endpoint de prédiction de prix journaliers pour les propriétaires de voitures.

-----

## 1\. 📊 Analyse & Visualisation (Web Dashboard Streamlit)

L'objectif principal est de fournir des informations factuelles pour déterminer la meilleure stratégie de **délai minimum entre deux locations** afin de réduire l'insatisfaction client due aux retards de restitution, tout en minimisant la perte de revenus potentielle.

Le tableau de bord interactif est construit avec **Streamlit** et répond aux questions clés de la gestion produit concernant le **seuil** (durée du délai minimum) et le **champ d'application** (toutes les voitures vs. uniquement les voitures Connect).

### Fonctionnalités du Dashboard

  * **Analyse du Delta de Temps** : Visualisation de la distribution du temps écoulé entre deux locations consécutives, avec des filtres pour simuler l'impact d'un délai minimum.
  * **Impact du Retard Précédent** : Étude de la corrélation entre le retard de la location précédente et l'état de la location suivante (`successful` ou `failed`), segmentée par type de check-in (`mobile` ou `connect`).
  * **Mesures Clés** : Affichage des pourcentages de locations potentiellement affectées pour aider à trouver le juste équilibre entre l'amélioration de l'expérience utilisateur et l'optimisation des revenus.

### 🔗 Liens de Production

| Service | URL |
| :--- | :--- |
| **Tableau de Bord Streamlit** | `[https://huggingface.co/docs/hub/en/spaces-sdks-streamlit](https://huggingface.co/spaces/MaFae/Jedha_Bloc_5_GetAround)` |


### Technologies Utilisées

  * **Framework** : Streamlit
  * **Analyse/Manipulation de Données** : Pandas, NumPy
  * **Visualisation** : Plotly Express

-----

## 2\. 🤖 Pilier Machine Learning & API

Ce volet se concentre sur l'optimisation de la tarification journalière pour les propriétaires, en utilisant un modèle de Machine Learning entraîné sur des données de tarification de véhicules.

Le modèle est exposé via une API pour permettre son intégration dans les systèmes de production.

### Endpoint /predict

L'API est hébergée en ligne et propose un endpoint `/predict` qui permet de soumettre les caractéristiques d'un véhicule (modèle, kilométrage, puissance, options, etc.) et de recevoir une estimation du prix de location journalier.


### 🔗 Liens de Production

| Service | URL |
| :--- | :--- |
| **Documentation API** | `[https://huggingface.co/docs](https://mafae-jedha-bloc-5-getaround-api.hf.space/docs#/)` |


#### Exemple d'Entrée (JSON)

```json
{
  "input": [
    {
      "model_key": "Peugeot", 
      "mileage": 100000.0, 
      "engine_power": 135.0, 
      "fuel": "diesel", 
      "paint_color": "black", 
      "car_type": "sedan", 
      "private_parking_available": true, 
      "has_gps": true, 
      "has_air_conditioning": false, 
      "automatic_car": false, 
      "has_getaround_connect": true, 
      "has_speed_regulator": false, 
      "winter_tires": true
    }
  ]
}
```

#### Exemple de Sortie (JSON)

```json
{
  "prediction": [60.50]
}
```

### Technologies Utilisées

  * **API Framework** : FastAPI (recommandé pour la performance et les docs automatiques)
  * **Modèle ML** : Scikit-Learn Pipeline (enregistré via `joblib`)
  * **Déploiement** : Hugging Face Spaces (ou autre service cloud)

-----

