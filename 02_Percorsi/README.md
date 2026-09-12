# Percorsi

Due macro aree, divise per durata. Ogni percorso è completo dentro la propria cartella.

```
02_Percorsi/
  20h/   Infanzia · Primaria · Secondaria · Segreteria_ATA
  10h/   Scuola_10h · Segreteria_10h
```

## 20h · 10 incontri da 2 ore

| Cartella | Stato |
|---|---|
| `20h/Primaria/` | completo. È il percorso di riferimento: gli incontri comuni 01-05 e 10 che stanno qui dentro sono la **versione base** da cui derivano gli altri percorsi. |
| `20h/Infanzia/` | comuni adattati e pratica 06 fatta. Le pratiche 07, 08, 09 contengono ancora i deck della Primaria come segnaposto. |
| `20h/Secondaria/` | completo: comuni, quattro pratiche e consegna in PDF. |
| `20h/Segreteria_ATA/` | completo: comuni, quattro pratiche e scalette formatori. Mancano i PDF di consegna. |

## 10h · 10 moduli da 1 ora, aggregabili in 5 incontri da 2 ore

| Cartella | Stato |
|---|---|
| `10h/Scuola_10h/` | **gruppi misti** (primaria, medie, superiori). Derivato dalla Primaria: dibattiti extra marcati col flag "se avanza tempo", Incontro 5 senza il Progetto, blocco pratico su **Gemini** al posto di Claude. Vedi `10h/Scuola_10h/CAMBIAMENTI.md`. |
| `10h/Segreteria_10h/` | **personale ATA e di segreteria**. Derivato dalla Segreteria_ATA 20h con lo stesso metodo: flag "se avanza tempo", Incontro 5 senza il Progetto, blocco pratico su **Gemini**. Modulo 6 riscritto, moduli 7, 8 e 9 convertiti senza perdere slide. Vedi `10h/Segreteria_10h/CAMBIAMENTI.md` e `01_Progetto/PIANO_SEGRETERIA_GEMINI.md`. |

I programmi ufficiali delle quattro edizioni da 10 ore (Primaria, Secondaria, Segreteria, Formatori e Figure di sistema) stanno in `01_Progetto/Programmi/10h/`. I deck costruiti sono due: il misto e la segreteria. Mancano ancora Formatori e Figure di sistema.

## Schema interno, uguale per tutti

- `01_Incontro_1` … `05_Incontro_5`: blocco comune, 12 ore con il 10.
- `06` … `09`: blocco pratico, 8 ore, uno strumento per incontro.
- `10_Incontro_10`: futuro e chiusura.
- `_Consegna/`: i PDF e lo zip da passare a formatori e scuole.

In `10h/Scuola_10h/` lo schema è lo stesso, ma ogni modulo dura 1 ora e la pratica 06 è su Gemini (`06_Pratica_Gemini`).

Metodo di lavoro e piano dei due percorsi mancanti: `01_Progetto/PIANO_SECONDARIA_SEGRETERIA.md`.
Impianto dei percorsi da 10 ore: `01_Progetto/PIANO_PERCORSI_10H.md`.
Standard su scalette, slide e testi: `00_Standard/MODUS_OPERANDI.md`.
