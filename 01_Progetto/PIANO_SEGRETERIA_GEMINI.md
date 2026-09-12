# Segreteria 10h su Gemini · piano di costruzione

> Sorgente: `02_Percorsi/20h/Segreteria_ATA/`, che resta il riferimento.
> Metodo: lo stesso già usato per `02_Percorsi/10h/Scuola_10h/`, ricavato dal diff vero fra i due percorsi.
> Scritto il 26 agosto 2026. **Costruito il 27 agosto 2026**: il percorso sta in `02_Percorsi/10h/Segreteria_10h/`, l'elenco puntuale delle modifiche è nel suo `CAMBIAMENTI.md`.
> Standard: `00_Standard/MODUS_OPERANDI.md`.

---

## PARTE 0 · Il metodo, misurato sul 10h che c'è già

Ho confrontato riga per riga i deck di `Scuola_10h` con quelli della Primaria da cui derivano. Il risultato è netto e vale la pena scriverlo, perché smentisce l'idea di partenza:

| Deck | Slide nel 20h | Slide nel 10h |
|---|---|---|
| Incontro 1 | 31 | **31** |
| Incontro 2 | 43 | **43** |
| Incontro 3 | 43 | **43** |
| Incontro 4 | 44 | **44** |
| Incontro 5 | 41 | **35** |
| Incontro 10 | 36 | **36** |
| Pratica Canva | 13 | **13** |
| Pratica NotebookLM | 10 | **10** |
| Pratica Laboratorio | 16 | **16** |
| Pratica 1 | 21 (Claude) | 24 (Gemini, deck nuovo) |

**Il 10h non taglia le slide. Taglia il tempo.** Su otto deck su dieci la differenza è di sole due cose: nove righe di CSS per il riquadro `.flag`, e un `div` inserito nelle slide di dibattito in eccesso, che dice *"Se avanza tempo. Altrimenti resta uno spunto: ci ragionate voi."* Nemmeno la numerazione cambia: l'Incontro 4 continua a dire `32 / 43`.

Le uniche due eccezioni sono esattamente quelle che dici tu:

1. **L'Incontro 5**, che perde il Progetto e passa da 41 a 35 slide.
2. **La lezione 6**, che è un deck nuovo perché cambia lo strumento.

Tutto il resto, comprese le pratiche 07, 08 e 09, si porta avanti con un trova e sostituisci sul nome del percorso e qualche riga sui tempi.

---

## PARTE 1 · Dove la Segreteria non è come la Scuola

C'è un punto in cui il metodo della Scuola non basta, e va deciso prima di aprire i file.

Ho sommato le durate dichiarate nelle scalette del blocco pratico della Segreteria:

| Lezione | Durata dichiarata | Slide |
|---|---|---|
| 06 · Claude | **3h20** (la scaletta stessa la chiama "1,5 moduli") | 21 |
| 07 · Dati e ricerca | **2h55** | 27 |
| 08 · NotebookLM | 2h | 11 |
| 09 · Laboratorio | 2h | 16 |
| **Totale** | **10h15** | |

Il blocco pratico del 20h vale 8 ore. **Il materiale che c'è ne vale 10 e un quarto.** Nella Scuola questo problema non c'era: le pratiche erano già a misura, 13, 10 e 16 slide.

Conseguenza sul conto vero della compressione:

| Blocco | 20h | 10h | Taglio |
|---|---|---|---|
| Comune, 6 moduli | 12h | 6h | 50%, e si fa col flag |
| Pratico, 4 moduli | 10h15 di materiale reale | 4h | **61%** |

Il comune si comprime col metodo della Scuola, senza pensarci. **Il blocco pratico va ridisegnato nei tempi, non solo marcato.** La buona notizia è che il passaggio a Gemini lavora nella stessa direzione: fa cadere da solo circa 40 minuti della lezione 06, come si vede nella Parte 3.

---

## PARTE 2 · Il dizionario Claude e Gemini

| Nel 20h con Claude | Nel 10h con Gemini | Tenuta |
|---|---|---|
| **Progetto** (contenitore con memoria) | **Gem**: istruzioni che restano, più fino a 10 file di conoscenza, caricati o presi da Drive | Piena, è lo stesso oggetto |
| **Preferenze personali** | **Istruzioni personalizzate**, più le **Info salvate** | Piena |
| **Skill richiamata con "/"** | Non esiste. Ogni skill diventa **una Gem dedicata** | Parziale, e va detto in aula |
| **Ricerca approfondita** | **Deep Research** | Piena, anche sul piano gratuito con 5 ricerche al mese |
| **Fogli dentro Claude** | Si carica .xlsx o .csv in chat, oppure si converte in Google Sheets e si lavora con **Chiedi a Gemini** dentro il foglio | Piena, e in una scuola su Google è meglio di prima |
| **Claude in Excel** (citato come "esiste, si installa") | **Gemini in Google Sheets**, che non si installa | Migliora, cade la nota sull'add-in |
| **Live Artifact** (il cruscotto delle scadenze) | **Canvas**, e dove c'è **Sheets canvas** il cruscotto vive dentro il foglio | Piena sulla carta, da verificare sulla licenza |
| **Automazioni** | **Scheduled actions** | Da verificare sulla licenza |
| **NotebookLM** | NotebookLM | Identico, è già Google |

Due cose che il passaggio a Gemini regala, e che con questo pubblico contano:

- **Nessun account nuovo.** Si entra da `gemini.google.com` con l'account della scuola. Per un ufficio che vive dentro Drive e Gmail toglie l'obiezione numero uno.
- **Il foglio non esce da Google.** Il registro si converte in Google Sheets e resta nel Drive dell'istituto.

E i due punti dove Gemini non fa la stessa cosa hanno già un piano B che non fa saltare la lezione: le **automazioni** si lanciano a mano se la licenza non c'è, e il **cruscotto** si scrive su Canvas, che funziona ovunque, con Sheets canvas come riga in fondo.

---

## PARTE 3 · Modulo per modulo, cosa si fa davvero

### Moduli 1, 2, 3, 4 e 10 · si aggiunge il flag, non si toglie niente

Nessuna slide eliminata, nessuna rinumerazione. Si copia il blocco CSS `.flag` dalla Scuola e si inseriscono i riquadri. Ho verificato per contenuto, non per numero, e la Segreteria coincide quasi ovunque con la Scuola:

| Modulo | Slide totali | Flag su | Restano attive |
|---|---|---|---|
| 1 | 31 | **S27** (come cambierà il vostro ruolo), **S29** (cosa nessuna macchina potrà mai fare) | S4 (apertura) e S26 (il vostro ufficio) |
| 2 | 43 | **S9**, **S21**, **S26** (le tre "provate voi"), **S35** (lo studente e il chatbot) | la domanda sul contesto e la pratica finale |
| 3 | 32 | **S24** e **S25** (il terzo e il quarto caso di "Lo useresti?") | **S15 resta attivo**: è l'unico dibattito del modulo. E restano i primi due casi, la circolare pubblica e l'elenco degli alunni, che sono i due che insegnano la regola |
| 4 | 44 | **S32** e **S33** (Pratica 1) | Pratica 2, che è quella da cui portano a casa qualcosa |
| 10 | 36 | **S31** e **S32** | **S33**, la domanda che chiude il cerchio con l'Incontro 1 |

Nota sul modulo 3: la Segreteria ha già 32 slide contro le 43 della Primaria, quindi è già stato tagliato una volta. Per questo qui il flag va sui casi pratici e non sul dibattito, al contrario della Scuola.

Nel modulo 10 cambiano anche due caselle della scheda dei quattro strumenti: *Claude* diventa *Gemini*, *Claude in Excel* diventa *Gemini nei fogli*. Il caso Anthropic della slide sull'informazione **resta**: è un caso di diritto d'autore con fonte, non pubblicità a un concorrente.

### Modulo 5 · la sola vera amputazione

Si ripete esattamente quello che è stato fatto nella Scuola, dove l'Incontro 5 è passato da 41 a 35 slide:

- Cadono le **sette slide del Progetto** (da S15 a S21: la parte 2, il contesto sempre uguale, dentro il Progetto, il tutorial, il prompt di inizio, la prima chat, il Progetto compilato) e vengono sostituite da **tre slide** che raccontano lo stesso concetto come **contesto permanente**.
- Cade **S29** (*"Il Progetto si rifà ogni volta, il file una volta sola"*), che senza il Progetto non ha più senso.
- La pratica passa **da due tempi a uno**: si scrive il file, e basta. La Gem si costruisce nel modulo 6.
- **IPU resta intera.** Il file di contesto permanente resta ed è il centro del modulo.

In più, una cosa che nella Scuola non c'era e qui va sistemata: le slide **S32 e S33** offrono ancora *"quattro versioni, per ordine di grado"*, primaria, medie, superiori e ATA. In un percorso per la segreteria ne serve **una sola**. Le due slide diventano una. È un residuo dell'adattamento dalla Primaria, ma **si corregge solo qui, nel 10h. Il 20h resta com'è.**

Conto finale: **41 slide diventano 33.**

### Modulo 6 · il deck nuovo, il 60% del lavoro

Oggi sono 21 slide e 3h20 di materiale su Claude Cowork. Non si converte: si sostituisce, sul modello del deck Gemini della Scuola, che sta in 24 slide e 60 minuti.

| Slide di oggi | Cosa ne facciamo |
|---|---|
| 1-4 (copertina, dove siamo, il salto) | Restano, cambia il nome dello strumento |
| **5-11** (un generalista, le tre versioni, Chat contro Cowork, com'è fatta dentro, le quattro funzioni) | Si sostituiscono con l'anatomia di Gemini: cos'è, si entra con l'account che avete, e le quattro cose che contano, cioè chat, file, Canvas, Gem. Modello: slide 5, 6 e 9 di `Scuola_10h/06_Pratica_Gemini`. **Cade tutta la distinzione Chat, Cowork e Code**, che è di Claude e basta: sono 8 minuti che se ne vanno da soli |
| **nuova, dopo la 6** | La regola sui dati ripresa dal modulo 3, prima di caricare qualsiasi cosa. Qui pesa più che altrove: in segreteria i dati personali sono il mestiere. Modello: slide 7 della Scuola |
| 12-14 (si parte, prompt del progetto, comunicazione dall'archivio) | **Restano identici.** Cambia una parola: si aprono le Istruzioni della Gem invece della prima chat del Progetto |
| 15 (preferenze personali) | Resta, si incolla nelle Istruzioni personalizzate |
| **16-17** (installa il Prompt Optimizer, il testo della skill) | Diventano **la Gem scrittore di prompt**: tre passi, testo da incollare, cinque minuti. Il testo esiste già in `Asset_Gem_Scrittore_di_Prompt.md`, va ritarato sul lessico della segreteria |
| 18 (skill utili per voi) | Diventa **Gem utili per voi**. Le quattro restano: tono istituzionale, da normativa ad avviso, controllo prima di inviare, risposta allo sportello |
| **19** (prompt per creare una skill) | **Cade.** Gemini non ha un creatore di abilità, e sono altri 15 minuti che se ne vanno |
| **20** (automazione, le novità del mondo scuola) | **Cade.** In un'ora non ci sta, ed è la funzione che dipende dalla licenza |
| **21** (il cruscotto delle scadenze) | **Cade**, per lo stesso motivo. Resta materiale buono per il 20h |

Asset collegati, conversione pulita:

- `Progetto_Demo_Mail/` diventa **`Gem_Demo_Mail/`**: `ISTRUZIONI_PROGETTO.md` si incolla nelle Istruzioni della Gem, e i cinque file (archivio famiglie, colleghi, enti, modulistica, scadenzario) diventano i file di conoscenza. **Sono sei su un tetto di dieci: ci stanno interi.**
- `Asset_Skill_Prompt_Optimizer.md` diventa `Asset_Gem_Scrittore_di_Prompt.md`, versione segreteria.
- La cartella si chiama `06_Pratica_Gemini`.

Il solo passaggio a Gemini toglie **circa 40 minuti** (le tre versioni, il secondo movimento delle skill, il creatore di abilità). Il resto della compressione lo fa la struttura della Scuola: guida breve, e la maggior parte del tempo sulle mani.

### Modulo 7 · Dati e ricerca, il modulo da ridisegnare

È il deck più lungo del progetto, 27 slide e 2h55, e va portato a 60 minuti. **Il deck resta intero, 27 slide.** Anche qui vale il metodo della Scuola: non si taglia, si marca.

Il cuore non si tocca: le slide 9-18, l'anatomia dei due prompt lunghi, sono metodo puro (ruolo, vincoli di vigenza, gerarchia delle fonti, regole anti-allucinazione) e funzionano identiche su Deep Research.

Il colpo di regia della lezione, cioè *"la ricerca si lancia all'inizio e gira mentre si lavora sui fogli"*, in un'ora funziona anche meglio: si lancia al minuto dieci e si riapre al minuto quaranta.

Cosa si fa:

- **Flag sul secondo prompt**, quello del fornitore: le quattro slide del blocco (S15 il gancio, S16, S17, S18 l'anatomia) prendono il riquadro "Se avanza tempo". Restano nel deck, quindi chi vuole se le legge, ma in un'ora si porta a casa il prompt A per intero. Lo scheletro è lo stesso e la slide 15 lo dice già: chi ha capito il primo sa leggere il secondo da solo.
- La slide **21** (*"come si lavora, dentro Claude senza installare niente"*) si riscrive per Gemini, e la riga sull'add-in di Excel **cade**.
- Le slide 23, 24, 25, i tre movimenti sui fogli, **non si toccano**: sono la parte che stupisce e quella che useranno davvero.
- Il secondo hands-on (blocco 8, la ricerca loro) diventa **compito a casa con il prompt consegnato**, che è già la riserva prevista dalla scaletta del 20h.

Risultato: **27 slide restano 27**, quattro col flag, e i tempi si riscrivono su 60 minuti.

Da rifare prima dell'aula: la prova dei numeri del `Registro_richieste_sportello.xlsx` su Gemini, perché il `README_FORMATORE.md` promette al formatore risultati precisi (62 richieste, 916 minuti, gennaio a 46).

### Modulo 8 · NotebookLM, si porta avanti così com'è

**Zero occorrenze di Claude nel deck e nella scaletta.** Come nella Scuola, cambia solo il footer del percorso e il tempo della pratica, che da un'ora scende a 35 minuti. In un percorso Gemini questa lezione smette di essere l'ospite di un altro mondo.

### Modulo 9 · Laboratorio

Il flusso a quattro passi regge identico. Nella Scuola questo deck è passato al 10h **senza perdere una slide**, riducendo solo il laboratorio da 85 a 35 minuti. Qui uguale:

| Slide | Intervento |
|---|---|
| 3 | *Claude, quello che scrive* diventa *la vostra Gem*. Il Progetto Mail diventa Gem Mail |
| 7 | I due riquadri *CLAUDE* diventano *GEMINI* |
| 9, 12 | I prompt **non cambiano**, cambia dove si incollano |
| 10, 11 | Invariati |
| 13 | Il laboratorio da 85 minuti scende a 35 |

---

## PARTE 4 · Le tre decisioni, prese

Decise da Luca il 27 agosto 2026.

1. **Le Skill diventano Gem.** Il messaggio in aula cambia da *"un attrezzo che richiami ovunque"* a *"quattro assistenti, uno per lavoro, e sapete sempre da chi andare"*. Per un ufficio funziona meglio, e fa cadere due slide.
2. **Il modulo 7 non si taglia.** Resta a 27 slide. Il secondo prompt, quello del fornitore, prende il flag "Se avanza tempo". Il metodo della Scuola vale anche qui: non si toglie, si marca.
3. **Le quattro versioni per ordine di grado** diventano una sola, quella della segreteria, **solo nel 10h**. Il 20h non si tocca.

---

## PARTE 5 · Da verificare prima dell'aula

- [ ] Gemini attivo sull'account Workspace dell'istituto, e le **Gem** disponibili
- [ ] **Deep Research**: sul piano gratuito sono 5 ricerche al mese, quindi una a testa in aula basta, ma va saputo prima
- [ ] **Scheduled actions** attive oppure no: decide se la slide 20 del modulo 6 si fa dal vivo o si racconta
- [ ] **Sheets canvas** presente oppure no: decide la riga in fondo alla slide 21
- [ ] **Caricamento di file** consentito dall'amministratore di dominio: senza quello cadono la Gem con i materiali e tutto il modulo 7
- [ ] Piano B trasversale: se l'account della scuola è chiuso si lavora con l'account personale su `gemini.google.com`. Cambia l'accesso, non la lezione
- [ ] Riprovare su Gemini i numeri del registro delle richieste

---

## PARTE 6 · Ordine di lavoro

| Passo | Cosa | Peso |
|---|---|---|
| 1 | **Modulo 6**, deck nuovo su Gemini e conversione degli asset | 45% |
| 2 | **Modulo 7**, ridisegno dei tempi e le tre slide del prompt B | 20% |
| 3 | **Modulo 5**, l'amputazione del Progetto, copiata dalla Scuola | 15% |
| 4 | **Moduli 1, 2, 3, 4, 10**, CSS del flag più 10 riquadri, e le due caselle del modulo 10 | 10% |
| 5 | **Moduli 8 e 9**, footer e tempi | 5% |
| 6 | `CAMBIAMENTI.md` del percorso e consegna in PDF e zip | 5% |

Cartella di destinazione: `02_Percorsi/10h/Segreteria_10h/`, con lo schema `01_Modulo_1` fino a `10_Modulo_10` più `_Consegna/`. Come in `Scuola_10h`, **niente scalette formatori**: nel 10h non ci sono.

Il programma ufficiale esiste già: `01_Progetto/Programmi/10h/PROGRAMMA_10h_Segreteria.html`. Va riletto a fine lavoro per verificare che i dieci moduli corrispondano ancora, visto che parla ancora di strumenti al plurale e non nomina Gemini.

---

## Fonti verificate su Gemini

- Gem, istruzioni e fino a 10 file di conoscenza anche da Drive: [Google Workspace](https://workspace.google.com/blog/product-announcements/new-gemini-gems-deeper-knowledge-and-business-context)
- Gem e Deep Research sui piani Workspace: [Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/03/gemini-gems-deep-research-available-for-more-google-workspace-customers.html)
- Istruzioni personalizzate valide su ogni chat: [Gemini Apps Help](https://support.google.com/gemini/answer/16598625)
- Scheduled actions e requisiti di piano: [Google](https://blog.google/products-and-platforms/products/gemini/scheduled-actions-gemini-app/)
- Deep Research, 5 ricerche al mese sul piano gratuito: [Gemini plans and usage limits](https://www.revolgy.com/insights/blog/gemini-plans-change-with-new-usage-limits-across-tiers)
- Caricamento e analisi di file .xlsx e .csv: [Gemini Apps Help](https://support.google.com/gemini/answer/14903178)
- Chiedi a Gemini dentro Google Sheets: [Google Docs Editors Help](https://support.google.com/docs/answer/14218565)
- Canvas, da un prompt a una mini-app: [Gemini Canvas](https://gemini.google/overview/canvas/)
- Sheets canvas, distribuzione agosto 2026: [Google Workspace blog](https://blog.google/products-and-platforms/products/workspace/sheets-canvas-for-google-sheets-spreadsheets/)
