# -*- coding: utf-8 -*-
from common import *

d = deck(7, """  SLIDE 1-3 = apertura. SLIDE 4-7 = chi avete davanti e il tono (le tre sedie, giudica/invita, il patto d'aula).
  SLIDE 8-11 = le domande (dibattito in scala, la domanda tolta, le riserve). SLIDE 12-17 = l'imprevisto, il piano B, il tempo, i dati in aula.
  SLIDE 18-19 = esercizio a gruppi di tre e dibattito. SLIDE 20-22 = sotto il cofano, ponte, chiusura.""")

d.cover(eyebrow(7), "Condurre|l'aula", "Modulo 7 · il tono, le domande, il tempo, e cosa fare quando qualcosa va storto")

d.cards("Dove siamo", "Dalla carta all'aula", [
    ("6", "indigo", "Avete un incontro costruito", "Scaletta, slide e prompt. Sulla carta funziona."),
    ("7", "cyan", "Oggi: portarlo davanti a persone vere", "Come si parla, come si fa parlare, come si tiene il tempo."),
    ("8", "coral", "Poi preparate l'aula", "Nel prossimo modulo: la demo, i dati verificati, le risposte alle obiezioni."),
], chipcolor="cyan")

d.stmt("Per cominciare", "Una buona scaletta regge l'imprevisto.|Un buon formatore lo {cy:usa}.")

d.hook("Chi avete davanti", "Chi avrete davanti,|il primo {cy:giorno}?")

d.cards("Le tre sedie", "In ogni aula ce ne sono tre", [
    ("1", "cyan", "Chi è già avanti", "La usa da mesi. Rischia di annoiarsi, o di prendersi la stanza. Dategli un compito: aiutare il vicino."),
    ("2", "violet", "Chi non ne vede l'utilità", "\"Non trovo l'utilità dell'IA.\" Non va convinto a parole: va portato su un lavoro suo, che gli pesa."),
    ("3", "coral", "Chi ha paura di sbagliare", "Scrive per chiedere \"come si installa\". Ha bisogno di un primo passo che non possa andare male."),
], chipcolor="violet")

d.cols("Il tono", "La stessa cosa, in due toni",
       ("GIUDICA", "muted", [
           "\"Dovete impegnarvi\"",
           "\"Siete indietro rispetto ai vostri studenti\"",
           "\"È facilissimo\"",
           "\"Chi non la usa resterà fuori\""]),
       ("INVITA", "indigo", [
           "\"Più ci mettete del vostro, più portate a casa\"",
           "\"Siete gli unici che possono insegnare la differenza\"",
           "\"Il buon risultato arriva al secondo giro. È normale\"",
           "\"Più siete esperti, meglio la usate\""]),
       takeaway="Chi si sente giudicato si difende. Chi si sente capace prova.")

d.analogy("Dai nostri corsi", "Il patto d'aula, nei primi cinque minuti", "🤝", "indigo",
          "{b:\"Io non sono qui per convincervi che l'IA è bella.\"}||\"Voi mi date attenzione e i vostri casi veri. Io vi do un metodo che potete usare da lunedì. {co:{b:Ci state?}}\"",
          "Si aspetta la risposta, davvero. È una domanda, non una formula.")

d.hook("Le domande", "Come si fa parlare|una stanza che non {cy:parla}?")

d.row("Il dibattito in scala", "Tre domande, dal vicino al lontano", [
    ("1", "indigo", "Il vissuto", "\"Nel vostro lavoro: dove vi ha già aiutato? E dove vi ha deluso?\""),
    ("2", "cyan", "Il ruolo", "\"Come cambierà il vostro ruolo?\""),
    ("3", "coral", "La domanda aperta", "\"Cosa pensate che l'IA non potrà mai fare?\""),
], chipcolor="coral", takeaway="La terza non si chiude: si raccolgono le ipotesi. Torna all'ultimo incontro.")

d.pex("Dai nostri corsi · una domanda tolta, una tenuta",
      "\"È giusto usare un'IA addestrata su libri presi senza permesso?\"",
      "\"Un collega vi passa una verifica fatta con l'IA in due minuti. Cosa guardate prima di darla alla vostra classe?\"",
      "La prima l'abbiamo tolta su segnalazione delle formatrici, dopo le aule. Una buona domanda ha <b>più di una risposta</b> e parte dal <b>loro mestiere</b>.",
      badlab="Tolta · la risposta era scontata", goodlab="Tenuta · raccoglie il loro giudizio")

d.cards("Se la stanza tace", "Tre riserve, in quest'ordine", [
    ("1", "indigo", "A coppie, due minuti", "Chi non parla davanti a venti persone parla con una. Poi si raccoglie."),
    ("2", "cyan", "Un'affermazione da contestare", "\"Un insegnante che usa l'IA per preparare le lezioni sta barando. Vero o falso?\""),
    ("3", "coral", "Una demo dal vivo", "Si apre lo strumento e si fa una cosa sola, su una richiesta che viene dalla stanza."),
], chipcolor="coral")

d.hook("L'imprevisto", "E quando lo strumento|vi {cy:tradisce} in diretta?")

d.cards("La demo", "Tre abitudini che la salvano", [
    ("1", "indigo", "Provata il giorno prima", "Non la settimana prima: l'interfaccia cambia. E sullo stesso account che userete in aula."),
    ("2", "cyan", "Il risultato in un'altra scheda", "Se si blocca o ci mette troppo, mostrate quello già pronto e andate avanti."),
    ("3", "coral", "L'errore si usa", "Quando l'IA sbaglia davanti a tutti, è il momento migliore per insegnare a controllare."),
], chipcolor="cyan")

d.cols("Il piano B", "Cambiano due slide, non la lezione",
       ("SE SUCCEDE", "coral", [
           "L'assistente su misura non è attivo",
           "L'account della scuola non entra",
           "La ricerca approfondita ci mette dieci minuti",
           "Il file non si carica"]),
       ("ALLORA", "indigo", [
           "Il testo si incolla come prima riga della chat",
           "Si usa l'account personale: cambia solo l'accesso",
           "Si lancia all'inizio e si riapre più tardi",
           "Si incolla il testo, oppure lo mostrate voi"]),
       chipcolor="coral", takeaway="Ogni piano B si scrive in scaletta, prima. In aula si esegue, non si inventa.")

d.cards("Il tempo", "Tre regole per non sforare", [
    ("1", "indigo", "I punti di controllo", "In scaletta: \"al minuto 25 devo essere qui\". L'orologio si guarda tre volte, non una."),
    ("2", "cyan", "Cosa si salta", "Deciso prima, e scritto. Sulle slide lo segniamo con \"Se avanza tempo\"."),
    ("3", "coral", "Cosa si protegge", "La prova e la domanda aperta. Si accorcia la spiegazione, mai il momento in cui fanno loro."),
], chipcolor="violet")

d.stmt("La regola", "Non si decide in aula cosa tagliare.|Si decide prima cosa {cy:proteggere}.")

d.boxes("I dati, in aula", "La regola che vale anche per voi",
        "Niente dati veri di alunni, famiglie o colleghi negli esempi. Nemmeno \"solo per far vedere\".",
        "Le demo si fanno su materiali inventati o resi anonimi. E i minori non aprono account.",
        "Chi forma è il primo {cy:esempio}: se lo fate voi, lo faranno loro.")

d.debate("\"Io queste cose non le uso:|tanto {ink:sbaglia}.\" Cosa rispondete?",
         "Tre giri da cinque minuti. Le altre due: \"Non ho tempo\" e \"Così i ragazzi non imparano più\".",
         tag="A GRUPPI DI TRE", room="Uno forma, uno obietta, uno osserva", small=True, label="ESERCIZIO")

d.debate("Qual è la domanda che {ink:temete}|di più dai vostri colleghi?", flag=True, small=True)

d.cards("Sotto il cofano", "Cosa abbiamo fatto con voi, fin qui", [
    ("1", "indigo", "Il tono", "Mai un \"dovete\". Provate a ricordarne uno, in sette moduli."),
    ("2", "cyan", "La scala", "Ogni dibattito è partito da quello che avete vissuto, non da un'opinione."),
    ("3", "coral", "Il tempo", "I riquadri \"Se avanza tempo\" li avete visti: erano decisi prima."),
], chipcolor="violet", takeaway="Quello che in aula sembra naturalezza, è preparazione.", label="SOTTO IL COFANO")

d.ponte("Il prossimo modulo", "Preparare l'aula", "Con Gemini preparate quello che serve prima di entrare: il dato, l'obiezione, la demo.",
        [("1", "indigo", "Il dato verificato"), ("2", "cyan", "L'obiezione provata"), ("3", "coral", "La demo pronta")])

d.closing("In una frase", "In aula non si porta un argomento.|Si portano delle {cy:persone}, da un punto a un altro.", size="6")

d.save(out(7))
