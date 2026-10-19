# Percorso Scuola 14h · cosa è cambiato

> Sorgenti: i sei moduli teorici vengono dallo **Scuola_10h** (1 ora l'uno, gruppi misti), le quattro pratiche dalla **Primaria 20h** (2 ore l'una, su Claude).
> Pubblico: docenti. Strumenti del blocco pratico: **Claude**, Canva, NotebookLM.
> Costruito il 19 ottobre 2026 con lo stesso principio della `14h/Segreteria_14h`, su richiesta di Luca.

## Il conto delle ore

6 moduli teorici da 1 ora + 4 moduli pratici da 2 ore = **14 ore**.

I teorici sono quelli del 10h, già tagliati sul tempo con il flag **"Se avanza tempo"**: regola ed elenco dei flag in `10h/Scuola_10h/CAMBIAMENTI.md`. Le pratiche sono quelle della Primaria 20h, intere. La Primaria è il percorso da cui è nato lo Scuola_10h: il suo blocco pratico ha gli stessi quattro strumenti, con Claude al posto di Gemini.

Nei teorici si è toccato solo quello che il 10h aveva cambiato per Gemini. Il punto vero è il **Progetto**: il 10h lo aveva tolto dall'Incontro 5, qui torna, perché la pratica 06 lo richiama come "già visto nell'Incontro 5" e ci incolla dentro il file di contesto permanente.

In calendario, i moduli 1 e 2 e i moduli 3 e 4 si possono accorpare in due incontri da 2 ore, come nel 10h.

## Modulo per modulo

I numeri delle slide sono quelli stampati in basso a destra su ogni slide.

| # | Deck | Ore | Sorgente | Slide | Cosa è cambiato |
|---|---|---|---|---|---|
| 1 | Incontro 1 | 1 | Scuola 10h | 31 | Niente. |
| 2 | Incontro 2 | 1 | Scuola 10h | 43 | Niente. |
| 3 | Incontro 3 | 1 | Scuola 10h | 42 | Niente. Restano le due varianti di attività, primaria e medie-superiori. |
| 4 | Incontro 4 | 1 | Scuola 10h | 43 | Slide 42, "La prossima volta": "Il contesto permanente" torna "Il Progetto", come nel 20h. |
| 5 | **Incontro 5** | 1 | Scuola 10h, più il Progetto dalla Primaria 20h | **da 34 a 35** | Torna il Progetto. Dettaglio sotto. |
| 6 | Pratica 1 · Claude | 2 | Primaria 20h | 21 | Invariata. Senza il file di setup con le credenziali: vedi sotto. |
| 7 | Pratica 2 · Canva | 2 | Primaria 20h | 13 | Invariata. |
| 8 | Pratica 3 · NotebookLM | 2 | Primaria 20h | 10 | Invariata. |
| 9 | Pratica 4 · Laboratorio | 2 | Primaria 20h | 16 | Invariato. |
| 10 | Incontro 10 | 1 | Scuola 10h | 35 | Slide 12 e 14. Dettaglio sotto. |

## Incontro 5 nel dettaglio

La base è il modulo 5 dello Scuola 10h: tre versioni del prompt (primaria, medie, superiori, senza la segreteria) e la pratica in un tempo solo, in cui si scrive il file. Dalla Primaria 20h torna il Progetto:

- **Slide 12:** "Da qui nasce il contesto permanente: smette di essere usa e getta" diventa "Da qui nasce il Progetto: il contesto smette di essere usa e getta".
- **Slide 14 e 15:** tornano quelle del 20h, "Parte 2 · Il Progetto" e "Il Progetto" (con "Vive nel Progetto" e "Col Progetto, lo scrivete una volta sola").
- **Slide 16:** il titolo "Dentro il contesto permanente" diventa "Dentro il Progetto". Resta l'esempio del 10h ("una scheda, una verifica, un compito riuscito"), che parla anche alla primaria.
- **Slide 17, nuova:** "Un Progetto compilato · Assistente verifiche di storia, terza media", identica al 20h.
- **Slide 23, "Il salto":** torna il testo del 20h, "Il Progetto lo impostate ogni volta" e "Il Progetto si rifà ogni volta."
- **Slide 32:** "Nel prossimo incontro lo mettiamo dentro Gemini." diventa "Nel prossimo incontro lo mettiamo dentro Claude."

Restano fuori, come nel 10h: il tutorial della prima chat, il prompt di inizio, la slide "La prima chat non chiede un lavoro" e la seconda pratica, quella in cui si costruisce il primo Progetto. Il Progetto si costruisce nella pratica 06.

**Asset del modulo 5:**
- `PROMPT_FILE_CONTESTO_PERMANENTE.md` è quello della Primaria 20h, che parla di Progetto, senza la versione della segreteria. Quello del 10h diceva "Nell'Incontro 6 lo mettiamo dentro una Gem di Gemini".
- `PROMPT_INIZIO_PROGETTO.md` è copiato dalla Primaria 20h anche se la sua slide non c'è: la scaletta della pratica 06 lo propone a chi vuole costruire il Progetto da zero.

## Incontro 10 nel dettaglio

- **Slide 12:** il titolo "Il contesto permanente: dati, istruzioni, esempi" diventa "Il Progetto: la memoria permanente", come nel 20h.
- **Slide 14, i quattro strumenti:** la scheda di Gemini torna quella di Claude del 20h, "Il partner organizzativo: Progetto, skill, routine, live artifact per stare in programma". Canva, NotebookLM e Laboratorio non cambiano.

## Aperti

- **Gli esempi delle pratiche sono della primaria.** I teorici reggono una stanza mista, le pratiche no: Progetto demo di Geografia per la quarta, esempi tagliati sulla primaria, tre esempi Canva da primaria. Per un gruppo di medie e superiori il blocco pratico giusto è quello della Secondaria 20h.
- **Incontro 10, slide 11**, il ripasso di IPU: dice ancora "Da qui nasce il contesto permanente.", mentre nel 20h dice "Da qui nasce il Progetto.". Da allineare se Luca dà l'ok.
- **Scaletta della pratica 06:** dice che nell'Incontro 5 ognuno ha "abbozzato un primo Progetto". Nel 14h quella pratica non c'è: ha scritto il file e ha visto il Progetto compilato.
- **Il file di setup del formatore**, `Pratica_Primaria_1_SETUP_FORMATORE.html`, non è stato copiato: contiene le credenziali dell'account del corso ed è escluso da git. Resta in `20h/Primaria/06_Pratica_Claude/` e si passa al formatore per un canale separato.
- **Scalette dei moduli teorici:** non ci sono, come nel 10h. I tempi li regge il flag. Le pratiche hanno le scalette e le guide formatori della Primaria 20h.
- **PDF dei deck e `_Consegna/`:** da generare.

## Da verificare prima dell'aula

- [ ] Account Claude a pagamento per tutti, con l'app installata sul computer (pratica 06)
- [ ] Account Canva per tutti, con Canva Code disponibile (pratica 07)
- [ ] Accesso a NotebookLM (pratiche 08 e 09)
- [ ] Mandare le istruzioni di accesso qualche giorno prima: nei moduli da un'ora non c'è tempo per i login
