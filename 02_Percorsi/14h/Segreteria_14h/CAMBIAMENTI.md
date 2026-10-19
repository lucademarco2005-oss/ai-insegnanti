# Percorso Segreteria 14h · cosa è cambiato

> Sorgenti: i sei moduli teorici vengono dal **Segreteria_10h** (1 ora l'uno), le quattro pratiche dal **Segreteria_ATA 20h** (2 ore l'una).
> Pubblico: personale ATA e di segreteria. Strumento del blocco pratico: **Claude**.
> Costruito il 19 ottobre 2026 su decisione di Luca: serve un percorso per le segreterie che usi Claude in modo specifico, e il 10h usa Gemini.

## Il conto delle ore

6 moduli teorici da 1 ora + 4 moduli pratici da 2 ore = **14 ore**.

I teorici sono quelli del 10h, già tagliati sul tempo con il flag **"Se avanza tempo"**: la regola e l'elenco dei flag stanno in `10h/Segreteria_10h/CAMBIAMENTI.md`. Le pratiche sono quelle del 20h, intere.

Nei teorici si è toccato solo quello che il 10h aveva cambiato per Gemini. Il punto vero è il **Progetto**: il 10h lo aveva tolto dall'Incontro 5, qui torna, perché la pratica 06 lo apre come "già visto nell'Incontro 5" e ci incolla dentro il file di contesto permanente.

In calendario, i moduli 1 e 2 e i moduli 3 e 4 si possono accorpare in due incontri da 2 ore, come nel 10h.

## Modulo per modulo

I numeri delle slide sono quelli stampati in basso a destra su ogni slide.

| # | Deck | Ore | Sorgente | Slide | Cosa è cambiato |
|---|---|---|---|---|---|
| 1 | Incontro 1 | 1 | 10h | 31 | Niente. |
| 2 | Incontro 2 | 1 | 10h | 43 | Niente. |
| 3 | Incontro 3 | 1 | 10h | 31 | Niente. Il caso Anthropic resta. |
| 4 | Incontro 4 | 1 | 10h | 43 | Slide 42, "La prossima volta": "Il contesto permanente" torna "Il Progetto", come nel 20h. |
| 5 | **Incontro 5** | 1 | 10h, più il Progetto dal 20h | **da 33 a 34** | Torna il Progetto. Dettaglio sotto. |
| 6 | Pratica 1 · Claude | 2 | 20h | 21 | Invariata. |
| 7 | Pratica 2 · Dati e ricerca | 2 | 20h | 27 | Invariata. La cartella si chiama `07_Pratica_Dati_Ricerca`, come nel 10h: nel 20h ha ancora il vecchio nome `07_Pratica_Claude_Excel`. |
| 8 | Pratica 3 · NotebookLM | 2 | 20h | 11 | Invariata. |
| 9 | Pratica 4 · Laboratorio | 2 | 20h | 16 | Invariato. |
| 10 | Incontro 10 | 1 | 10h | 35 | Slide 12 e 14. Dettaglio sotto. |

## Incontro 5 nel dettaglio

La base è il modulo 5 del 10h: una versione sola del prompt, quella della segreteria, e la pratica in un tempo solo, in cui si scrive il file. Dal 20h torna il Progetto:

- **Slide 12:** "Da qui nasce il contesto permanente" diventa "Da qui nasce il Progetto".
- **Slide 14, 15 e 16:** tornano le tre del 20h, cioè "Parte 2 · Il Progetto", "Il Progetto" (con "Vive nel Progetto") e "Dentro il Progetto".
- **Slide 17, nuova:** "Un Progetto compilato · Assistente mail della segreteria", identica al 20h. È il seme del Progetto Mail.
- **Slide 23, "Il salto":** torna il testo del 20h, "Il Progetto lo impostate ogni volta" e "Il Progetto si rifà ogni volta."
- **Slide 31:** "Nel prossimo incontro lo mettiamo dentro Gemini." diventa "Nel prossimo incontro lo mettiamo dentro Claude."

Restano fuori, come nel 10h: il tutorial della prima chat, il prompt di inizio, la slide "La prima chat non chiede un lavoro" e la seconda pratica, quella in cui si costruisce il primo Progetto. Il Progetto si costruisce nella pratica 06.

Restano come nel 10h la slide 10 ("Diventa la vostra prima prova") e la 25 ("Stesso metodo del prompt"): nel 20h rimandavano alla seconda pratica e al tutorial, che qui non ci sono.

## Incontro 10 nel dettaglio

- **Slide 12:** il titolo "Il contesto permanente: dati, istruzioni, esempi" diventa "Il Progetto: la memoria permanente", come nel 20h.
- **Slide 14, i quattro strumenti:** Claude (con il Progetto Mail), Ricerca approfondita, NotebookLM, Claude sui fogli. È la scheda del 10h riportata su Claude.

## Aperti

- **Incontro 10, slide 11**, il ripasso di IPU: dice ancora "Da qui nasce il contesto permanente.", mentre nel 20h dice "Da qui nasce il Progetto.". Da allineare se Luca dà l'ok.
- **Scaletta della pratica 06:** rimanda al Progetto Mail "visto compilato a slide 20" dell'Incontro 5. Nel 14h è la slide 17.
- **Scalette dei moduli teorici:** non ci sono, come nel 10h. I tempi li regge il flag. Le pratiche hanno le scalette del 20h.
- **Tempi delle pratiche:** la 06 dichiara circa 3h20 di materiale e la 07 circa 2h55, su moduli da 2 ore. È così anche nel 20h. Valgono le priorità scritte nelle scalette: nella 06 si proteggono Progetto e Skill.
- **PDF dei deck e `_Consegna/`:** da generare.

## Da verificare prima dell'aula

- [ ] Account Claude a pagamento per tutti, con l'app installata sul computer (pratica 06)
- [ ] Ricerca approfondita attiva sul piano usato in aula (pratiche 07 e 09)
- [ ] Accesso a NotebookLM (pratiche 08 e 09)
- [ ] Mandare le istruzioni di accesso qualche giorno prima: nei moduli da un'ora non c'è tempo per i login
