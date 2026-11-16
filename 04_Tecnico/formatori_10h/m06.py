# -*- coding: utf-8 -*-
from common import *

d = deck(6, """  SLIDE 1-4 = apertura e perché. SLIDE 5 = la funzione (Canvas). SLIDE 6-8 = caso d'uso 1, la scaletta.
  SLIDE 9 = caso d'uso 2, le slide. SLIDE 10-11 = caso d'uso 3, il foglio dei prompt, e le tre regole sui prompt.
  SLIDE 12-13 = chi fa cosa, sotto il cofano. SLIDE 14-16 = pratica, condivisione, chiusura.""")

d.cover(eyebrow(6), "Dalla scaletta|ai materiali", "Modulo 6 · Canvas: la scaletta, le slide, il foglio dei prompt")

d.hook("Per cominciare", "Quanto vi serve per preparare|{cy:un'ora} di formazione?", "Dite un numero. Lo riprendiamo alla fine.")

d.cards("Dove siamo", "Dal percorso alla lezione", [
    ("4", "indigo", "Avete casi d'uso e sequenza", "Il percorso sulla carta, scritto con il progettista e corretto da voi."),
    ("5", "cyan", "Sapete com'è fatta una lezione", "Le 4 mosse per uno strumento, il blocco a domande per un'idea."),
    ("6", "coral", "Oggi costruite un incontro intero", "Scaletta, slide e prompt pronti per i vostri colleghi. Uno solo, ma finito."),
], chipcolor="cyan")

d.stmt("Il perché", "Prima la scaletta. Poi le slide.|{cy:Mai} il contrario.")

d.cards("La funzione", "Canvas: la risposta diventa un documento", [
    ("📄", "indigo", "Si apre a fianco della chat", "Dal menu con il più, sotto la casella dove scrivete, scegliete Canvas."),
    ("✎", "cyan", "Si corregge riga per riga", "Selezionate un pezzo e chiedete di cambiarlo, oppure ci scrivete dentro voi."),
    ("⇪", "coral", "Esce da Gemini", "Il testo si esporta in Documenti. Le slide si aprono in Presentazioni, da rifinire a mano."),
], chipcolor="cyan")

d.code("Da copiare · Caso d'uso 1", "La scaletta di un incontro",
       "Dentro il progettista, con Canvas aperto.",
       Q("""Scrivimi in Canvas la scaletta dell'incontro {slot:[numero e titolo]} del mio percorso, durata {slot:[minuti]}. In alto tre righe: la durata divisa per blocchi, la frase chiave dell'incontro, cosa riprende dall'incontro prima. Poi i blocchi, ciascuno con i minuti, la domanda che lo apre, cosa dico io, cosa fanno loro e la slide che serve. Almeno metà del tempo è pratica. In fondo tre sezioni: cosa proteggere se sono in ritardo e cosa saltare; le riserve se la stanza non parla; le cose da preparare prima dell'aula, segnate con ATTENZIONE."""),
       size="2.85")

d.field("Esempio", "Com'è fatta una scaletta che regge", [
    "{b:IN ALTO.} La durata con i minuti per blocco. La frase chiave. Il raccordo con l'incontro prima.",
    "{b:I BLOCCHI.} Ognuno con i suoi minuti, la domanda che lo apre, cosa fa chi conduce, cosa fanno loro.",
    "{b:SE SEI IN RITARDO.} Cosa si protegge sempre, cioè la prova, e cosa si salta senza danni.",
    "{b:RISERVE.} Due domande in più, una demo, un caso pronto: per quando un blocco dura meno del previsto.",
    "{b:DA PREPARARE.} Account, file, prompt già provati, il risultato atteso aperto in un'altra scheda.",
])

d.cards("Tempi onesti", "Tre regole sui minuti", [
    ("1", "indigo", "Mai meccanici", "Non cinque blocchi da otto minuti. Un concetto semplice ne dura tre, uno difficile otto."),
    ("2", "cyan", "Sommate davvero", "Scrivete i minuti accanto a ogni blocco e fate la somma. Se supera l'ora si taglia adesso, non in aula."),
    ("3", "coral", "La pratica si protegge", "Quando si sfora, la tentazione è tagliare la prova. È l'unica cosa che non si taglia."),
], chipcolor="violet")

d.code("Da copiare · Caso d'uso 2", "Dalla scaletta alle slide",
       "Nella stessa chat. Le slide sono l'ultima cosa, e sono poche.",
       Q("""Dalla scaletta che abbiamo scritto, preparami le slide dell'incontro. Regole: una slide, una sola idea; poco testo, grande; al massimo tre punti per slide. Usa solo quattro tipi di slide e scrivi il tipo accanto a ognuna: DOMANDA (apre un blocco, la leggo io alla stanza), CONTENUTO (titolo e tre punti), FRASE (una frase da ricordare, da sola), CONFRONTO (una domanda a cui risponde la stanza). Ogni blocco comincia con una DOMANDA. Niente dati senza fonte: dove servirebbe un numero scrivi [dato da verificare]. Prima fammi vedere l'elenco dei titoli: le slide le crei quando ti dico che va bene."""),
       size="2.75")

d.code("Da copiare · Caso d'uso 3", "Il foglio dei prompt per i colleghi",
       "È il materiale che useranno davvero in aula: i prompt pronti, da copiare.",
       Q("""Per la parte pratica dell'incontro preparami il foglio dei prompt da dare ai colleghi: tre prompt pronti da copiare, uno per ciascun caso d'uso. Ogni prompt è un testo scorrevole, senza etichette, con dentro: per chi lavora l'IA, il compito con un verbo preciso, la classe o i destinatari, la durata o la lunghezza, il formato, e la riga "se una cosa non la sai, dimmelo invece di inventarla". Metti fra parentesi quadre le parti che ognuno deve cambiare. Sopra ogni prompt scrivi in una riga dove si incolla e cosa esce."""),
       size="2.85")

d.cards("Dai nostri corsi", "Tre regole sui prompt che mostrate", [
    ("1", "indigo", "Per intero, mai riassunti", "Sulla slide va il testo vero, da copiare. Il riassunto di un prompt non serve a nessuno: è un errore che abbiamo già fatto una volta."),
    ("2", "cyan", "Provati prima", "Ogni prompt si prova sullo strumento, il giorno prima. L'interfaccia cambia, e un prompt che in aula non funziona costa la fiducia."),
    ("3", "coral", "Letti ad alta voce", "In aula il prompt si legge tutto, parola per parola. È lì che capiscono com'è fatto."),
], chipcolor="violet")

d.cols("Chi fa cosa", "Gemini prepara. Voi firmate.",
       ("LO FA GEMINI", "cyan", [
           "La prima stesura della scaletta",
           "L'elenco delle slide",
           "I prompt per i colleghi, in bozza",
           "Tre versioni di una domanda d'apertura"]),
       ("RESTA A VOI", "indigo", [
           "Gli esempi veri, presi dai vostri colleghi",
           "I tagli: cosa entra in un'ora e cosa no",
           "Ogni dato, verificato alla fonte",
           "Provare tutto prima dell'aula"]),
       takeaway="L'IA fa la bozza, il giudizio resta vostro. Vale anche per chi forma.")

d.row("Sotto il cofano", "Cosa abbiamo fatto con voi in quest'ora", [
    ("1", "indigo", "Perché", "La scaletta prima delle slide."),
    ("2", "cyan", "Funzione", "Canvas: scrive, corregge, esporta."),
    ("3", "violet", "Caso d'uso", "Tre prompt pronti: scaletta, slide, foglio dei prompt."),
    ("4", "coral", "Prova", "Adesso, su un incontro vostro."),
], chipcolor="violet", takeaway="Avete visto tre casi e ne portate in fondo uno: meglio una cosa finita che tre abbozzate.", label="SOTTO IL COFANO")

d.practice("Tocca a voi · circa 33 minuti", "Un incontro del vostro percorso.|Scaletta, poi {ink:slide}, poi prompt.",
           "Sceglietene uno solo e portatelo in fondo. La scaletta va anche sulla scheda 3 del quaderno.")

d.debate("Quanto ci avete messo?|E cosa avete dovuto {ink:correggere} voi?", tag="CONDIVISIONE", room="Tre minuti", label="CONDIVISIONE")

d.closing("In una frase", "Un incontro costruito in un'ora.|Con dentro il {cy:vostro} giudizio.")

d.save(out(6))
