# je vais utiliser l'API de Google pour générer un texte sur les tendances actuelles du marché des cryptomonnaies
import google.generativeai as genai
import json
import os
from dotenv import load_dotenv


load_dotenv()
print("Clé API chargée :", os.getenv("GOOGLE_API_KEY2"))

API_KEY = os.getenv("GOOGLE_API_KEY2")

if not API_KEY:
    raise ValueError("La clé API est introuvable. Vérifie ton fichier .env.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash-8b-001")

prompt = "Analyse les tendances actuelles du marché des cryptomonnaies et donne un aperçu des évolutions à venir."
response = model.generate_content(prompt)



crypto_analysis = response.text

with open("crypto_analysis.json", "w", encoding="utf-8") as file:
    json.dump({"crypto_analysis": crypto_analysis}, file, ensure_ascii=False, indent=4)

print("Analyse stockée avec succès dans crypto_analysis.json")


#Je vais transformer le texte généré en un fichier audio
import json
from gtts import gTTS
import re
import pygame


with open("crypto_analysis.json", "r", encoding="utf-8") as file:
    data = json.load(file)

text = data.get("crypto_analysis", "Aucune analyse disponible.")

text = re.sub(r"\*", "", text)

if text.strip():
    tts = gTTS(text=text, lang="fr")
    tts.save("crypto_analysis.mp3")  

    print("audio généré.")
else:
    print("Le fichier JSON ne contient pas d'analyse valide.")
 

#Je vais recuperer le prix des crypto en eur 
import requests
import pandas as pd
from datetime import datetime, timezone

cryptos = {
    "bitcoin": "bitcoin",
    "ethereum": "ethereum",
    "solana": "solana"
}

base_url = "https://api.coingecko.com/api/v3/coins/{}/market_chart"

params = {
    "vs_currency": "eur",
    "days": "7",
    "interval": "daily"
}

for name, crypto_id in cryptos.items():
    response = requests.get(base_url.format(crypto_id), params=params)

    if response.status_code == 200:
        data = response.json()
        prices = data.get("prices", [])

        formatted_data = []
        for timestamp, price in prices:
            date = datetime.fromtimestamp(timestamp / 1000, tz=timezone.utc).strftime('%Y-%m-%d')
            formatted_data.append([date, price])

        df = pd.DataFrame(formatted_data, columns=["Date", "Prix (EUR)"])
        csv_filename = f"{name}_prix_7jours.csv"
        df.to_csv(csv_filename, index=False, encoding="utf-8")

        print(f"Données enregistrées dans {csv_filename}")
    else:
        print(f"Erreur lors de la récupération des données pour {name}")


# Je vais passer à l'analyse des données 
import cohere
import os
import nbformat as nbf
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

if not API_KEY:
    raise ValueError("Clé API Cohere manquante ! Vérifie ton fichier .env.")

print("Clé API chargée :", API_KEY[:5] + "..." + API_KEY[-5:]) 

# Initialiser Cohere
co = cohere.Client(API_KEY)

# Prompt détaillé pour générer le code
prompt = """
Écris un notebook Jupyter pour analyser les cryptomonnaies (Bitcoin, Ethereum, Solana).
Utilise l'API CoinGecko pour récupérer les prix des 7 derniers jours et calcule :
- La moyenne mobile (SMA, EMA)
- La volatilité des prix
-Utilise mes fichiers bitcoin_prix_7jours.csv, ethereum_prix_7jours.csv et solana_prix_7jours.csv
Affiche les résultats sous forme de **graphique** avec Matplotlib.
Ajoute des cellules Markdown expliquant chaque étape.
"""

# Générer le code avec Cohere
response = co.generate(
    model="command",  # Essaie "command" ou "command-r" selon ton accès
    prompt=prompt,
    max_tokens=1000
)

# Extraire le texte généré
generated_code = response.generations[0].text

# Créer un notebook Jupyter
nb = nbf.v4.new_notebook()

# Ajouter une cellule Markdown d'introduction
nb.cells.append(nbf.v4.new_markdown_cell("# 📊 Analyse des Cryptos avec CoinGecko\n"
                                         "Ce notebook analyse Bitcoin, Ethereum et Solana "
                                         "à l'aide des indicateurs financiers suivants :\n"
                                         "- **Moyenne mobile (SMA, EMA)**\n"
                                         "- **Indice de force relative (RSI)**\n"
                                         "- **Volatilité**\n\n"
                                         "Les données proviennent de l'API **CoinGecko**."))

# Ajouter le code généré par Cohere dans une cellule de code
nb.cells.append(nbf.v4.new_code_cell(generated_code))

notebook_filename = "Analyse_Crypto.ipynb"
with open(notebook_filename, "w", encoding="utf-8") as f:
    nbf.write(nb, f)

print(f"Notebook généré : {notebook_filename}")
print("Ouvre-le avec Jupyter Notebook pour voir l'analyse étape par étape.")