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