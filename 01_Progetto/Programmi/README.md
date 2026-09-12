# Programmi ufficiali

I documenti che si mandano alle scuole. Stessa impaginazione per tutti: 13 pagine 16:9, deck HTML autonomo, PDF esportato dallo stesso file.

```
Programmi/
  20h/   i quattro percorsi da 10 incontri da 2 ore
  10h/   le quattro edizioni da 10 moduli da 1 ora
```

## 20h

| File | Percorso | Colore |
|---|---|---|
| `20h/PROGRAMMA_Primaria.html` | Primaria | viola |
| `20h/PROGRAMMA_Infanzia.html` | Infanzia | corallo |
| `20h/PROGRAMMA_Secondaria.html` | Secondaria | ciano |
| `20h/PROGRAMMA_ATA_Segreteria.html` | ATA e Segreteria | verde |

## 10h

| File | Percorso | Colore |
|---|---|---|
| `10h/PROGRAMMA_10h_Primaria.html` + `.pdf` | Primaria | viola |
| `10h/PROGRAMMA_10h_Secondaria.html` + `.pdf` | Secondaria | ciano |
| `10h/PROGRAMMA_10h_Segreteria.html` + `.pdf` | ATA e Segreteria | verde |
| `10h/PROGRAMMA_10h_Formatori_Figure_di_Sistema.html` + `.pdf` | Formatori e figure di sistema, gruppo misto primaria e secondaria | indaco |
| `10h/PROGRAMMA_Scuola_10h.html` | versione generica "Scuola", precedente alle quattro edizioni | viola |

Le quattro edizioni da 10 ore hanno gli stessi 10 moduli, ma i punti di ogni modulo sono riscritti sul pubblico. Nel modulo 5 si insegna il file di contesto permanente al posto del Progetto, come deciso in `PIANO_PERCORSI_10H.md`. Lo strumento del blocco pratico è Gemini.

## Come si esporta il PDF

Non basta la stampa da riga di comando: perde gli sfondi colorati e il font Inter. Serve Chrome pilotato via protocollo, con `printBackground: true`, foglio 1280x720 px e attesa di `document.fonts.status === "loaded"`.
