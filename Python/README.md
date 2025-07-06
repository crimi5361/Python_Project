## ÉNONCÉ DU PROJET PYTHON : Test automatique d’identifiants via Web Automation + Logs + POO


## //Objectif général

Créer un programme Python capable de :
-Lire un fichier Excel contenant des identifiants (User/Password) et des liens de sites (URL)

-Automatiquement tenter de se connecter à chaque site

#Pour chaque tentative :

-Si la connexion est réussie, capturer un screenshot de la page

-Enregistrer les informations dans un fichier log.txt : site, identifiant, statut (200 ou erreur), heure, succès/échec

-Les captures réussies doivent être stockées dans un dossier screenshots/

#Le tout doit être encapsulé dans un programme structuré en POO



## Structure attendue

projet_scraping/
│
├── data.xlsx        ← Le fichier Excel à charger
├── main.py          ← Le script principal
├── logger.py        ← Classe de gestion des logs
├── scraper.py       ← Classe de gestion des connexions et screenshots
├── screenshots/     ← Dossier où seront enregistrées les captures
└── logs.txt         ← Fichier de log



### Technologies recommandées ( laisse l'Etudiant faire ses recherche ne pas lui communiquer )

pandas pour lire le fichier Excel
selenium pour les connexions web automatisées
openpyxl (moteur Excel supporté par pandas)
datetime pour l'horodatage
os, pathlib, time pour la gestion système