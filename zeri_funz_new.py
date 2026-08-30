import matplotlib.pyplot as plt
import math
import sympy as sp
import numpy as np

#DERIVATA DELLA FUNZ.
def deriv(f):
    x = sp.symbols('x')
    derivata=sp.diff(f, x)
    return derivata

def newton(x0, f_num, d_num, t, max_i):
    x_n=x0
    s=t+1 #SERVE PER CAPIRE SE CI STIAMO AVVICINANDO O NO ALLO 0
    c=0
    while s>t and c<max_i:
        y=f_num(x_n)
        der=d_num(x_n)
        
        if abs(der)<t:
            print('ATTENZIONE! Derivata nulla in: ',x_n)
            x_n1=x_n-y/der
            return None
        
        x_n1 = x_n - y / der
        s = abs(x_n1 - x_n) # AGGIORNAMENTO SCARTO
        x_n = x_n1
        c += 1
        if c<max_i:
            print(c,'° iterazione:',x_n) 
    print('La soluzione determinata dopo',c,'iterazioni vale:',x_n)
    return x_n

x=sp.symbols('x') #DEFINISCE LA X COME SIMBOLO(OVVERO QUELLA CHE CAMBIA)
funz=input('Inserisci la funzione-> ')
f=sp.simplify(funz) #RENDE LA FUNZ LEGGIBILE DA SYMPY (CONVERTE LE STRINGHE IN "FUNZIONI" MATEMATICHE LEGGIBILI DA SYMPY)
d=deriv(f)
f_num=sp.lambdify(x, f, 'numpy') #CONVERTE LA FUNZIONE SIMBOLICA (f) IN FUNZIONE REALE
d_num=sp.lambdify(x, d, 'numpy')

#PRIMO GRAFICO SENZA INTERSEZIONI

punti_x = np.linspace(-10, 10, 2000) #GENERA 2000 PUNTI TRA -10 E 10
plt.plot(punti_x, f_num(punti_x),label=funz,color='orchid')
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.title('FUNZIONE')
plt.legend(loc='best')
plt.axhline(0,color='black')  
plt.axvline(0,color='black')
plt.grid(True)
plt.show()

x0=float(input('Inserisci una X che potrebbe essere vicino allo 0 della funzione-> '))
t=float(input('Inserisci la tolleranza massima-> '))
max_i=int(input('Inserisci il massimo di iterazioni-> '))

#GRAFICO CON L'INTERSEZIONI

zero=newton(x0, f_num, d_num, t, max_i)
plt.plot(punti_x, f_num(punti_x),label=funz,color='orchid')
plt.plot(zero,0,'o', color='red', label='intersezioni x')
plt.annotate(xy=(zero,0),text=round(zero,3))
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.grid(True)
plt.show()