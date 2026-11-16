# -*- coding: utf-8 -*-
from common import *

d = deck(5, """  SLIDE 1-4 = apertura: due tipi di lezione. SLIDE 5-11 = lo stampo 1, le 4 mosse (una slide per mossa, la ricerca, la variante da un'ora).
  SLIDE 12-18 = lo stampo 2, il blocco a domande (i quattro colori, tensione prima del dato, calare nella scuola, i dati).
  SLIDE 19-20 = esercizio e dibattito. SLIDE 21-23 = sotto il cofano, ponte, chiusura.""")

d.cover(eyebrow(5), "Costruire|la lezione", "Modulo 5 · le 4 mosse per uno strumento, il blocco a domande per un'idea")

d.cards("Dove siamo", "Dal percorso all'ora di lezione", [
    ("4", "indigo", "Casi d'uso e sequenza", "Il percorso c'è, sulla carta: cosa si fa e in che ordine."),
    ("5", "cyan", "Oggi: com'è fatta un'ora", "Due stampi. Uno per quando insegnate uno strumento, uno per quando spiegate un'idea."),
    ("6", "coral", "Poi la costruite", "Nel prossimo modulo, con Canvas: scaletta, slide e prompt di un incontro vostro."),
], chipcolor="cyan")

d.hook("Per cominciare", "Una lezione su uno strumento|e una su un'{cy:idea} si fanno uguali?")

d.cols("Due stampi", "Due tipi di lezione, due strutture",
       ("QUANDO INSEGNATE UNO STRUMENTO", "cyan", [
           "Le 4 mosse: perché, funzione, caso d'uso, prova",
           "Si chiude con un oggetto fatto da loro",
           "Esempio: l'assistente su misura, Canvas"]),
       ("QUANDO SPIEGATE UN'IDEA", "indigo", [
           "Il blocco: domanda, contenuto, frase, stanza",
           "Si chiude con una frase da ricordare",
           "Esempio: i dati da non caricare, come si verifica"]),
       takeaway="Un incontro vero li alterna: un blocco per capire, quattro mosse per fare.")

d.row("Lo stampo 1", "Le 4 mosse", [
    ("1", "indigo", "Perché", "A cosa serve, prima di come si usa."),
    ("2", "cyan", "Funzione", "Una sola, mostrata dal vivo."),
    ("3", "violet", "Caso d'uso", "Su un compito di scuola, già pronto."),
    ("4", "coral", "Prova", "Subito, sul mio caso o sul vostro."),
], chipcolor="cyan", takeaway="Le avete già vissute due volte: nel modulo 2 e nel modulo 4.")

d.cards("Mossa 1 · Perché", "Si parte da quello che pesa", [
    ("?", "indigo", "Una domanda, non una definizione", "\"Quante volte, a maggio, vi siete accorti di essere indietro col programma?\" Poi arriva il pianificatore."),
    ("⏱", "cyan", "Dura un minuto", "Il perché non è una lezione nella lezione. È una frase che fa dire: questo mi riguarda."),
    ("◎", "coral", "Gli adulti lo chiedono", "Chi impara da adulto vuole sapere a cosa gli serve, prima di metterci fatica."),
], chipcolor="indigo")
d.source("Knowles, principi dell'apprendimento adulto, in TEAL Center, Adult Learning Theories, 2011")

d.cards("Mossa 2 · Funzione", "Una sola, dal vivo", [
    ("1", "indigo", "Una funzione alla volta", "Non il menu. Una cosa: quella che risolve il problema appena nominato."),
    ("★", "cyan", "Prima il risultato", "Fate vedere cosa esce, poi come ci si arriva. Lo stupore viene prima dei passaggi."),
    ("▶", "coral", "Dal vivo, non in fotografia", "Si fa davanti a loro, sullo strumento vero. Con il risultato già pronto in un'altra scheda, se si inceppa."),
], chipcolor="cyan")

d.cards("Mossa 3 · Caso d'uso", "Su un compito di scuola, già pronto", [
    ("✎", "indigo", "Un lavoro che riconoscono", "La verifica, la scheda, la comunicazione alle famiglie. Non un esempio preso da un altro mestiere."),
    ("▤", "cyan", "Il prompt è sulla slide, intero", "Lo leggete ad alta voce e lo copiano. Le parti da cambiare sono fra parentesi quadre."),
    ("✓", "coral", "L'avete provato ieri", "Sullo stesso account che userete in aula. Sapete già cosa esce."),
], chipcolor="violet")

d.cards("Mossa 4 · Prova", "Subito, e su una cosa loro", [
    ("1", "indigo", "Subito", "In aula, non a casa. Quello che si rimanda a casa non si fa."),
    ("2", "cyan", "Sul mio caso o sul vostro", "Chi è insicuro rifà il mio esempio. Chi è pronto lo porta sul proprio lavoro."),
    ("3", "coral", "Una cosa finita", "\"Meglio una cosa finita e usabile che tre abbozzate.\" Si sceglie all'inizio e si porta in fondo."),
], chipcolor="coral")

d.cards("Non l'abbiamo inventato noi", "Si impara meglio quando...", [
    ("1", "indigo", "...si parte da un problema vero", "Non da un elenco di argomenti."),
    ("2", "cyan", "...qualcuno fa vedere come si fa", "La dimostrazione, prima della spiegazione."),
    ("3", "violet", "...si prova subito", "Si applica, non si ascolta soltanto."),
    ("4", "coral", "...lo si porta nel proprio lavoro", "Quello che resta è quello che si usa."),
], chipcolor="violet")
d.source("Da Merrill, First Principles of Instruction, 2002")

d.cols("La variante onesta", "Quando l'ora è una sola",
       ("ALLA LETTERA", "indigo", [
           "Perché, funzione, caso d'uso, prova",
           "Poi di nuovo, per la funzione dopo",
           "Ogni funzione ha la sua prova",
           "Serve tempo: due ore, non una"]),
       ("IN UN'ORA", "cyan", [
           "Un perché solo, all'inizio",
           "Due o tre funzioni, ciascuna col suo caso",
           "Una prova sola, alla fine, a scelta",
           "È quello che facciamo anche noi, spesso"]),
       chipcolor="violet", takeaway="La prova può essere una sola. Ma non può mancare, e non può essere a casa.")

d.hook("Lo stampo 2", "E quando non c'è uno strumento|da {cy:mostrare}?")

d.row("Lo stampo 2", "Il blocco: quattro slide, quattro colori", [
    ("?", "indigo", "Domanda", "Viola. La fate voi alla stanza: apre il blocco."),
    ("≡", "cyan", "Contenuto", "Chiara. Un titolo e tre punti, non di più."),
    ("!", "ink", "Frase", "Scura. Una frase sola, da portare via."),
    ("…", "coral", "Stanza", "Arancione. Parlano loro."),
], takeaway="Il colore è una funzione: quando vedono l'arancione, sanno che tocca a loro.")

d.cols("Tensione prima del dato", "Lo stesso numero, due effetti",
       ("A FREDDO", "muted", [
           "\"L'81% degli studenti italiani usa l'IA\"",
           "La stanza prende nota",
           "Qualcuno pensa: non i miei",
           "Il dato è un'informazione"]),
       ("COME SPECCHIO", "indigo", [
           "\"Quanti dei vostri studenti la usano ogni giorno?\"",
           "La stanza risponde, e si sbilancia",
           "Poi arriva l'81%",
           "Il dato è una sorpresa"]),
       takeaway="Prima si chiede, poi si mostra. Mai il numero a freddo.")
d.source("GoStudent Education Future Report 2025")

d.cards("Dentro la scuola", "Tre mosse per calare un'idea", [
    ("1", "indigo", "Una persona", "Non \"lo studente\": Marco, in fondo a destra. Non \"l'utente\": la collega di lettere."),
    ("2", "cyan", "Un oggetto del mestiere", "La verifica, la circolare, la griglia, il verbale. Le idee si misurano su quelli."),
    ("3", "coral", "Un gesto", "\"Se non lo incollereste sulla porta della classe, non caricatelo.\" Una norma diventa un gesto."),
])

d.stat("La maledizione della conoscenza", "Quello che è chiaro a voi non è chiaro a loro", [
    ("50%", "delle canzoni: quante pensava di far riconoscere chi le tamburellava con le dita", "dark"),
    ("2,5%", "quante ne hanno riconosciute davvero gli ascoltatori: 3 su 120", "lite"),
], "Chi sa una cosa non riesce più a immaginare di non saperla. Per questo: una slide, un'idea.",
    "Elizabeth Newton, tesi di dottorato, Stanford University 1990", chipcolor="violet")

d.cards("I dati", "Tre regole sui numeri", [
    ("1", "indigo", "Si capisce in due secondi", "\"Come tutto il Giappone\" si ricorda, un coefficiente no. Se va spiegato, si riscrive a parole."),
    ("2", "cyan", "Ha sempre la fonte", "Piccola, in fondo alla slide. E l'avete aperta voi, non solo letta da qualche parte."),
    ("3", "coral", "Se è virale, si controlla due volte", "Il \"mezzo litro d'acqua a domanda\" girava ovunque. Non era verificato: lo diciamo in slide."),
], chipcolor="cyan")

d.stmt("L'ultima regola", "Ogni allarme si chiude|con una cosa che si può {cy:fare}.")

d.debate("Scrivete la {ink:domanda} che apre la vostra|lezione. E la frase che la chiude.",
         "Su carta, cinque minuti. Poi leggetele al vicino: gli è venuta in mente una risposta, prima che parlaste?",
         tag="ESERCIZIO", room="Tocca a voi · 20 minuti", small=True, label="ESERCIZIO")

d.debate("Qual è l'idea più difficile del vostro percorso?|Con che {ink:scena di scuola} la spieghereste?", flag=True, small=True)

d.cards("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("1", "indigo", "Due stampi, già visti", "Li avete vissuti nei moduli da 1 a 4, prima di sentirli nominare oggi."),
    ("2", "cyan", "Esempi nostri", "Ogni regola aveva un esempio preso da un corso vero, errori compresi."),
    ("3", "coral", "Una prova", "Avete scritto una domanda e una frase vostre, e qualcuno le ha lette."),
], chipcolor="violet", takeaway="È lo stesso ordine che chiediamo a voi: prima si vive, poi si dà il nome.", label="SOTTO IL COFANO")

d.ponte("Il prossimo modulo", "Dalla scaletta ai materiali", "Con Canvas costruite un incontro intero del vostro percorso.",
        [("1", "indigo", "Scaletta"), ("2", "cyan", "Slide"), ("3", "coral", "Prompt")])

d.closing("In una frase", "Uno strumento si insegna facendolo usare.|Un'idea, facendola {cy:riconoscere}.")

d.save(out(5))
