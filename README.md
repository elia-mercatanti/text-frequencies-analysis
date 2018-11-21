# Frequency Analyzer

Sviluppo di un programma che consenta l'analisi delle frequenze in un testo (sequenza di caratteri).

Esercizio di programmazione 3.1 per il Corso Data Security and Privacy - Set 1

# Come Utilizzarlo

Il codice sviluppato per questo programma richiede i sequenti pacchetti: 'numpy', 'matplotlib' e 'pandas'. Tali 
pacchetti devono essere installati prima di far partire l'applicazione.

Per testare il codice è sufficente avviare tramite un interprete python il file Frequency_Analyzer.py

# Come Funziona

Una volta avviato, il programma richiede all'utente di inserire il nome del file che contiene il testo da analizzare.
- Ogni testo, per essere analizzato, deve essere salvato in un file .txt nella cartella 'texts'.
- Nella cartella 'text' è gia presente di default il testo relativo al primo capitolo di Moby dick, chiamato 
  "moby_dick_chapter1.txt".
- Se vogliamo analizzare il testo di Moby Dick basterà inserire il nome del file "moby_dick_chapter1.txt" quando il 
  programma lo richiede all'inizio.

Una volta inserito il nome del file di testo l'applicazione stampa a video un piccolo menù dove è possibile avviare
le principali funzioni di analisi del testo. Per avviare una funzione basta semplicemente inserire il numero 
corrispondente ad essa e premere invio.

Di seguito viene riportato cosa producono tutte e 4 le funzioni.
1. Histogram of the frequency of the 26 letters.
   Funzione che consente all'utente di disegnare l'istogramma della frequenza delle lettere nel testo selezioanto da
   analizzare.
   - Il grafico dell'istogramma viene inoltre salvato in formato pdf nella cartella "plots".
2. Empirical distribution of q-grams.
   Funzione che consente all'utente di calcolare la distribuzione empirica dei q-grammi.
   - Una volta avviata la funzione viene richiesto all'utente di inserire il parametro q per decidere la lunghezza dei
     q-grammi che si vuole analizzare.
3. Index of coincidence and entropy of the q-grams distribution.
   Funzione che consente all'utente di calcolare l'indice di coincidenza e l'entropia della distribuzione dei q-grammi
   calcoalta con la funzione precedente.
   - Se l'utente avvia questa funzione prima di aver eseguito la funzione 2 viene stampato un messaggio di errore che 
     avvisa l'utente di eseguire prima la funzione 2.
4. Quit.
   Funzione che consente la chiusura del programmma.

# Author
Elia Mercatanti