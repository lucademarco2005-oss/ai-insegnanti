# -*- coding: utf-8 -*-
from common import *

d = deck(8, """  SLIDE 1-4 = apertura e perché (tre volte che ci siamo corretti). SLIDE 5-7 = funzione 1, Deep Research, con il prompt e la regola dei tre controlli.
  SLIDE 8-9 = funzione 2, il collega difficile. SLIDE 10-11 = funzione 3, la demo e l'esercizio con l'errore.
  SLIDE 12-13 = la lista dei controlli, sotto il cofano. SLIDE 14-16 = pratica, ponte, chiusura.""")

d.cover(eyebrow(8), "La demo, i dati,|le obiezioni", "Modulo 8 · con Gemini si prepara quello che serve prima di entrare in aula")

d.hook("Per cominciare", "Cosa succede se in aula|un dato che citate è {cy:falso}?")

d.cards("Dai nostri corsi", "Tre volte che ci siamo corretti", [
    ("1", "coral", "Il numero che non c'era", "Due percentuali attribuite a un grande istituto di ricerca. Nella fonte originale non c'erano. Tolte."),
    ("2", "violet", "La fonte che non si trovava", "Uno studio citato con università e anno. Cercato: non verificabile. Sostituito con uno che si può aprire."),
    ("3", "indigo", "Il dato virale", "\"Mezzo litro d'acqua a domanda.\" Lo ripetevano tutti. Le stime variano di decine di volte: lo spieghiamo in slide."),
], chipcolor="coral")

d.stmt("Il perché", "Davanti a degli insegnanti,|un dato sbagliato costa {cy:tutto il resto}.")

d.cards("Funzione 1", "Deep Research: la ricerca con le fonti", [
    ("🔎", "indigo", "Cerca, legge e scrive un rapporto", "Dal menu con il più scegliete Deep Research. Vi propone un piano, lo approvate, parte."),
    ("⏳", "cyan", "Ci mette alcuni minuti", "Si lancia all'inizio e si riapre dopo. Sugli account della scuola le ricerche sono contate: una alla volta."),
    ("🔗", "coral", "Vi dà i link, non la verità", "Ogni affermazione ha la sua fonte accanto. Aprirla resta un lavoro vostro."),
], chipcolor="cyan")

d.code("Da copiare · Caso d'uso 1", "Verificare un dato prima di metterlo in slide",
       "Lanciatela subito: la riaprite fra venti minuti.",
       Q("""Devo usare questo dato in una formazione per insegnanti: {slot:[il dato, con la fonte che ho trovato]}. Verificalo. Trova la fonte primaria, cioè il rapporto o l'articolo originale, non chi lo cita. Dimmi: chi l'ha prodotto e in che anno; su quante persone e di quale Paese; la frase esatta e la pagina in cui compare il numero; se il numero che ho io corrisponde o è stato deformato passando di mano in mano. Se non trovi la fonte primaria, scrivilo chiaramente e non proporre un numero simile al suo posto. Chiudi con un giudizio in una riga: si può usare, si può usare con una precisazione, non si può usare."""),
       size="2.8")

d.cards("La regola", "Un dato entra in slide se passa tre controlli", [
    ("1", "indigo", "Ho aperto la fonte primaria", "Il rapporto vero, non l'articolo che lo riassume. Ho visto il numero con i miei occhi."),
    ("2", "cyan", "So di chi parla", "Quante persone, quale Paese, quale anno. \"Il 60% degli insegnanti\": di dove?"),
    ("3", "coral", "Si capisce in due secondi", "Se devo spiegarlo, lo riscrivo a parole. Se non ci riesco, non lo uso."),
], chipcolor="violet")

d.cards("Funzione 2", "Gemini fa il collega difficile", [
    ("🎭", "indigo", "Gli date una parte", "Un collega con molti anni di scuola, stanco delle novità. Non è contrario: è poco convinto."),
    ("↔", "cyan", "Voi rispondete, lui insiste", "Tre scambi. Non cede alla prima frase, come non cede un collega vero."),
    ("✓", "coral", "Poi esce dal ruolo", "E vi dice cosa ha funzionato, cosa lo ha irrigidito, e una frase migliore."),
], chipcolor="cyan")

d.code("Da copiare · Caso d'uso 2", "L'obiezione, provata prima",
       "In una chat normale. Rispondete come rispondereste in aula.",
       Q("""Fai la parte di un collega insegnante che partecipa a una formazione sull'intelligenza artificiale. Hai molti anni di scuola, hai visto passare tante novità e sei stanco. Non sei contrario: sei poco convinto. La tua obiezione è: {slot:["Io queste cose non le uso, tanto sbaglia"]}. Io sono il formatore e ti rispondo. Resta nel ruolo per tre scambi: non cedere alla prima risposta, e ribatti come farebbe una persona vera, con esempi dalla vita di scuola. Dopo il terzo scambio esci dal ruolo e dimmi: cosa ti ha convinto, cosa ti ha irrigidito, e una frase che avrebbe funzionato meglio."""),
       size="2.8")

d.cards("Funzione 3", "La demo che non tradisce", [
    ("1", "indigo", "Una richiesta fatta male, apposta", "La scrivete voi, corta e vaga. In aula la migliorate insieme, un pezzo alla volta."),
    ("2", "cyan", "Tre risposte, una con un errore", "Per l'esercizio \"La usereste?\": due vanno bene, una ha un errore sottile da scovare."),
    ("3", "coral", "Il risultato, già salvato", "Tutto quello che mostrerete dal vivo lo avete anche pronto, in una scheda aperta."),
], chipcolor="cyan")

d.code("Da copiare · Caso d'uso 3", "Tre risposte, una con l'errore",
       "Il materiale per l'esercizio in cui i colleghi fanno i correttori.",
       Q("""Sto preparando un esercizio per insegnanti: devono leggere tre risposte dell'IA e decidere quale userebbero. Il compito era: {slot:[il compito, ad esempio "una scheda di ripasso sulle frazioni per la quinta primaria"]}. Scrivimi tre risposte, della stessa lunghezza e con lo stesso tono sicuro. Due sono corrette e utilizzabili. Una contiene un solo errore di contenuto, plausibile e non evidente, del tipo che un insegnante di quella materia riconosce e un lettore frettoloso no. Non segnalare qual è. Dopo le tre risposte, separata da una riga, scrivimi la soluzione per me: quale contiene l'errore, qual è, e perché è facile non vederlo."""),
       size="2.75")

d.qlist("Prima dell'aula", "La lista dei controlli", [
    "Ho provato tutto ieri, sull'account che userò in aula",
    "I prompt sono in un file, pronti da incollare",
    "Il risultato di ogni demo è aperto in un'altra scheda",
    "So cosa faccio se l'assistente non è attivo, se l'account non entra, se cade la rete",
    "Tre giorni prima ho mandato a tutti le istruzioni per accedere",
], note="Cinque righe, dieci minuti. È la scheda 5 del quaderno.", chipcolor="coral")

d.row("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("1", "indigo", "Perché", "Tre errori nostri, prima di qualunque strumento."),
    ("2", "cyan", "Funzione", "Tre, una alla volta: ricerca, collega difficile, demo."),
    ("3", "violet", "Caso d'uso", "Un prompt pronto per ciascuna."),
    ("4", "coral", "Prova", "Adesso: un dato, un'obiezione, una demo."),
], chipcolor="violet", takeaway="È la variante da un'ora: un perché solo, tre funzioni, una prova alla fine.", label="SOTTO IL COFANO")

d.practice("Tocca a voi · circa 33 minuti", "Un {ink:dato} verificato. Un'obiezione|provata. Una demo pronta.",
           "Lanciate per prima la ricerca, poi il collega difficile. Mentre aspettate, compilate la lista dei controlli.", size="5.8")

d.ponte("Il prossimo modulo", "Sei minuti", "Portate un pezzo della vostra lezione: lo conducete davanti a tre colleghi.",
        [("6'", "indigo", "Conducete"), ("3'", "cyan", "Ascoltate")])

d.closing("In una frase", "L'improvvisazione migliore|è quella {cy:preparata}.")

d.save(out(8))
