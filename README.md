# Presentation
Cette page contient les deux fichiers principaux d'un projet que j'ai réalisé afin d'appuyer ma candidature à la formation de data scientist chez OpenCLassRooms.

Le projet représente un workflow de data science, il comprend plusieurs étapes :

- 1 : Récolte de données en ligne par scraping
- 2 : Aggrégation et chargement des données dans l'environnemnet de travail
- 3 : Analyse descriptive
- 4 : Modélisation
- 5 : Evaluation des performances du modèle et critique

Le fichier scrap.py représente la première étape. C'est une fonction appelée depuis un autre script simple (non inclu dans ce dossier) qui fait une boucle sur une liste d'urls.

Le fichier regression_multiple.ipynb contient le reste des étapes. Un modèle de regression est appliqué à des features extraits du texte afin de prédire la note que les users attribuent.
