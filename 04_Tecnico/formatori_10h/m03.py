# -*- coding: utf-8 -*-
from common import *

d = deck(3, """  SLIDE 1-3 = apertura. SLIDE 4-11 = Passo 3, i casi d'uso (progettare a ritroso, i quattro criteri, il confronto).
  SLIDE 12-18 = Passo 4, la sequenza (tre regole, come l'abbiamo fatto noi, adattare, errori nostri, stanza mista).
  SLIDE 19-20 = esercizio e dibattito. SLIDE 21-23 = sotto il cofano, ponte, chiusura.""")

d.cover(eyebrow(3), "Dal bisogno|alla sequenza", "Modulo 3 · come si scelgono i casi d'uso e in che ordine si mettono")

d.cards("Dove siamo", "Il filo del percorso", [
    ("1", "indigo", "Il mestiere di chi forma", "Tre scelte: il metodo e non lo strumento, dentro la scuola, qualcosa in mano a ogni incontro."),
    ("2", "cyan", "Pubblico e traguardo", "Li avete scritti la volta scorsa: chi sono i vostri colleghi e cosa avranno in mano alla fine."),
    ("3", "coral", "Oggi: casi d'uso e sequenza", "Su cosa li fate lavorare, e in che ordine. Oggi sulla carta, nel prossimo modulo con Gemini."),
], chipcolor="cyan")

d.stmt("Per cominciare", "Un percorso non è un elenco di argomenti.|È una strada verso un {cy:traguardo}.")

d.hook("Passo 3 · I casi d'uso", "Da dove si comincia a progettare:|dall'inizio o dalla {cy:fine}?")

d.row("Progettare a ritroso", "Tre domande, in quest'ordine", [
    ("1", "indigo", "Dove arrivano", "Il traguardo: cosa avranno in mano alla fine."),
    ("2", "cyan", "Come lo vedo", "La prova: da cosa capisco che ci sono arrivati."),
    ("3", "coral", "Cosa facciamo", "Solo adesso: attività, strumenti, slide."),
], takeaway="Chi parte dalle slide riempie le ore. Chi parte dal traguardo le sceglie.")
d.source("McTighe e Wiggins, Understanding by Design Framework, ASCD 2012")

d.hook("Passo 3 · I casi d'uso", "Cosa rende {cy:buono}|un caso d'uso?")

d.cards("Passo 3 · I casi d'uso", "I quattro criteri", [
    ("1", "indigo", "Si ripete", "Un lavoro che fanno ogni settimana, non una volta l'anno."),
    ("2", "cyan", "Pesa", "Un lavoro che darebbero via volentieri: ruba tempo, annoia, mette ansia."),
    ("3", "violet", "Si finisce in aula", "In venti minuti di prova esce un oggetto finito, usabile la settimana dopo."),
    ("4", "coral", "Non tocca dati personali", "Si può fare senza nomi di alunni, di famiglie, di colleghi."),
])

d.analogy("Dai nostri corsi", "La domanda che trova i casi d'uso", "🔁", "violet",
          "{b:\"Qual è il lavoro che vi ripetete ogni settimana e che dareste volentieri via?\"}||La facciamo in ogni aula, prima di aprire lo strumento. {co:{b:Le risposte sono i casi d'uso.}} Non li scegliamo noi: li dicono loro.",
          "Il pianificatore dell'anno è nato da una frase: \"a maggio siamo sempre indietro col programma\".")

d.cols("Il confronto", "Lo stesso strumento, due casi d'uso",
       ("FA EFFETTO", "muted", [
           "Una poesia sull'autunno in rima baciata",
           "Un'immagine divertente da far vedere ai colleghi",
           "\"Chiedetegli quello che volete\"",
           "In aula si ride. Lunedì non cambia niente"]),
       ("SERVE", "indigo", [
           "La comunicazione alle famiglie per l'uscita del 14 marzo",
           "La scheda facilitata per chi resta indietro",
           "La verifica con la sua griglia di valutazione",
           "In aula si lavora. Lunedì si usa"]),
       takeaway="L'effetto sorpresa dura un'ora. Un lavoro risparmiato dura un anno.")

d.analogy("Dai nostri corsi", "Il caso d'uso migliore finisce con un numero", "⏱", "cyan",
          "Con le segreterie leggiamo insieme un registro delle richieste allo sportello: {b:quali domande tornano, e quante volte}.||Poi si fa il conto del tempo. {co:{b:Sul registro di esempio che usiamo in aula}} esce un numero che nessuno si aspetta.",
          "\"Due domande ripetute: quasi 23 ore in un anno.\" È l'ultima slide di quel modulo.", chipcolor="cyan")

d.stmt("La regola", "La funzione arriva come {cy:soluzione}.|Mai come novità.")

d.hook("Passo 4 · La sequenza", "E in che {cy:ordine}|si mettono le cose?")

d.cards("Passo 4 · La sequenza", "Tre regole per mettere in fila", [
    ("1", "indigo", "Prima il metodo, poi lo strumento", "Se sanno chiedere bene, ogni strumento è facile. Se sanno solo dove cliccare, al primo aggiornamento sono da capo."),
    ("2", "cyan", "Un filo solo", "Un caso che attraversa tutti gli incontri: la stessa classe, la stessa materia, lo stesso ufficio. Meno fatica per chi segue."),
    ("3", "coral", "Ogni incontro lascia un pezzo", "Quello che si costruisce oggi serve la volta dopo. Nessuno riparte da zero, e c'è un motivo per tornare."),
])

d.cols("Come l'abbiamo fatto noi", "Venti ore, due blocchi",
       ("12 ORE · IL METODO", "indigo", [
           "Cos'è l'IA e perché ci riguarda",
           "I 4 principi per lavorarci",
           "Etica, dati, responsabilità",
           "Come si scrive una richiesta",
           "Dal prompt al sistema, e uno sguardo avanti"]),
       ("8 ORE · GLI STRUMENTI", "cyan", [
           "L'assistente di base, reso proprio",
           "Uno strumento per creare i materiali",
           "Uno strumento per studiare sulle proprie fonti",
           "Il laboratorio: tutto insieme, su una lezione vera"]),
       chipcolor="violet", takeaway="Nelle prime ore lo strumento si tocca cinque minuti, solo per dare evidenza a un'idea.")

d.row("Il filo", "Un caso solo, che cresce a ogni incontro", [
    ("🌍", "indigo", "Primaria", "Geografia in quarta: la stessa classe, dalla verifica al quiz."),
    ("🍂", "coral", "Infanzia", "L'autunno: l'attività, il racconto, l'avviso ai genitori."),
    ("📜", "violet", "Secondaria", "Storia in terza media: la Prima guerra mondiale."),
    ("✉", "cyan", "Segreteria", "Le mail dell'ufficio: dal rinvio dell'assemblea all'archivio."),
], chipcolor="violet", takeaway="Chi segue non impara un contesto nuovo ogni volta. Impara solo la cosa nuova.")

d.cols("Adattare", "Struttura ferma, esempi mobili",
       ("NON CAMBIA", "indigo", [
           "La sequenza degli incontri",
           "I principi e le frasi da ricordare",
           "Le 4 mosse e il ritmo a domande",
           "Il tipo di oggetto che portano a casa"]),
       ("CAMBIA", "coral", [
           "Gli esempi: su quello che fanno davvero",
           "Le parole: \"compito\" diventa \"attività\"",
           "La frase d'apertura, tagliata sul loro ruolo",
           "Il caso che fa da filo"]),
       takeaway="Per passare dalla primaria all'infanzia abbiamo cambiato gli esempi, non il corso.")

d.cards("Dai nostri corsi", "Tre errori che abbiamo fatto noi", [
    ("1", "coral", "Il pubblico sbagliato", "Un percorso per la secondaria nato con gli esempi della primaria. Rifatto: gli esempi suonavano falsi e la stanza non si riconosceva."),
    ("2", "violet", "Troppo materiale", "Una lezione pratica che sulla carta valeva tre ore e venti, in un incontro da due. Lo si scopre in aula, ed è tardi."),
    ("3", "indigo", "Lo strumento mai provato", "Una funzione messa in programma senza averla verificata sugli account veri. Tolta prima di andare in aula."),
], chipcolor="coral")

d.cards("La stanza mista", "Se davanti avete ordini di scuola diversi", [
    ("⫴", "indigo", "Esempi a binari appaiati", "Lo stesso passaggio su due esempi, con l'etichetta: primaria, medie, superiori. Ognuno legge il suo."),
    ("✎", "cyan", "Esercizi \"sul vostro caso\"", "\"Prendete un compito che date spesso\" si adatta da solo a qualunque classe."),
    ("◐", "coral", "Plenaria mista, pratica divisa", "Si ascolta insieme, si prova in gruppi dello stesso ordine di scuola."),
])

d.debate("Qual è il lavoro che i vostri colleghi|ripetono ogni settimana e {ink:darebbero via}?",
         "Dieci righe a testa, su carta. Poi il filtro dei quattro criteri: ne restano tre.",
         tag="ESERCIZIO", room="Tocca a voi · 20 minuti", small=True, label="ESERCIZIO")

d.debate("Se aveste {ink:metà del tempo},|quale incontro togliereste?",
         "E cosa vi dice, questo, di quello che conta davvero nel vostro percorso?", flag=True, small=True)

d.row("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("?", "indigo", "Domanda", "Ogni blocco è partito da una domanda viola, prima del contenuto."),
    ("≡", "cyan", "Contenuto", "Poche slide chiare, con una sola idea ciascuna."),
    ("!", "ink", "Frase", "Una frase scura, da portare via."),
    ("…", "coral", "Stanza", "Una domanda arancione: avete parlato voi."),
], chipcolor="violet", takeaway="Sono i quattro colori delle nostre slide. Li smontiamo nel modulo 5.", label="SOTTO IL COFANO")

d.ponte("Il prossimo modulo", "L'assistente", "Costruite con Gemini il progettista che conosce il metodo, e gli fate scrivere casi d'uso e sequenza.",
        [("3", "indigo", "Casi d'uso"), ("4", "cyan", "Sequenza")])

d.closing("In una frase", "Scegliete i casi dal loro {cy:lunedì}.|Il resto del percorso viene di conseguenza.")

d.save(out(3))
