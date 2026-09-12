# Incontro 4 · Parlare all'IA: il metodo del prompt

> Durata 2h | Metodo del prompt ~40 min · Riconoscere l'IA ~13 min · Due momenti pratici ~45 min · Dove l'IA sbaglia ~10 min · Apertura/chiusura ~12 min
> **Nota tempi:** la lezione è densa. Se serve tagliare, gli esempi della Parte A si riducono a 3 (gli altri restano materiale) e la Parte C tiene un solo esempio a confronto. Si protegge sempre Pratica 2.
> **Chiave trasversale (vale a ogni livello):** un buon prompt non è un linguaggio segreto, è dire bene quello che già sapete di voler ottenere. Vale alle medie come alle superiori, in ogni disciplina.
> **Raccordo (continuità):** I2 il metodo e una lezione sull'IA da progettare, I3 un'attività per i propri ragazzi. Oggi chiudiamo il cerchio operativo: con il prompt si costruiscono davvero quei materiali.
> **Fonte struttura:** ricalca la presentazione "Utilizzare l'IA in Modo Potenziante" (istintivo vs sistematico, le 5 fasi, multi-formato).
> **Regole:** segue il MODUS_OPERANDI (ganci, domandine, dati chiari con fonte, tono che invita, niente "—" né "→").

---

## BLOCCO 0 — Ripresa e apertura (4 min)
- Dove siamo: sappiamo cos'è l'IA, abbiamo un metodo, sappiamo cosa è giusto. Manca il gesto pratico: parlarle bene.
- Frase di apertura: "Non serve un linguaggio segreto. Serve dire con ordine quello che avete in testa."
- Anticipare il filo: prima il metodo del prompt, poi un primo esercizio veloce, poi dove l'IA sbaglia, poi costruiamo davvero la lezione che state preparando dall'Incontro 2.

---

## PARTE A — Dall'istinto al metodo (~35 min) · LA PARTE PIÙ RICCA

### Gancio → istintivo vs sistematico
Slide-gancio: **"Quando l'IA vi delude, è colpa sua o di come gliel'avete chiesto?"**

### BLOCCO 1 — Prompt istintivo vs sistematico (5 min)
- Istintivo: due righe buttate lì, a volte funziona a volte no, e non si capisce perché. Casuale e inconsistente.
- Sistematico: una struttura che funziona per design, riutilizzabile e coerente, che migliora nel tempo.
- Dato: i prompt strutturati sono preferiti nel **73% dei casi** rispetto a quelli scritti di getto (OpenAI 2024).
- Il punto: non è talento, è metodo. Lo stesso che insegnamo agli studenti.

### BLOCCO 2 — Le 5 fasi del prompt (15 min)
> Si spiegano una per una, e l'esempio cresce: lo stesso compito che si raffina passo dopo passo.

- **1. Obiettivo:** cosa devo fare, come lo voglio, che formato mi serve. Senza obiettivo arriva una risposta generica. Il formato è la cosa più sottovalutata ("in tabella", "in 5 punti", "in 100 parole" cambia tutto).
- **2. Contesto:** chi sei, chi è il destinatario, che ruolo deve avere l'IA, quali dettagli servono. L'IA non sa niente di voi se non glielo dite. Nota: "sei un esperto" generico serve a poco; serve un ruolo concreto (storia in una terza media, 24 alunni, argomento mai affrontato; oppure italiano al biennio con quattro DSA in classe).
- **3. Esempi e materiali:** mostrare invece di descrivere. Uno screenshot, un testo, un modello del "fatto bene". Un esempio vale più di cento istruzioni.
- **4. Valutazione:** il primo risultato è una bozza, non un verdetto. Niente "no" secchi: feedback mirati, spiegare cosa manca e perché. *(Contro-intuitivo: la maggior parte dà feedback troppo poveri e ottiene di peggio.)*
- **5. Iterazione:** il primo prompt è quasi sempre da correggere, è normale. Si raffina, si divide per sezioni, si aggiungono vincoli. Iterare migliora la qualità di circa un terzo rispetto al colpo singolo (OpenAI 2024).
- *Chiusura del blocco:* "Prima di inviarlo, rileggi: c'è l'obiettivo? c'è il contesto? c'è un esempio?". E ricordare il multi-formato: il prompt si può anche dettare a voce, dallo smartphone.

### BLOCCO 3 — Esempi: fatto male vs fatto bene (15 min)
> Cuore della lezione. 5 coppie, una per tipo di pubblico (così ognuno si riconosce). Ogni "fatto bene" ha dentro le 5 fasi.
> ⚠ Da preparare: questi esempi stampati/mostrati, idealmente con l'output reale a fianco per un paio di essi.

**Esempio 1 · Verifica (secondaria)**
- Male: *"Fammi una verifica sulla Seconda guerra mondiale."*
- Bene: *"Sei un insegnante di storia di terza media. Prepara una verifica sulla Seconda guerra mondiale per 22 alunni di livello eterogeneo. Struttura: 4 domande a risposta chiusa, 3 a risposta aperta breve (massimo 5 righe), 1 di collegamento causa-effetto. Linguaggio semplice, frasi corte. Ti allego la mia verifica dell'anno scorso: tienine il tono e la difficoltà. Alla fine indica, per ogni domanda, l'obiettivo che verifica. Se un argomento non è nel programma che ti allego, non inserirlo."*
- Le 5 fasi: Obiettivo (struttura e formato) · Contesto (chi sei, che classe) · Esempi (verifica allegata) · Valutazione (obiettivo per domanda) · Iterazione (vincolo "solo dal programma").

**Esempio 2 · Spiegare un concetto (medie)**
- Male: *"Spiega le equazioni di primo grado."*
- Bene: *"Sei un insegnante di matematica di terza media. Spiega le equazioni di primo grado a ragazzi di 13 anni che le incontrano per la prima volta. Parti da un solo esempio concreto (la bilancia in equilibrio), un passaggio per volta, nessun termine tecnico non spiegato. Massimo 200 parole. Concludi con 3 esercizi di difficoltà crescente per capire se hanno capito. Se usi una parola difficile, spiegala subito tra parentesi."*
- Le 5 fasi: Obiettivo (200 parole, 3 esercizi) · Contesto (matematica, 13 anni, prima volta) · Esempi (la bilancia) · Valutazione (esercizi di controllo) · Iterazione (vincolo sulle parole difficili).

**Esempio 3 · Comunicazione ai genitori (superiori)**
- Male: *"Scrivi una mail ai genitori per il viaggio d'istruzione."*
- Bene: *"Sei il coordinatore di una terza di liceo scientifico. Scrivi ai genitori per il viaggio d'istruzione a Praga dal 12 al 15 aprile. Tono cordiale e chiaro, massimo 150 parole. Devono risultare evidenti: quota e cosa comprende, scadenza dell'acconto, documenti necessari, docenti accompagnatori, data della riunione informativa. Chiudi con i contatti del coordinatore. Non usare un tono burocratico."*
- Le 5 fasi: Obiettivo (150 parole, info chiave) · Contesto (coordinatore, terza liceo) · Materiali (i dati del viaggio) · Valutazione (cosa deve risultare evidente) · Iterazione (negativo: niente burocratese).

**Esempio 4 · Progettare la lezione (trasversale, continuità con I2-I3)**
- Male: *"Fammi una lezione sull'intelligenza artificiale."*
- Bene: *"Sei un insegnante di secondaria di primo grado. Progetta una lezione di 50 minuti per una seconda media per imparare a capire quando un'informazione è affidabile, usando l'IA come esempio. Obiettivo: alla fine i ragazzi sanno verificare una fonte. Struttura in 3 momenti (apertura con una domanda, attività a gruppi, discussione finale) con i tempi di ciascuno. Per l'attività proponi un esempio concreto svolgibile in classe. Indica i materiali. Se serve un dispositivo, dammi anche un'alternativa senza."*
- Le 5 fasi: Obiettivo (50 min, 3 momenti) · Contesto (chi, che classe) · Esempi (attività concreta) · Valutazione (obiettivo finale verificabile) · Iterazione (alternativa senza dispositivo).

**Esempio 5 · Griglia di valutazione (secondaria)**
- Male: *"Fammi una griglia per valutare i temi."*
- Bene: *"Sei un insegnante di italiano del biennio. Crea una griglia per valutare un tema argomentativo su 4 criteri: aderenza alla traccia, struttura e coerenza, lessico, correttezza grammaticale. Per ogni criterio definisci 4 livelli (insufficiente, sufficiente, buono, ottimo) con una descrizione breve e concreta di cosa li distingue. Formato tabella. Pesa i criteri in modo che la grammatica valga al massimo un quarto del voto. Usa un linguaggio che potrei condividere con gli studenti."*
- Le 5 fasi: Obiettivo (griglia, 4 criteri, tabella) · Contesto (italiano, biennio) · Materiali (i criteri) · Valutazione (descrittori e pesi) · Iterazione (linguaggio condivisibile).

- **Sintesi:** il "fatto male" è corto e vago, il "fatto bene" è lungo solo perché dice le cose giuste. Non è più difficile: è solo più pensato.

### BLOCCO 3-bis — Due tecniche in più (6 min, solo Secondaria)
Slide 31 e 32. Sono il "prompt engineering intermedio" promesso nel programma.
- **Esempi (few-shot):** invece di descrivere lo stile che volete, glielo fate vedere. Si incollano due tracce o due consegne già scritte da voi e si chiede di produrne altre con la stessa struttura. Funziona meglio di qualunque aggettivo.
- **Ragionamento passo passo (chain-of-thought):** "prima ragiona passo per passo, poi rispondi". Serve dove i passaggi contano: problema di matematica, analisi del testo, correzione motivata. Doppio guadagno: si vede dove sbaglia, e il ragionamento esplicito diventa la spiegazione da portare in classe.
- Nota di regia: qui si può mostrare dal vivo la differenza sullo stesso prompt, con e senza la riga del ragionamento.

### BLOCCO 4 — Una marcia in più: il semaforo di affidabilità (5 min)
> Tecnica avanzata che si aggiunge al prompt. Non è una sesta fase: è un accessorio che si incolla in fondo per difendersi dalle allucinazioni (che vedremo tra poco). Si chiede all'IA di dichiarare quanto è sicura.
- Idea: invece di lasciare che l'IA risponda "sempre e con sicurezza", le si chiede di mettere un semaforo accanto a ogni informazione.
- Snippet da incollare in fondo a un prompt:
  > *"Presenta i risultati così: tabelle pulite per le parti con numeri o dati; accanto a ogni informazione un'etichetta ✅ verificato, ⚠️ parziale, ❌ non verificato; in cima, il livello di confidenza complessivo (Alto / Medio / Basso); chiudi con 'Cosa manca ancora' e i passi per verificarlo."*
- Lettura a semaforo: ✅ verde è dove ti fidi, ⚠️ giallo è dove controlli, ❌ rosso è dove non ti fidi.
- Il punto: una sola riga in più nel prompt e l'IA ti dice da sola dove stare attento. È il ponte verso la prossima parte.

---

## PRATICA 1 — Scrivi un prompt, subito (~12 min)
> Appena finito il metodo. Caldo, leggero, una vittoria veloce.

- "Prendete una cosa vostra, piccola, della prossima settimana: una mail, una consegna, una griglia, una circolare. Scrivete UN prompt fatto bene con le 5 fasi."
- Si lavora su carta, da soli (8 min). Poi un giro lampo: 2-3 leggono il loro prompt ad alta voce (4 min).
- Domanda di chiusura (non una frase): **"Qual è la fase che vi è venuta più difficile da scrivere?"**
- ⚠ Riserva: avere un prompt-modello già pronto da mostrare se la stanza si blocca.

---

## PARTE B — Dove l'IA sbaglia (~10 min)
> Volutamente breve. Due cose sole: inventa quando non sa, e si porta dietro il passato. Più la difesa pratica.

### Gancio → allucinazioni
Slide-gancio: **"Vi è mai capitato un risultato perfetto nella forma, ma sbagliato nei fatti?"**

### BLOCCO 5 — Allucinazioni (5 min)
- L'IA tende a rispondere sempre. Quando non sa, non dice "non lo so": dice qualcosa di plausibile. Inventa con sicurezza.
- Metafora per insegnanti: lo studente brillante che, pur di non ammettere di non sapere, costruisce una risposta convincente. Lo riconoscete già.
- La difesa l'avete già in mano: il semaforo di affidabilità di prima ("se non sai, dimmelo, non inventare", etichette ✅ ⚠️ ❌, dai il testo su cui rispondere). Una riga nel prompt, e l'errore non passa più inosservato.
- **Domandina (1 min):** "Su quali vostre materie un errore così passerebbe inosservato?"

### Gancio → bias
Slide-gancio: **"Se l'IA impara dal passato, quali idee del passato si porta dietro?"**

### BLOCCO 6 — I bias, un caso solo (5 min)
- L'IA riflette i dati con cui è stata addestrata. I pregiudizi del passato diventano decisioni automatiche. Non è cattiveria: è lo specchio del mondo com'era.
- **Caso Amazon (2018):** un sistema automatico per selezionare i curriculum penalizzava le candidate donne. Aveva imparato da dieci anni di assunzioni in gran parte maschili, e ne aveva dedotto che "uomo" fosse un segnale positivo. Amazon lo ha ritirato.
- Il punto per la scuola: quando l'IA produce materiali per i ragazzi, lo specchio del passato può riaffiorare. Accorgersene è parte del mestiere.
- *Difesa in una riga (chiusura di Parte B):* più una decisione è importante e difficile da correggere, più resta vostra. L'IA prepara, l'umano decide. Per le scelte ad alto impatto è anche un obbligo di legge (AI Act, Art. 14).

---

## PARTE C — Riconoscere un testo scritto dall'IA (~13 min)
> Competenza civica e didattica: oggi un testo su due che leggiamo può essere generato. Saperlo riconoscere serve a noi e ai ragazzi. E la stessa guida, al contrario, serve a scrivere meglio con l'IA (altro pezzo da aggiungere al prompt).

### Gancio → riconoscere l'IA
Slide-gancio: **"Quanto siete sicuri di riconoscere un testo scritto da una macchina?"**

### BLOCCO 7 — Il paradosso comunicativo (2 min)
- Il corto circuito: scrivo tre punti chiave, li faccio gonfiare dall'IA in un testo lungo, lo mando a qualcuno che lo fa riassumere, di nuovo con l'IA. In mezzo, il senso evapora.
- Per questo serve una bussola: capire quando un testo è stato generato (o pesantemente assistito) dall'IA. Tre famiglie di indizi: stile, struttura, vocabolario.

### BLOCCO 8 — I tre indizi (6 min)
- **1. Stile, tono, contenuto.** Tono troppo neutro e levigato (manca ironia, attrito, imperfezione). Hype teatrale ("storico", "straordinario", "incredibile") anche su cose ordinarie. Pochi dettagli concreti e vissuti: resta sul generale. Sapore di traduzione dall'inglese, poche sfumature locali.
- **2. Struttura e forma.** Prolisso: spiega più del necessario. Struttura scolastica "a pacchetto" (introduzione, sviluppo, conclusione), e ogni paragrafo che tira le somme. Elenchi puntati ovunque. Grassetto abusato. Punteggiatura anglosassone, su tutte la lineetta lunga.
- **3. Vocabolario e tic.** La regola del tre (aggettivi in triade: "affascinante, dinamico e innovativo"). Connettori formali ripetuti ("inoltre", "pertanto", "tuttavia", "di conseguenza"). Frasi fatte ("è importante notare che", "in conclusione"). La struttura "non è X, è Y" ("non è un software, è una rivoluzione").

### BLOCCO 9 — Due esempi a confronto (3 min)
> Mostrare il testo "AI" e accanto la versione umana, con gli indizi evidenziati. ⚠ Da preparare con gli indizi marcati.

**Esempio 1 · Comunicazione alle famiglie (settimana della lettura)**
- Versione AI: *"La lettura non è solo un'attività, è una vera e propria rivoluzione per la mente dei nostri studenti. In un mondo sempre più digitale, veloce e frenetico, dedicare tempo ai libri rappresenta un gesto straordinario e di enorme significato. È importante notare che leggere stimola l'immaginazione, arricchisce il vocabolario e rafforza l'empatia. Inoltre favorisce la concentrazione e, di conseguenza, il rendimento. Per questo promuoviamo un'iniziativa affascinante, dinamica e innovativa: la Settimana della Lettura. In sintesi, un'occasione imperdibile."* → tic: "non è X è Y", hype, triade, connettori, chiusura scolastica.
- Versione umana: *"Quest'anno dedichiamo una settimana alla lettura. Dal 10 al 14 marzo, in ogni classe, mezz'ora al giorno per leggere insieme: libri scelti dai ragazzi, ad alta voce o in silenzio. Leggere a quell'età aiuta a trovare le parole e a mettersi nei panni degli altri. Ma soprattutto è un piacere, e vorremmo che i ragazzi lo riscoprissero senza il peso del voto. Chi vuole, porti da casa un libro a cui tiene."*

**Esempio 2 · Paragrafo sull'IA a scuola**
- Versione AI: *"L'intelligenza artificiale non è semplicemente uno strumento, è un'opportunità senza precedenti per la didattica. Inoltre permette di personalizzare l'apprendimento in modo straordinario. Tuttavia è fondamentale ricordare che ogni tecnologia va usata con consapevolezza. In definitiva, l'AI può diventare un alleato prezioso, dinamico e versatile per ogni insegnante. In conclusione, il futuro della scuola passa anche da qui."* → tic: "non è X è Y", connettori, triade, hype, doppia chiusura.
- Versione umana: *"L'intelligenza artificiale può aiutare a insegnare: prepara esercizi diversi per chi va veloce e per chi ha bisogno di tempo, e fa risparmiare ore. Resta però uno strumento, e dipende da chi lo usa. Va guardato con occhio critico, soprattutto quando produce materiali per i ragazzi. Usata con la testa, toglie all'insegnante il lavoro ripetitivo e lascia quello che conta."*

### BLOCCO 10 — La provocazione finale (2 min)
- Volete scrivere meglio con l'IA? Usate questa guida al contrario. Incollatela nel prompt e chiedete all'IA di evitare tutti questi punti: niente hype, niente triadi automatiche, niente chiusure scolastiche, niente connettori superflui, niente lineette lunghe.
- È un altro accessorio del prompt, come il semaforo: una manciata di righe che alza di colpo la qualità del testo. I risultati sorprendono.
- *Transizione:* "Ora avete il metodo, le difese e perfino come far suonare umano un testo. Mettiamo tutto al lavoro sulla vostra lezione."

---

## PRATICA 2 — Costruiamo la lezione che state creando (~33 min)
> Il momento forte. Qui si chiude il cerchio: la lezione/attività progettata negli Incontri 2 e 3 ora diventa reale, con il prompt.

### Apertura (3 min)
- "Negli incontri scorsi avete progettato un'attività per i vostri ragazzi. Oggi la costruiamo davvero: scriviamo il prompt che genera i suoi materiali."
- Vale in ogni disciplina: chi insegna storia genera la verifica, chi insegna matematica la scheda di esercizi graduati, chi insegna lingue la traccia di produzione scritta. Stesso metodo.

### Costruzione (20 min)
Ognuno scrive il prompt completo per produrre il materiale della propria lezione, con le 5 fasi:
1. **Obiettivo:** che materiale voglio, in che formato, per quale momento della lezione.
2. **Contesto:** chi sono, che classe, che età, cosa sanno già.
3. **Esempi e materiali:** cosa allego come modello del "fatto bene".
4. **Valutazione:** le tre cose che controllerò prima di portarlo in classe.
5. **Iterazione:** la prima correzione che già immagino di dover chiedere.
- ⚠ Spunti pronti per chi non parte: la scheda dell'attività, la consegna per i ragazzi, una storia introduttiva, la griglia di osservazione, la comunicazione alle famiglie.

### Confronto a coppie (6 min)
- Ognuno legge il proprio prompt all'altro. Domanda guida: "Cosa hai messo nel contesto che io non avevo pensato?"

### Tocco strumento e condivisione (4 min)
- Un volontario manda il suo prompt in diretta, si guarda il risultato insieme. ⚠ Serve un dispositivo collegato.
- Condivisione (come domanda): **"Cosa è cambiato nel risultato grazie a una sola delle cinque fasi?"**

**Output:** ognuno esce con **un prompt strutturato pronto** e con il primo materiale vero della propria lezione sull'IA.

**Aggancio all'Incontro 5:** "Oggi un prompt alla volta. La prossima volta lo facciamo diventare un sistema: scegliere dove conviene davvero, e insegnare all'IA a ragionare come voi."

---

## Buchi di tempo e riserve
- **Parte A (la più ricca):** se gli esempi corrono, mostrarne 3 in aula e lasciare gli altri 2 come materiale. Se avanza tempo, far iterare un esempio dal vivo.
- **Pratica 1:** se la stanza è calda, allungare il giro di letture; se è fredda, mostrare il prompt-modello e farlo adattare.
- **Parte B:** è già minima. Se proprio stringe, il bias resta a una frase e si tiene solo il caso Amazon.
- **Pratica 2 (il cuore):** proteggere questo tempo. Se si va lunghi, tagliare prima il confronto a coppie, non la costruzione.

## Gap operativi da preparare prima dell'aula
- [ ] Le 5 coppie di esempi prompt (male/bene) stampate, con l'output reale a fianco per almeno 2
- [ ] I due esempi testo-AI / testo-umano con gli indizi evidenziati (Parte C)
- [ ] Un prompt-modello già costruito sulle 5 fasi, per sbloccare la stanza
- [ ] Gli spunti pronti per Pratica 1 e Pratica 2 (mail, consegna, scheda, griglia, storia, circolare)
- [ ] I dati chiave su slide con fonte (OpenAI 73%, caso Amazon 2018, AI Act Art. 14)
- [ ] Un dispositivo collegato per i due tocchi strumento

## Frasi chiave dell'incontro
> **Un buon prompt è dire bene quello che già sapete di volere. Il "fatto bene" è lungo solo perché è pensato. Il primo tentativo è una bozza: il valore sta nel ciclo. L'IA inventa con sicurezza quando non sa, e si porta dietro il passato: voi sapete riconoscerlo. E oggi la lezione che progettate da settimane diventa reale.**
