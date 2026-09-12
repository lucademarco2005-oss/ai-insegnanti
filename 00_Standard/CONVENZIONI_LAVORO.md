# CONVENZIONI DI LAVORO

> Come si lavora su questo progetto, in concreto.
> `MODUS_OPERANDI.md` dice **come devono venire** scalette, slide e testi. Questo file dice **come si arriva** a produrli: chi decide, cosa si tocca e cosa no, quali trappole sono già state calpestate.
> Nato per non perdere, passando la cartella ad altre persone, le regole che erano rimaste nella testa di chi ha lavorato finora.
> Ultimo aggiornamento: 12 settembre 2026.

---

## 0. Chi decide

**Luca De Marco decide nel merito didattico.** L'azienda partner dà cornice contrattuale e linee guida; le scelte su contenuto, struttura e slide sono di Luca. Chiunque lavori qui, persona o AI, **propone**: non chiude una decisione di contenuto da solo.

Sul resto (riordino file, refuso, build, rigenerazione di un export) si agisce e si riferisce.

---

## 1. Le tre regole di velocità

Date da Luca il 24 e 25 agosto 2026. Servono ad andare veloce senza che lui perda il controllo.

**1. Applica e passa avanti nello stesso messaggio.** Decisi i cambiamenti di una lezione, li applichi ai file **e nello stesso messaggio presenti già l'analisi della lezione successiva**. Non si aspetta il turno dopo per discutere il pezzo dopo.

**2. Tocca solo quello che ti è stato detto.** Parole sue: *"modifica solo le slide che ti ho detto"*. Se lavorando trovi altre slide che diventano incoerenti, **le segnali in fondo al messaggio e non le tocchi**. Le sistema lui, quando vuole.

**3. Non chiedere, mostra.** Parole sue: *"non devi chiedermi, devi solo mostrarmi bene il risultato finale come lo vuoi impostare"*. Invece di una domanda con opzioni, scrivi il risultato per intero (testi delle slide, prompt verbatim, struttura) e lui corregge. Le domande vere si tengono per le decisioni che cambiano davvero il lavoro, e si raggruppano in un messaggio.

**Forma del messaggio:** due parti. (1) "Fatto": elenco secco di cosa hai applicato, con i testi finali dove servono. (2) La lezione successiva, già proposta per intero. In coda, se serve, una riga sulle incoerenze che non hai toccato.

---

## 2. Approvazione delle modifiche ai deck

**Una slide non si riscrive senza un ok sul contenuto.** Prima si propone il cambio (testo nuovo per intero), poi si edita l'HTML, poi si rigenera l'export.

Questo non contraddice la regola 1: l'ok e la produzione non sono due giri separati, sono lo stesso messaggio. Quello che non si fa è editare venti slide e mostrarle a cose fatte.

Vale in modo stretto sul percorso **Infanzia**, dove Luca ha già fatto una sua revisione su carta e la call con Giorgia: prima di toccare quei deck si rilegge `02_Percorsi/20h/Infanzia/_MODIFICHE_INFANZIA.md`, che contiene il transcript integrale della call del 29 giugno più le modifiche estratte per lezione.

**Formato delle revisioni:** `slide N: "vecchio" -> "nuovo"`, citando le parole esatte, tutto raggruppato in un messaggio. I colori si indicano solo per nome: stanno in un unico `:root`.

---

## 3. La Primaria è il riferimento

Gli incontri comuni in `02_Percorsi/20h/Primaria/` sono la **versione base**. Ogni altro percorso (Infanzia, Secondaria, Segreteria_ATA, e i due 10h) si costruisce **adattando quei file**, non ripartendo da zero.

Quando una regola generale cambia, si cambia prima la Primaria, poi si propaga.

Metodo di adattamento documentato: `01_Progetto/PIANO_SECONDARIA_SEGRETERIA.md`. Esempio concreto di adattamento con transcript: `02_Percorsi/20h/Infanzia/_MODIFICHE_INFANZIA.md`.

---

## 4. Sequenza reale dei 10 incontri

**Incontri 1-5 comuni, poi i 4 incontri pratici, poi l'Incontro 6** (futuro e chiusura).

> ⚠ **Attenzione, c'è una fonte sbagliata in repo.** `01_Progetto/PERCORSI_STRUTTURA.md` (intorno a riga 15) descrive una sequenza vecchia e superata ("I1-I4, poi i 4 pratici, poi I5, I6"), e una nota interna in `Incontro_5/INCONTRO_5_SCALETTA.md` la conferma. **È un retaggio: non fidarti di quei due punti.** Luca ha chiarito che l'Incontro 5 viene **prima** dei pratici.

Conseguenza pratica: quando i docenti arrivano ai 4 incontri pratici hanno **già** il concetto di Progetto, il loro file di contesto permanente ("ragiona come me") e l'IPU, tutti introdotti nell'Incontro 5. Le lezioni pratiche **non li reintroducono**: ci costruiscono sopra.

---

## 5. Architettura del blocco pratico

4 incontri pratici per ciascuno dei 4 percorsi 20h = 16 slot. Non si scrivono 16 scalette: si costruisce **per strumento, con riuso pragmatico** (le parti simili restano simili, si diverge solo dove serve). Sette sorgenti:

| # | Sorgente | Percorsi |
|---|---|---|
| 1 | Claude pratico | tutti e 4 |
| 2 | Canva | Primaria, Infanzia, Secondaria |
| 3 | NotebookLM | Primaria, Secondaria, ATA |
| 4 | Claude in Excel | solo ATA |
| 5 | ElevenLabs + Suno | solo Infanzia |
| 6 | Granola + Canva | solo ATA (è anche il suo laboratorio finale) |
| 7 | Laboratorio finale | Primaria, Infanzia, Secondaria |

Mappa slot per percorso: **Primaria** [1,2,3,7] · **Infanzia** [1,2,5,7] · **Secondaria** [1,3,2,7] · **ATA** [1,4,3,6].

Cartelle: `06_Pratica_Claude/`, `07_Pratica_Canva/`, `08_Pratica_NotebookLM/`, `09_Pratica_Laboratorio/`. Gli asset condivisi (progetto demo, `Asset_Skill_Prompt_Optimizer`, `SETUP_FORMATORE`) stanno in `06_Pratica_Claude/` perché è lì che vengono introdotti.

Ogni lezione pratica ha una **guida formatori** (`*_scaletta_formatori.html`): una scaletta di step da seguire, cosa mostrare a schermo click per click, fedele ai transcript di Luca. Niente riquadro blu introduttivo.

---

## 6. Trappole già calpestate

**Copiando un deck, copia anche `assets/`.** I deck referenziano le immagini con percorso relativo, per esempio `<img class="bigimg" src="assets/learn-your-way.png">` nella slide 28 dell'Incontro 1. Se copi solo gli `.html` la slide esce con l'immagine rotta. Oggi l'unica immagine del progetto è `01_Incontro_1/assets/learn-your-way.png`, replicata in tutti i percorsi.

Controllo da fare **prima** di dire che un percorso è pronto:

```bash
for f in */*.html; do
  grep -o 'src="[^"h][^"]*"' "$f" | sed 's/src="//;s/"//' | while read r; do
    [ -f "$(dirname "$f")/$r" ] && echo "OK    $f -> $r" || echo "MANCA $f -> $r"
  done
done
```

**I prompt di esempio vanno verbatim, non riassunti.** La slide 17 del deck Claude pratico riporta il testo vero e integrale del Prompt Optimizer. Riassumerlo è un errore già fatto e già corretto una volta.

**`_Consegna/` è una copia.** Contiene duplicati dei file di lavoro del percorso, assemblati per la consegna ai formatori. Non è una fonte: se una modifica va fatta, si fa nella cartella di lavoro e poi si riassembla. Per questo `_Consegna/` è escluso da git (vedi `.gitignore`) e va escluso anche dall'estrazione Graphify.

**Il render visivo lo verifica una persona.** Il controllo dei contenuti si può fare da testo, ma se lavori in un ambiente senza browser non puoi dire che un deck "è a posto" visivamente: lo apre Luca in Chrome. La slide più densa va segnalata per la verifica.

---

## 7. Cosa non sta in questa repo

- **`03_Team/`**: CV, attestati e modulistica compensi dei collaboratori. Sono dati personali di terzi, restano in locale.
- **`_Consegna/` e gli `.zip`**: pacchetti di consegna, si riassemblano.
- **I PDF dei deck**: export, si rigenerano da HTML con Cmd+P (Orizzontale, Margini Nessuno, Grafica di sfondo ON). Restano in repo solo i PDF che sono **sorgente** e servono in aula: `Scrittore di prompt.pdf` e il paper Mancini per NotebookLM.
- **`graphify-out/`**: knowledge graph, si rigenera con `/graphify`.
- **`node_modules/`**: dipendenze del tooling slide.
