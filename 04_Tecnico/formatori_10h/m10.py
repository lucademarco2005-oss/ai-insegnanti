# -*- coding: utf-8 -*-
from common import *

d = deck(10, """  SLIDE 1-3 = ripasso (i 6 passi, i due stampi). SLIDE 4-7 = misurare (quattro livelli, tre strumenti leggeri).
  SLIDE 8-10 = correggere e adattare. SLIDE 11-14 = far durare (riaprire, le coppie, la cornice normativa).
  SLIDE 15-17 = dibattito che chiude il cerchio e piano personale. SLIDE 18-20 = sotto il cofano e chiusura.""")

d.cover(eyebrow(10), "Dopo|l'aula", "Modulo 10 · come si capisce se ha funzionato, come si corregge, come si fa durare")

d.row("Il ripasso", "I 6 passi, ora che li avete fatti", [
    ("1", "indigo", "Pubblico", "La scheda, con i loro ganci."),
    ("2", "cyan", "Traguardo", "Un verbo, un oggetto, una scadenza."),
    ("3", "violet", "Casi d'uso", "Dieci, poi tre: quelli che pesano."),
    ("4", "coral", "Sequenza", "Il metodo prima, un filo, un pezzo a incontro."),
    ("5", "indigo", "Lezione", "Le 4 mosse e il blocco."),
    ("6", "cyan", "Regia", "Tono, tempo, piano B."),
], chipcolor="cyan")

d.cols("Il ripasso", "I due stampi di una lezione",
       ("LE 4 MOSSE · PER UNO STRUMENTO", "cyan", ["Perché", "Funzione", "Caso d'uso", "Prova"]),
       ("IL BLOCCO · PER UN'IDEA", "indigo", ["Domanda", "Contenuto", "Frase", "Stanza"]),
       chipcolor="cyan", takeaway="Uno strumento si insegna facendolo usare. Un'idea, facendola riconoscere.")

d.hook("Misurare", "Come si capisce se un corso|ha {cy:funzionato}?")

d.row("Quattro livelli", "Quattro domande, dalla più facile alla più vera", [
    ("1", "indigo", "È piaciuto?", "Lo dicono a fine incontro."),
    ("2", "cyan", "Hanno imparato?", "Si vede da quello che fanno in aula."),
    ("3", "violet", "Lo usano?", "Si vede dopo due settimane, nel loro lavoro."),
    ("4", "coral", "Cambia qualcosa?", "Per gli studenti, per l'ufficio, per la scuola."),
], takeaway="Quasi tutti i corsi misurano solo la prima. La terza è quella che conta.")
d.source("Kirkpatrick, i quattro livelli di valutazione della formazione")

d.stmt("La misura", "Il gradimento si misura in aula.|Il risultato, {cy:due settimane dopo}.")

d.cards("Tre strumenti leggeri", "Come si misura, senza questionari", [
    ("1", "indigo", "La domanda di uscita", "\"Quale di queste cose userete già la prossima settimana?\" A voce, prima di salutare."),
    ("2", "cyan", "Il materiale portato", "L'incontro dopo si apre così: \"Chi ha usato qualcosa? Fatecelo vedere.\""),
    ("3", "coral", "Il messaggio a quindici giorni", "Tre righe: cosa hai usato, cosa ti ha bloccato, cosa ti serve."),
])

d.hook("Correggere", "E dopo la prima volta,|cosa si {cy:cambia}?")

d.cards("Dai nostri corsi", "Quello che abbiamo cambiato dopo le aule", [
    ("1", "indigo", "Le domande", "Due riscritte e una tolta, su segnalazione di chi le aveva fatte in aula: non aprivano la discussione."),
    ("2", "cyan", "La durata", "Una lezione accorciata perché quella prima era già lunga. Deciso guardando l'orologio, non la scaletta."),
    ("3", "coral", "L'ordine", "In un'aula un concetto non passava e un altro sì. Abbiamo messo prima quello che passava."),
], chipcolor="violet")

d.cols("Adattare", "Lo stesso percorso, per un altro pubblico",
       ("RESTA", "indigo", ["I 6 passi e la sequenza", "Le frasi da ricordare", "Le 4 mosse", "Il tono"]),
       ("SI RIFÀ", "coral", ["La scheda del pubblico, da capo", "Gli esempi e il caso che fa da filo", "Le parole del loro mestiere", "La frase d'apertura"]),
       takeaway="Per ogni pubblico nuovo: stessa struttura, esempi nuovi, una frase d'apertura nuova.")

d.hook("Far durare", "E perché non resti|un corso {cy:solo}?")

d.stat("Riaprire", "Mettersi alla prova vale più che rileggere", [
    ("56%", "ricordato dopo una settimana da chi si era messo alla prova", "dark"),
    ("42%", "ricordato dopo una settimana da chi aveva solo riletto", "lite"),
], "Ogni incontro si apre con una domanda sul precedente. Non con un riassunto fatto da voi.",
    "Roediger e Karpicke, Psychological Science, 2006. Esperimento su 120 studenti universitari")

d.cards("Far durare", "Tre cose che tengono vivo un corso", [
    ("1", "indigo", "Le coppie", "Due colleghi che si mostrano a vicenda cosa hanno provato. È il sostegno fra pari che porta la novità in classe."),
    ("2", "cyan", "La cartella comune", "I prompt che funzionano, in un posto solo, con il nome di chi li ha provati."),
    ("3", "coral", "Un appuntamento", "Mezz'ora al mese: cosa ha funzionato, cosa no. Messo in calendario adesso."),
])
d.source("Sul sostegno fra pari: Joyce e Showers, Student Achievement Through Staff Development, 2002 (stima degli autori)")

d.boxes("La cornice", "La scuola è tenuta a occuparsene",
        "Chi usa sistemi di intelligenza artificiale adotta misure per formare il proprio personale.",
        "Lo chiede l'articolo 4 del regolamento europeo sull'IA. Non serve un certificato: serve farlo, e tenerne traccia.",
        "Le linee guida del Ministero suggeriscono un {cy:piano di formazione} per tutto il personale. Il vostro percorso può essere quel piano.",
        chipcolor="cyan")
d.source("Regolamento UE sull'intelligenza artificiale, art. 4. Linee guida MIM allegate al DM 166/2025")

d.debate("Tra tre mesi, da cosa capirete|che il vostro corso è {ink:servito}?",
         "Ve l'abbiamo chiesto nel primo modulo. Adesso avete gli strumenti per rispondere.", room="Torna dal modulo 1", small=True)

d.debate("Cosa vi serve dalla vostra scuola|per farlo {ink:davvero}?", flag=True, small=True)

d.qlist("Il piano", "Una data, un gruppo, un primo incontro", [
    "Quando: la data del primo incontro, scritta",
    "A chi: il gruppo con cui parto, anche piccolo",
    "Cosa: l'incontro che ho già costruito e provato",
    "Con chi: il collega che mi dà una mano in aula",
    "Come lo saprò: la domanda che farò dopo due settimane",
], note="È la scheda 6 del quaderno. Cinque righe, da compilare prima di uscire.", chipcolor="coral")

d.row("Sotto il cofano", "L'intero percorso, sotto il cofano", [
    ("1", "indigo", "L'avete vissuto", "Ogni modulo usava il metodo che spiegava."),
    ("2", "cyan", "L'avete smontato", "Una slide a ogni modulo: cosa c'era dentro."),
    ("3", "violet", "L'avete rifatto", "Sul vostro percorso, un pezzo alla volta."),
    ("4", "coral", "L'avete provato", "Sei minuti, davanti a qualcuno."),
], chipcolor="violet", takeaway="Vivere, smontare, rifare, provare. È lo stesso ordine che potete usare con i vostri colleghi.", label="SOTTO IL COFANO")

d.stmt("Dove siete arrivati", "Non avete seguito un corso.|Ne avete {cy:costruito} uno.")

d.closing("Per chiudere", "I menu cambieranno ancora.|Il vostro {cy:metodo}, no.")

d.save(out(10))
