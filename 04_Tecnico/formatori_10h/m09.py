# -*- coding: utf-8 -*-
from common import *

d = deck(9, """  SLIDE 1-3 = apertura e come funziona. SLIDE 4-7 = la griglia, il feedback, il patto, la logistica.
  SLIDE 8-9 = la prova e la condivisione. SLIDE 10-11 = il prompt per il dopo e sotto il cofano. SLIDE 12-13 = ponte e chiusura.""")

d.cover(eyebrow(9), "Sei minuti|in aula", "Modulo 9 · si conduce, si osserva, ci si dice cosa tenere e cosa cambiare")

d.hook("Per cominciare", "Si impara a condurre ascoltando|o {cy:conducendo}?")

d.cards("Come funziona", "La prova in piccolo", [
    ("6'", "indigo", "Conducete un pezzo vero", "Sei minuti della vostra lezione: una funzione con le 4 mosse, oppure un'idea, dalla domanda d'apertura alla domanda alla stanza."),
    ("3'", "cyan", "Ricevete due cose", "Dai colleghi del gruppo: una cosa da tenere e una da cambiare. Nient'altro."),
    ("↻", "coral", "Si gira", "Gruppi da quattro: ognuno conduce una volta e osserva tre volte. Nove minuti a turno."),
], chipcolor="cyan")

d.analogy("Da dove viene", "Si chiama microteaching, e ha sessant'anni", "🎬", "violet",
          "Nasce a Stanford nel 1963 per formare i futuri insegnanti: {b:una lezione di pochi minuti}, a un piccolo gruppo, e un riscontro subito dopo.||{co:{b:Poi si rifà la lezione.}} È questo il punto: si prova quando sbagliare non costa niente.",
          "Provare un pezzo e sentirsi dire subito cosa tenere: è così che si impara a condurre.")
d.source("Dwight Allen, Micro-teaching: A Description, Stanford University 1967")

d.cards("La griglia", "Cosa guarda chi osserva", [
    ("1", "indigo", "Il perché è arrivato prima?", "Ho capito a cosa serviva, prima di vedere come si fa."),
    ("2", "cyan", "Era dentro la scuola?", "C'erano una persona, un compito, una scena che riconosco."),
    ("3", "violet", "Ho fatto qualcosa?", "Ho risposto, scritto, provato. Non ho solo ascoltato."),
    ("4", "coral", "Cosa mi porto via?", "Saprei ripetere la frase chiave, o rifare il gesto, domani."),
])

d.cols("Il feedback", "Due frasi, e basta",
       ("COSÌ AIUTA", "indigo", [
           "\"Tieni la domanda d'apertura: mi ha fatto pensare subito al mio caso\"",
           "\"Cambia l'esempio: era di un'altra materia e mi sono perso\"",
           "Cose che ho visto, dette in prima persona"]),
       ("COSÌ NO", "muted", [
           "\"Bravo, bello, mi è piaciuto\"",
           "\"Secondo me dovresti coinvolgere di più\"",
           "Giudizi sulla persona, consigli generici"]),
       takeaway="Una cosa da tenere, una da cambiare. Chi riceve ascolta e ringrazia: non si difende.")

d.stmt("Il patto", "Qui si può sbagliare.|È il posto giusto per {cy:farlo}.")

d.cards("Come ci si organizza", "In presenza e a distanza", [
    ("▣", "indigo", "In presenza", "Gruppi da quattro agli angoli della stanza. Chi conduce resta in piedi, con il proprio schermo."),
    ("▢", "cyan", "A distanza", "Stanze separate da quattro. Chi conduce condivide lo schermo. Un cronometro per stanza."),
    ("⏱", "coral", "Il tempo lo tiene il gruppo", "Sei minuti e ci si ferma, anche a metà frase. Fermarsi in tempo fa parte della prova."),
], chipcolor="violet")

d.practice("Tocca a voi · 36 minuti", "Sei minuti {ink:conducete}.|Tre minuti ascoltate.",
           "Quattro turni da nove minuti. Chi osserva compila la scheda 4 del quaderno.")

d.debate("Cosa avete visto fare a un collega|che da domani farete {ink:anche voi}?", tag="CONDIVISIONE", room="Cinque minuti", small=True, label="CONDIVISIONE")

d.code("Da copiare · dopo la prova", "Dai feedback alle tre modifiche",
       "Stasera, dentro il progettista. Incollate la scaletta e quello che vi hanno detto.",
       Q("""Ho provato sei minuti della mia lezione davanti a tre colleghi. Ti incollo la scaletta e quello che mi hanno detto: per ognuno, una cosa da tenere e una da cambiare. Non riscrivere la lezione. Dimmi solo le tre modifiche che la migliorano di più, in ordine di importanza, e per ciascuna cosa cambio esattamente e perché. Se due colleghi mi hanno detto cose opposte, fammelo notare e chiedimi com'è andata secondo me. {slot:[scaletta e feedback]}"""),
       size="2.9")

d.cards("Sotto il cofano", "Perché l'abbiamo fatto così", [
    ("1", "indigo", "Breve", "Sei minuti bastano per vedere cosa regge e cosa no."),
    ("2", "cyan", "Vero", "Un pezzo della vostra lezione, davanti a colleghi veri."),
    ("3", "coral", "Con un riscontro subito", "Due frasi a caldo valgono più di un questionario a fine corso."),
], chipcolor="violet", takeaway="Fate lo stesso con chi formerete: fateli provare presto, in piccolo, e dite subito cosa tenere.", label="SOTTO IL COFANO")

d.ponte("Il prossimo modulo", "Dopo l'aula", "Come si capisce se ha funzionato, come si corregge, come si fa durare.",
        [("1", "indigo", "Misurare"), ("2", "cyan", "Correggere"), ("3", "coral", "Far durare")])

d.closing("In una frase", "Adesso sapete com'è stare|dall'{cy:altra parte} della slide.")

d.save(out(9))
