# Percorso Formatori 10h · Insegnare a insegnare l'IA

> Per formatori e figure di sistema: docenti che dovranno formare i colleghi sull'intelligenza artificiale.
> 10 moduli da 1 ora, 5 teorici e 5 pratici. Aggregabili in 5 incontri da 2 ore.
> Strumento: **Gemini**, usato e spiegato. Nessun altro strumento è necessario.
> Costruito il 16 novembre 2026. Non ancora erogato.

## In una frase

Alla fine delle dieci ore ogni partecipante ha in mano **un percorso suo**, per i propri colleghi: pubblico e traguardo scritti, casi d'uso scelti, una sequenza di incontri, un incontro costruito per intero, sei minuti provati davanti a qualcuno, e una data.

## Come è fatto

**Il doppio binario.** Ogni cosa che insegniamo a fare con i colleghi, prima la facciamo con i partecipanti (sono corsisti), poi la smontiamo (sono formatori), poi la rifanno sul proprio percorso. In ogni deck c'è una slide **"Sotto il cofano"** che dice cosa è stato fatto con loro in quell'ora, e perché.

**I 6 passi** sono la mappa del percorso. **Le 4 mosse** e **il blocco** sono i due stampi di una lezione.

| Incontro | Modulo teorico | Modulo pratico (Gemini) | Passo | Cosa esce dalle mani |
|---|---|---|---|---|
| 1 | **1 · Il mestiere di chi forma** | **2 · Gemini: la base, fatta bene** (chat, file, le 5 fasi, farsi intervistare) | 1 Pubblico, 2 Traguardo | Scheda del pubblico e traguardo |
| 2 | **3 · Dal bisogno alla sequenza** | **4 · L'assistente che vi conosce** (Gem o Skill: lo scrittore di prompt e il progettista di percorsi) | 3 Casi d'uso, 4 Sequenza | L'assistente, tre casi d'uso, la sequenza |
| 3 | **5 · Costruire la lezione** | **6 · Dalla scaletta ai materiali** (Canvas: scaletta, slide, foglio dei prompt) | 5 Lezione | Un incontro intero |
| 4 | **7 · Condurre l'aula** | **8 · La demo, i dati, le obiezioni** (Deep Research, il collega difficile, l'esercizio con l'errore) | 6 Regia | Un dato verificato, un'obiezione provata, la lista dei controlli |
| 5 | **10 · Dopo l'aula** | **9 · Sei minuti in aula** (la prova, con il riscontro dei colleghi) | Prova e correzione | Tre riscontri e il piano con la data |

Nell'ultimo incontro la prova (modulo 9) viene prima della chiusura (modulo 10).

## Cosa c'è in questa cartella

```
01_Modulo_1 … 10_Modulo_10
   Modulo_N.html                  il deck (sorgente, export PDF via stampa)
   MODULO_N_SCALETTA.md           la scaletta per chi conduce: minuti, cosa dire, punti di controllo,
                                  cosa saltare se si è in ritardo, riserve, cose da preparare
   Modulo_N_guida_formatore.html  solo nei moduli pratici (2, 4, 6, 8, 9): cosa mostrare a schermo, in ordine
04_Modulo_4/Asset_Assistente_*.md i testi delle istruzioni dei due assistenti, identici alle slide
Materiali/
   Quaderno_del_formatore.html    il quaderno dei partecipanti: il metodo in una pagina e sei schede
   PROMPT_PRONTI.md               tutti i prompt del percorso, identici alle slide
NOTE_EROGAZIONE.md                verifiche sugli account, Gem e Skill, le mail pronte, cosa non è ancora provato
CAMBIAMENTI.md                    da dove viene ogni pezzo, e il registro delle correzioni dopo le aule
_Consegna/                        PDF e zip per i formatori (è una copia, non una fonte)
```

Il perché di ogni scelta, il reverse engineering dei percorsi esistenti e le fonti verificate stanno in `01_Progetto/PIANO_FORMATORI_10H.md`.
Il programma ufficiale è `01_Progetto/Programmi/10h/PROGRAMMA_10h_Formare_i_Formatori.html`.

## I tempi

| Modulo | Tipo | Slide | Esposizione o guida | Stanza che lavora | Chiusura |
|---|---|---|---|---|---|
| 1 | teorico | 24 | 26 | 28 | 6 |
| 2 | pratico | 23 | 20 | 36 | 4 |
| 3 | teorico | 23 | 28 | 27 | 5 |
| 4 | pratico | 20 | 24 | 33 | 3 |
| 5 | teorico | 23 | 28 | 27 | 5 |
| 6 | pratico | 16 | 22 | 33 | 5 |
| 7 | teorico | 22 | 27 | 27 | 6 |
| 8 | pratico | 16 | 22 | 33 | 5 |
| 9 | pratico | 14 | 9 | 43 | 8 |
| 10 | teorico | 20 | 26 | 26 | 8 |
| **Totale** | | **201** | **232** | **313** | **55** |

Laboratori e dibattiti: 313 minuti su 600, il **52%**. Il vincolo del bando (almeno il 50%) regge, ma solo se ogni modulo tiene il suo pezzo pratico: per questo ogni scaletta dice cosa si protegge sempre.

## Prima di erogarlo

1. Leggere `NOTE_EROGAZIONE.md`, soprattutto la parte su Gem e Skill.
2. **Provare tutti i prompt dentro Gemini**, sull'account che si userà: sono stati scritti e riletti, non ancora provati.
3. Aprire i deck in Chrome e guardarli a schermo intero almeno una volta. Le slide più dense, da controllare per prime: modulo 4 slide 9, 11 e 12 (i testi delle istruzioni) e modulo 1 slide 13.
4. Esportare i PDF se servono aggiornati: stampa, orizzontale, margini nessuno, grafica di sfondo attiva.
