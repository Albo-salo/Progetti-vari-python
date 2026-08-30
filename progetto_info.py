import matplotlib.pyplot as plt

#def per calcolare le y per il grafico trategg. e non

def f(lx):
    ly=[]
    l1_x=[]
    l1_y=[]
    i=0
    while i<len(lx):
        x=lx[i]
        y=eval(p)
        ly.append(y)
        if lx[i]>-1.9 and lx[i]<1.9:
            l1_x.append(lx[i])
            x=lx[i]
            y=eval(p)
            l1_y.append(y)
        i+=1
    return ly,l1_x,l1_y

#intersezione con asse x

def itr_x(ly,lx):
    x_intersezioni=[]
    y_intersezioni=[]
    i=0
    while i< len(ly)-1:
        if ly[i]*ly[i+1]<0:
            m=round((lx[i]+lx[i+1])/2,2)
            x_intersezioni.append(m)
            y_intersezioni.append(0)
        i+=1
    return x_intersezioni,y_intersezioni

#intersezione con asse y

def itr_y(p):
    x=0
    y=round(eval(p),2)
    return x,y

#valori massimi e minimi di x e y

def max_P(ly):
    t=1
    l_max_x=[] 
    l_max_y=[] 
    l_min_x=[] 
    l_min_y=[] 
    while t<(len(ly)-1): 
        if (ly[t]>ly[t-1]) and (ly[t]>ly[t+1]): 
            l_max_x.append(lx[t]) 
            l_max_y.append(ly[t]) 
        if (ly[t]<ly[t-1]) and (ly[t]<ly[t+1]): 
            l_min_x.append(lx[t]) 
            l_min_y.append(ly[t]) 
        t+=1
    return l_max_x,l_max_y,l_min_x,l_min_y

#controllo se la funzione è pari, dispari o nessuna delle due

def controlla_parita(p):
    test_x = [1, 2, 3]
    pari=True
    dispari=True
    i=0
    while i<len(test_x):
        x=test_x[i]
        y_pos=eval(p)
        x =-test_x[i]
        y_neg=eval(p)
        if y_pos!=y_neg:
            pari=False
        if y_pos!=-y_neg:
            dispari=False
        i+=1
    if pari:
        print("La funzione è pari")
    elif dispari:
        print("La funzione è dispari")
    else:
        print("La funzione non è né pari né dispari")

#inizializzo tutte le variabili

lx=[]
i=-2
e=0
z=0
d=0

#while per 'generare' delle x

while i<=2:
    lx.append(i)
    i+=0.001

scelta=input('''La funzione da visualizzare la vuoi creare specificando il grado della x e poi i coeficienti o la vuoi creare te da capo?
               digita:  
               1 grado della x e coefficienti
               2 crearla da 0
               scelta (digita il numero)-> ''')
if scelta=='1':
    p=''
    g=int(input('Grado della x-> '))
    gr=g
    o=0
    while o<=g:
        coef=input('Inserisci il coefficiente-> ')
        if gr!=0:
            p+=coef+"*x**"+str(gr) +'+'
            gr-=1
        else:
            p += coef + "*x**"+ str(gr)
        o+=1
    p=p.replace('^','**')
    s=p.replace('**','^')
    ly,l1_x,l1_y=f(lx)
    l_max_x,l_max_y,l_min_x,l_min_y=max_P(ly)
    x,y=itr_y(p)
    x_intersezioni,y_intersezioni=itr_x(ly,lx)
    print("Funzione generata:", p)
    
    #stampo il valore delle intersezioni
    
    while e<len(x_intersezioni):
        x_val=x_intersezioni[e]
        y_val=y_intersezioni[e]
        plt.annotate(xy=(x_val,y_val),text=(x_val))
        e+=1
    
    #stampo il punto min
    
    while d<(len(l_min_x)):
        x_min=round(l_min_x[d],1)
        y_min=round(l_min_y[d],1)
        plt.annotate(xy=(x_min,y_min),text=(x_min,y_min))
        d+=1
    
    #stampo il punto max
    
    while z<(len(l_max_x)): 
        x_max=round(l_max_x[z],1)
        y_max=round(l_max_y[z],1)
        plt.annotate(xy=(x_max,y_max),text=(x_max,y_max))
        z+=1
    
    #creo il grafico
    
    plt.plot(lx,ly,'--',color='orchid')
    plt.plot(l1_x,l1_y,'-',label=s,color='orchid')
    plt.plot(x_intersezioni, y_intersezioni, 'o', color='red', label='intersezioni x')
    plt.plot(x,y,'o',color='orange',label='intersezioni y')
    plt.hlines(0,min(lx),max(lx),linestyles='-',color='black')
    plt.vlines(0,min(ly),max(ly),linestyles='-',color='black')
    plt.xlim(min(lx),max(lx))
    plt.ylim(min(ly),max(ly))
    plt.fill_between(lx, ly, color='orchid', alpha=0.1)
    plt.annotate(xy=(x,y),text=(y))
    plt.plot(l_max_x,l_max_y,'o',color='green',label='punto max')
    plt.plot(l_min_x,l_min_y,'o',color='blue',label='punto min') 
    plt.title('FUNZIONE')
    plt.legend(loc='best')
    plt.grid()
    plt.show()
    controlla_parita(p)

if scelta=='2':
    p=input('Inserisci la funzione-> ')
    p=p.replace('^','**')
    s=p.replace('**','^')
    ly,l1_x,l1_y=f(lx)
    x_intersezioni,y_intersezioni=itr_x(ly,lx)
    x,y=itr_y(p)
    l_max_x,l_max_y,l_min_x,l_min_y=max_P(ly)
    
    #stampo il punto max e il punto min

    while z<(len(l_max_x)): 
        x_max=round(l_max_x[z],1)
        y_max=round(l_max_y[z],1)
        plt.annotate(xy=(x_max,y_max),text=(x_max,y_max))
        z+=1
    while d<(len(l_min_x)):
        x_min=round(l_min_x[d],1)
        y_min=round(l_min_y[d],1)
        plt.annotate(xy=(x_min,y_min),text=(x_min,y_min))
        d+=1

    #stampo il valore delle intersezioni 

    while e<len(x_intersezioni):
        x_val=x_intersezioni[e]
        y_val=y_intersezioni[e]
        plt.annotate(xy=(x_val,y_val),text=(x_val))
        e+=1
    
    plt.plot(x_intersezioni,y_intersezioni,'o',color='red')

    plt.plot(x,y,'o',color='orange')

    #creazione grafico

    plt.plot(lx,ly,'--',color='orchid')
    plt.plot(l1_x,l1_y,'-',label=p,color='orchid')
    plt.plot(x_intersezioni, y_intersezioni, 'o', color='red', label='intersezioni x')
    plt.plot(x,y,'o',color='orange',label='intersezioni y')
    plt.hlines(0,min(lx),max(lx),linestyles='-',color='black')
    plt.vlines(0,min(ly),max(ly),linestyles='-',color='black')
    plt.xlim(min(lx),max(lx))
    plt.ylim(min(ly),max(ly))
    plt.fill_between(lx, ly, color='orchid', alpha=0.1)
    plt.annotate(xy=(x,y),text=(y))
    plt.plot(l_max_x,l_max_y,'o',color='green',label='punto max')
    plt.plot(l_min_x,l_min_y,'o',color='blue',label='punto min') 
    plt.title('FUNZIONE')
    plt.legend(loc='best')
    plt.grid()
    plt.show()
    controlla_parita(p)