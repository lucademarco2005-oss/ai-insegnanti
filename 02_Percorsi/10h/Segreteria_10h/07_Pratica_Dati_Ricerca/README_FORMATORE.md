# Lezione 2 pratica · Dati e ricerca · Guida per il formatore

## Il file demo: `Registro_richieste_sportello.xlsx`

Un registro finto ma verosimile delle richieste arrivate in segreteria in un anno scolastico, da settembre ad aprile. **240 righe, nessun dato personale**: non c'è un nome, un indirizzo o un numero di protocollo. È il file su cui gira tutta la Parte B.

Colonne: Data, Canale, Tipo di richiesta, Ufficio, Minuti impiegati, Esito, Note.

### È sporco apposta
Le sporcature sono quelle vere di un registro tenuto a mano da più persone:
- **Date in tre formati diversi** (2025-10-14, 14/10/2025, 4/3/2026) e **una data impossibile** (31/02/2026)
- **Lo stesso tipo di richiesta scritto in quattro modi** ("Informazioni iscrizioni", "info iscrizioni", "INFO ISCRIZIONI", "informazioni su iscrizione")
- **Canali e uffici** con maiuscole diverse e spazi finali ("Didattica " con lo spazio)
- **Due righe completamente vuote** e **due righe duplicate**
- **Una cella "Minuti impiegati" scritta a parole** ("circa 15")

Se il file fosse pulito, la lezione non avrebbe senso: metà del valore è vedere che l'IA se ne accorge e chiede.

### Cosa deve uscire dall'analisi (i numeri veri)
Servono al formatore per capire se il risultato è giusto, **non vanno anticipati in aula**.

| | |
|---|---|
| Richieste totali | 238 valide, più 2 righe vuote e 2 duplicati |
| Tipo più frequente | **Informazioni iscrizioni: 62 richieste** |
| Tempo che si mangia | **916 minuti, oltre 15 ore in un anno**, solo per quelle |
| Secondo per tempo | Problema registro elettronico: 31 richieste, 455 minuti |
| Mese di picco | **Gennaio: 46 richieste contro le 26 di un mese normale** |
| Canali | Mail 85, telefono 84, sportello 69: quasi in parità |

### Il colpo finale della lezione
Le due voci in cima, informazioni iscrizioni e problema registro elettronico, valgono insieme **circa 1370 minuti l'anno, quasi 23 ore**. Sono ore spese a rispondere sempre alle stesse due domande.

La conclusione che deve arrivare da sola: **un avviso fatto bene e una FAQ tolgono tre giornate di lavoro all'anno.** E l'avviso e la FAQ li sanno già fare, li hanno costruiti nella lezione su Claude con la skill "risposta allo sportello". La lezione sui dati non serve a fare grafici: serve a **decidere cosa scrivere**.

## Come si sostituisce con dati veri
Il file è ricostruito. Se una scuola fornisce il proprio registro, si sostituisce, a due condizioni: nessun nome e nessun riferimento identificabile, e almeno le colonne tipo, canale e tempo. La lezione funziona identica.

## Perché non usiamo il componente aggiuntivo di Excel
Si lavora **dentro Claude**: si carica il file, si lavora, si scarica il risultato. Nessun add-in da installare, nessun piano da verificare, nessuna dipendenza dalla versione di Office dell'istituto. Claude in Excel si cita in due righe e si va avanti: esiste, fa la stessa cosa dentro il foglio, e chi vuole se lo guarda a casa.
