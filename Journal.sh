pip install google-generativeai

# Installation d'environnement
pip install python-dotenv

# Créer un fichier .env
touch .env
nano .env

# git/github
rm -rf .git
git init
git branch -M main
git add .
git commit -m "first commit"
gh repo create IA_Générative --public
git remote add origin https://github.com/JXPM/IA_Generative.git
git push --set-upstream origin main

# Supprimer le fichier .env du suivi git
git rm --cached .env
rm '.env'

#create .gitignore
touch .gitignore

# Ajout du fichier .gitignore
git add .gitignore

# Commit du fichier .gitignore
git commit -m "Ajout du fichier .gitignore"

pip install google-generativeai # (API Gemini )
pip install gtts # ( Google Text−to−Speech )
pip install requests pandas # ( Requetes web et manipulation de donnees )
pip install matplotlib seaborn # ( Visualisation des donnees )
pip install pycoingecko # (API CoinGecko pour recuperer les prix de scryptos )
pip install pygame # ( Pour jouer des sons )
pip install nbformat #(Pour le format)

#Lancer le script depuis mon terminal 
python3 Tchaipo_IA.py

#fichier Maj et push 
git status 
git add .
git commit -m "Maj"
git push origin main