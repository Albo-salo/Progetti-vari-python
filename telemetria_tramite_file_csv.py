import pandas as pd
import time
import matplotlib.pyplot as plt
df=pd.read_csv('telemetria.csv')
plt.ion()
fig, ax= plt.subplots()
linea, =ax.plot([],[],color='black', marker='o')
ax.set_title('Velocità in tempo reale')
ax.set_xlabel('Tempo (s)')
ax.set_ylabel('Velocità (km/h)')
ax.grid(True)
tempi=[]
veloc=[]
for i in range (len(df)):
    tempo=df['tempo'][i]
    vel=df['velocità'][i]
    tempi.append(tempo)
    veloc.append(vel)
    linea.set_data(tempi, veloc)
    ax.relim()
    ax.autoscale_view()
    plt.draw()
    plt.pause(1)
print('Finito')
plt.show()
input('Invio per chiudere')
plt.close()