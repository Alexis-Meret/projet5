# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 07:23:22 2020

@author: User
"""

import pickle
import  numpy as np
import matplotlib.pyplot as plt
T,X,Y=pickle.load(open("donneesTXY.pic",'rb'))
"""question 1"""
def enregistrer (T,X,Y):
    f=open("mesures.txt","w")
    N=len(T)
    f.write("-"*10)
    f.write("mesures")
    f.write("-"*10)
    f.write("\n")
    f.write("{}\n".format(N))
    f.write("temps,X,Y\n")
    for i in range (N):
        f.write("{0:.6f},{1:.6f},{2:.6f}\n".format(T[i],X[i],Y[i]))
    f.close()
enregistrer(T,X,Y)
"""question2"""
def relire():
    f=open("mesures.txt","r")
    tab=f.readlines()
    N=len(tab)
    tab_X=np.zeros(N-3)
    tab_Y=np.zeros(N-3)
    tab_T=np.zeros(N-3)
    for i in range(3,N):
        A=tab[i]
        A=A.split(",")
        tab_T[i-3] = float(A[0])
        tab_X[i-3] = float(A[1])
        tab_Y[i-3] = float(A[2])
    return tab_T,tab_X,tab_Y

"""question 3"""
t,x,y=relire()
plt.plot(t,x,"o-",label="x(t)")
plt.legend()
plt.grid()
plt.xlabel("t")
plt.ylabel("x")
plt.show()

"""question 4"""
V_x=(x[1:]-x[:-1])/(t[1:]-t[:-1])
plt.plot(x[:-1],V_x,label="x(t)")
plt.legend()
plt.grid()
plt.xlabel("t")
plt.ylabel("x")
plt.show()

