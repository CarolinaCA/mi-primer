import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

a=0.2        #input probability 
b=0.8        #output probability
t1=0.6       #tasep input probability
t2=0.6       #tasep output probability
matriz=[]
mu=5         #Required iterations
ty=[]
n=0
z=0

#Defining the functions. Where "caminado" is the walking function, entrada is the input and salida is the output function
def caminado(n):
    micro_tub=[0]*n                            #Creating an list of n zeros 
    ty=micro_tub.copy()
    matriz.append(ty)
    micro_tub_2=micro_tub.copy()
    for interaciones in range(1): 
        micro_tub=micro_tub_2.copy();
        i=0
        for r in micro_tub:                   
            if r==1:                           #looking for 1's in list 
                if i<n-1:                     
                    if micro_tub[i+1]==0:
                        micro_tub_2[i+1]=1
                        micro_tub_2[i]=0
                        ty=micro_tub_2.copy()
                        matriz.append(ty)
                else:
                    micro_tub_2=salida(micro_tub_2,n)
                    ty=micro_tub_2.copy()
                    matriz.append(ty)
            micro_tub_2=tasep(micro_tub_2,n)
            i+=1
        micro_tub_2=entrada(micro_tub_2,n)
    return micro_tub_2
    
def entrada(micro_tubo,n):              #input function
    
    micro_tub_2=micro_tubo.copy()           
    for w in range(n):
        alpha=random.random()     
        if alpha<=a:     
            if micro_tub_2[0]==0:
                micro_tub_2[0]=1 
                ty=micro_tub_2.copy()
                matriz.append(ty)
    return micro_tub_2
    
    
def salida(micro_tubo,n):               #output function
    beta=random.random()
    if beta<=b:
        micro_tubo[n-1]=0
    return micro_tubo
    

                    
def tasep(micro_tubo,n):                #tasep-lk evaluation function
    for h in range(n-1):
        theta=random.random()
        gamma=random.random()
        if micro_tubo[h]==0:
            if gamma<=t1:               #step input
                micro_tubo[h]=1
                ty=micro_tubo.copy()
                matriz.append(ty)
                
        else:
            if theta <=t2:              #step output
                micro_tubo[h]=0     
                ty=micro_tubo.copy()
                matriz.append(ty)
                
    return micro_tubo

def apply_rules(carino):
    length = len(carino)
    for z in range(length):
        [carino[z][0:n]]
      

def update(index,img, carino):
    length = len(matriz)
    if index<length:   
        img.set_data([matriz[index]])

def animate(n):
    caminado(n)
    length = len(matriz)
    for z in range(length):
        carino=[matriz[z][0:n]]
        
        fig, ax = plt.subplots()
        ax.set_axis_off()
        img=plt.imshow(carino,cmap=plt.cm.binary)
    anim = animation.FuncAnimation(fig, update, fargs=(img,carino,), interval=100)

    anim.save('simulation2.gif', writer='molecularmotor')
    
print("---------------------------------")
if __name__ == '__main__':
    animate(100)
    
