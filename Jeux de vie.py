# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 15:32:31 2018

@author: Nasreddine
"""

import numpy as np
import time as tm
n=100
def init_grille(n):
  grille = np.random.randint(2,size=(n,n))
  return grille

grid=init_grille(n)

def evolution1(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=np.zeros((irange,jrange))
    for j in range(jrange):
        for i in range(irange):
            cell_state=0
            nb_neigh=get_nbneigh(grid,(i,j))
            if nb_neigh==2:
                cell_state=grid[i][j]
            elif nb_neigh==3:
                cell_state=1
            res_grid[i,j]=(cell_state)
    return res_grid

######################################################################################
    
"Calcul du temps dexecution "
debut=tm.time()
res_grid=evolution1(grid)
fin=tm.time()
temp=fin-debut

print ("le temps de calcul de la fonction evolution1 quand la grille est de taille ",n,"*",n,"est:" )
print (temp)        

#######################################################################################


def get_nbneigh(grid,coord):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    i=coord[0]
    j=coord[1]
    biinf=max(0,i-1)
    bisup=min(irange-1,i+1)
    bjinf=max(0,j-1)
    bjsup=min(jrange-1,j+1)
    nb_neigh=0
    for ii in range(biinf,bisup+1):
        for jj in range(bjinf,bjsup+1):
            if grid[ii][jj] == 1:
                nb_neigh=nb_neigh+1
    nb_neigh=nb_neigh-grid[i][j]
    return nb_neigh

###########################################################################################

import cProfile 
cProfile.run('evolution1(grid)')

###########################################################################################
def evolution1_corr(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=[[] for i in range(irange)]
    for j in range(jrange):
        for i in range(irange):
            cell_state=0
            biinf=max(0,i-1)
            bisup=min(irange-1,i+1)
            bjinf=max(0,j-1)
            bjsup=min(jrange-1,j+1)
            nb_neigh=0
            for ii in range(biinf,bisup+1):
                for jj in range(bjinf,bjsup+1):
                    if grid[ii][jj] == 1:
                        nb_neigh=nb_neigh+1
            nb_neigh=nb_neigh-grid[i][j]
            if nb_neigh==2:
                cell_state=grid[i][j]
            elif nb_neigh==3:
                cell_state=1
            res_grid[i].append(cell_state)
    return res_grid

##################################################################################################
"Calcul du temps dexecution "
debut1=tm.time()
res_grid_corr=evolution1_corr(grid)
fin1=tm.time()
temp1=fin1-debut1
###################################################################################################

print ("le temps de calcul de la fonction evolution1_corr quand la grille est de taille ",n,"*",n,"est:" )
print (temp1)       

###################################################################################################
import cProfile 
cProfile.run('evolution1_corr(grid)')
###################################################################################################

def evolution1_ndarray(grid):
    irange=grid.shape[0]
    jrange=grid.shape[1]
    res_grid=np.zeros(irange)
    res_grid=[[] for i in range(irange)]
    for j in range(jrange):
        for i in range(irange):
            cell_state=0
            biinf=max(0,i-1)
            bisup=min(irange-1,i+1)
            bjinf=max(0,j-1)
            bjsup=min(jrange-1,j+1)
            nb_neigh=0
            for ii in range(biinf,bisup+1):
                for jj in range(bjinf,bjsup+1):
                    if grid[ii][jj] == 1:
                        nb_neigh=nb_neigh+1
            nb_neigh=nb_neigh-grid[i][j]
            if nb_neigh==2:
                cell_state=grid[i][j]
            elif nb_neigh==3:
                cell_state=1
            res_grid[i]=cell_state
    return res_grid
# #################################################################################################
"Calcul du temps dexecution "
debut2=tm.time()
res_grid_ndarray=evolution1_ndarray(grid)
fin2=tm.time()
temp2=fin2-debut2
##################################################################################################

print ("le temps de calcul de la fonction evolution1_ndarray quand la grille est de taille ",n,"*",n,"est:" )
print (temp2)       

##################################################################################################
import cProfile 
cProfile.run('evolution1_ndarray(grid)')
######################################################################################

def enlarge_grille(grille):
  irange=grille.shape[0]
  jrange=grille.shape[1]
  res_grille=np.zeros((irange+2,jrange+2))
  res_grille[1:irange+1,1:jrange+1]=grille[:,:]
  return res_grille
  
def evolution2(grille):
  irange=grille.shape[0]
  jrange=grille.shape[1]
  res_grille=np.zeros((irange-2,jrange-2))
  for i in range(1,irange-1):
    for j in range(1,jrange-1):
      c=0
      for ii in range(i-1,i+2):
        for jj in range(j-1,j+2):
          c=c+grille[ii][jj]
      c=c-grille[i][j]
      if c==2:
        res_grille[i-1][j-1]=grille[i][j]
      elif c==3:
        res_grille[i-1][j-1]=1
  return res_grille

#######################################################################################
res_enlarge_grille=init_grille(n) #crétation d'une nouvelle grille
res_enlarge_grille=enlarge_grille(res_enlarge_grille) #application de la fonction enlarge_grille
res_grille= evolution2(res_enlarge_grille)# application de la fonction evolution 2

########################################################################################

def evolution_store(grille):
    irange=grille.shape[0]
    jrange=grille.shape[1]
    A=irange-2
    B=jrange-2
    C=irange-1
    D=jrange-1
    res_store=np.zeros((A,B))
     
    for i in range (1,C):
        c=[0,0,0]
        for ii in range (i-1,i+2):
            c[1]=c[1]+grille[ii][1]
        for ii in range (i-1,i+2):
            c[2]=c[1]+grille[ii][2]
        for j in range(2,D):
            c[0]=c[1]
            c[1]=c[2]
            c[2]=0    
            for ii in range(i-1,i+2):
                c[2]=c[2]+grille[ii][j+1]
            k=c[0]+c[1]+c[2]
            if k==2:
                res_grille[i-1][j-1]=grille[i][j]
            elif k==3:
                res_store[i-1][j-1]=1
    return res_store
res_store=evolution_store(res_grille)

    
    









##