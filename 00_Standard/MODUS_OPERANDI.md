# MODUS OPERANDI — Corso AI Insegnanti
> Regole e principi operativi distillati dal lavoro su Incontro 1 (scaletta + script + deck HTML).
> **Questo file è lo standard.** Ogni nuovo incontro, scaletta, slide o testo deve rispettarlo. In caso di dubbio, qui.
> Ultimo aggiornamento: 4 giugno 2026.

---

## 0. REGOLE ASSOLUTE (non si violano mai)

1. **Mai il trattino lungo "—" (em-dash).** Usa punto, virgola o due punti. Vale per slide, scalette, testi, ovunque.
2. **Mai la freccia "→" come nota del relatore.** Le indicazioni di regia stanno nella scaletta, non sulla slide. (La "→" è ammessa solo dentro un contenuto tecnico, es. `input → output`.)
3. **Solo dati chiari.** Niente coefficienti o numeri illeggibili per un non addetto (es. `r=−0,75`). Se un dato non si capisce in 2 secondi, si riformula a parole o si cambia.
4. **Ogni dato ha la fonte.** Sempre citata, piccola, in fondo alla slide. Solo fonti verificate (vedi §6).
5. **Tono mai inquisitorio.** Inviti, non imposizioni. "Più ci mettete del vostro, più portate a casa", non "dovete impegnarvi".
6. **Una slide = un'idea.** Se servono due concetti, due slide.

---

## 1. FILOSOFIA DEL CORSO

- **Insegniamo il metodo, non il tool.** I tool cambiano ogni 6 mesi; il metodo resta. La frase-chiave del corso: *"La differenza non è lo strumento. È il metodo."*
- **L'IA è un superpotere, non una scorciatoia.** Frame centrale, ripetuto: uso attivo (potenzia) vs uso passivo (atrofizza).
- **Gli insegnanti sono il pubblico, ma anche il messaggio.** Quello che imparano a fare con l'IA è quello che dovranno trasmettere agli studenti.
- **Interattivo e pratico, mai frontale.** Si impara facendo, provando, sbagliando. Il confronto vale quanto la spiegazione.
- **Chiudere i cerchi.** Una domanda aperta posta all'inizio (es. "cosa non potrà mai fare l'IA?") torna alla fine del corso.

---

## 2. STRUTTURA DI UN INCONTRO (2h)

- **Formato base:** ~1h teoria + ~1h pratica/dibattito. La pratica è flessibile: Q&A, dibattito guidato, hands-on, scelti in aula.
- **I tool si insegnano negli 8h pratici**, non nelle 12h comuni. Nelle 12h il tool si "tocca" solo per dare evidenza concreta a un concetto (5-10 min, reattivo, non pianificato).
- **Ritmo a ganci.** Ogni concetto si apre con una *slide-gancio*: una domanda introduttiva del relatore (es. "Ma quindi, in cosa è brava davvero l'IA?"). Dà ritmo e tiene alta l'attenzione. Pattern su tutta la presentazione.
- **Tensione prima del dato.** Si chiede alla stanza, si raccolgono le risposte, *poi* si mostra il numero come specchio. Mai il dato a freddo.
- **Dibattito in scala.** Da concreto a astratto: (1) esperienza vissuta sul loro caso → (2) il loro ruolo → (3) domanda aperta filosofica. Le domande devono essere **distinte tra loro**, non variazioni della stessa.
  - Almeno una domanda **tagliata sul loro lavoro** ma **generica per ogni grado** (deve funzionare da Infanzia a Secondaria).
  - La domanda aperta **non si risponde**: si raccolgono le ipotesi.
- **Sequenza dei 10 incontri flessibile.** Tipico: 4 teorici + 4 pratici + 2 teorici di chiusura. I due finali (futuro/metodo avanzato) vanno dopo la pratica, così sfruttano l'esperienza fatta.

---

## 3. COME SI COSTRUISCE UNA SCALETTA

- **Articolare tutti i concetti**, non solo i titoli dei blocchi: ogni idea da esprimere, gerarchizzata.
- **Tempi onesti, mai meccanici.** Non "5 fasi × 8 min". Un concetto semplice dura 3 min, uno difficile 8. Stimare realmente.
- **Identificare i buchi di tempo.** Per ogni blocco a rischio (può durare meno del previsto) preparare materiale di riserva. Il dibattito è il rischio maggiore: tenere 30 min di riserve in tasca (domande provocatorie, demo live, casi pronti).
- **Esempi concreti per ogni blocco.** Frasi pronte, scene tipiche, analogie. Non concetti astratti.
- **Segnalare i gap operativi.** Cosa va preparato *prima* dell'aula (es. 3 output IA per "Lo useresti?", un prompt da iterare in diretta, un template di Progetto). Marcare con ⚠.
- **Ogni blocco ha una transizione esplicita** verso il successivo (il "perché" di quella sequenza).

---

## 4. SISTEMA SLIDE — DESIGN

### Principi
- **Colorato e moderno**, densità di testo **media**: la slide è un vero supporto per chi espone (regge anche senza il relatore), non solo un'ancora.
- **Una slide = un'idea**, testo grande, molto spazio.
- **Numero di slide su tutte** (per referenziarle nelle revisioni).

### Il colore è una funzione (riflesso condizionato)
| Sfondo | Significato |
|---|---|
| **Navy scuro (`--ink` #1E1B4B)** | Statement chiave |
| **Chiaro (`--light` #F6F5FF)** | Contenuto |
| **Viola pieno (`--indigo` #4F46E5)** | GANCIO: domanda introduttiva del relatore |
| **Arancio (`--coral` #F97316)** | DIBATTITO: parla la stanza |

### Palette
`--ink #1E1B4B` · `--indigo #4F46E5` · `--violet #7C3AED` · `--cyan #06B6D4` (dati/accento) · `--coral #F97316` (dibattito) · `--light #F6F5FF` · `--text #1A1730` · `--muted #6B6790`.

### Kit dei tipi di slide (riusabili in tutto il corso)
Copertina · Statement · Dato shock · Concetto (titolo + max 3 punti) · Analogia (icona grande + testo) · Confronto (due colonne) · Citazione · Gancio (domanda viola) · Dibattito (domanda arancio) · Ponte/Chiusura.
Tutti gli incontri si costruiscono combinando questi mattoni. Cambia il contenuto, non il sistema.

### Motivi ricorrenti
Cerchi colorati morbidi negli angoli · chip-etichetta in alto a sinistra (sezione) · pallini colorati come firma · barretta corallo sopra gli statement.

---

## 5. FORMATO TECNICO (deck HTML)

- **Output = HTML autonomo** (`Incontro_N.html`), non PowerPoint. Più facile da modificare, scala a ogni schermo, si esporta in PDF/slide via stampa.
- **Unità `cqh`/`cqw`** (container query): il testo scala con la slide, niente testo tagliato.
- **Ogni slide** = `<section class="slide">` con commento `<!-- SLIDE N -->` per editing rapido.
- **Colori in un solo punto** (`:root`): cambiarli è una riga.
- **Export:** Stampa (Cmd/Ctrl+P) → Orizzontale → Margini Nessuno → Grafica di sfondo ON → PDF. CSS `@media print` = una slide per pagina, colori pieni.
- **Navigazione:** frecce + scroll + F schermo intero (JS minimale incluso).
- **QA:** controllo contenuti via markitdown; il render visivo finale lo fa Luca (ambiente senza browser). La slide più densa va sempre verificata.

---

## 6. DATI E FONTI

### Fonti verificate da usare
WEF Future of Jobs 2025 · GoStudent 2025 · MIT 2025 (Your Brain on ChatGPT) · Gerlich 2025 · Oliver Wyman Forum 2026 · HEPI 2025 · Ethan Mollick *Co-Intelligence* 2024 · GDPR Art. 9 · AI Act Annex III · DM 166/2025.

### Dati da NON usare (non verificati / superati)
- McKinsey "−30% manuali / −20% nozioni base" → non confermato nelle fonti primarie. Usa WEF 2025.
- "BSI 2025" per il calo junior → la fonte verificata è Oliver Wyman Forum 2026.

### Regola
Numeri chiari e d'impatto (es. "81% vs 25%", "170M ruoli creati"). Mai coefficienti statistici sulle slide. Sempre la fonte citata.

---

## 7. WORKFLOW DI REVISIONE (efficienza tempo/token)

Per Luca, quando chiede modifiche:
- **Sempre `slide N` + cosa cambiare.** Es: `slide 5: "81%" → "78%"`.
- **Per il testo: vecchio → nuovo** (citare le parole esatte = edit chirurgico).
- **Per i colori: solo quale** (stanno in `:root`).
- **Raggruppare tutto in un messaggio** (1 turno invece di N).
- **Distinguere contenuto da stile.**
- Le **regole generali date una volta valgono per sempre** (entrano qui).

Per modifiche strutturali (aggiunte/riordini di slide) si rigenera il file: la rinumerazione va fatta in modo sistematico.

---

## 8. CHECKLIST PRE-EROGAZIONE (gap operativi tipici)

- [ ] Output IA pre-preparati per gli esercizi "Lo useresti?" (diversi per ordine di grado)
- [ ] Prompt "sbagliato" reale da iterare in diretta nella demo prompting
- [ ] Template di Progetto (Claude) già costruito da mostrare
- [ ] Esempio di system prompt "ragionare come insegnante" su un caso concreto
- [ ] Materiale di riserva per i buchi di tempo del dibattito

---

## Principi in una riga
> **Insegna il metodo, non il tool. Una slide un'idea. Apri ogni concetto con una domanda. Tensione prima del dato. Solo dati chiari con fonte. Il colore è una funzione. Mai "—", mai "→". Tono che invita.**
