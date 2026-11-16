# -*- coding: utf-8 -*-
from common import *

d = deck(2, """  SLIDE 1-3 = apertura e patto dell'ora. SLIDE 4-10 = la lezione vissuta da corsisti (le 4 mosse, senza nominarle).
  SLIDE 11-14 = sotto il cofano. SLIDE 15-21 = Passo 1 (pubblico) e Passo 2 (traguardo). SLIDE 22-23 = pratica e chiusura.""")

d.cover(eyebrow(2), "Gemini:|la base, fatta bene", "Modulo 2 · prima da corsisti, poi da formatori, poi tocca a voi")

d.hook("Per cominciare", "Come si spiega uno strumento|a chi non l'ha mai {cy:aperto}?",
       "Fra poco lo vedete fare. Poi guardiamo insieme com'è fatto.")

d.cards("Il patto di quest'ora", "Un'ora, tre tempi", [
    ("1", "indigo", "Da corsisti · 10 minuti", "Vi facciamo, in piccolo, la lezione che facciamo ai docenti. Voi siete i docenti: seguite e provate."),
    ("2", "cyan", "Sotto il cofano · 5 minuti", "La riguardiamo da formatori: cosa c'era dentro, in che ordine, e perché in quell'ordine."),
    ("3", "coral", "Tocca a voi · 40 minuti", "Con Gemini costruite il primo pezzo del vostro percorso: chi avete davanti e dove lo portate."),
], chipcolor="cyan")

d.hook("Da corsisti · si parte", "Quando l'IA vi delude,|è colpa sua o di come gliel'avete {cy:chiesto}?")

d.cards("Lo strumento", "Cos'è Gemini", [
    ("◆", "indigo", "L'intelligenza artificiale di Google", "La stessa famiglia di strumenti che la scuola usa già: Drive, Documenti, Gmail."),
    ("🔑", "cyan", "Si entra con l'account che avete", "Da gemini.google.com, con l'account della scuola oppure con il vostro. Nessuna registrazione nuova."),
    ("✳", "violet", "Generalista", "Testo, immagini, PDF, fogli di calcolo. Bravo un po' a tutto, come gli altri assistenti."),
])

d.cards("Com'è fatto", "Le quattro cose che contano", [
    ("💬", "indigo", "La chat", "Dove chiedete. Una conversazione per argomento, non una sola infinita."),
    ("📎", "cyan", "I file", "Trascinate dentro un PDF, la foto di una pagina, un foglio. Lavora su quelli."),
    ("📄", "violet", "Canvas", "Il pannello dove la risposta diventa un documento che correggete riga per riga."),
    ("💎", "coral", "L'assistente su misura", "Una versione di Gemini che vi conosce già. Si chiamava Gem, oggi la trovate anche come Skill."),
])

d.boxes("Prima di caricare", "Una regola sola, sui dati",
        "Se non lo incollereste sulla porta della classe, non caricatelo qui.",
        "Niente nomi di alunni o di colleghi, niente PEI, niente certificazioni, niente verbali.",
        "Il materiale si anonimizza: {cy:\"un collega di lettere, vicino alla pensione\"}, non il suo nome.")

d.row("Il metodo", "Le 5 fasi di una richiesta fatta bene", [
    ("1", "indigo", "Obiettivo", "Cosa vi serve, detto con un verbo preciso."),
    ("2", "cyan", "Contesto", "Per chi, in quanto tempo, a che livello."),
    ("3", "violet", "Esempi", "Un materiale vostro da cui prendere tono e forma."),
    ("4", "coral", "Valutazione", "Leggete, e dite cosa non va."),
    ("5", "indigo", "Iterazione", "Il buon risultato arriva al secondo giro."),
], takeaway="Non serve un linguaggio segreto. Serve dire con ordine quello che avete in testa.")

d.pex("Il caso · preparare una formazione",
      "\"Preparami un corso sull'intelligenza artificiale per i miei colleghi.\"",
      "\"Sono l'animatrice digitale di un istituto comprensivo. Devo preparare un primo incontro di due ore sull'IA per 20 colleghi di primaria e medie: quasi nessuno la usa, molti temono di perdere tempo. Alla fine voglio che ognuno abbia preparato con Gemini un materiale vero per la settimana dopo. Proponimi la scaletta con i minuti, e per ogni blocco dimmi cosa faccio io e cosa fanno loro. Ti incollo sotto la scaletta di un incontro che mi è riuscito bene: tienine il ritmo. Prima di scrivere, fammi le domande che ti servono, una alla volta.\"",
      "Le 5 fasi: <b>Obiettivo</b> · <b>Contesto</b> · <b>Esempi</b> · <b>Valutazione</b> · <b>Iterazione</b>")

d.hook("Prova lampo · tre minuti", "Aprite Gemini e riscrivete|una richiesta {cy:vostra}.",
       "Una cosa che dovete preparare davvero questa settimana. Il vicino vi dice quale fase manca.", label="PROVA LAMPO")

d.stmt("Fine della lezione da corsisti", "Adesso cambiate sedia.|Riguardatela da {cy:formatori}.", chipcolor="cyan")

d.row("Sotto il cofano", "Le 4 mosse che avete appena vissuto", [
    ("1", "indigo", "Perché", "La domanda sulla delusione. Prima il problema, poi lo strumento."),
    ("2", "cyan", "Funzione", "Cos'è, com'è fatto, la regola sui dati. Poco, e solo quello che serve."),
    ("3", "violet", "Caso d'uso", "La stessa richiesta, fatta male e fatta bene, su un compito vostro."),
    ("4", "coral", "Prova", "Tre minuti, su una cosa vera. Subito, non a casa."),
], chipcolor="violet", takeaway="Perché, funzione, caso d'uso, prova. In quest'ordine, per ogni cosa che insegnate.", label="SOTTO IL COFANO")

d.cols("Sotto il cofano", "Lo stesso strumento, due lezioni diverse",
       ("IL TOUR DELLO STRUMENTO", "muted", [
           "Si parte dal menu: tutte le funzioni, una dopo l'altra",
           "L'esempio è generico, vale per chiunque",
           "La prova è rimandata a casa",
           "Dopo un mese resta il ricordo di una bella demo"]),
       ("LE 4 MOSSE", "indigo", [
           "Si parte dal problema: cosa vi fa perdere tempo",
           "L'esempio è un compito di scuola, riconoscibile",
           "La prova è in aula, sul proprio caso",
           "Dopo un mese resta un materiale che si usa"]),
       chipcolor="violet", takeaway="Stessa ora, stesso strumento. Cambia quello che resta.")

d.stmt("La regola", "Una funzione senza un caso d'uso|è solo una {cy:curiosità}.")

d.hook("Passo 1 · Il pubblico", "Chi avrete davanti,|{cy:davvero}?",
       "Non \"i docenti\". Quei venti colleghi, in quella scuola, quest'anno.")

d.cards("Passo 1 · Il pubblico", "La scheda del pubblico, in quattro domande", [
    ("1", "indigo", "Chi sono", "Ordine di scuola, materie, età, quanti. E chi è lì perché deve."),
    ("2", "cyan", "Da dove partono", "Chi non l'ha mai aperta, chi la usa senza dirlo, chi è già avanti."),
    ("3", "violet", "Cosa temono", "Perdere tempo, sbagliare con i dati, sentirsi indietro, essere giudicati."),
    ("4", "coral", "Cosa ripetono ogni settimana", "Verifiche, schede, verbali, comunicazioni. È qui che nascono i casi d'uso."),
])

d.analogy("Dai nostri corsi", "I ganci si raccolgono, non si inventano", "🎣", "violet",
          "Nei primi incontri {b:fateli parlare molto}: della loro giornata, delle classi, di quello che li stanca.||{co:{b:Segnatevi le parole che usano.}} Gli esempi dei moduli dopo si fanno su quelle, non su quelle del manuale.",
          "Chi forma non deve sapere tutto della loro giornata. Deve chiederla.")

d.code("Da copiare · Passo 1", "Fatevi intervistare da Gemini",
       "In una chat nuova. Rispondete come vi viene: è lei che mette in ordine.",
       Q("""Devo preparare un percorso di formazione sull'intelligenza artificiale per i miei colleghi e voglio prima capire bene chi ho davanti. Fammi da intervistatore: una domanda alla volta, in tutto non più di otto, e aspetta la mia risposta prima di passare alla successiva. Chiedimi chi sono i colleghi (ordine di scuola, materie, quanti), da dove partono con l'IA, cosa temono, quali lavori ripetono ogni settimana e quanto tempo avremo insieme. Non mi servono i loro nomi e non chiedermeli. Alla fine scrivimi la scheda del pubblico in quattro paragrafi: chi sono, da dove partono, cosa temono, cosa ripetono ogni settimana. Aggiungi in fondo tre cose che non ti ho detto e che dovrei scoprire prima di cominciare."""),
       size="2.75")

d.field("Esempio compilato", "Una scheda del pubblico, come esce", [
    "{b:CHI SONO.} 22 docenti di un istituto comprensivo: 9 di primaria, 13 di medie. Età media alta. Sono lì perché il collegio l'ha deliberato.",
    "{b:DA DOVE PARTONO.} Cinque non hanno mai aperto una chat. Una decina l'ha provata una volta. Tre la usano già, senza dirlo.",
    "{b:COSA TEMONO.} Di perdere tempo, di sbagliare con i dati degli alunni, di sentirsi dire che sono indietro.",
    "{b:COSA RIPETONO OGNI SETTIMANA.} Verifiche e griglie, schede differenziate, comunicazioni alle famiglie, verbali dei consigli.",
    "{b:DA SCOPRIRE.} Se sull'account della scuola Gemini è attivo. Chi può darmi una mano in aula.",
])

d.hook("Passo 2 · Il traguardo", "Alla fine, cosa avranno|{cy:in mano}?",
       "Non cosa sapranno. Cosa avranno fatto, e potranno rifare da soli.")

d.pex("Passo 2 · Il traguardo",
      "\"Alla fine del corso i colleghi conosceranno Gemini e le sue potenzialità.\"",
      "\"Alla fine dei tre incontri ogni collega avrà costruito il proprio assistente su misura, e lo avrà usato per preparare un materiale vero da portare in classe la settimana dopo.\"",
      "Un traguardo si scrive con un <b>verbo</b>, un <b>oggetto finito</b> e una <b>scadenza</b>.",
      badlab="Vago", goodlab="Si può verificare")

d.practice("Tocca a voi · circa 33 minuti", "Prima la {ink:scheda del pubblico}.|Poi il traguardo, in una frase.",
           "Fatevi intervistare, correggete quello che non torna, e scrivete il traguardo sulla scheda 1 del quaderno.")

d.closing("In una frase", "Il primo pezzo c'è: sapete {cy:chi} sono|e {cy:dove} li portate.")

d.save(out(2))
