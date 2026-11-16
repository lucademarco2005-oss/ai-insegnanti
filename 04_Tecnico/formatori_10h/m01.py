# -*- coding: utf-8 -*-
from common import *

d = deck(1, """  SLIDE 1-4 = patto d'aula e dibattito di apertura. SLIDE 5-9 = perché i corsi non lasciano traccia (dati, tre modi di sbagliare).
  SLIDE 10-15 = cosa fa la differenza (la ricerca, le tre scelte, dentro la scuola, la paura). SLIDE 16-19 = la mappa: i 6 passi e i cinque incontri.
  SLIDE 20-21 = dibattito. SLIDE 22-24 = sotto il cofano, ponte, chiusura.""")

d.cover(eyebrow(1), "Il mestiere|di chi forma", "Modulo 1 · perché tanti corsi non lasciano traccia, e cosa fa la differenza")

d.cards("Il patto d'aula", "Come funziona questo percorso", [
    ("1", "indigo", "Prima lo vivete", "Ogni cosa che vi insegniamo a fare con i colleghi, prima la facciamo con voi. Siete corsisti."),
    ("2", "cyan", "Poi lo smontiamo", "Alziamo il cofano: cosa c'era dentro, in che ordine, perché. Siete formatori."),
    ("3", "coral", "Poi lo rifate voi", "Sul vostro percorso, per i vostri colleghi, con Gemini. A ogni incontro un pezzo in più."),
], chipcolor="cyan")

d.stmt("Il patto", "Più ci mettete del vostro,|più portate a {cy:casa}.")

d.debate("Qual è l'ultimo corso che vi ha|cambiato il {ink:lunedì mattina}?",
         "Non il più bello. Quello dopo il quale avete fatto una cosa in modo diverso.")

d.hook("Il problema", "Perché tanti corsi piacciono,|e poi non cambia {cy:niente}?")

d.stat("Il dato", "Formarsi non basta a cambiare", [
    ("55%", "dei docenti dice che la formazione seguita ha migliorato il proprio modo di insegnare", "dark"),
    ("29%", "indica l'intelligenza artificiale come bisogno di formazione: è il tema più richiesto", "lite"),
], "Quasi un docente su due esce da un corso e insegna come prima. E l'IA è il corso che chiedono di più.",
    "OCSE, TALIS 2024. Media dei Paesi OCSE, docenti di secondaria di primo grado")

d.stat("In Italia", "E da noi, sull'IA?", [
    ("25%", "dei docenti italiani ha usato l'IA nel lavoro nell'ultimo anno. La media OCSE è 36%", "dark"),
    ("69%", "di chi non la usa dice di non avere le conoscenze per farlo", "lite"),
], "Chi non la usa, spesso, non è contrario: non ha avuto qualcuno che gliela insegnasse. Quel qualcuno siete voi.",
    "OCSE, TALIS 2024, nota Paese Italia. Docenti di secondaria di primo grado")

d.cards("Tre modi di sbagliare", "Come fallisce un corso sull'IA", [
    ("1", "coral", "Il tour dello strumento", "Tutte le funzioni, una dopo l'altra. Si esce sapendo dove cliccare, non perché farlo."),
    ("2", "violet", "L'IA spiegata da sopra", "Reti neurali, scenari, grandi numeri. Tutto vero, e lontanissimo dalla seconda B."),
    ("3", "indigo", "La lezione che si ascolta", "Due ore di slide e una bella demo. La prova, però, è rimandata a casa."),
], chipcolor="coral")

d.stmt("La misura", "Un corso non si misura in aula.|Si misura il {cy:lunedì dopo}.")

d.hook("La risposta", "E allora, cosa fa|la {cy:differenza}?")

d.stat("Cosa dice la ricerca", "Cosa avevano in comune i corsi riusciti", [
    ("35", "studi su 35 mostravano un modello: qualcuno faceva vedere come si fa", "dark"),
    ("34", "su 35 facevano provare, non solo ascoltare", "lite"),
    ("31", "su 35 duravano nel tempo, non un giorno solo", "lite"),
], "Trentacinque studi rigorosi su corsi che hanno cambiato l'insegnamento. Tre cose tornano quasi sempre.",
    "Darling-Hammond, Hyler, Gardner, Effective Teacher Professional Development, Learning Policy Institute 2017", small=True)

d.cards("Le nostre tre scelte", "Le tre scelte che reggono i nostri corsi", [
    ("1", "indigo", "Il metodo, non lo strumento", "Gli strumenti cambiano ogni sei mesi. Un modo di lavorare resta, e passa da uno strumento all'altro."),
    ("2", "cyan", "Dentro la scuola, non sopra", "Ogni idea atterra su una scena di scuola: una verifica, una circolare, un consiglio di classe."),
    ("3", "coral", "Qualcosa in mano, ogni volta", "Ogni incontro finisce con un oggetto fatto da loro, sul proprio caso, usabile la settimana dopo."),
])

d.cols("Dentro la scuola", "La stessa idea, detta in due modi",
       ("DA SOPRA", "muted", [
           "\"I modelli hanno limiti nel ragionamento contestuale\"",
           "\"Serve supervisione umana sugli output\"",
           "\"Attenzione ai dati sensibili, articolo 9 del GDPR\"",
           "\"L'automazione ha gradi diversi di rischio\""]),
       ("DENTRO LA SCUOLA", "indigo", [
           "\"Non sa che Marco, in fondo a destra, va incoraggiato\"",
           "\"Un collega vi passa una verifica fatta in due minuti: cosa guardate?\"",
           "\"Se non lo incollereste sulla porta della classe, non caricatelo\"",
           "\"La bozza di una circolare sì. Il voto a uno studente no\""]),
       chipcolor="cyan", takeaway="A sinistra si annuisce. A destra ci si riconosce.")

d.stmt("Prima di tutto", "Prima di chiedere fatica,|togliete la {cy:paura}.")

d.cards("Dai nostri corsi", "Tre frasi che abbassano la difesa", [
    ("1", "indigo", "\"Sull'IA siamo tutti, in parte, principianti.\"", "La dice chi conduce, nei primi cinque minuti."),
    ("2", "cyan", "\"Non siete indietro. Siete gli unici che possono insegnare la differenza.\"", "Subito dopo il dato sugli studenti che la usano già."),
    ("3", "coral", "\"Il buon risultato arriva al secondo o terzo passaggio. È normale.\"", "Prima della prima prova, non dopo."),
], chipcolor="violet", takeaway="Anche le prime formazioni negli Stati Uniti sono partite da qui: prima ridurre il disagio, poi gli strumenti.")
d.source("RAND, Diliberti, Lake, Weiner, aprile 2025")

d.hook("La mappa", "Come si {cy:costruisce}|un percorso così?")

d.row("La mappa", "I 6 passi per costruire un percorso", [
    ("1", "indigo", "Pubblico", "Chi ho davanti."),
    ("2", "cyan", "Traguardo", "Cosa avranno in mano."),
    ("3", "violet", "Casi d'uso", "Su cosa lavorano."),
    ("4", "coral", "Sequenza", "In che ordine."),
    ("5", "indigo", "Lezione", "Com'è fatta un'ora."),
    ("6", "cyan", "Regia", "Come si conduce."),
], takeaway="Poi si prova davanti a qualcuno, e si corregge. Sono i cinque incontri di questo percorso.")

d.row("Il percorso", "Cinque incontri, un pezzo alla volta", [
    ("1", "indigo", "Il mestiere", "Pubblico e traguardo."),
    ("2", "cyan", "Il progetto", "Casi d'uso e sequenza."),
    ("3", "violet", "La lezione", "Scaletta, slide, prompt."),
    ("4", "coral", "L'aula", "Demo, dati, obiezioni."),
    ("5", "indigo", "La prova", "Sei minuti in aula, e il piano."),
], chipcolor="cyan", takeaway="A ogni incontro un'ora per capire e un'ora per fare. Sempre con Gemini aperto.")

d.stmt("Dove arrivate", "Alla fine non avrete appunti.|Avrete un {cy:percorso vostro}, pronto per l'aula.", size="7")

d.debate("Fra i vostri colleghi, chi sarà il più|{ink:difficile} da portare a bordo?",
         "Non il nome: il tipo. E cosa avrebbe bisogno di sentirsi dire, nei primi cinque minuti?", small=True)

d.debate("Tra tre mesi, da cosa capirete|che il vostro corso è {ink:servito}?",
         "Questa non si chiude oggi. La riprendiamo nell'ultimo modulo.", room="Resta aperta", small=True)

d.row("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("1", "indigo", "Il patto", "Vi abbiamo chiesto qualcosa, prima di darvi qualcosa."),
    ("2", "coral", "La domanda prima", "Avete raccontato i vostri corsi prima di vedere un dato."),
    ("3", "cyan", "Il dato come specchio", "Il 55% è arrivato dopo, a confermare quello che avevate detto."),
    ("4", "ink", "La domanda aperta", "L'ultima non ha risposta: torna alla fine del percorso."),
], chipcolor="violet", takeaway="Niente di questo è spontaneo. È scritto in scaletta, minuto per minuto.", label="SOTTO IL COFANO")

d.ponte("Il prossimo modulo", "Gemini, la base", "La vivete da corsisti, la smontiamo, e costruite il primo pezzo del vostro percorso.",
        [("1", "indigo", "Pubblico"), ("2", "cyan", "Traguardo")])

d.closing("In una frase", "Non vi insegniamo l'IA.|Vi insegniamo a {cy:insegnarla}.")

d.save(out(1))
