# Piano di lavoro · I 6 percorsi nuovi da 10 ore

> Proposta di impianto per i 6 percorsi entrati: 2 Segreteria e 4 scuola a gruppi misti.
> Scritto il 24 agosto 2026. Nessuna scaletta e nessuna slide si tocca prima dell'ok di Luca.
> Standard di riferimento: `00_Standard/MODUS_OPERANDI.md`. Metodo di adattamento: `01_Progetto/PIANO_SECONDARIA_SEGRETERIA.md`.

---

## PARTE 0 · Il fatto che cambia il conto del lavoro

Ho contato le occorrenze di "Claude" dentro i deck del blocco comune, su Secondaria e su Segreteria:

| Deck | Occorrenze di "Claude" |
|---|---|
| Incontro 1 | 0 |
| Incontro 2 | 0 |
| Incontro 3 | 1 (citazione di passaggio) |
| Incontro 4 | 0 |
| Incontro 5 | 0 |
| Incontro 10 | 1 o 2 (citazione di passaggio) |

**Le 12 ore comuni sono già indipendenti dallo strumento.** La slide 17 dell'Incontro 5 dice già, testualmente: *"Vale su Progetti, GPT personalizzati, Gemini Gems"*.

Conseguenza operativa: il passaggio da Claude a Gemini **non è una riscrittura del corso**. Tocca solo i 4 moduli pratici e due slide del comune. Il lavoro vero sui percorsi da 10 ore è un lavoro di **compressione**, non di conversione.

---

## PARTE 1 · Cosa sono davvero i 6 percorsi

Sei corsi, ma **due prodotti**:

| Prodotto | Edizioni | Pubblico | Sorgente da cui si costruisce |
|---|---|---|---|
| **A · Scuola 10h** | 4 | gruppi misti: medie, superiori, e primaria se presente | Secondaria (che ha già medie e superiori appaiate) più gli esempi della Primaria |
| **B · Segreteria 10h** | 2 | personale ATA e di segreteria | Segreteria_ATA (comune già costruito) |

Si costruiscono **due percorsi**, si erogano sei volte. Questo va detto subito perché cambia la stima: non sono 60 ore di materiale nuovo, sono 20.

Cartelle proposte:

```
02_Percorsi/10h/Scuola_10h/
02_Percorsi/10h/Segreteria_10h/
01_Progetto/Programmi/10h/
01_Progetto/Programmi/20h/
```

Stesso schema interno dei percorsi da 20 ore, `01_Modulo_1` fino a `10_Modulo_10`, più `_Consegna/`.

**File separati, non un deck unico con le slide nascoste.** Tentazione: una sola sorgente per 20h e 10h, con le slide tagliate marcate da una classe CSS. Si scarta: la numerazione di pagina salta, l'export PDF diventa condizionale, e comunque i deck divergono perché gli esempi del misto sono diversi. Meglio due file, con il costo di manutenzione doppio messo in conto.

---

## PARTE 2 · La struttura: 10 moduli da 60 minuti

**Il modulo da 60 minuti è l'unità atomica.** Non si tocca il numero dei moduli, non si toccano gli argomenti, non si tocca l'ordine. Si dimezza la durata di ciascuno.

Questo tiene in piedi tre cose insieme: il programma ufficiale resta leggibile come quello da 20 ore, i deck si derivano per taglio e non per riscrittura, e la calendarizzazione resta libera.

**La calendarizzazione è una scelta della scuola, non nostra:**

- **5 incontri da 2 ore** (2 moduli per incontro): raccomandato. Meno overhead di connessione, il ritmo gancio, dibattito, pratica respira meglio, e la logistica presenze resta identica a quella dei corsi da 20 ore.
- **10 incontri da 1 ora**: possibile, ma su 10 collegamenti si perdono circa 100 minuti tra ingressi e saluti, cioè un modulo intero su dieci.

Il materiale è lo stesso nei due casi. Nel programma ufficiale si scrive "10 moduli da 1 ora, aggregabili in 5 incontri da 2 ore", come già si fa oggi con la frase "riadattabili a orari diversi".

### Il template dei tempi, uguale per tutti i moduli

| Tipo di modulo | Esposizione | Laboratorio o dibattito | Chiusura | Slide massime |
|---|---|---|---|---|
| Teorico (moduli 1-5 e 10) | 27 min | 28 min | 5 min | **20** |
| Pratico (moduli 6-9) | 18 min | 37 min | 5 min | **13** |

### Il vincolo del bando regge

Laboratori hands-on maggiori o uguali al 50% (PNRR DM 219/2025). Con questo template:

- 6 moduli teorici × 28 min = 168 min
- 4 moduli pratici × 37 min = 148 min
- **Totale 316 minuti su 600 = 52,7%**

Il margine c'è ma è sottile: **ogni modulo deve avere il suo laboratorio**, non si può sacrificare il dibattito di un modulo teorico per finire la teoria. Va scritto nella scaletta come vincolo, non come indicazione.

---

## PARTE 3 · Claude diventa Gemini: cosa resta, cosa cade

### La mappatura, funzione per funzione

| Nel percorso 20h (Claude) | In Gemini | Verdetto per le 10h |
|---|---|---|
| **Progetto** (memoria e istruzioni permanenti) | **Gem** (istruzioni più file di conoscenza) | **Esce dalle slide teoriche.** Il concetto viaggia sul file di contesto permanente, la Gem si costruisce con le mani nel modulo 7. Vedi il nodo qui sotto |
| **File di contesto permanente** | identico, è un testo che si incolla | **Resta invariato.** È l'asset più tool-agnostic che abbiamo, funziona ovunque |
| **Skill richiamate con "/"** | non esiste | **Cade.** Il Prompt Optimizer diventa una **Gem "scrittore di prompt"**, il testo in `Asset_Skill_Prompt_Optimizer.md` si riusa quasi verbatim come istruzioni della Gem |
| **Automazioni e Schedule** | azioni pianificate, dipendono dal piano ⚠ | **Fuori dalle 10 ore.** Si cita in 1 minuto, non si prova |
| **Live Artifact e app interattive** | **Canvas** (documenti, infografiche, pagine) | **Resta in forma ridotta.** Un solo esempio, dentro il modulo 6. Il pianificatore dell'anno e il cruscotto delle scadenze cadono |
| **Cowork dal computer** | non esiste | **Cade del tutto** |

### Il nodo Progetto: dove sono le citazioni e cosa se ne fa

Le citazioni del Progetto come funzione dello strumento ci sono, e sono concentrate. Le ho contate una per una sui deck della Secondaria (identiche su quelli della Segreteria):

| Deck | Slide che citano il Progetto come funzione | Uso generico della parola, nessun intervento |
|---|---|---|
| **I5** | 12, 14, 15, 16, 17, 18, 20, 26, 28, 38 | 10, 29, 36 ("il vostro primo progetto", "progettare") |
| **I10** | 11, 12, 14 | nessuna |
| **I4** | 44 (il ponte verso I5) | 18, 41 (il verbo progettare) |
| **I2** | nessuna | 23, 40 (il verbo progettare) |

Un fatto da mettere agli atti prima di decidere: **Gemini una cosa equivalente ce l'ha, si chiama Gem** (istruzioni salvate più file di conoscenza). Quindi la strada non è obbligata. Ma la tua indicazione resta quella giusta, e per una ragione che va oltre il nome dello strumento.

**Oggi l'Incontro 5 insegna lo stesso movimento due volte.** Prima con il Progetto (slide 14 fino a 20: la prima chat, il prompt di inizio, il Progetto compilato), poi con il file di contesto permanente (slide 26 fino a 33: il prompt che vi intervista, il file compilato). Due tutorial, due prompt da copiare, due esempi compilati, per dire la stessa cosa: il contesto che non cambia si scrive una volta sola.

In due ore ci stanno tutti e due, e uno rinforza l'altro. **In un'ora se ne insegna uno solo, e quello giusto è il file**, per tre motivi:

1. È indipendente dallo strumento. Un testo che si incolla funziona in Gemini, in Claude, in ChatGPT e in quello che uscirà a dicembre. Il Progetto e la Gem no.
2. Non dipende dal piano dell'account. Se sull'account della scuola le Gem non sono attive, il file funziona lo stesso.
3. È già scritto e già pronto: `PROMPT_FILE_CONTESTO_PERMANENTE.md` esiste in tutti i percorsi e non va toccato.

**La decisione operativa, quindi:**

- **Cadono** le slide 15, 17, 18, 20 e 38 dell'I5, cioè tutto il secondo tutorial. Sono 5 slide recuperate proprio nel deck che si tagliava peggio.
- **Si riscrivono** la 16 (i tre blocchi dati, istruzioni ed esempi restano, perdono la cornice "dentro il Progetto" e diventano "cosa mettete nel contesto permanente") e la 26 (perde il confronto "il Progetto si rifà ogni volta, il file una volta sola", che senza il Progetto non ha più senso).
- **Resta una sola slide nuova**, corta, alla fine del blocco: dove vive il contesto permanente. In una Gem se l'account ce l'ha, altrimenti lo si incolla all'inizio della chat. Trenta secondi, non un tutorial.
- **La pratica dell'I5 passa da due tempi a uno.** Oggi è "prima il vostro file, poi il vostro primo Progetto". Nelle 10 ore si scrive solo il file. La Gem si costruisce nel modulo 7, con le mani sulla tastiera invece che su carta.
- **I10**: la slide 11 perde l'ultima riga, le slide 12 e 13 si fondono in una sola sul contesto permanente, la 14 va riscritta comunque perché elenca Claude, skill, routine e live artifact.
- **I4 slide 44**: è il ponte verso I5 e cita il Progetto. Cade già con il taglio, nessun lavoro in più.

Risultato: l'Incontro 5 scende a **18 slide invece di 21**, e diventa il modulo che respira meglio invece del più stretto. Il metodo non perde niente: IPU resta intera, il contesto permanente resta, ragionare come me resta.

### Cosa ci guadagniamo passando a Gemini

Non è solo una perdita, e conviene raccontarlo così anche alle scuole:

- **Account istituzionale.** Se l'istituto è su Google Workspace, i docenti hanno già l'accesso. Niente registrazioni, niente carte di credito, niente limiti di età, dati dentro il perimetro della scuola. Nei corsi da 20 ore la creazione degli account è sempre il primo attrito dell'aula: qui sparisce.
- **NotebookLM è di casa.** Stesso account, stesso Drive, zero attrito nel modulo 8.
- **Risolve due rischi tecnici già segnalati** nel piano Segreteria: Claude in Excel (dipendeva da un componente aggiuntivo mai verificato) diventa il file caricato dentro Gemini oppure Gemini dentro Fogli; Granola (terza parte americana, nodo consenso sulle registrazioni) diventa la presa appunti di Gemini dentro Meet, cioè dentro gli strumenti che la scuola già usa.

### ⚠ Verifiche bloccanti prima di promettere la pratica

1. **Edizione Workspace dell'istituto**: Gemini e NotebookLM sono attivi per il personale? Su quale piano?
2. **Gem**: disponibili sull'account scolastico, e con quanti file di conoscenza?
3. **Presa appunti di Gemini in Meet** (solo prodotto B): attiva? Su quale edizione?
4. **NotebookLM su PDF scansionati senza testo** (solo prodotto B): è il formato normale dell'archivio di segreteria, e resta il rischio già segnalato ad agosto.

Se una di queste cade, il piano B è sempre lo stesso: si lavora sul file caricato dentro la chat. Meno elegante, stesso risultato didattico.

---

## PARTE 4 · Come si dimezza un modulo teorico

### La regola di taglio, in cinque righe

1. **Si tiene la spina dorsale intera**: un gancio viola, il concetto, uno statement, il dibattito. Il ritmo non si tocca.
2. **Gli esempi passano da cinque a due**, uno per ordine di scuola.
3. **I blocchi "l'IA nel mondo"** (ambiente, zero-click, model collapse, deepfake, uso emotivo) passano da 9 slide a 3 o 4. Restano come argomento, perdono la profondità.
4. **Cadono gli statement doppi**, cioè quando due slide navy dicono la stessa cosa con parole diverse. Ne resta una.
5. **I dibattiti passano da tre domande a una**, la più tagliata sul loro lavoro. Le altre due finiscono nelle riserve della scaletta.

Non cade nessun argomento. Cade la profondità degli esempi e la lunghezza del confronto.

### Il conto, deck per deck

Base: i deck della Secondaria. Le liste sono una proposta da validare slide per slide, come sempre.

| Deck | Oggi | Nelle 10h | Slide che restano |
|---|---|---|---|
| **I1** Cos'è l'IA | 31 | **20** | 1, 2, 4, 5, 7, 8, 9, 10, 11, 12, 13, 16, 17, 18, 19, 20, 24, 26, 29, 31 |
| **I2** I 4 principi | 43 | **21** | 1, 3, 4, 7, 10, 12, 16, 17, 19, 22, 23, 25, 27, 28, 33, 35, 38, 39, 40, 41, 43 |
| **I3** Etica | 37 | **20** | 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 19, 23, 24, 27, 29, 31, 34, 35, 37 |
| **I4** Il prompt | 45 | **21** | 1, 4, 5, 7, 8, 9, 10, 11, 12, 15, 16, 21, 22, 24, 25, 29, 30, 37, 41, 42, 45 |
| **I5** Dal prompt al sistema | 40 | **18** | 1, 4, 5, 6, 10, 11, 16\*, 22, 24, 25, 26\*, 29, 30, 31, 33, 35, 37, 40, più 1 slide nuova (dove vive il contesto permanente). Le slide con \* si riscrivono |
| **I10** Futuro e chiusura | 35 | **20** | 1, 2, poi 4 slide di ripasso **nuove** che sostituiscono le 3-14, poi 15, 16, 17, 19, 20, 21, 22, 25, 26, 27, 29, 32, 33, 35 |

Totale blocco comune: da 231 slide a 120, cioè meno 48%.

### Cosa cade davvero, e dove finisce

- **I1**: cade il blocco "ribalta lo strumento" (slide 21, 22, 23). Non si butta: diventa un hands-on dentro il modulo pratico 6, dove è più utile.
- **I2**: il blocco sull'uso emotivo dell'IA da parte degli adolescenti passa da 9 slide a 4 (gancio, dato, statement, dibattito). Le tre domande per principio diventano una sola, quella sul contesto.
- **I3**: il blocco "l'IA nel mondo" passa da 13 slide a 5. Cade il caso Anthropic con il suo dibattito. I 7 spunti di attività per medie e superiori diventano 3, gli altri 4 vanno nella consegna come materiale scritto.
- **I4**: i 5 esempi "fatto male, fatto bene" diventano 2. Cadono i due esercizi su carta accorpati in uno solo. Le tecniche avanzate (fatevi intervistare dall'IA, few-shot, prima il ragionamento) escono dal deck teorico ed entrano nel modulo pratico 6, dove si provano invece di ascoltarle.
- **I5**: le 4 slide di IDENTIFICA diventano 1, e cade tutto il blocco Progetto (vedi il nodo nella Parte 3). Era il deck che si tagliava peggio, con questa scelta diventa il più comodo.
- **I10**: è l'unico deck che richiede **slide nuove**, non solo tagli. Le 13 slide di ripasso vanno accorpate in 4, una per coppia di incontri.

### Nota di produzione

Ogni slide porta il numero di pagina scritto a mano nel formato `5 / 31`. Tagliando, tutti i numeri vanno rifatti. È un lavoro meccanico e va fatto con uno script sul file HTML, non a mano, altrimenti si sbaglia di sicuro. Lo stesso script serve 10 volte per percorso.

---

## PARTE 5 · Il blocco pratico ridisegnato

Quattro moduli da 60 minuti, 18 minuti di guida e 37 di mani sulla tastiera.

**Il filo conduttore diventa il kit personale.** Nei percorsi da 20 ore il filo era un Progetto demo (Geografia, Autunno, Storia) costruito dal formatore. In 4 ore non c'è tempo per costruire il caso del formatore e poi anche il proprio. Si ribalta: **ogni modulo produce un pezzo del kit del partecipante**, e alla fine il kit è completo.

| Modulo | Prodotto A · Scuola | Cosa esce dalle mani del partecipante |
|---|---|---|
| **6** | **Gemini: la base fatta bene.** La schermata, i file caricati, la chat come luogo di lavoro, le 5 fasi applicate a un compito vero, Canvas per il documento. Qui rientrano le tecniche uscite da I4 | il primo materiale vero, fatto bene |
| **7** | **La Gem: l'assistente che vi conosce.** Si prende il file di contesto permanente scritto nel modulo 5 e si costruisce la Gem. Due esempi appaiati: assistente di classe (primaria) e assistente di materia (medie e superiori). Più la Gem "tutor socratico" da dare agli studenti, che copre l'argomento del programma | la propria Gem funzionante |
| **8** | **NotebookLM: le vostre fonti.** Solo le fonti, cita il punto, niente invenzioni. Le tre colonne, poi lo Studio: mappa, quiz, audio di ripasso | il proprio notebook con i propri materiali |
| **9** | **Canva e montaggio finale.** Due esempi (presentazione e scheda), poi il ponte: è la Gem che scrive il prompt per Canva. Ultimi 20 minuti, si monta il pezzo finale | la lezione o l'unità completa |

Cade rispetto alle 20 ore: il gioco interattivo con Canva Code (bello ma lungo), il laboratorio finale da 85 minuti, il tour delle funzioni avanzate. Il gioco resta nella consegna come tutorial scritto.

| Modulo | Prodotto B · Segreteria | Cosa esce dalle mani del partecipante |
|---|---|---|
| **6** | **Gemini: circolari, verbali, risposte alle famiglie.** La base più le 5 fasi su un documento vero d'ufficio | una circolare vera, scritta bene |
| **7** | **La Gem "Segreteria".** Istruzioni, modulistica, tono istituzionale. Si riusa direttamente il materiale di `Progetto_Demo_Mail` come conoscenza della Gem | la Gem dell'ufficio |
| **8** | **I dati: Gemini sui fogli.** Il file caricato in chat, oppure Gemini dentro Fogli se l'edizione lo consente. Pulire, organizzare, estrarre tendenze | il proprio foglio, letto e sintetizzato |
| **9** | **NotebookLM sull'archivio, più il laboratorio finale.** Ricerca semantica sulle circolari, riassunto di una normativa lunga. Negli ultimi 15 minuti il flusso completo: dagli appunti di una riunione al verbale | l'archivio interrogabile |

**[decisione]** Nel prodotto B, Canva resta fuori. Per la segreteria vale meno di dati e archivio, e nei 60 minuti del modulo 9 non ci sta insieme a NotebookLM. Alternativa se lo si vuole tenere: si sacrifica la ricerca semantica e il modulo 9 diventa "dal verbale alla locandina".

---

## PARTE 6 · Il problema vero del prodotto A: la stanza mista

In aula ci saranno insieme docenti di ordini diversi. Un esempio tarato sulla terza media annoia il superiore e spaventa il maestro. Cinque contromisure concrete, tutte già usate nel materiale esistente:

1. **Esempi a binari appaiati.** Il deck della Secondaria lo fa già: gli esempi di I4 sono etichettati "medie", "superiori", "trasversale". Nel misto ogni slide di esempio porta due colonne con l'etichetta dell'ordine, e chi espone legge quella della propria stanza. Se la primaria è nel gruppo, il terzo binario si aggiunge solo sugli esempi, non su tutto il deck.
2. **Gli esercizi sono sempre "sul vostro caso".** Un esercizio formulato come "prendete un compito che date spesso" si adatta da solo. Tutti i laboratori del corso sono già scritti così: questa è la ragione per cui il misto è possibile.
3. **Gruppi omogenei nell'hands-on.** Nei 37 minuti pratici si dividono per ordine di scuola, in stanze separate se la piattaforma lo permette, altrimenti per tavoli. La plenaria è mista, la pratica no.
4. **"Lo useresti?" con due mazzi.** L'esercizio del modulo 3 richiede output pre-preparati: se ne preparano due serie, primaria e secondaria, e ogni gruppo prende la sua.
5. **Vocabolario neutro e coerente.** "I vostri studenti" funziona dai 6 ai 19 anni. "Alunni", "ragazzi", "bambini" no: si sceglie una parola sola e si tiene per tutto il percorso.

**[decisione 1] La primaria è dentro o fuori?** Cambia il lavoro sugli esempi: dentro significa un terzo binario su circa 15 slide dei 6 deck comuni più il modulo 7. Fuori significa partire dalla Secondaria e non toccare quasi nulla. Fino a risposta contraria costruisco per il caso più largo, cioè primaria compresa, perché è quello che non si può recuperare a posteriori.

---

## PARTE 7 · Cosa si perde, detto onestamente

Serve saperlo prima, perché è quello che si racconterà alla scuola e ai formatori.

**Non si perde:** nessun argomento. Tutti e 10 i moduli restano, il metodo resta intero (5 fasi, IPU, contesto permanente, Gem), l'etica resta, il futuro resta, il rapporto teoria e pratica resta 60 e 40 come nelle 20 ore.

**Si perde:**

1. **La profondità del confronto.** Da 60 o 70 minuti di dibattito a 28. Da tre domande a una. È la perdita più grossa, perché il dibattito è il pezzo in cui gli insegnanti si riconoscono.
2. **L'uso avanzato dello strumento.** Chi esce dalle 10 ore sa usare bene l'IA di base e ha la sua Gem. Non sa costruire un sistema. È esattamente la differenza tra i due prodotti, e va scritta nel programma senza girarci intorno.
3. **Il laboratorio lungo.** Gli 85 minuti in cui si costruiva una lezione intera dall'idea alla presentazione non ci sono. Li sostituisce il kit costruito a pezzi, un pezzo per modulo.
4. **Il margine di recupero.** In un modulo da 2 ore un blocco che sfora si riassorbe. In uno da 60 minuti no.

Da cui una regola nuova per le scalette da 10 ore: **ogni scaletta porta i checkpoint temporali e una colonna "se sei in ritardo, salta questo"**. Nei percorsi da 20 ore bastavano le riserve per i buchi di tempo. Qui serve l'opposto: cosa si taglia in diretta.

E un accorgimento di erogazione: **il collegamento e l'accesso all'account non possono mangiare il modulo 6.** Si manda 3 giorni prima una mail con le istruzioni di accesso a Gemini con l'account della scuola, e chi conduce entra 10 minuti prima per chi ha problemi.

---

## PARTE 8 · Piano di lavoro e stima

### Cosa si riusa, cosa si taglia, cosa si scrive

| Pezzo | Prodotto A · Scuola | Prodotto B · Segreteria |
|---|---|---|
| 6 deck comuni | taglio dai deck Secondaria, più il binario primaria sugli esempi | **taglio puro** dai deck Segreteria già costruiti |
| Modulo 6 pratico | nuovo, ma corto e derivato dal deck Claude | adattamento di `Pratica_Segreteria_1_Claude` |
| Modulo 7 pratico | nuovo (la Gem), il più corto di tutti | nuovo, riusa `Progetto_Demo_Mail` |
| Modulo 8 pratico | taglio dal deck NotebookLM (già 10 slide) | nuovo (dati e fogli) |
| Modulo 9 pratico | taglio dai deck Canva e Laboratorio | nuovo (archivio più verbale) |
| Programma ufficiale | copia e adatta dal PROGRAMMA Secondaria | copia e adatta dal PROGRAMMA ATA |

### Ordine di lavorazione proposto

1. **Le 4 verifiche ⚠ sugli account Google.** Bloccanti: senza risposta non si scrive un hands-on. Mezza giornata.
2. **Le decisioni marcate [decisione]**, in particolare la primaria dentro o fuori.
3. **Prodotto A, blocco comune**: 6 deck. Vale per 4 corsi su 6, quindi si fa per primo.
4. **Prodotto A, blocco pratico**: 4 moduli.
5. **Prodotto B, blocco comune**: 6 deck, taglio puro.
6. **Prodotto B, blocco pratico**: 4 moduli, è la parte con più materiale nuovo.
7. **Programmi ufficiali, scalette formatori, PDF, consegna.**

### Stima

| Fase | Giornate |
|---|---|
| Verifiche e decisioni | 0,5 |
| A, comune (6 deck: taglio, esempi, rinumerazione) | 3 |
| A, pratico (2 tagli e 2 nuovi) | 3 |
| B, comune (6 deck, taglio puro) | 2 |
| B, pratico (1 adattamento e 3 nuovi) | 3,5 |
| Programmi, scalette formatori, PDF, consegna | 2 |
| **Totale** | **circa 14 giornate** |

Punto di controllo di Luca dopo ogni deck, nel formato di sempre: `slide N: vecchio, nuovo`.

---

## PARTE 9 · Le decisioni che servono da Luca

1. **La primaria è nella stanza dei 4 corsi misti, sì o no?** Cambia il lavoro sugli esempi.
2. **Calendarizzazione**: 5 incontri da 2 ore (raccomandato) oppure 10 da 1 ora? Il materiale è lo stesso, cambia il programma ufficiale e la logistica presenze.
3. **Gemini è una richiesta della scuola o una nostra scelta?** Se è vincolo dell'istituto, va scritto nel programma. Se è nostra scelta, si può tenere Claude nei moduli in cui è meglio e usare Gemini dove l'account istituzionale conta.
4. **Prodotto B, modulo 9**: NotebookLM più verbale (proposto) oppure verbale più Canva?
5. **Le 4 edizioni del prodotto A sono davvero identiche**, o due sono più sbilanciate su un ordine di scuola? Se lo sono, conviene saperlo prima e preparare due mazzi di esempi invece di uno.
