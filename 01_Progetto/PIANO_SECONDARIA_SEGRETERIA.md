# Piano di lavoro · Percorsi Secondaria e Segreteria (ATA)

> Ricostruzione del metodo usato per Primaria e Infanzia, e sua applicazione ai due percorsi che restano.
> Scritto il 22 agosto 2026. Nessuna scaletta e nessuna slide si tocca prima dell'ok di Luca.

---

## PARTE 1 · Come abbiamo lavorato finora (metodo ricostruito)

Il percorso **Primaria** è la sorgente. È stato costruito da zero, lezione per lezione, e da lì è nato l'**Infanzia** per adattamento. Questi sono gli step reali, nell'ordine in cui sono avvenuti.

### Step 0 · La base (una volta sola, già fatta)
Il blocco comune (6 incontri, 12h) e le 4 lezioni pratiche della Primaria sono lo scheletro di tutto. Ogni percorso nuovo non riparte da zero: riparte da questi file.

### Step 1 · Raccogliere il contesto reale dell'ordine di scuola
Prima di scrivere una riga si capisce **cosa fa davvero quella gente tutti i giorni**.
Per l'Infanzia è stata una call registrata con Giorgia Vassanelli (29 giugno, link Fathom nel log) più il contesto raccolto da Luca per fascia d'età: 3 anni (pittorico, manipolativo, racconti), mezzani (arte, elaborati 3D, LIM, Innovamat), 5 anni (scientifico, materiali naturali, classificazione).
Regola emersa dal transcript, parole di Luca: *"le prime lezioni falle parlare molto per capire la loro quotidianità, segnati i loro ganci e fai gli esempi sulle cose che ti dicono"*.
Senza questo step gli esempi suonano falsi e la platea non si sente coinvolta.

### Step 2 · Decidere il reframe del percorso
Una frase che decide il taglio di tutto il resto.
Infanzia: *non è una competenza da usare con i bambini, è una competenza vostra, professionale*. Da lì discende che i fenomeni scomodi (chatbot confidenti, deepfake) si raccontano a scopo informativo e non come "cosa che riguarda i vostri bambini".

### Step 3 · Passata slide per slide sul materiale esistente
Con il referente davanti, si scorrono tutte le lezioni e si marca ogni slide come: **invariata**, **cambia l'esempio**, **cambia l'esercizio**, **cambia il frame**, **da aggiungere**.
Output: un file `_MODIFICHE_<PERCORSO>.md` con due parti, l'estrazione per lezione con i numeri di slide citati (2.16, 4.13, 6.13, 6.20, 10.6, 10.14) e il transcript integrale sotto.
Vantaggio: quando si edita si sa esattamente cosa toccare e perché, e si può rileggere la fonte.

### Step 4 · Scegliere un filo conduttore unico per le 4 pratiche
Primaria: `Progetto_Demo_Geografia` (classe quarta, orientamento e carte).
Infanzia: **tema Autunno**, scelto perché funziona su 3 anni, mezzani e 5 anni, e riusato in tutte e quattro le lezioni pratiche (Claude progetta l'attività, ElevenLabs le dà voce, Canva fa il gioco, il Laboratorio monta la lezione completa).
Il filo unico è quello che fa sembrare le 4 lezioni un percorso e non 4 corsi staccati.

### Step 5 · Adattare una lezione alla volta, in quest'ordine
1. **Scaletta `.md`** (regia completa: blocchi, minuti, esempi, prompt verbatim, gap operativi marcati con ⚠).
2. **Ok di Luca sulla scaletta.** Qui si discute, non dopo.
3. **Deck HTML** (`Pratica_<Percorso>_N_<Tool>.html`), stesso sistema slide, footer e copertina del percorso.
4. **Scaletta formatori HTML**, il runbook click per click di cosa mostrare a schermo.
5. **PDF** di deck e runbook.
6. **Asset** collegati (cartella Progetto demo, file di esempio, fonti).

Cosa cambia realmente nel passaggio Primaria verso Infanzia, misurato sul diff della lezione Claude: la struttura, i blocchi e i minuti restano identici. Cambiano il vocabolario (classe diventa sezione, verifica diventa attività o scheda), gli esempi, il Progetto demo, la frase chiave in testa. È un lavoro di sostituzione chirurgica, non di riscrittura.

### Step 6 · Pacchetto di consegna
Cartella per lezione (`1_Claude`, `2_...`), solo PDF più i materiali, più lo zip. È una copia dei file di lavoro, va esclusa dall'estrazione Graphify.

### Regole trasversali sempre valide
- Nessuna modifica alle slide senza ok di Luca, slide per slide.
- `00_Standard/MODUS_OPERANDI.md` vale su tutto: mai em-dash, mai frecce come note del relatore, una slide una idea, il colore è una funzione, tono che invita.
- Le lezioni pratiche presuppongono i 5 incontri comuni già fatti: Progetto, file di contesto permanente e IPU sono già noti, non si reintroducono.

---

## PARTE 2 · Cosa serve per Secondaria e Segreteria

### Le sorgenti e il riuso

| Lezione pratica | Secondaria | Segreteria (ATA) |
|---|---|---|
| 1 | Claude · base Primaria, adattamento esempi | Claude · base Primaria, ripensata per l'ufficio |
| 2 | NotebookLM · base Primaria, adattamento esempi | Claude in Excel · **sorgente nuova, da zero** |
| 3 | Canva · base Primaria, adattamento esempi | NotebookLM · base Primaria, esempi tutti nuovi |
| 4 | Laboratorio · base Primaria, taglio da decidere | Granola più Canva · **sorgente nuova, da zero** |

Traduzione in carico di lavoro: la **Secondaria è un adattamento** (quattro lezioni su quattro hanno una base solida, come è stato per l'Infanzia). La **Segreteria è mezzo percorso nuovo**: due sorgenti non esistono e le due che esistono vanno ripensate più a fondo, perché il pubblico non insegna. Niente classe, niente lezione, niente studenti.

### Il blocco comune (12h)
Per la **Secondaria** i 6 incontri comuni sono già tarati bene: sono nati con esempi da scuola secondaria (studenti, plagio, chatbot, valutazione). Previsione: ritocchi minimi.
Per la **Segreteria** invece il comune richiede più lavoro dei percorsi docenti. Vanno rifatti tutti gli esercizi che presuppongono una classe: "un compito che dai spesso", "progetta una lezione sull'IA per i tuoi studenti", il caso "Lo useresti?" su output didattici. Diventano circolare, verbale, risposta a una famiglia, documento di protocollo. In più serve un blocco privacy molto più duro degli altri percorsi: in segreteria si maneggiano dati di minori, certificazioni, protocolli.

---

## PARTE 3 · Definizione proposta

> Proposta di partenza, da validare e correggere. I punti marcati **[decisione]** sono di Luca.

### SECONDARIA

**Reframe proposto:** i vostri studenti l'IA la usano già, e la usano male. Voi non state imparando a usarla per voi, state imparando a stare un passo avanti e a insegnargliela.

**Filo conduttore proposto:** un'unica unità didattica portata avanti in tutte e quattro le lezioni, così come l'Autunno per l'Infanzia. **[decisione]** materia e classe della demo, per esempio Storia in una terza media oppure Letteratura al biennio.

- **L1 · Claude.** Base: il tour a stazioni della Primaria (Progetto, Impostazioni, Skill, Schedule, Live Artifact). Cambia il Progetto demo, che diventa il progetto della materia con banca esercizi, programmazione annuale e criteri di valutazione. Live Artifact: il pianificatore del programma per stare in pari, che alla secondaria è il caso d'uso più forte. Blocco nuovo rispetto alla Primaria, previsto dal programma ufficiale: domande socratiche e come guidare l'uso che ne fanno i ragazzi.
- **L2 · NotebookLM.** Base Primaria quasi invariata nella struttura. Differenza vera: qui gli studenti hanno l'età per usarlo, quindi non è solo teacher facing. Si aggiunge lo studio autonomo guidato e il podcast di ripasso costruito sui materiali del docente.
- **L3 · Canva.** Base Primaria, tre esempi dal vivo più il ponte con Claude che scrive i prompt. Cambiano gli esempi: infografica su un concetto complesso, modello per guidare ricerche e tesine.
- **L4 · Laboratorio.** **[decisione]** due tagli possibili: (a) come la Primaria, si costruisce un'unità didattica completa coi tre strumenti; (b) come il programma ufficiale annunciato, si imposta una ricerca guidata con verifica delle fonti e fact-checking. La (b) è più distintiva per la secondaria, la (a) riusa quasi tutto.

**[decisione] Secondaria unica oppure I e II grado separati.** È aperta da giugno in `PERCORSI_STRUTTURA.md`. Impatta tutto: se separate, gli strumenti del II grado (Wolfram, DeepL, ricerca accademica) diventano una quinta e sesta sorgente.

### SEGRETERIA (ATA)

**Reframe proposto:** non si tratta di scrivere più veloce. Si tratta di togliere dalla vostra giornata il lavoro che non richiede una testa umana, e di tenere per voi quello che invece la richiede, cioè il rapporto con le famiglie e la responsabilità sui dati.

**Filo conduttore proposto:** un unico caso di ufficio seguito per quattro lezioni, per esempio la gestione di una circolare dal protocollo alla pubblicazione, oppure il ciclo delle iscrizioni. **[decisione]** quale.

- **L1 · Claude.** Struttura del tour della Primaria, contenuti tutti nuovi. Progetto demo "Segreteria": modelli di circolari, format dei verbali, FAQ delle famiglie, scadenzario. Skill: il prompt optimizer resta, si aggiunge una skill sul tono istituzionale. Schedule: il promemoria delle scadenze ricorrenti. Live Artifact: un cruscotto delle scadenze.
- **L2 · Claude in Excel.** Sorgente nuova. **⚠ da verificare prima di prometterla**: disponibilità reale del componente aggiuntivo, piano necessario, se funziona su Excel dell'istituto. Piano B già pronto: si carica il file dentro Cowork e ci si lavora lì, stesso risultato didattico senza dipendere dall'add-in.
- **L3 · NotebookLM.** Struttura Primaria, esempi tutti nuovi: archivio circolari, ricerca semantica sui PDF, riassunto di una normativa lunga, ritrovare un documento in pochi secondi. **⚠ da verificare**: la resa sui PDF scansionati senza testo, che in segreteria sono la norma.
- **L4 · Granola più Canva.** Sorgente nuova, ed è anche il laboratorio finale del percorso. **⚠ da verificare**: Granola su Windows, resa in italiano, e soprattutto il consenso alla registrazione di collegi e riunioni. Se il nodo privacy non si scioglie, si sostituisce con una trascrizione fatta a valle su un file audio già autorizzato.

**Nodo trasversale del percorso ATA:** i dati. Va costruito un blocco "cosa non entra mai in un'IA" con esempi veri di segreteria, più duro di quello dei percorsi docenti.

---

## PARTE 4 · Cosa manca prima di poter partire

1. **Il contesto della segreteria.** È il vero blocco. Serve una call con almeno una persona che in segreteria ci lavora: giornata tipo, quali documenti produce, quali gestionali usa, cosa la fa impazzire. Senza, gli esempi saranno finti e la platea se ne accorge. Per la Secondaria il contesto è più accessibile, ma una call con un docente di riferimento serve comunque per i "ganci".
2. **Le decisioni marcate [decisione]** qui sopra.
3. **Le verifiche tecniche marcate ⚠** su Claude in Excel, Granola e NotebookLM sui PDF scansionati.
4. **Ordine di lavorazione.** In `PERCORSI_STRUTTURA.md` la priorità di erogazione dice Primaria, poi Segreteria, poi Infanzia, poi Secondaria. Da confermare o aggiornare.

## Sequenza operativa proposta, con i punti di controllo di Luca

1. Call di contesto sul percorso scelto. **Controllo:** Luca conferma i ganci raccolti.
2. Scrittura del file `_MODIFICHE_<PERCORSO>.md`, reframe e filo conduttore. **Controllo:** Luca approva reframe e filo.
3. Lezione pratica 1: scaletta `.md`. **Controllo:** Luca valida la scaletta.
4. Deck HTML più scaletta formatori. **Controllo:** Luca rivede a video, revisioni in formato `slide N: vecchio, nuovo`.
5. Si ripete dal punto 3 per le lezioni 2, 3, 4.
6. Adattamento del blocco comune per quel percorso.
7. Pacchetto di consegna.
