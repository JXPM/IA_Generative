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
