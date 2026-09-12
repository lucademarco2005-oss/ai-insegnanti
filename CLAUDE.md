# Progetto: AI Insegnanti

Formazione docenti sull'IA (PNRR DM 219/2025). Lead: Luca De Marco.

## Organizzazione cartelle
- `00_Standard/` — modus operandi, **convenzioni di lavoro**, sistema slide, ricerca verificata
- `01_Progetto/` — contesto PM, struttura percorsi, scalette 6 incontri, piani di lavoro e `Programmi/` (i programmi ufficiali, divisi in `20h/` e `10h/`)
- `02_Percorsi/` — **il contenuto formativo, diviso per durata.** `20h/` contiene `Primaria/`, `Infanzia/`, `Secondaria/`, `Segreteria_ATA/`; `10h/` contiene `Scuola_10h/`. Dentro ogni percorso lo stesso schema: `01_Incontro_1` … `05_Incontro_5` (comune), `06` … `09` (pratica, uno strumento per incontro), `10_Incontro_10`, `_Consegna/` (PDF e zip). Vedi `02_Percorsi/README.md`.
- `03_Team/` — formatori, CV standard, brief software di coordinamento, `Modulistica_Compensi/` (ricevuta con ritenuta d'acconto per i collaboratori). **Solo in locale da Luca: escluso dalla repo condivisa perché contiene dati personali dei collaboratori.**
- `04_Tecnico/` — tooling e materiali grezzi: `slide_build/`, `Originali/`, tutorial
- `graphify-out/` — knowledge graph (resta alla radice, è lì che lo scrive lo skill). Non versionato: si rigenera con `/graphify`.

**La Primaria è il percorso di riferimento:** gli incontri comuni che stanno in `02_Percorsi/20h/Primaria/` sono la versione base, gli altri percorsi si costruiscono adattando quei file.

## Modus operandi — LEGGERE SEMPRE PRIMA DI LAVORARE
Due file, entrambi obbligatori prima di produrre qualsiasi cosa:

- **`00_Standard/MODUS_OPERANDI.md`**: lo standard su **come devono venire** scalette, script e slide. Va rispettato in ogni nuovo incontro, deck o testo.
- **`00_Standard/CONVENZIONI_LAVORO.md`**: **come si arriva** a produrli. Chi decide, cosa si tocca e cosa no, la sequenza reale dei 10 incontri, l'architettura del blocco pratico, e le trappole già calpestate (fra cui una fonte sbagliata in repo su cui non bisogna fidarsi). Se stai per modificare un deck o costruire un percorso, leggilo.

### Regole assolute (non si violano mai)
1. **Mai il trattino lungo "—" (em-dash).** Usa punto, virgola o due punti.
2. **Mai la freccia "→" come nota del relatore** sulle slide. Le note di regia stanno nella scaletta.
3. **Solo dati chiari** (niente coefficienti tipo `r=−0,75`), **sempre con fonte verificata**.
4. **Tono che invita, mai inquisitorio.**
5. **Una slide = un'idea.**

### Sintesi del metodo
- Si insegna il **metodo, non il tool**. I tool si insegnano negli 8h pratici, non nelle 12h comuni.
- Ogni concetto si apre con una **slide-gancio** (domanda introduttiva, sfondo viola). Tensione prima del dato.
- **Il colore è una funzione:** navy = statement chiave · chiaro = contenuto · viola = gancio · arancio = dibattito.
- Slide **colorate e moderne**, densità media (vero supporto per chi espone), numero su ogni slide.
- I deck sono **HTML autonomi** (`Incontro_N.html`, unità `cqh`, export PDF via stampa), non PowerPoint.

### Revisioni (efficienza)
Modifiche via `slide N: vecchio → nuovo`, raggruppate in un messaggio. Le regole generali date una volta entrano nel MODUS_OPERANDI e valgono per sempre.

## Lavoro condiviso (git)

Questa cartella è una repo git privata, condivisa fra Luca e il project manager. Si versiona la **sorgente**, non l'output: i deck sono gli `.html`, i PDF sono un export e si rigenerano. Cosa è escluso e perché sta in `.gitignore` e nella §7 di `CONVENZIONI_LAVORO.md`.

Se lavori con Claude Code non serve conoscere git: chiedi "scarica gli aggiornamenti" prima di iniziare e "manda le modifiche" quando hai finito.

**Prima di iniziare a lavorare, sempre:** allineati con il remoto (`git pull`). Due persone che modificano lo stesso deck in parallelo sono l'unico modo realistico di farsi male qui.

**Quando hai finito un blocco di lavoro:** commit con un messaggio che dica *cosa* è cambiato a livello di contenuto, non di file. `"Incontro 2 Secondaria: riscritte slide 12-15 sul dibattito"`, non `"update html"`.

## Contesto
Vedi `00_Standard/CONVENZIONI_LAVORO.md` (come si lavora, da leggere per primo), `01_Progetto/CONTESTO_PM.md` (progetto), `00_Standard/RICERCA_CONTENUTI.md` (dati verificati + fonti), `01_Progetto/SCALETTE_6_INCONTRI.md` (panoramica 6 incontri), `01_Progetto/PIANO_SECONDARIA_SEGRETERIA.md` (metodo di adattamento e piano dei due percorsi mancanti), `02_Percorsi/20h/Primaria/01_Incontro_1/` (deck e scaletta di riferimento), `02_Percorsi/20h/Infanzia/_MODIFICHE_INFANZIA.md` (come si adatta un percorso, con transcript), `00_Standard/MODUS_OPERANDI.md` (standard completo).
