# Percorso Segreteria 10h · cosa è cambiato

> Sorgente: percorso **Segreteria_ATA 20h**. Pubblico: personale ATA e di segreteria.
> 10 moduli da 1 ora. Aggregabili in 5 incontri da 2 ore.
> Strumento del blocco pratico: **Gemini** al posto di Claude.
> Metodo: lo stesso di `10h/Scuola_10h`. Piano completo: `01_Progetto/PIANO_SEGRETERIA_GEMINI.md`.

## La regola: non si tagliano le slide, si taglia il tempo

Dove c'erano più domande di dibattito, la prima resta e le altre prendono un flag in basso a destra: **"Se avanza tempo. Altrimenti resta uno spunto: ci ragionate voi."**
Le domande non spariscono dalle slide, così i partecipanti ci ragionano comunque. Sono 16 slide in tutto.

Le uniche due eccezioni sono il **modulo 5**, che perde il Progetto, e il **modulo 6**, che è un deck nuovo.

## Modulo per modulo

| # | Deck | Slide | Cosa è cambiato |
|---|---|---|---|
| 1 | Incontro 1 | 31, invariate | Flag su 27 e 29. Restano attivi il dibattito di apertura (4) e quello sul loro ufficio (26). |
| 2 | Incontro 2 | 43, invariate | Flag su 9, 21, 26, 35. Resta attiva la pratica finale. |
| 3 | Incontro 3 | 32, invariate | Flag sul terzo e quarto caso di "Lo useresti?" (24 e 25). **Il dibattito 15 resta attivo:** è l'unico del modulo, e i primi due casi (la circolare pubblica e l'elenco degli alunni) sono quelli che insegnano la regola. Il **caso Anthropic resta**: è diritto d'autore, non pubblicità a un concorrente. |
| 4 | Incontro 4 | 44, invariate | Flag su Pratica 1 (32 e 33): in un'ora si fa una pratica sola, e la Pratica 2 è quella che porta a casa i materiali. La scheda del ripasso dice "il contesto permanente" al posto del "Progetto". |
| 5 | **Incontro 5** | **da 40 a 33** | Tolto il Progetto: cadono sette slide (la parte 2, il contesto sempre uguale, dentro il Progetto, il tutorial, il prompt di inizio, la prima chat, il Progetto compilato) sostituite da tre che raccontano la stessa cosa come **contesto permanente**. Cade la 29 ("il Progetto si rifà ogni volta"). Le due slide sulle **quattro versioni per ordine di grado diventano una**, quella della segreteria: nel 20h restano quattro, qui no. La pratica passa da due tempi a uno: si scrive il file, la Gem si costruisce nel modulo 6. **IPU resta intera.** |
| 6 | **Pratica 1 · Gemini** | **deck nuovo, 20** | Struttura: com'è fatto Gemini (chat, file, Canvas, Gem), la regola sui dati ripresa dal modulo 3, poi **due Gem**. La prima è lo **scrittore di prompt**, testo pronto, tre minuti, uguale per tutti (asset `Asset_Gem_Scrittore_di_Prompt.md`). La seconda è la **Gem Mail dell'ufficio**, costruita col file del modulo 5 e con l'archivio (`Gem_Demo_Mail/`). Poi le istruzioni personalizzate e quattro idee di Gem. **Niente routine e niente cruscotto:** in un'ora non ci stanno, e sono le due cose che dipendono dalla licenza. Cade anche tutta la parte su Chat, Cowork e Code e il creatore di abilità. 35 minuti sulle mani. |
| 7 | Pratica 2 · Dati e ricerca | 27, invariate | **Il deck non si taglia.** Il secondo prompt, quello del fornitore, prende il flag: la slide 15 col riquadro pieno, le 16, 17 e 18 con la versione compatta in alto a destra. I due prompt lunghi non cambiano di una parola. La slide 21 passa a Gemini e cade la nota sull'add-in di Excel: al suo posto, portare il registro in Google Sheets e chiamare Gemini da dentro il foglio. Il secondo hands-on diventa compito a casa col prompt consegnato. |
| 8 | Pratica 3 · NotebookLM | 11, invariate | Invariata. Solo il tempo della pratica, da 1 ora a 35 minuti. |
| 9 | Pratica 4 · Laboratorio | 16, invariate | Invariato nell'obiettivo. Claude diventa Gemini nel ripasso, nel flusso e nei due prompt di esempio. Il Progetto Mail diventa la Gem Mail. Il laboratorio passa da 85 a 35 minuti. |
| 10 | Incontro 10 | 36, invariate | Il ripasso del Progetto diventa ripasso del contesto permanente. La scheda dei quattro strumenti è riallineata ai quattro moduli veri: **Gemini, Deep Research, NotebookLM, Gemini nei fogli**. Nel 20h c'è ancora "Granola e Canva", che in quel percorso non si insegnano: lì non è stato toccato. Flag su 31 e 32, resta attiva la domanda che chiude il cerchio (33). |

## Il dizionario Claude e Gemini

| Nel 20h | Qui |
|---|---|
| Progetto | **Gem** (istruzioni più fino a 10 file di conoscenza, anche da Drive) |
| Preferenze personali | **Istruzioni personalizzate** |
| Skill richiamata con "/" | **Una Gem per lavoro.** Non esiste un equivalente, e il messaggio cambia di conseguenza |
| Ricerca approfondita | **Deep Research** |
| Fogli dentro Claude | File caricato in chat, oppure il registro portato in Google Sheets con **Chiedi a Gemini** |
| Claude in Excel | **Gemini in Google Sheets**, che non si installa |
| Live Artifact | **Canvas**. Nel 10h non si insegna: la slide del cruscotto è caduta |
| Automazioni | **Scheduled actions**. Nel 10h non si insegnano: la slide della routine è caduta |

## Da verificare prima dell'aula

- [ ] Gemini attivo sull'account Workspace dell'istituto, e le **Gem** disponibili
- [ ] **Deep Research**: sul piano gratuito sono 5 ricerche al mese, quindi una a testa in aula basta
- [ ] **Caricamento di file** consentito dall'amministratore di dominio: senza quello cadono la Gem con i materiali e tutto il modulo 7
- [ ] Riprovare su Gemini i numeri del `Registro_richieste_sportello.xlsx`: il `README_FORMATORE.md` promette al formatore risultati precisi
- [ ] Piano B trasversale: se l'account della scuola è chiuso si lavora con l'account personale su `gemini.google.com`. Cambia l'accesso, non la lezione

## Tempi, modulo tipo

Teorico: 27 minuti di esposizione, 28 di dibattito, 5 di chiusura.
Pratico: 18 minuti di guida, 37 di mani sulla tastiera, 5 di condivisione.

Attenzione: il blocco pratico del 20h vale **10h15 di materiale dichiarato** contro le 8 ore di budget. Portarlo a 4 ore è un taglio del 61%, non del 50%. Il modulo 7 resta il più teso: si regge sul fatto che la Deep Research si lancia al minuto dieci e si riapre al minuto quaranta, mentre si lavora sui fogli.
