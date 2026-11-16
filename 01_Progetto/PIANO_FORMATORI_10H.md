# Piano · Percorso Formatori 10h

> Il percorso che insegna a degli insegnanti come formare i colleghi sull'intelligenza artificiale.
> Questo file contiene il reverse engineering dei percorsi esistenti, la ricerca verificata sulla formazione, e le logiche con cui il percorso è stato costruito.
> Scritto il 16 novembre 2026, dal memo vocale di Luca. Il percorso costruito sta in `02_Percorsi/10h/Formatori_10h/`.
> Standard seguito: `00_Standard/MODUS_OPERANDI.md`. Nessun file esistente è stato modificato, tranne i due README di indice.

---

## PARTE 0 · In breve

**Il mandato.** Dieci ore, cinque di teoria e cinque di pratica, per insegnare a dei docenti come si forma sull'IA. Unico vincolo: si usa e si spiega Gemini. Alla fine devono avere in mente, e aver messo in pratica, i passi con cui si costruisce un percorso.

**Cosa è stato costruito.**

- 10 deck HTML (201 slide), nello stile dei deck esistenti.
- 10 scalette per chi conduce, con minuti, punti di controllo, cosa saltare, riserve e cose da preparare.
- 5 guide pratiche per il formatore (moduli 2, 4, 6, 8, 9): cosa mostrare a schermo, in ordine.
- Il quaderno del formatore: il metodo in una pagina e sei schede di lavoro.
- 13 prompt pronti, fra cui l'assistente "Progettista di percorsi", che ha il metodo scritto nelle istruzioni.
- Note di erogazione, programma ufficiale, registro dei cambiamenti.

**L'idea che regge tutto: il doppio binario.** I partecipanti vivono ogni cosa da corsisti, poi la smontano da formatori, poi la rifanno sul proprio percorso. Il reverse engineering che Luca ha chiesto non è solo in questo file: è dentro il corso. Ogni deck ha una slide "Sotto il cofano" che dice cosa è stato fatto con loro in quell'ora, e perché.

**Tre decisioni prese senza chiedere**, perché cambiano poco e si correggono in fretta:

1. Teoria e pratica si alternano modulo per modulo (un'ora per capire, un'ora per fare), invece della struttura 5 teorici, 4 pratici, 1 di chiusura degli altri 10h.
2. Solo Gemini, senza Canva e senza NotebookLM. Le funzioni: chat e file, assistente su misura, Canvas, Deep Research.
3. Il programma ufficiale è un file nuovo. Quello che esisteva per "Formatori e Figure di sistema" descrive un altro prodotto (i dieci moduli standard, per un gruppo misto) e non è stato toccato. Vedi Parte 6.

---

## PARTE 1 · Reverse engineering: cosa regge i percorsi esistenti

Analizzati per intero: i sei incontri teorici della Primaria (234 slide), le quattro lezioni pratiche, i moduli Gemini dei 10h, le scalette, le guide dei formatori, i registri dei cambiamenti, e la call del 29 giugno con la formatrice.

**Un'avvertenza prima dell'elenco.** Nei materiali non ci sono dati di gradimento o di risultato dei corsi. Che siano andati bene è un'informazione di Luca. Quello che segue descrive come sono fatti e quali scelte, verosimilmente, li hanno fatti funzionare: è un'analisi di progetto, non una misura.

### I 12 elementi, in ordine di peso

**1. Una sola tesi, ripetuta per dieci incontri: il metodo, non lo strumento.**
Compare nel primo incontro ("La differenza non è lo strumento. È il metodo."), apre il secondo ("I tool cambiano ogni sei mesi. Il metodo no.") e chiude l'ultimo. Dà al docente qualcosa che non scade. Verifica sul campo: in `PIANO_PERCORSI_10H.md` il conteggio delle occorrenze di "Claude" nei sei deck comuni è quasi zero, e infatti il passaggio a Gemini ha toccato due slide.

**2. Il docente passa da "in ritardo" a "insostituibile".**
"Non siete indietro. Siete gli unici che possono ancora insegnare la differenza." arriva subito dopo il dato sugli studenti. "Più siete esperti, meglio usate l'IA: la vostra competenza è il filtro." Si toglie la difesa prima di chiedere fatica.

**3. La domanda viene prima del contenuto.**
Su 234 slide, 27 sono ganci viola e 17 sono domande arancioni. Il modulo base è sempre lo stesso: domanda, contenuto, frase da ricordare, domanda alla stanza. Chi ascolta ha già un'ipotesi in testa quando arriva il dato.

**4. Tensione prima del dato.**
"Quanti dei vostri studenti usano l'IA ogni giorno?" e solo dopo "81% contro 25%". Il dato è uno specchio, non un'informazione.

**5. Ogni concetto atterra su un oggetto del mestiere.**
È il punto che Luca ha descritto nel memo: l'IA non come cosa che sta sopra, ma calata dentro la scuola. Il meccanismo, ricostruito dalle slide, ha tre mosse:

| Il concetto generale | Come diventa scuola | La mossa |
|---|---|---|
| I limiti del modello | "Capire che Marco va incoraggiato" | una persona |
| La supervisione umana | "Un collega vi passa una verifica fatta con l'IA in due minuti. Cosa guardate?" | un oggetto del mestiere |
| I dati sensibili, GDPR | "Se non lo incollereste sulla porta della classe, non caricatelo" | un gesto |
| La reversibilità dell'errore | "Bozza di una circolare" contro "Valutare uno studente" | un oggetto del mestiere |
| L'automazione | "Cosa si ripete, ogni settimana" | un gesto |

**6. Nella pratica: perché, funzione, caso d'uso, prova.**
È lo schema che Luca ha dettato nel memo. Verificato sui materiali:

- È applicato **alla lettera** nella lezione Dati e ricerca della Segreteria (un perché e una prova per ciascuna funzione) e, sulla carta, nella scaletta della lezione Claude ("ogni stazione apre con la sua panoramica, poi due o tre esempi tagliati sulla primaria, poi lo fanno loro").
- **In aula** spesso diventa: un perché solo, poi più funzioni ciascuna col suo caso, e una prova libera alla fine. La guida del formatore della lezione Claude mette sette demo in fila e un solo passo di pratica.

Il percorso insegna lo schema alla lettera e dichiara la variante: modulo 5, slide 11, "Quando l'ora è una sola". È più onesto, e chi forma deve sapere cosa si può comprimere e cosa no: la prova può essere una sola, ma non può mancare e non può essere a casa.

**7. Il caso d'uso è un dolore riconoscibile.**
I criteri impliciti con cui sono scelti: si ripete ("Qual è il lavoro che vi ripetete ogni settimana e che dareste volentieri via?"), pesa ("a maggio siamo sempre indietro col programma"), si usa subito ("Quale dei tre userete già la prossima settimana?"), si può misurare ("Due domande ripetute: quasi 23 ore in un anno"), non tocca dati personali. La funzione arriva come soluzione.

**8. Un filo per percorso, e un oggetto che cresce.**
Geografia in quarta, l'autunno, la storia in terza media, le mail dell'ufficio. E nel teorico: la lezione progettata nell'incontro 2 torna nel 3 e nel 4; la domanda aperta del primo incontro si chiude nell'ultimo. Nei 10h il filo diventa il kit personale: ogni modulo produce un pezzo.

**9. Ogni incontro finisce con qualcosa in mano.**
Le slide "Output:", "meglio una cosa finita e usabile che tre abbozzate", "la prima cosa vera".

**10. Prompt pronti, testati, sulla slide. E il primo oggetto costruito scrive gli altri.**
In ogni percorso la prima cosa che si costruisce è lo scrittore di prompt. Toglie la paura del foglio bianco al pubblico meno tecnico. Regola già pagata una volta: il prompt va in slide per intero, non riassunto.

**11. Rigore sui dati, con l'onestà detta ad alta voce.**
Fonte in piè di slide, coefficienti tradotti in parole, dati virali smontati in slide ("mezzo litro d'acqua"). Con una platea di insegnanti è quello che costruisce credibilità.

**12. La regia è scritta per reggere l'imprevisto, e si corregge sul campo.**
Buchi di tempo, riserve in ordine, cosa proteggere, liste di cose da preparare, piani B sugli account. E le correzioni vengono da chi era in aula: due domande riscritte e una tolta "su segnalazione delle formatrici, perché la risposta era scontata".

### Tre cose che i materiali mostrano e che conviene sapere

- **Il tono.** Quasi tutte le frasi da ricordare hanno la forma "non è X, è Y". Funziona a voce. È anche uno dei segnali che l'incontro 4 insegna a riconoscere nei testi generati. Nel percorso nuovo è usato meno.
- **Il sovraccarico.** Il blocco pratico da 20 ore dichiara 10 ore e 15 di materiale su 8 disponibili; la lezione Claude 3 ore e 20 su 2. È diventato il materiale del modulo 6: "sommate davvero i minuti".
- **Cosa non si adatta.** Fra un pubblico e l'altro cambiano gli esempi, le parole e la frase d'apertura. Non la struttura. È la slide 16 del modulo 3: "Struttura ferma, esempi mobili".

---

## PARTE 2 · Cosa dice la ricerca, e come si lega alle nostre scelte

Ricerca fatta sulle fonti primarie il 16 novembre 2026. I link sono nella Parte 4.

| Quello che facciamo | Cosa dice la ricerca | Fonte |
|---|---|---|
| Si prova in aula, si mostra come si fa, si lavora sul proprio contenuto | Su 35 studi rigorosi di corsi che hanno cambiato l'insegnamento: 35 mostravano un modello, 34 facevano provare, 31 duravano nel tempo | Darling-Hammond, Hyler, Gardner 2017 |
| Le 4 mosse | Si impara meglio partendo da un problema reale, attivando quello che si sa, vedendo una dimostrazione, applicando, portando nel proprio lavoro | Merrill 2002 |
| La mossa 1, il perché | Gli adulti hanno bisogno di sapere perché imparano una cosa (è un principio, non una legge) | Knowles |
| Dalla demo alla prova | Rilascio graduale della responsabilità; piccoli passi con pratica dopo ogni passo | Pearson e Gallagher 1983; Rosenshine 2012 |
| Prima il traguardo, poi le attività | Progettazione a ritroso in tre fasi | McTighe e Wiggins |
| Una slide, un'idea | La memoria di lavoro tiene pochi elementi alla volta; togliere il materiale estraneo aiuta | Sweller; Mayer |
| Calare nella scuola, non dare per scontato | Chi sa una cosa sovrastima quanto è chiara agli altri: 50% previsto, 2,5% reale | Newton 1990 (tesi) |
| Aprire ogni incontro con una domanda sul precedente | Chi si mette alla prova ricorda di più di chi rilegge: 56% contro 42% dopo una settimana | Roediger e Karpicke 2006 |
| I sei minuti in aula | Il microteaching nasce a Stanford nel 1963: lezioni brevi, riscontro subito, si rifà | Allen 1967 |
| Misurare il lunedì dopo | Quattro livelli: reazione, apprendimento, comportamento, risultati | Kirkpatrick |
| Le coppie di colleghi | Il sostegno fra pari è quello che porta la novità in classe (stima degli autori) | Joyce e Showers 2002 |
| Togliere la paura prima degli strumenti | Le prime formazioni dei distretti americani sono partite dal ridurre il disagio | RAND 2025 |

**Il dato che apre il percorso** (modulo 1): secondo TALIS 2024, in media nei Paesi OCSE solo il 55% dei docenti dice che la formazione seguita ha migliorato il proprio insegnamento, e l'IA è il tema su cui chiedono più formazione (29%). In Italia il 25% dei docenti ha usato l'IA nell'ultimo anno, contro il 36% della media OCSE.

---

## PARTE 3 · Il percorso: architettura e logiche

### I tre livelli del metodo che i partecipanti portano via

1. **I 6 passi** per costruire un percorso: Pubblico, Traguardo, Casi d'uso, Sequenza, Lezione, Regia. Poi si prova davanti a qualcuno e si corregge.
2. **I due stampi** di una lezione: le 4 mosse per uno strumento (perché, funzione, caso d'uso, prova) e il blocco per un'idea (domanda, contenuto, frase, stanza).
3. **Le regole** che non si saltano: metodo e non strumento, dentro la scuola, dato con fonte, oggetto finito, allarme che si chiude con una cosa da fare, decidere prima cosa proteggere.

Sono raccolti in una pagina nel quaderno ("Il metodo in una pagina") e nelle istruzioni dell'assistente "Progettista di percorsi".

### La logica di ogni incontro

| Incontro | Teoria: cosa capiscono | Pratica: cosa fanno con Gemini | Perché in quest'ordine |
|---|---|---|---|
| **1** | Perché tanti corsi non lasciano traccia. Le tre scelte. La mappa dei 6 passi | Vivono una lezione vera sulla chat, la smontano, e si fanno intervistare da Gemini per scrivere pubblico e traguardo | Prima di tutto vivono il metodo, senza nome. Il nome arriva dopo |
| **2** | Come si sceglie un caso d'uso (quattro criteri). Come si mette in fila (tre regole). I nostri errori | Costruiscono l'assistente che conosce il metodo e gli fanno proporre casi d'uso e sequenza | I casi li scelgono prima a mano: così hanno un termine di confronto con quello che propone l'IA |
| **3** | I due stampi di una lezione. Tensione prima del dato. Calare nella scuola | Con Canvas: scaletta, slide, foglio dei prompt di un incontro | La scaletta prima delle slide: è la regola che insegnano e quella che seguono |
| **4** | Il tono, le domande, il tempo, il piano B | Con Deep Research verificano un dato; Gemini fa il collega difficile; preparano una demo | L'obiezione la provano prima fra loro (modulo 7), poi con Gemini (modulo 8) |
| **5** | Misurare, correggere, adattare, far durare. Si chiude la domanda aperta | Sei minuti a testa, con una cosa da tenere e una da cambiare | Nessuno esce senza aver condotto almeno una volta |

### Come è stato rispettato il vincolo Gemini

| Funzione di Gemini | Dove si spiega | Caso d'uso per chi forma |
|---|---|---|
| Chat, file, le 5 fasi | Modulo 2 | Farsi intervistare per scrivere la scheda del pubblico |
| Assistente su misura (Gem o Skill) | Modulo 4 | Lo scrittore di prompt e il progettista di percorsi |
| Canvas | Modulo 6 | La scaletta, le slide, il foglio dei prompt |
| Deep Research | Modulo 8 | Verificare un dato prima di metterlo in slide |
| Chat con un ruolo | Modulo 8 | Provare la risposta a un'obiezione |

Ogni funzione è insegnata con le 4 mosse, su un compito del formatore. È il doppio binario: imparano Gemini mentre imparano come si insegna Gemini.

**La sorpresa di novembre 2026: i Gem diventano Skill.** Google sta sostituendo i Gem. Sugli account della scuola restano fino a giugno 2027, sugli account personali spariscono a dicembre. Le slide dicono "assistente su misura" e nominano tutti e due. Invece di essere un problema, è diventato la slide 7 del modulo 4: "I menu cambiano ogni sei mesi. Per questo si insegna il metodo." Dettagli in `NOTE_EROGAZIONE.md`.

### Le scelte di costruzione, e perché

- **"Sotto il cofano".** Una slide per modulo, sempre con la stessa etichetta. È il momento in cui cambiano sedia. Senza, il doppio binario resterebbe implicito e i partecipanti imparerebbero Gemini, non a insegnarlo.
- **Gli errori nostri, raccontati.** Tre nel modulo 3, tre nel modulo 8, tre correzioni nel modulo 10. È la parte "trial and error" del memo. Raccontare cosa non ha funzionato è quello che rende credibile il resto, ed è materiale che un altro corso non ha.
- **I casi d'uso si scelgono due volte.** A mano nel modulo 3, con l'assistente nel modulo 4. Chi ha già una sua lista corregge la proposta dell'IA invece di accettarla. È il primo dei 4 principi, applicato a chi forma.
- **Carta e penna nei moduli teorici.** Gli esercizi dei moduli 3 e 5 sono su carta, apposta: lo strumento si apre nel modulo pratico. È la regola "il metodo prima dello strumento", applicata al percorso stesso.
- **Il microteaching nell'ultimo incontro.** È la prova che il mandato chiedeva: "abbiano messo in pratica". Sei minuti bastano a vedere cosa regge.
- **La domanda che resta aperta.** "Tra tre mesi, da cosa capirete che il vostro corso è servito?" si apre nel modulo 1 e si chiude nel modulo 10, come la domanda aperta del primo incontro dei percorsi esistenti.
- **Nessun riassunto all'inizio dei moduli.** Ogni modulo si apre con una domanda di ripresa. È coerente con quello che il modulo 10 insegna a fare.

### Cosa è stato lasciato fuori, e perché

- **I contenuti sull'IA in sé** (cos'è, etica, futuro). Il pubblico sono formatori e figure di sistema: il percorso dà per fatto, o in corso, quello di base. Chi non l'ha fatto può seguire prima uno dei 10h per docenti. Va detto nel programma, ed è scritto.
- **Canva e NotebookLM.** Fuori dal vincolo. NotebookLM, che nel frattempo si chiama Gemini Notebook, è nominabile a voce come passo successivo.
- **Le funzioni che dipendono dalla licenza** (pianificazioni, video, Gemini Live): stessa scelta fatta per gli altri 10h.

---

## PARTE 4 · Fonti verificate, e dati da non usare

Aperte sulle fonti primarie il 16 novembre 2026, salvo dove indicato.

### Usate nelle slide

| Dato | Dove | Fonte |
|---|---|---|
| 55% dice che la formazione ha migliorato il proprio insegnamento; 29% indica l'IA come bisogno di formazione (media OCSE) | M1 s6 | OCSE, TALIS 2024. Rapporto completo |
| 25% dei docenti italiani ha usato l'IA; 69% di chi non la usa dice di non avere le conoscenze | M1 s7 | OCSE, TALIS 2024, nota Paese Italia: https://invalsi-areaprove.cineca.it/docs/2025/Indagini_Internazionali/RAPPORTI/TALIS_Nota_Paese_OCSE.pdf |
| 35, 34 e 31 studi su 35 | M1 s11 | Darling-Hammond, Hyler, Gardner 2017: https://learningpolicyinstitute.org/product/effective-teacher-professional-development-report |
| Le prime formazioni sono partite dal ridurre il disagio | M1 s15 | RAND, Diliberti, Lake, Weiner, aprile 2025: https://www.rand.org/pubs/research_reports/RRA956-31.html |
| Progettazione a ritroso | M3 s5 | McTighe e Wiggins 2012: https://files.ascd.org/staticfiles/ascd/pdf/siteASCD/publications/UbD_WhitePaper0312.pdf |
| Il bisogno di sapere perché | M5 s6 | Knowles, in TEAL Center 2011: https://lincs.ed.gov/sites/default/files/11_%20TEAL_Adult_Learning_Theory.pdf |
| Quattro dei cinque principi | M5 s10 | Merrill 2002: https://mdavidmerrill.files.wordpress.com/2019/04/firstprinciplesbymerrill.pdf |
| 81% degli studenti italiani usa l'IA | M5 s14 | GoStudent 2025 (già in `RICERCA_CONTENUTI.md`) |
| 50% previsto, 2,5% reale (3 su 120) | M5 s16 | Newton 1990, tesi di dottorato, Stanford, p. 41 |
| Microteaching, Stanford 1963 | M9 s4 | Allen 1967: https://files.eric.ed.gov/fulltext/ED019224.pdf |
| I quattro livelli | M10 s5 | Kirkpatrick: https://www.kirkpatrickpartners.com/the-kirkpatrick-model/ |
| 56% contro 42% dopo una settimana | M10 s12 | Roediger e Karpicke 2006, esperimento 1 |
| Sostegno fra pari | M10 s13 | Joyce e Showers 2002, **stima degli autori** |
| Art. 4 del regolamento europeo sull'IA; linee guida MIM | M10 s14 | Reg. UE 2024/1689, modificato dal Reg. UE 2026/1744; DM 166/2025 |

### Da non usare (girano, ma non reggono)

1. **Il "cono dell'apprendimento"** (10% di ciò che leggiamo, 90% di ciò che facciamo): senza base empirica, attribuito falsamente a Dale.
2. **Joyce e Showers "5% contro 95%"** come dato misurato: sono stime del libro del 2002, e in rete ne girano almeno tre versioni diverse.
3. **"Dimentichiamo il 70% in 24 ore":** Ebbinghaus aveva un solo soggetto e sillabe senza senso.
4. **"Gli insegnanti risparmiano sei settimane l'anno con l'IA":** è un'autostima dei soli utilizzatori settimanali, negli Stati Uniti (Gallup e Walton 2025).
5. **"Servono almeno 49 ore di formazione":** è una media di nove studi, non una soglia.
6. **"18.000 dollari per insegnante":** tre distretti americani, 2015.
7. **Il valore di Hattie per il microteaching:** è un coefficiente, cambia fra le edizioni, e non va in slide.
8. **AI Act, art. 4, come obbligo di formazione certificata:** nessun certificato è richiesto, e il testo è cambiato a luglio 2026.
9. **"INDIRE 2025: il 52,4% degli insegnanti italiani usa l'IA":** campione autoselezionato. Vedi Parte 6.

---

## PARTE 5 · Cosa serve prima della prima erogazione

In ordine:

1. **Provare i 13 prompt dentro Gemini**, sull'account che si userà. Sono stati scritti e riletti, non provati: è la regola che il percorso stesso insegna, e qui non era possibile rispettarla.
2. **Le verifiche sugli account** di `NOTE_EROGAZIONE.md`, con l'amministratore della scuola.
3. **Guardare i deck a schermo.** Il controllo fatto: nessun testo fuori pagina su 201 slide, e la resa a vista delle slide più dense. Resta da fare la visione a schermo intero in Chrome.
4. **Dopo la prima aula:** correggere i minuti delle scalette e scrivere le correzioni nel registro di `CAMBIAMENTI.md`.

---

## PARTE 6 · Segnalazioni, senza aver toccato niente

Cose trovate lavorando, fuori dal mandato. Restano come sono finché Luca non decide.

1. **Il programma "Formatori e Figure di sistema" che esisteva già** (`01_Progetto/Programmi/10h/PROGRAMMA_10h_Formatori_Figure_di_Sistema.html`) descrive i dieci moduli standard per un gruppo misto. È un prodotto diverso da questo. Il nuovo programma si chiama `PROGRAMMA_10h_Formare_i_Formatori.html`. Va deciso se il vecchio resta come seconda edizione o viene sostituito, soprattutto se è già stato mandato a una scuola.
2. **Gem e Skill nei percorsi già consegnati.** `Scuola_10h` e `Segreteria_10h` parlano solo di Gem. Sugli account della scuola funzionano ancora fino a giugno 2027, ma dal 17 novembre 2026 i Gem si aprono da un altro menu, e sugli account personali spariscono a dicembre.
3. **NotebookLM si chiama Gemini Notebook** dal luglio 2026. I deck 08 di tutti i percorsi usano il vecchio nome.
4. **`00_Standard/RICERCA_CONTENUTI.md`, riga su INDIRE 2025:** il "52,4% degli insegnanti italiani usa l'IA" viene da un campione autoselezionato (1.035 su 1.803 rispondenti). Andrebbe riformulato.
5. **L'articolo 4 dell'AI Act** è stato riscritto a luglio 2026. Dove i deck esistenti lo citano, la formulazione va ricontrollata.
6. **`Segreteria_10h/07_Pratica_Dati_Ricerca/README_FORMATORE.md`** dice ancora "Si lavora dentro Claude".
7. **Credenziali.** Il file di memoria `lezione-claude-primaria.md` contiene email e password dell'account del corso in chiaro. Non è nella repo, ma conviene toglierle.
