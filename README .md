# 🏎️ Motorsport Telemetry Analysis Tool

Repository dedicata allo sviluppo di script in Python per l'estrazione, l'elaborazione e la visualizzazione grafica di dati telemetrici reali del motorsport.

## 📊 Progetto Principale: `telemetria_reale.py`
Questo script permette di effettuare un'**analisi comparativa delle prestazioni tra due piloti** estraendo i dati telemetrici ufficiali delle sessioni di Formula 1 tramite API.

### 🚀 Funzionalità Chiave
- **Integrazione API:** Connessione ai flussi dati ufficiali tramite la libreria `FastF1`.
- **Data Filtering:** Isolamento automatico e ottimizzato dei giri più veloci (*fastest laps*) di ciascun pilota tramite algoritmi in `Pandas`.
- **Analisi della Distanza (Distance-based):** Sovrapposizione dei grafici basata sullo spazio tracciato (e non sul tempo) per garantire la perfetta confrontabilità dei punti di staccata, velocità di percorrenza e inserimento in curva.
- **Visualizzazione Avanzata:** Generazione di grafici ad alta risoluzione del profilo *Speed-vs-Distance* con palette colori ufficiali dei team tramite `Matplotlib`.

### 🛠️ Tecnologie e Librerie Utilizzate
- **Language:** Python 3
- **Data Manipulation:** Pandas, NumPy
- **Motorsport Data Handling:** FastF1
- **Data Visualization:** Matplotlib

---
*Progetto sviluppato in ottica di applicazione pratica per i reparti Elettronica e Vehicle Performance nei contesti Formula Student.*
