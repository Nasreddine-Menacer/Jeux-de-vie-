# Jeux-de-vie-

Les jeux de la vie, ou automates cellulaires, sont définis sur une grille de
cellules. Les cellules sont dans un état donné. L’état des cellules évolue dans
le temps en fonction de l’état des cellules suivantes selon des règles simples.

Règles de base
• Etat 0 ou 1, i.e. morte ou vivante
• R1 : une cellule morte possédant exactement 3 voisins nait, i.e. Etat 0->1
• R2 : une cellule vivante possédant 2 ou 3 voisins reste vivante, i.e. Etat 1->1
• R3 : une cellule vivante qui possède moins de 2 voisins ou plus de 3 voisins
meurt par isolement ou surpeuplement i.e. Etat 1->0

![Capture](https://user-images.githubusercontent.com/109802352/180657888-71dac03e-859c-4c07-98f5-6445303e6dbc.PNG)
