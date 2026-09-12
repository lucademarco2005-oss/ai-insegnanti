# Struttura Percorsi — AI Insegnanti
> 20h totali per percorso = **12h comune** (uguale per tutti, già costruita) + **8h pratica** (differenziata per tipo di percorso)
> Modello aggiornato al 9 giugno 2026. Sostituisce la vecchia struttura "4 blocchi B1-B4 + sessioni 7-10".

---

## Modello di erogazione

- Percorso totale = **20h = 10 incontri da 2h**.
- **Blocco comune = 6 incontri (12h)**, identico per tutti gli ordini. Vedi `PERCORSO_I.md` (impianto) e `SCALETTE_6_INCONTRI.md` (scalette costruite).
- **Blocco pratico = 4 incontri (8h)**, differenziato per **4 tipi di percorso**: Infanzia, Primaria, Secondaria, ATA/Segreteria.
- **Strumento base in aula = Claude** (Progetti = cartelle con memoria e istruzioni). Trasversale a tutti gli incontri, comune e pratici.
- Vincolo bando: laboratori hands-on ≥ 50% del tempo (PNRR DM 219/2025).

**Sequenza di erogazione consigliata:** I1, I2, I3, I4, poi i 4 incontri pratici, poi I5, I6 di chiusura.
*I5 e I6 vengono dopo la pratica perché fanno leva sull'esperienza con i tool già fatta.*

---

## BLOCCO COMUNE — 12h (6 incontri, tutti i percorsi)

Costruito. Riferimento di dettaglio: `SCALETTE_6_INCONTRI.md` e le cartelle `Incontro_1` … `Incontro_6`.

| # | Titolo | Stato |
|---|---|---|
| I1 | Cos'è l'IA e perché ti riguarda | costruito |
| I2 | Il metodo: i 4 principi | costruito |
| I3 | Etica, responsabilità e l'IA nel mondo | costruito |
| I4 | Parlare all'IA: il metodo del prompt | costruito |
| I5 | Dal prompt al sistema: rendere l'IA tua (IPU + Progetto) | costruito |
| I6 | Futuro e chiusura | scheletro |

Si insegna il **metodo, non il tool**. I tool specifici si insegnano nel blocco pratico.

---

## BLOCCO PRATICO — 8h per percorso (4 incontri)

> **Impianto in definizione** (valutazione strumenti in corso). Gli strumenti elencati sotto sono **candidati** ripresi dalla proposta esterna (`PROPOSTA_FORMAZIONE_LINEE-GUIDA.md`), da confermare o sostituire.

Logica proposta dei 4 incontri pratici:
- **P-1 — Claude applicato al proprio ordine:** non le basi (già nel comune), ma i casi d'uso specifici dell'ordine di grado.
- **NotebookLM — candidato trasversale:** stesso strumento su tutti i percorsi documentali (Primaria, Secondaria, ATA), con materiali del proprio ordine. Meno naturale per l'Infanzia.
- **P-3 e P-4 — strumenti ad hoc dell'ordine** (vedi menu sotto).

---

### P1 — Infanzia (8h)
Focus: mediare tra bambino e tecnologia, narrazione, inclusione. Strumenti **teacher-facing** (li usa il docente, non i bambini).

**Strumenti candidati:** Claude · Canva Magic Studio (immagini/materiali sicuri) · voce: ElevenLabs / Speechify (audiolibri, "Voci Magiche") · Suno (canzoncine mnemoniche) · demo brevi: Quick Draw, Animated Drawings.

- IA per scenari e personaggi da input verbali dei bambini
- Audiolibri personalizzati e storie sonore (rumori natura + voci personaggi)
- Prompt per immagini sicure (es. bosco incantato, acquerello, niente elementi spaventosi)

---

### P2 — Primaria (8h)
Focus: progettazione assistita, differenziazione didattica, gamification.

**Strumenti candidati:** Claude · MagicSchool.ai (suite docente: lezioni, differenziazione, quiz) · Canva · quiz interattivi (Curipod / Quizizz AI) · Suno · (Gemini/Firefly come alternative).

- Prompt iterativi per testi didattici e fiabe
- Laboratorio "Design Assistant": scheletro lezione + materiali (mappe, quiz)
- Adattare i contenuti a diversi livelli di apprendimento
- Giochi didattici: escape room, cacce al tesoro, enigmi in cornice narrativa

---

### P3 — Secondaria (8h)
Focus: cittadinanza digitale, prompt engineering, studio autonomo, preparazione accademica.
> **Decisione aperta:** mantenere Secondaria unica oppure separare **Sec. I** e **Sec. II** (gli strumenti del II grado, ricerca accademica/codice/calcolo, sono molto diversi).

**Strumenti candidati:** Claude · Perplexity (ricerca con fonti, fact-checking) · NotebookLM (studio, mappe) · MindMeister / Goblin.tools.
**Solo II grado (se separato):** Consensus / Elicit (paper) · Wolfram Alpha · DeepL Pro (lingue, latino/greco) · v0.dev / Replit (indirizzi tecnici).

- Prompt engineering: ruolo + contesto + task; Chain-of-Thought e Few-Shot al II grado
- Piani di studio e mappe concettuali adattive
- "Interroga l'IA": farsi spiegare un errore; debate assistito; verifica fonti
- Patto formativo docenti-studenti sull'uso etico

---

### P4 — ATA / Segreteria (8h)
Focus: semplificazione amministrativa, comunicazione istituzionale, gestione dati.

**Strumenti candidati:** Claude · Gemini per Google Workspace (contesto reale di segreteria) · NotebookLM (archivio, ricerca semantica) · Otter.ai o alternativa (verbali; verificare resa in italiano) · Goblin.tools.

- Automatizzare verbali, circolari, comunicazioni ("Aiutami a scrivere")
- Estrarre tendenze da fogli di calcolo; analisi dati (voti/presenze)
- Ricerca semantica su archivio e PDF scannerizzati
- Modelli di risposta "umana" per le FAQ delle famiglie

---

## Decisioni aperte (prima di costruire le scalette pratiche)
1. **Secondaria unica o Sec. I + Sec. II separate?** (impatta numero percorsi e tool)
2. **Claude e NotebookLM:** basi nel blocco comune + riapplicazione nel pratico, oppure tutto nel pratico?
3. **Consolidamento ridondanze:** una sola app presentazioni (Gamma, già nel comune), una sola app immagini (Canva). Conferma.
4. **3 tool ad hoc confermati per ogni percorso** (oltre a Claude).

---

## Note operative
- Laboratori hands-on ≥ 50% del tempo (vincolo bando).
- Ogni incontro = 2h. Blocco comune = 6 incontri, blocco pratico = 4 incontri.
- Priorità erogazione: Primaria, poi Segreteria, poi Infanzia, poi Secondaria.
- Molti tool richiedono account con limite d'età e sono server USA: per Infanzia/Primaria vanno inquadrati come strumenti del docente, mai usati direttamente dai minori (GDPR / dati minori).
