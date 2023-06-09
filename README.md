# fos-data-engineering

to install dependencies, run: `pip install -r requirements.txt`

description de projet :
le but de cet exercice est de crie un fichier dockerfile qui nous permettre d'executer etl.py avec cron job a chaque 10 minutes (dans mon cas j'ai fais 1 minute ) 

erreur dans le crone :
J'ai crié une image avec build puis j'ai fais docker run my app : le cron marche chaque 1 minute mais le problème qu'il m'affiche une erreur : python not found du coup il n'exécute pas etl.Py 
remarque : j'ai essayé avec FROM python:latest et FROM python:3.8 c'est la même chose . 
