# -*- coding: utf-8 -*-
from common import *

d = deck(4, """  SLIDE 1-4 = apertura e perché. SLIDE 5-7 = la funzione (e il cambio di nome Gem / Skill).
  SLIDE 8-9 = caso d'uso 1, lo scrittore di prompt. SLIDE 10-15 = caso d'uso 2, il progettista di percorsi, con i prompt dei Passi 3 e 4.
  SLIDE 16-18 = principio, piano B, sotto il cofano. SLIDE 19-20 = pratica e chiusura.""")

d.cover(eyebrow(4), "L'assistente|che vi conosce", "Modulo 4 · dal contesto scritto una volta al progettista di percorsi")

d.hook("Dove arriviamo oggi", "E se l'IA non ripartisse|ogni volta da {cy:zero}?")

d.cards("Dove siamo", "Dal pubblico al percorso", [
    ("2", "indigo", "Avete la scheda del pubblico e il traguardo", "Passi 1 e 2, dal modulo 2. Sono il materiale di partenza di oggi."),
    ("3", "cyan", "Sapete riconoscere un buon caso d'uso", "Passi 3 e 4, dal modulo 3: i quattro criteri e le tre regole della sequenza."),
    ("4", "coral", "Oggi li costruite, con un assistente che conosce il metodo", "Casi d'uso e sequenza del vostro percorso, scritti e pronti da correggere."),
], chipcolor="cyan")

d.stmt("Il perché", "Il contesto si scrive {cy:una volta}.|Poi lavora per voi, ogni volta.")

d.cards("La funzione", "Una versione di Gemini che vi conosce", [
    ("✎", "indigo", "Istruzioni che restano", "Chi siete, come lavorate, come volete le risposte. Le scrivete una volta."),
    ("▤", "cyan", "I vostri file sempre a portata", "La scheda del pubblico, una scaletta ben riuscita, il regolamento della scuola."),
    ("↺", "coral", "La richiamate quando volete", "Ogni nuova chat parte già sapendo tutto. Niente preamboli, mai più."),
], chipcolor="cyan")

d.cols("Attenzione al nome", "Si chiamava Gem. Ora la trovate come Skill.",
       ("SE VEDETE \"SKILL\"", "indigo", [
           "Barra laterale, Personalizza, Skill, Crea",
           "Crea manualmente: nome, descrizione, istruzioni, file",
           "In chat la richiamate scrivendo @ e il suo nome"]),
       ("SE VEDETE ANCORA \"GEM\"", "cyan", [
           "Sugli account della scuola restano per tutto quest'anno scolastico",
           "Si aprono dalle Impostazioni: Gem, poi Nuovo Gem",
           "Nome, istruzioni, conoscenza. Poi Salva"]),
       chipcolor="coral", takeaway="Cambia il nome e cambia il menu. Quello che ci scrivete dentro è identico.")

d.stmt("Vale anche per i vostri colleghi", "I menu cambiano ogni sei mesi.|Per questo si insegna il {cy:metodo}.", chipcolor="cyan")

d.cards("Caso d'uso 1 · tre minuti", "Lo scrittore di prompt", [
    ("✎", "indigo", "Non fa il lavoro: scrive la richiesta", "Gli dite cosa vi serve, anche di corsa. Vi restituisce il prompt fatto bene, da copiare."),
    ("?", "cyan", "Vi fa al massimo due domande", "Che classe, quanto tempo, che formato. Poi scrive. Sono le 5 fasi, messe da lui."),
    ("↺", "coral", "È il primo che farete costruire ai colleghi", "Tre minuti, testo pronto da incollare, serve dal primo giorno. Toglie la paura del foglio bianco."),
], chipcolor="coral")

d.code("Da copiare · Istruzioni", "Lo scrittore di prompt: il testo, tutto",
       "Nome: Scrittore di prompt. File: nessuno, non gli servono.", SCRITTORE, sm=True)

d.cards("Caso d'uso 2 · il vostro", "Il progettista di percorsi", [
    ("◆", "indigo", "Conosce il metodo", "Le 4 mosse, il blocco teorico, l'oggetto finito a ogni incontro: sono scritti nelle sue istruzioni."),
    ("⇄", "cyan", "Propone, non decide", "Vi dà dieci casi d'uso e una sequenza. Scegliere, tagliare e correggere resta a voi."),
    ("!", "coral", "Non inventa i numeri", "Dove servirebbe un dato scrive \"dato da verificare\". Lo verificherete nel modulo 8."),
], chipcolor="coral")

d.code("Da copiare · Istruzioni, parte 1", "Il progettista: chi è e come lavora",
       "Nome: Progettista di percorsi. Incollate di seguito la parte 1 e la parte 2.", PROGETTISTA_1, sm=True, size="2.5")

d.code("Da copiare · Istruzioni, parte 2", "Il progettista: il metodo che segue",
       "File da aggiungere, se il vostro account lo permette: la scheda del pubblico.", PROGETTISTA_2, sm=True, size="2.5")

d.code("Da copiare · Passo 3", "Dieci casi d'uso. Poi ne restano tre.",
       "Dentro il progettista. In fondo incollate la scheda del pubblico e il traguardo.",
       Q("""Ti incollo la scheda del pubblico e il traguardo del mio percorso. Proponimi dieci casi d'uso, cioè dieci lavori veri che questi colleghi fanno ogni settimana e in cui Gemini li può aiutare. Per ognuno scrivi: il lavoro, quanto spesso lo fanno, e cosa avrebbero in mano dopo venti minuti di prova. Scarta quelli che richiedono dati personali di alunni o famiglie. Poi mettili in ordine, dal più sentito al meno sentito, e dimmi quali tre sceglieresti per cominciare, e perché. {slot:[scheda del pubblico e traguardo]}"""),
       size="2.9")

d.code("Da copiare · Passo 4", "La sequenza degli incontri",
       "Nella stessa chat, dopo aver scelto i vostri tre casi.",
       Q("""Con i tre casi d'uso che ho scelto, proponimi la struttura del percorso: {slot:[numero]} incontri da {slot:[durata]}. Per ogni incontro scrivi il titolo, la domanda che lo apre, cosa imparano, quale caso d'uso provano e quale oggetto finito portano a casa. Metti il metodo prima dello strumento, e fai in modo che ogni incontro riparta da quello che hanno costruito nell'incontro prima. In fondo dimmi cosa proteggere se salta un incontro."""),
       size="2.9")

d.field("Esempio", "Una sequenza, dopo le correzioni", [
    "{b:INCONTRO 1 · Perché ci riguarda.} Apre: \"Quanti dei vostri studenti la usano ogni giorno?\" Si prova: una richiesta fatta bene, su un compito proprio. Si porta a casa: il primo materiale.",
    "{b:INCONTRO 2 · L'assistente che vi conosce.} Apre: \"E se non ripartisse ogni volta da zero?\" Si prova: il proprio assistente. Si porta a casa: l'assistente della propria classe.",
    "{b:INCONTRO 3 · Dal materiale alla lezione.} Apre: \"Quanto ci mettete a preparare un'ora?\" Si prova: una lezione intera. Si porta a casa: la lezione della settimana dopo.",
], size="2.7")

d.stmt("Il primo principio, anche qui", "L'assistente fa la bozza.|Il percorso lo {cy:decidete} voi.")

d.boxes("Piano B", "Se sul vostro account l'assistente non c'è",
        "Il testo delle istruzioni si incolla all'inizio di una chat normale, come prima riga.",
        "Funziona lo stesso. Si perde solo la comodità di non rifarlo ogni volta.",
        "Cambiano {cy:due slide}, non la lezione. E ditelo ai colleghi prima che lo scoprano da soli.")

d.row("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("1", "indigo", "Perché", "Il contesto scritto una volta sola."),
    ("2", "cyan", "Funzione", "L'assistente: istruzioni, file, richiamo."),
    ("3", "violet", "Caso d'uso", "Due, già pronti: lo scrittore e il progettista."),
    ("4", "coral", "Prova", "Adesso, sul vostro percorso."),
], chipcolor="violet", takeaway="E una scelta in più: il primo oggetto che si costruisce scrive tutti gli altri.", label="SOTTO IL COFANO")

d.practice("Tocca a voi · circa 33 minuti", "Costruite il {ink:progettista}.|Poi casi d'uso e sequenza.",
           "Dieci casi, ne tenete tre. Poi la sequenza, sulla scheda 2 del quaderno. Correggete tutto quello che non vi somiglia.")

d.closing("In una frase", "Avete un percorso sulla carta.|Dal prossimo modulo gli diamo una {cy:lezione}.")

d.save(out(4))
