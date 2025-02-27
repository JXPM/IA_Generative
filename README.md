# Analyse des Cryptomonnaies avec IA G ́en ́erative

Ce projet permet d'analyser les tendances des cryptomonnaies (Bitcoin, Ethereum, Solana) en récupérant leurs données depuis CoinGecko, en générant des graphiques et en effectuant une analyse avancée avec **Gemini AI**. Une version audio de l'analyse est également générée avec **gTTS**.

## Fonctionnalités

- **Récupération des données** depuis l'API CoinGecko (prix en EUR sur 30 jours).
- **Visualisation des tendances** avec Matplotlib.
- **Analyse approfondie** avec Gemini AI.
- **Conversion en audio** de l'analyse avec gTTS.
- **Interface en ligne de commande** pour sélectionner une crypto.

## Structure du projet

- Tchaipo.ipynb est le fichier contenant les première commande exécuté la première journée pour s'entrainer 
- Tchaipo.py est le fichier contenant la première partie avec l'utilisation des API GOOGLE ET COHERE avec les différentes bibliotheques (pour lancer il faut faire python Tchaipo_IA.py/python3 Tchaipo_IA.py)
- Analyse_crypto.ipynb est le fichier contenant la derniere partie de mon code et le parametre pour générer graphique, audio et analyse txt en fonction de la crypto
- Crypto_analysis.json est le fichier contenant l'analyse écrite généré par l'API GOOGLE
- Solana_prix_7jours, bitcoin_prix_7jours et etherum_prix_7jours.csv sont les fichiers contenant les données générées avec mon API
- Mon fichier Journal.sh contient toute les commande que j'ai utilisé dans mon terminal 
