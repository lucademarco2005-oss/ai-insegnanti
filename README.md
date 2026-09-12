# AI Insegnanti

Formazione docenti sull'Intelligenza Artificiale, bando **PNRR DM 219/2025**.
Lead e decisore didattico: **Luca De Marco**.

Questa repo contiene il **contenuto formativo** del progetto: scalette, deck, materiali d'aula, standard di produzione. È privata.

---

## Se è la prima volta che apri questa cartella

**1. Clona la repo e apri la cartella con Claude Code.**

```bash
git clone <url-della-repo> "AI Insegnanti"
```

**2. Non serve leggere tutto.** Claude Code carica da solo `CLAUDE.md` alla radice, che contiene le regole del progetto e i puntatori a tutto il resto. Se vuoi capire come si lavora qui prima di toccare qualcosa, i due file da leggere sono:

| File | Cosa ti dice |
|---|---|
| `00_Standard/MODUS_OPERANDI.md` | Come devono **venire** scalette, slide e testi. Regole assolute, sistema slide, palette, fonti verificate. |
| `00_Standard/CONVENZIONI_LAVORO.md` | Come si **lavora**. Chi decide, cosa si tocca e cosa no, la sequenza reale degli incontri, le trappole già calpestate. |

**3. Il contesto del progetto** (numeri, istituti, team, timeline) sta in `01_Progetto/CONTESTO_PM.md`.

---

## Il giro di lavoro quotidiano

Con Claude Code non serve conoscere git. Basta questo:

| Quando | Cosa dire a Claude |
|---|---|
| Prima di iniziare | "scarica gli aggiornamenti" |
| Finito un blocco di lavoro | "manda le modifiche" |

Se preferisci i comandi:

```bash
git pull        # prima di iniziare, sempre
git add -A && git commit -m "descrizione del cambio" && git push
```

**Allineati sempre prima di iniziare.** Due persone che modificano lo stesso deck in parallelo è l'unico modo realistico di farsi male su questa repo.

**Messaggi di commit sul contenuto, non sui file.** `"Incontro 2 Secondaria: riscritte slide 12-15 sul dibattito"`, non `"update html"`. Così lo storico si legge come un diario del progetto.

---

## Com'è organizzata

| Cartella | Contenuto |
|---|---|
| `00_Standard/` | Gli standard: modus operandi, convenzioni di lavoro, sistema slide, ricerca con fonti verificate. |
| `01_Progetto/` | Contesto del progetto, struttura dei percorsi, scalette dei 6 incontri comuni, piani di lavoro, programmi ufficiali. |
| `02_Percorsi/` | **Il contenuto formativo.** Diviso per durata (`20h/`, `10h/`) e poi per percorso. |
| `04_Tecnico/` | Tooling di build delle slide, materiali grezzi originali, tutorial. |

Dentro ogni percorso lo stesso schema: `01_Incontro_1` fino a `05_Incontro_5` (i comuni), da `06` a `09` (il blocco pratico, uno strumento per incontro), `10_Incontro_10`.

**La Primaria è il percorso di riferimento.** Gli incontri comuni in `02_Percorsi/20h/Primaria/` sono la versione base: gli altri percorsi si costruiscono adattando quei file, non ripartendo da zero.

---

## Due cose da sapere subito

**I deck sono HTML, non PowerPoint.** Ogni incontro è un `Incontro_N.html` autonomo che si apre in Chrome. Il PDF è un **export**, non la sorgente: si rigenera con Cmd+P (Orizzontale, Margini Nessuno, Grafica di sfondo ON). Per questo i PDF non sono in repo. Se modifichi un deck, modifichi l'HTML.

**Le decisioni di contenuto sono di Luca.** Si propone il cambio, si attende l'ok, poi si edita. Il dettaglio di come farlo senza rallentare sta nella §1 e §2 di `CONVENZIONI_LAVORO.md`.

---

## Cosa non troverai qui

Escluso volutamente, vedi `.gitignore`:

- `03_Team/`: CV, attestati e compensi dei collaboratori. Dati personali, restano in locale da Luca.
- `_Consegna/` e gli `.zip`: pacchetti di consegna ai formatori. Sono copie dei file di lavoro, si riassemblano.
- I PDF dei deck: export rigenerabili. Restano solo i pochi PDF che sono sorgente e servono in aula.
- `graphify-out/` e `node_modules/`: si rigenerano.
