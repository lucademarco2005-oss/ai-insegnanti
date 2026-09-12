# Ricerca contenuti — Blocco 12h
> Sintesi verificata da 5 ricerche parallele. Fonti primarie linkate. Correzioni ai dati esistenti segnalate.

---

## A — INTRODUZIONE / PAURE

**Gap studenti/insegnanti (dato shock opener):**
- 81% studenti italiani usa IA (GoStudent 2025) vs solo 25% insegnanti
- 66% insegnanti italiani non si sente formato (76% nelle scuole statali)
- Solo 10% teme sostituzione completa — la paura reale è perdere rilevanza

**Studio MIT (da usare con cautela):**
- Titolo: *"Your Brain on ChatGPT: Accumulation of Cognitive Debt"* — MIT Media Lab, 2025
- Preprint arXiv:2506.08872 — NON ancora peer-reviewed
- Finding: chi usa ChatGPT mostra minore coinvolgimento cerebrale (EEG); concetto di "debito cognitivo"
- Limite: n=54 soggetti, piccolo. Usarlo come spunto, non come prova definitiva.

**Frame "superpotere, non sostituto":**
- Ethan Mollick, *Co-Intelligence* (Wharton/Penguin, 2024) — riferimento più citato e aggiornato
- Concetti chiave: "jagged frontier" (IA eccelle dove ti aspetti fallisca e viceversa), 7 ruoli dell'IA (tutor, coach, collega, strumento…)
- Force multiplier per chi la padroneggia

**Fatica cognitiva:**
- Gerlich (2025), MDPI Societies — correlazione negativa uso IA ↔ pensiero critico (r=−0.75 mediato da cognitive offloading)
- Sciencedirect 2025: la AI literacy attenua l'effetto negativo — chi capisce come funziona delega meno ciecamente
- Principio: IA passiva atrofizza, IA attiva (valutare output, iterare) mantiene il pensiero critico

---

## B — METODO / PRINCIPI

**"AI-first mindset":**
- Coniato da Sundar Pichai (Google I/O 2017): "from mobile-first to AI-first"
- Differenza: strumento supplementare ("AI-inside") vs processo ridisegnato attorno all'IA ("AI-first")
- HCAIF Framework (Newcastle Business School / AACSB 2025): 5 pilastri + insiste su attribuzione e riflessione metacognitiva

**"Ragionare come insegnante" → meta-prompting:**
- Framework accademico: AI-TPACK (Springer 2025) — il prompt engineering come esternalizzazione della conoscenza pedagogica tacita
- Meta-prompting (arXiv 2311.11482): insegnare all'IA COME strutturare il ragionamento, non cosa pensare
- Il system prompt = rubric cognitivo — chi lo costruisce bene trasferisce il proprio framework disciplinare

---

## C — TECNICHE / PROMPTING

**Framework più semplice per non tecnici:**
- RTF (Role-Task-Format) — il più adottato, risolve ~80% dei casi d'uso quotidiani
- Prompt strutturati preferiti dagli annotatori nell'73% dei casi vs non strutturati (OpenAI 2024)
- Iterativo vs one-shot: iterativo migliora qualità ~35%, accuratezza ~22%

**Role prompting:**
- Funziona CON persona dettagliate (generate anche dall'IA stessa)
- NON funziona con "sei un esperto di..." generici — beneficio minimo o negativo
- GPT-3.5 con role immersion a due stadi: +10pp accuratezza matematica

**Libreria di prompt:**
- Due modelli enterprise: SME (esperti redigono→testano→pubblicano) e collaborativo (peer review e rating)
- Componenti: metadata di contesto, standard tono/formato, log output per compliance

**Human in the Loop — EU AI Act:**
- Art. 14(1): sistemi ad alto rischio devono essere sorvegliati da persone fisiche
- Annex III — obbligatorio in: istruzione (valutazione studenti, ammissioni), lavoro (hiring, performance), sanità
- Valutazione studenti con IA = sistema ad alto rischio

**Semafori (Traffic Light Framework):**
- Framework codificato (FacingDisruption) — già in uso enterprise
- Verde: errori visibili e reversibili in <5 min, IA autonoma
- Giallo: revisione esperto obbligatoria, regola 80/20
- Rosso: decisioni irreversibili ad alto impatto — umano decide, IA prepara

---

## D — RISCHI / BIAS / ALLUCINAZIONI

**Bias — 4 casi reali documentati:**
1. Amazon 2018 — CV penalizzava donne (trained su 10 anni dati storicamente maschili)
2. iTutorGroup 2023 — primo settlement legale ($365k) per rifiuto automatico over-55
3. HireVue 2025 — analisi espressioni facciali: a sorda ha suggerito "pratica l'ascolto attivo"
4. Workday 2024-2025 — primo class action certificato per bias IA nelle assunzioni

**Tassi di allucinazione (orientativi, variano per task):**
- GPT-4o: ~1.5% (Vectara benchmark, sintesi documentale)
- Claude 3.7: ~4.4%
- Su domande fuori dominio: fino al 58-88% di risposte inventate
- Trend: sceso dal 21% (2021) a <5% per task standard (2025)
- Metafora per insegnanti: "studente brillante che, quando non sa, inventa con grande sicurezza"

**Tecniche per ridurre allucinazioni (con evidence):**
- RAG (fornire documenti su cui rispondere): riduzione fino al 96% in combinazione con guardrail
- Chain-of-Thought: "spiega ragionamento passo per passo prima di rispondere"
- Vincoli espliciti: "rispondi solo su questo testo; se non trovi, dì non lo so"
- Formati strutturati con livelli di confidenza: Risposta | Evidenza | Certezza (alta/media/bassa)

**GDPR — cosa NON caricare (insegnanti italiani):**
- PEI, certificazioni DSA, dati sanitari studenti
- Elaborati con nome/cognome di minorenni
- Verbali disciplinari, segnalazioni servizi sociali
- Base legale: GDPR Art. 9 (categorie speciali), Art. 28 (DPA), AI Act Annex III punto 3
- Il Dirigente Scolastico è Titolare del Trattamento → risponde legalmente delle violazioni docenti
- Riferimento normativo italiano: DM 166/2025 (linee guida MIM sull'IA a scuola)

---

## E — FUTURO

**WEF Future of Jobs 2025 (dati verificati):**
- 170M ruoli creati vs 92M distrutti → +78M netti entro il 2030
- 39% competenze chiave cambierà (in calo dal 44% del 2023 — transizione in corso)
- 77% datori lavoro prevede upskilling; 63% cita gap competenze come barriera
- Top skills crescenti: IA & big data, pensiero critico, resilienza, curiosità/apprendimento continuo

**GenAI Wall:**
- Fonte accademica: HBS Working Paper 26-011 (settembre 2025) — definizione: soglia dove IA non colma gap di expertise
- Uso divulgativo (Fortune, maggio 2026): task entry-level automatizzati → pipeline formazione junior rotta
- Dati junior verificati: Oliver Wyman Forum CEO Survey 2026 — 43% dei CEO taglierà ruoli junior entro 1-2 anni (era 17% l'anno prima)
- Harvard/SSRN 2025: nelle aziende che adottano GenAI, impiego junior −7/12% in 6 trimestri; senior continua a crescere
- Il dato 39%/43% da "BSI 2025" nel tuo materiale originale: fonte verificata è Oliver Wyman Forum 2026

**Dati studenti italiani (verificati):**
- GoStudent 2025: 81% studenti italiani usa IA; 28% la impara a scuola
- HEPI 2025 (UK): 92% studenti universitari usa IA, 88% per valutazioni → la fonte "Cornell 2024" nel tuo materiale non è verificata
- INDIRE 2025: 52.4% insegnanti italiani usa IA per la didattica; sperimentazione ministeriale in 15 istituti

**McKinsey — CORREZIONE DATI:**
- I dati che avevi (-30% manuali, -20% nozioni base) NON corrispondono alle fonti primarie McKinsey
- Dati reali MGI 2024: −27% ore lavorative europee automatizzabili entro 2030; basic cognitive −14%; social & emotional +11%
- Usa il WEF 2025 come fonte principale — è più recente e verificato

**Errore reversibile vs irreversibile:**
- Framework Bezos (2015): Type 1 (irreversibile, one-way door) vs Type 2 (reversibile, two-way door) — largamente applicato all'AI deployment
- EDPS TechDispatch settembre 2025: reversibilità come criterio primario per il livello di supervisione umana
- ArXiv 2025 (2605.01415): formalizzazione accademica dell'"energy of irreversibility" come misura del rischio AI

---

## Formula IPU — analogie accademiche
- Rogers' Diffusion of Innovation: Knowledge → Trial → Adoption (1962/2003) — sovrapposizione quasi perfetta
- TAM (Davis 1986): perceived usefulness + ease of use → ancora il riferimento teorico base
- FAIGMOE (arXiv 2025): Strategic Assessment → Planning → Implementation → Operationalization

---

# Impatti dell'IA sul mondo (per Incontro 3)
> Ricerca verificata. Regola: sulle slide solo i dati SOLIDI; quelli "virali ma incerti" si tengono fuori o si segnalano.

## A — Impatto ambientale (data center)
Dati solidi (di sistema):
- Data center oggi (2024): ~415 TWh, circa 1,5% dell'elettricità mondiale. Crescita ~12% l'anno (IEA, Energy and AI, 2025).
- Proiezione 2030: ~945 TWh (raddoppio), circa 3% dell'elettricità globale, poco più di quanto consuma oggi tutto il Giappone (IEA 2025).
- Entro il 2030 negli USA i data center consumeranno più elettricità della produzione di alluminio, acciaio, cemento e prodotti chimici messi insieme (IEA 2025).
- Acqua: Google nel 2024 ha usato ~30 miliardi di litri d'acqua per data center e uffici, quasi raddoppiati in 3 anni (Google Environmental Report 2025).

Dati virali ma INCERTI (fuori dalle slide o da segnalare):
- "Una query IA = mezzo litro d'acqua" (Li et al. 2023): stima non confermata, solo ordine di grandezza.
- "Una query IA consuma 10 volte una ricerca Google": dato 2023 oggi contestato (le stime variano di 10-100 volte).
- CO2 di GPT-4: solo congetture, OpenAI non ha pubblicato i dati. (Solido invece: GPT-3 circa 552 t CO2 per l'addestramento, Patterson 2021.)

Il punto per il corso: l'impatto reale e documentato è quello AGGREGATO (i data center come un intero Paese), non quello della singola query. Il costo è nascosto: l'utente non lo vede.

## B — Ecosistema dell'informazione (il paradosso dei giornalisti)
Dati solidi:
- Zero-click: con il riassunto IA gli utenti cliccano un risultato solo nell'8% dei casi (contro il 15% senza); i link dentro il riassunto: 1% (Pew Research, luglio 2025).
- Col riassunto IA, il 26% chiude la ricerca senza aprire nessun sito (contro 16% senza) (Pew 2025).
- Traffico di ricerca Google verso gli editori: circa -33% globale (-38% USA) nell'anno fino a nov. 2025, su 2.500+ siti (Reuters Institute / Chartbeat, Trends 2026).
- New York Times contro OpenAI/Microsoft: causa dal dic. 2023, nel 2025 il giudice respinge l'archiviazione; NYT ha speso 10,8 mln $ in contenzioso IA nel 2024.
- Accordi di licenza (la via opposta): News Corp, Axel Springer, Condé Nast, Financial Times, Dotdash Meredith firmano con OpenAI/Google (cifre esatte riservate).
- "Model collapse" (Nature, 2024): addestrare l'IA in modo ricorsivo su contenuti generati da IA porta a degrado irreversibile. Meno fonti umane finanziate = più rischio.

Il paradosso: i giornalisti producono le informazioni su cui l'IA è addestrata e che l'IA rivende come risposte, ma non ricevono più i clic, quindi i ricavi. Se crolla chi finanzia l'informazione di qualità, crolla anche la materia prima dell'IA.

Angolo educativo: in un mondo dove l'IA "risponde e basta", la catena fonte-verifica-attribuzione diventa invisibile. Insegnare da dove vengono le informazioni, a risalire alla fonte e a distinguere contenuto finanziato e verificato da contenuto generato è una competenza civica di base.

## C — Disinformazione e deepfake
Dati solidi:
- Crescita: incidenti deepfake +10 volte dal 2022 al 2023, poi +4 volte dal 2023 al 2024. Nel 2024 i deepfake sono il 7% di tutti i tentativi di frode (Sumsub 2024).
- Caso simbolo: truffa del "finto CFO" ad Arup, Hong Kong (feb 2024): un dipendente bonifica 25,6 milioni di dollari dopo una videocall con deepfake del capo e dei colleghi.
- Voce clonata: bastano circa 3 secondi di audio per un clone vocale convincente (truffa del finto parente in emergenza). Difesa FTC: riattaccare, richiamare il numero noto, parola d'ordine di famiglia.
- In Italia: la Banca d'Italia ha denunciato video falsi col volto del Governatore per promuovere finti investimenti.
- Non si riconoscono a occhio: solo lo 0,1% delle persone distingue correttamente tutti i contenuti reali e falsi; oltre il 60% resta sicuro pur sbagliando (iProov 2025). Le voci false si smascherano solo nel 73% dei casi (UCL/PLOS One 2023).
- "Liar's dividend" (Chesney e Citron, 2019): in un mondo pieno di falsi, anche il vero può essere liquidato come "deepfake". Più cresce la consapevolezza dei falsi, più forte diventa questo effetto.

Dato scuola (solido e rilevante):
- Segnalazioni NCMEC di materiale pedopornografico generato con IA: da 4.700 (2023) a 67.000 (2024), a 440.000 nei soli primi 6 mesi 2025.
- Caso Lancaster Country Day School (Pennsylvania, 2024): due studenti hanno creato 347 immagini/video falsi di 59 compagne minorenni. Studenti hanno preso di mira compagne con deepfake sessuali in almeno 28 Paesi dal 2023.
- Inquadrarlo come reato (revenge porn, tutela del minore), non come "scherzo".

Angolo educativo: l'addestramento a "riconoscere il falso" migliora di pochissimo. La difesa non è visiva, è comportamentale: verificare la fonte, usare un canale alternativo, non condividere, dubitare prima di reagire emotivamente (UNESCO, Deepfakes and the crisis of knowing).

Dati da maneggiare con cautela: cifre tipo "+3.000% frode deepfake" o "+704% face-swap" (fonti commerciali): solo ordine di grandezza.

## D — Su cosa è addestrata l'IA: il caso Anthropic (libri piratati)
Lega il paradosso "chi paga chi crea" ai libri e agli autori. Dati confermati:
- Causa Bartz contro Anthropic (2024, California): tre autori, poi class action, accusano Anthropic di aver addestrato Claude scaricando milioni di libri da librerie pirata (LibGen, PiLiMi). Oltre 7 milioni di libri scaricati illegalmente.
- Sentenza del giudice Alsup (giugno 2025), la distinzione chiave: addestrare l'IA sui libri è "fair use" (lecito e trasformativo) e digitalizzare libri comprati legalmente è lecito, MA scaricare e conservare copie piratate NON è lecito. Il principio: conta COME ottieni l'opera. Comprarla e usarla sì, piratarla no.
- L'accordo (settembre 2025): 1,5 miliardi di dollari, circa 500.000 opere coperte, circa 3.000 dollari a libro. È il più grande recupero sul copyright della storia USA. Anthropic dovrà distruggere i file piratati.
- In evoluzione: approvazione finale del settlement attesa ad aprile 2026.
- Cause simili: Meta (causa Kadrey, libri da LibGen per Llama) e OpenAI affrontano contenziosi analoghi.

Perché è rilevante per la scuola: addestrare l'IA sul lavoro creativo altrui senza permesso e da fonti illegali può costare miliardi. Insegna due cose agli studenti: il lavoro creativo ha un valore e va rispettato; e il modo in cui ottieni un contenuto (lecito o pirata) conta, sempre, anche per loro.
