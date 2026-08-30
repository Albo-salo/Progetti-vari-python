import matplotlib.pyplot as plt
import math
import numpy as np

#LISTA DELLE Y DELLA FUNZ.
def f(lx, funz):
    ly = [eval(funz, {'x':x,**math.__dict__}) for x in lx]
    return ly

#ZERI FUNZ. METODO BIS.
def zeri(funz, a, b, t):
    def f(x):
        return eval(funz, {'x':x,**math.__dict__}) #PER PRENDERE ANCHE TRIGONOMETRIA (basta solo scrivere cos/tan/sin..., dict sta per dizionario)
    
    if f(a)*f(b)>0:
        print ('Non ci sono intersezioni')
        return None
    i=1
    while (b-a)>t:
        c=(a+b)/2
        if f(c)==0:
            print ('La soluzione determinata dopo',i,'iterazioni vale:',c)
            i+=1
            return c
        if f(a)*f(c)<0:
            b=c
            print (i,"° iterazione: ", b)
            i+=1
        else:
            a=c
            print (i,"° iterazione: ", a)
            i+=1
    print ('La soluzione determinata dopo',i,'iterazioni vale: ',(a+b)/2,'e si trova nell intervallo [',a,',',b,']')
    return (a+b)/2

#CREAZIONE LISTA DELLE X DELLA FUNZ.
lx=[]      
funz=input('Inserisci la funzione-> ')
i=-10
while i<=10:
    lx.append(i)
    i+=0.001

ly=f(lx, funz)

#PARTE GRAFICO
plt.plot(lx,ly,'-',label=funz,color='orchid')
plt.title('FUNZIONE')
plt.legend(loc='best')
plt.axhline(0,color='black')  
plt.axvline(0,color='black') 
plt.grid()
plt.show()

a=float(input('Inserisci estremo inf. intervallo di separazione-> '))
b=float(input('Inserisci estremo sup. intervallo di separazione-> '))
t=float(input('Inserisci la precisione richiesta-> '))

zero=zeri (funz, a, b, t)


#GRAFICO CON INT. SEGNATA
plt.plot(lx,ly,'-',label=funz,color='orchid')
plt.plot(zero,0,'o', color='red', label='intersezioni x')
plt.annotate(xy=(zero,0),text=round(zero,3))
plt.title('FUNZIONE')
plt.legend(loc='best')
plt.axhline(0,color='black')  
plt.axvline(0,color='black') 
plt.grid()
plt.show()