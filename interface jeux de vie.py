# -*- coding: utf-8 -*-
# Créé par Fred, le 09/04/2014
# Jeu de la vie de John Conway
from Tkinter import *
from random import randrange

haut = 100 # hauteur du tableau
large = 100 # largeur du tableau
cote = 5 # côté d'une cellule
vivant = 1
mort = 0
sortie=False
n_iterations=0

# Créer les tableaux
"""
table=[];tabletemp=[];grille=[]
for k in range(haut):
    tablel=[];tabletempl=[];grillel=[]
    for j in range(large):
        tablel.append(0)
        tabletempl.append(0)
        grillel.append(0)
    table.append(tablel)
    tabletemp.append(tabletempl)
    grille.append(grillel)
"""
table = [ [ 0 for y in range(haut) ]
     for x in range(large) ]
tabletemp = [ [ 0 for y in range(haut) ]
     for x in range(large) ]
grille = [ [ 0 for y in range(haut) ]
     for x in range(large) ]

def nouvelle_grille(n):
    if n==0:
    # placer au hasard environ 25% de cellules vivantes
        (...)
            (...)
    elif n==1:
    #un truc en forme d'angle droit
        (...)
            (...)
        (...)
            (...)
#    elif n==2:


def init():
    sortie=True
    if cote<=5:coltrait=''
    else:coltrait='gray'
    for y in range(haut):
        for x in range(large):
            table[x][y] = mort
            tabletemp[x][y] = mort
            grille[x][y] = can.create_rectangle((x*cote, y*cote
                ,(x+1)*cote, (y+1)*cote), outline=coltrait, fill="white")
    nouvelle_grille(1)
    sortie=False
    n_iterations=0

# Appliquer les 4 règles
def calculer():
    global n_iterations
    n_iterations+=1
    for y in range(haut):
        for x in range(large):
            nb_voisins=voisins_vivants(x,y)
# Règle 1 - Mort de solitude
            (...)
                (...)
 # Règle 2 - Toute cellule avec 2 ou 3 voisins survit.
            (...)
                (...)
 # Règle 3 - Mort par asphyxie
            (...)
                (...)
 # Règle 4 - Naissance
            (...)
                (...)
    for y in range(haut):
        for x in range(large):
            (...)

# Compter les voisins vivants - tableau circulaire
def voisins_vivants(a,b):
    nb_voisins = 0
    if table[(a-1)%large][(b+1)%haut] == 1:
        nb_voisins += 1
    if table[a][(b+1)%haut] == 1:
        nb_voisins += 1
    if table[(a+1)%large][(b+1)%haut] == 1:
        nb_voisins += 1
    if table[(a-1)%large][b] == 1:
        nb_voisins += 1
    if table[(a+1)%large][b] == 1:
        nb_voisins += 1
    if table[(a-1)%large][(b-1)%haut] == 1:
        nb_voisins += 1
    if table[a][(b-1)%haut] == 1:
        nb_voisins += 1
    if table[(a+1)%large][(b-1)%haut] == 1:
        nb_voisins += 1
    return nb_voisins

# Dessiner toutes les cellules
def dessiner():
    b3.config(text='nombre d\'itérations : '+str(n_iterations))
    for y in range(haut):
        for x in range(large):
            if table[x][y]==0: coul = "white"
            else: coul = "blue"
            can.itemconfig(grille[x][y], fill=coul)

# Calculer et dessiner le prochain tableau
def tableau():
    calculer()
    dessiner()
    if not sortie:
        fenetre.after(10, tableau)

def relance():
    sortie=True
    init()
    sortie=False

def quitte():
    global sortie
    sortie=True
    fenetre.destroy()

# Lancement du programme
fenetre = Tk()
fenetre.title("Le jeu de la vie de John Conway")
fenetre.iconbitmap('jeuvie.ico')
can = Canvas(fenetre, width=cote*large, height=cote*haut, highlightthickness=0)
can.grid(row=0,column=0,rowspan=10)
b1=Button(fenetre,text='Quitter',command=quitte)
b1.grid(row=10,column=1)
b2=Button(fenetre,text='Relance',command=relance)
b2.grid(row=9,column=1)
b3=Label(fenetre,text='nombre d\'itérations : '+str(n_iterations))
b3.grid(row=10,column=0)
init()
tableau()
fenetre.mainloop()

