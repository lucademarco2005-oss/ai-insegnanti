# -*- coding: utf-8 -*-
"""Genera le guide pratiche per il formatore (moduli pratici), nello stesso formato
delle `_scaletta_formatori.html` esistenti: setup, parte teorica veloce, passi da mostrare."""
import re, html, pathlib
from common import ROOT, TITOLI

CSS = """
  :root{
    --ink:#1E1B4B; --indigo:#4F46E5; --violet:#7C3AED; --cyan:#0891B2;
    --coral:#EA6A1E; --teal:#0E9488; --bg:#F7F6FB; --text:#1A1730; --muted:#6B6790; --line:#E6E3FB; --card:#fff;
  }
  *{box-sizing:border-box;margin:0;padding:0;}
  body{font-family:'Inter','Segoe UI',-apple-system,Arial,sans-serif;background:var(--bg);color:var(--text);line-height:1.5;}
  .wrap{max-width:900px;margin:0 auto;padding:36px 24px 80px;}
  header{margin-bottom:18px;}
  h1{font-size:30px;font-weight:800;color:var(--ink);}
  .sub{color:var(--muted);font-size:15px;margin-top:4px;}
  .sec-label{font-size:13px;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:28px 0 10px;}
  .block{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:20px 22px;margin-bottom:16px;border-left:6px solid var(--indigo);}
  .block.setup{border-left-color:var(--teal);} .block.teoria{border-left-color:var(--cyan);} .block.pratica{border-left-color:var(--coral);}
  .bhead{display:flex;align-items:baseline;gap:10px;margin-bottom:4px;flex-wrap:wrap;}
  .bnum{font-size:13px;font-weight:800;color:#fff;background:var(--indigo);border-radius:20px;padding:2px 10px;}
  .block.setup .bnum{background:var(--teal);} .block.teoria .bnum{background:var(--cyan);} .block.pratica .bnum{background:var(--coral);}
  .btitle{font-size:20px;font-weight:800;color:var(--ink);}
  .btime{font-size:13px;color:var(--muted);margin-left:auto;font-weight:600;}
  .steps{list-style:none;counter-reset:s;margin-top:10px;}
  .steps li{counter-increment:s;padding-left:30px;position:relative;margin-bottom:8px;font-size:15px;}
  .steps li::before{content:counter(s);position:absolute;left:0;top:1px;width:20px;height:20px;background:var(--indigo);color:#fff;border-radius:50%;font-size:12px;font-weight:700;display:flex;align-items:center;justify-content:center;}
  .steps b{color:var(--ink);}
  ul.plain{list-style:none;margin-top:8px;} ul.plain li{font-size:15px;padding-left:18px;position:relative;margin-bottom:6px;}
  ul.plain li::before{content:"";position:absolute;left:0;top:9px;width:6px;height:6px;border-radius:50%;background:var(--muted);}
  .say{margin-top:12px;background:#F0EFFA;border-radius:8px;padding:10px 14px;font-size:14.5px;font-style:italic;color:var(--ink);}
  .say b{font-style:normal;color:var(--violet);font-weight:700;}
  .prompt{margin-top:10px;background:#FFF8F2;border:1px solid #F6D9C2;border-radius:8px;padding:10px 14px;font-size:14px;color:var(--ink);}
  .prompt b{color:var(--coral);}
  .cue{display:inline-block;background:#FFF1E6;color:var(--coral);border:1px solid #F6D9C2;border-radius:6px;padding:1px 8px;font-size:13px;font-weight:700;margin-top:10px;}
  .note{margin-top:8px;font-size:13.5px;color:var(--muted);} .note b{color:var(--text);}
  @media print{ body{background:#fff;} .block{break-inside:avoid;} }
"""


def b(s):
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return re.sub(r"`([^`]+)`", r"<b>\1</b>", s)


def prompts_of(n):
    """Testi 'da copiare' del deck, per numero di slide."""
    t = (ROOT / ("%02d_Modulo_%d" % (n, n)) / ("Modulo_%d.html" % n)).read_text(encoding="utf-8")
    res = {}
    for m in re.finditer(r'<!-- SLIDE (\d+) · DA COPIARE -->.*?<div class="codebox[^"]*"[^>]*>(.*?)</div>\s*<div class="foot">', t, re.S):
        body = re.sub(r"<br\s*/?>", " ", m.group(2))
        body = html.unescape(re.sub(r"<[^>]+>", "", body)).strip()
        res[int(m.group(1))] = body
    return res


def render(n, sub, setup, teoria, passi):
    P = prompts_of(n)
    out = ['<!DOCTYPE html>\n<html lang="it">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">',
           "<title>Percorso Formatori · Modulo %d · Guida pratica per il formatore</title>\n<style>%s</style>\n</head>\n<body>\n<div class=\"wrap\">\n" % (n, CSS),
           '  <header>\n    <h1>Modulo %d · %s<br>Guida pratica per il formatore</h1>\n    <div class="sub">%s</div>\n  </header>\n' % (n, TITOLI[n], b(sub)),
           '  <div class="sec-label">Prima della lezione (setup)</div>\n  <div class="block setup">\n    <div class="bhead"><span class="bnum">0</span><span class="btitle">Da avere pronto</span></div>\n    <ul class="plain">\n%s\n    </ul>\n  </div>\n'
           % "\n".join("      <li>%s</li>" % b(x) for x in setup),
           '  <div class="sec-label">Parte guidata · slide, veloce</div>\n  <div class="block teoria">\n    <div class="bhead"><span class="bnum">T</span><span class="btitle">%s</span><span class="btime">%s</span></div>\n    <ul class="plain">\n%s\n    </ul>\n    <div class="cue">Slide deck: %s</div>\n  </div>\n'
           % (teoria["titolo"], teoria["tempo"], "\n".join("      <li>%s</li>" % b(x) for x in teoria["punti"]), teoria["slide"]),
           '  <div class="sec-label">Parte pratica · cosa mostrare, in ordine</div>\n']
    for i, p in enumerate(passi, 1):
        out.append('  <div class="block pratica">\n    <div class="bhead"><span class="bnum">%d</span><span class="btitle">%s</span>%s</div>\n    <ul class="steps">\n%s\n    </ul>'
                   % (i, p["titolo"], ('<span class="btime">%s</span>' % p["tempo"]) if p.get("tempo") else "",
                      "\n".join("      <li>%s</li>" % b(x) for x in p["passi"])))
        if p.get("prompt"):
            out.append('    <div class="prompt"><b>Prompt (slide %d, da leggere per intero):</b> %s</div>' % (p["prompt"], html.escape(P[p["prompt"]], quote=False)))
        if p.get("dire"):
            out.append('    <div class="say"><b>Da dire:</b> %s</div>' % b(p["dire"]))
        if p.get("nota"):
            out.append('    <div class="note">%s</div>' % b(p["nota"]))
        if p.get("slide"):
            out.append('    <div class="cue">Slide deck: %s</div>' % p["slide"])
        out.append("  </div>\n")
    out.append("</div>\n</body>\n</html>\n")
    txt = "\n".join(out)
    assert "—" not in txt and "→" not in txt
    path = ROOT / ("%02d_Modulo_%d" % (n, n)) / ("Modulo_%d_guida_formatore.html" % n)
    path.write_text(txt, encoding="utf-8")
    print("scritto", path.name)


# ------------------------------------------------------------------ MODULO 2
render(2, "La scaletta da seguire: cosa mostrare sullo schermo, in ordine. Un'ora: 10 minuti da corsisti, 5 sotto il cofano, 6 sui passi 1 e 2, 33 di pratica. Leggere sempre i prompt per intero.",
    ["**Gemini** aperto su gemini.google.com, sull'account che si userà in aula. Provato il giorno prima.",
     "In un file: la richiesta vaga e quella completa della slide 9, e il prompt dell'intervista (slide 18).",
     "In un'altra scheda: la risposta di Gemini alla richiesta completa, già pronta.",
     "Il **quaderno**, scheda 1, stampato o condiviso."],
    {"titolo": "Apertura e patto dell'ora", "tempo": "2 minuti", "slide": "1-3",
     "punti": ["Il gancio (slide 2) non si risponde.",
               "Il patto: per dieci minuti sono docenti a un nostro corso. Poi cambiano sedia.",
               "**Non nominare le 4 mosse** fino alla slide 12."]},
    [{"titolo": "Da corsisti: il perché e lo strumento", "tempo": "4 minuti", "slide": "4-7",
      "passi": ["Slide 4: la domanda sulla delusione. Due risposte per alzata di mano.",
                "Passa a **Gemini**. Mostra la pagina iniziale: la casella dove si scrive, il **più** sotto la casella (i file, Canvas, Deep Research), la barra laterale con le chat.",
                "Indica dove sta l'assistente su misura **su questo account**: può chiamarsi Gem oppure Skill.",
                "Torna alle slide: la regola dei dati (slide 7), letta per intero."],
      "dire": "Non serve conoscere tutto il menu. Servono quattro cose: la chat, i file, Canvas, l'assistente che vi conosce."},
     {"titolo": "Da corsisti: il caso d'uso", "tempo": "3 minuti", "slide": "8-9",
      "passi": ["Slide 8: le 5 fasi, veloce.",
                "In Gemini, **chat nuova**. Incolla la richiesta vaga: \"Preparami un corso sull'intelligenza artificiale per i miei colleghi.\" Mostra la risposta: generica, lunga, uguale per tutti.",
                "**Chat nuova.** Incolla la richiesta completa (slide 9) e leggila ad alta voce mentre la incolli.",
                "Mostra cosa cambia: prima di scrivere, fa delle domande. Se ci mette troppo, apri la scheda con la risposta già pronta."],
      "dire": "Stesso strumento, stessa persona. È cambiato quello che gli abbiamo detto."},
     {"titolo": "Da corsisti: la prova lampo", "tempo": "3 minuti", "slide": "10",
      "passi": ["Ognuno apre Gemini e riscrive una richiesta propria, vera, di questa settimana.",
                "A coppie: il vicino dice quale delle 5 fasi manca.",
                "Chi non riesce a entrare lavora con il vicino. Non fermare l'aula."]},
     {"titolo": "Sotto il cofano", "tempo": "5 minuti", "slide": "11-14",
      "passi": ["Slide 11: \"Adesso cambiate sedia.\" Pausa.",
                "Slide 12: per ogni mossa, di' quale slide era.",
                "Slide 13: chiedi quanti corsi hanno seguito che somigliavano alla colonna di sinistra.",
                "Slide 14."],
      "dire": "Perché, funzione, caso d'uso, prova. In quest'ordine, per ogni cosa che insegnate."},
     {"titolo": "Passo 1: la scheda del pubblico", "tempo": "4 minuti", "prompt": 18, "slide": "15-19",
      "passi": ["Slide 15-17: le quattro domande e i ganci.",
                "In Gemini, **chat nuova**. Incolla il prompt dell'intervista e leggilo per intero.",
                "Rispondi alle prime due domande, in modo rapido, con un pubblico di esempio. Fai vedere che aspetta la risposta prima di chiedere altro.",
                "Non finire l'intervista: mostra la scheda compilata della slide 19."],
      "nota": "Far notare tre cose nel prompt: una domanda alla volta, il tetto di otto, **\"non mi servono i loro nomi\"**."},
     {"titolo": "Passo 2: il traguardo", "tempo": "2 minuti", "slide": "20-21",
      "passi": ["Slide 21: vago e verificabile.",
                "La regola: un **verbo**, un **oggetto finito**, una **scadenza**."]},
     {"titolo": "Tocca a voi", "tempo": "33 minuti", "slide": "22",
      "passi": ["15 minuti: l'intervista, in una chat nuova.",
                "8 minuti: correggono la scheda che esce.",
                "6 minuti: scrivono il traguardo in una frase.",
                "4 minuti: copiano tutto sulla scheda 1 del quaderno."],
      "dire": "Alla fine cosa hanno in mano? Se la risposta è \"conoscono\" o \"sanno\", riscrivetela.",
      "nota": "Il formatore gira e sblocca. **Riserva per chi finisce:** chiedere a Gemini quali tre cose della scheda sono supposizioni e non fatti."},
     {"titolo": "Chiusura", "tempo": "4 minuti", "slide": "23",
      "passi": ["Due o tre leggono il proprio traguardo. La stanza dice se si può verificare.",
                "Aggancio al modulo 3: su cosa li fate lavorare, e in che ordine."]}])

# ------------------------------------------------------------------ MODULO 4
render(4, "La scaletta da seguire: cosa mostrare sullo schermo, in ordine. Un'ora: 24 minuti di guida, 33 di pratica, 3 di chiusura. **Il giorno prima va controllato se l'account mostra Gem o Skill.**",
    ["**Verificato il giorno prima:** sull'account compare **Gem**, **Skill** o nessuno dei due. I percorsi sono due, vedi il passo 1.",
     "Lo **Scrittore di prompt** e il **Progettista di percorsi** già costruiti sul proprio account.",
     "I testi delle istruzioni in un file condiviso (`Asset_Assistente_Scrittore_di_Prompt.md`, `Asset_Assistente_Progettista_di_Percorsi.md`).",
     "Una scheda del pubblico di esempio, con il traguardo.",
     "In un'altra scheda: la risposta dei dieci casi d'uso e quella della sequenza, già pronte."],
    {"titolo": "Apertura, perché, la funzione", "tempo": "8 minuti", "slide": "1-7",
     "punti": ["Chiedi chi ha con sé i tre casi d'uso scritti a mano nel modulo 3.",
               "Slide 4: il contesto si scrive una volta.",
               "Slide 6: **apri Gemini e fai vedere dove sta l'assistente su questo account** (passo 1 qui sotto).",
               "Slide 7: fermati. È una slide su come si insegna, non su Gemini."]},
    [{"titolo": "Dove si trova l'assistente", "tempo": "dentro gli 8 minuti", "slide": "6",
      "passi": ["**Se l'account mostra Skill:** barra laterale, **Personalizza**, **Skill**, **Crea**, **Crea manualmente**. Campi: nome, descrizione, istruzioni, file. In chat si richiama scrivendo **@** e il nome.",
                "**Se l'account mostra ancora Gem:** dalle **Impostazioni**, **Gem**, **Nuovo Gem**. Campi: nome, istruzioni, conoscenza. Poi **Salva**.",
                "**Se non c'è nessuno dei due:** si va avanti lo stesso. Il testo si incolla come prima riga di una chat normale (slide 17)."],
      "dire": "Cambia il nome e cambia il menu. Quello che ci scrivete dentro è identico.",
      "nota": "I nomi dei menu sono quelli verificati il 16 novembre 2026. **L'interfaccia cambia:** il riferimento buono è quello del giorno prima."},
     {"titolo": "Caso d'uso 1: lo Scrittore di prompt", "tempo": "4 minuti", "prompt": 9, "slide": "8-9",
      "passi": ["Slide 9: leggi il testo per intero.",
                "Costruiscilo dal vivo: nome **Scrittore di prompt**, incolla le istruzioni, nessun file, salva. Tre minuti.",
                "Provalo subito: \"Mi serve una verifica di storia sulla Prima guerra mondiale per la terza media.\"",
                "Mostra che torna con due domande, poi con il prompt completo."],
      "dire": "È il primo oggetto che farete costruire ai colleghi. Serve dal primo giorno e toglie la paura del foglio bianco."},
     {"titolo": "Caso d'uso 2: il Progettista di percorsi", "tempo": "8 minuti", "prompt": 13, "slide": "10-15",
      "passi": ["Slide 11 e 12: le istruzioni. Leggi per intero la **parte 2**: è il metodo in sei regole.",
                "Apri il Progettista **già costruito** (non costruirlo in diretta).",
                "Incolla il prompt dei casi d'uso (slide 13) con la scheda del pubblico di esempio.",
                "Commenta la risposta: quali ha scartato perché toccano dati personali? Quali tre propone?",
                "Nella stessa chat incolla il prompt della sequenza (slide 14). Mentre scrive, passa alla slide 15."],
      "dire": "La prima versione metteva lo strumento nel primo incontro. L'abbiamo spostato noi. L'assistente fa la bozza, il percorso lo decidete voi.",
      "nota": "Se la risposta tarda, apri la scheda con quella già pronta."},
     {"titolo": "Piano B e sotto il cofano", "tempo": "4 minuti", "slide": "16-18",
      "passi": ["Slide 17: il piano B, detto con calma.",
                "Slide 18: le 4 mosse di nuovo. E la scelta in più: il primo oggetto costruito scrive tutti gli altri."]},
     {"titolo": "Tocca a voi", "tempo": "33 minuti", "slide": "19",
      "passi": ["3 minuti: costruiscono lo Scrittore di prompt.",
                "7 minuti: costruiscono il Progettista (parte 1 e parte 2, una di seguito all'altra).",
                "10 minuti: dieci casi d'uso. Li confrontano con i tre scritti a mano. Tengono i tre migliori.",
                "10 minuti: la sequenza. La correggono.",
                "3 minuti: la copiano sulla scheda 2 del quaderno."],
      "dire": "Quale caso avevate scritto voi, e lui non ha proposto? Cosa avete cambiato nella sequenza?",
      "nota": "**Chi è bloccato sull'accesso** lavora in coppia o con il piano B. **Riserva per chi finisce:** chiedere quale incontro taglierebbe con metà del tempo."},
     {"titolo": "Chiusura", "tempo": "3 minuti", "slide": "20",
      "passi": ["\"Cosa avete corretto?\" Due risposte.", "Aggancio al modulo 5: com'è fatta un'ora di lezione."]}])

# ------------------------------------------------------------------ MODULO 6
render(6, "La scaletta da seguire: cosa mostrare sullo schermo, in ordine. Un'ora: 22 minuti di guida, 33 di pratica, 5 di condivisione. Leggere sempre i prompt per intero.",
    ["**Canvas** provato il giorno prima sull'account che si userà: dove si apre, cosa esporta.",
     "Il **Progettista di percorsi** del modulo 4, funzionante.",
     "In un'altra scheda: una scaletta di esempio già generata e corretta.",
     "In un'altra scheda: le slide di esempio già generate, aperte in Presentazioni.",
     "I tre prompt (slide 6, 9, 10) in un file condiviso."],
    {"titolo": "Apertura e perché", "tempo": "3 minuti", "slide": "1-4",
     "punti": ["Slide 2: scrivi alla lavagna due o tre dei numeri che dicono. Si riprendono alla fine.",
               "Slide 4: prima la scaletta, poi le slide. Il deck è l'ultima cosa che si fa."]},
    [{"titolo": "Apri Canvas", "tempo": "3 minuti", "slide": "5",
      "passi": ["In Gemini, dentro il **Progettista**. Sotto la casella di testo, il **più** (\"Aggiungi file\"), poi **Canvas**.",
                "Mostra il pannello che si apre a fianco della chat.",
                "Di' le tre cose: si apre a fianco, si corregge riga per riga, esce da Gemini."],
      "dire": "Non è un altro strumento. È la stessa chat, con un foglio accanto."},
     {"titolo": "Caso d'uso 1: la scaletta", "tempo": "6 minuti", "prompt": 6, "slide": "6-8",
      "passi": ["Leggi il prompt per intero. Fai notare le tre sezioni in fondo.",
                "Incollalo, con un incontro di esempio al posto delle parentesi quadre. Invia.",
                "Mentre scrive: slide 7, com'è fatta una scaletta che regge. Mostra quella che hai in mano.",
                "Torna a Canvas. **Seleziona un blocco** e chiedi: \"questo blocco dura troppo, portalo a sei minuti e togli il secondo esempio\".",
                "Mostra **Condividi ed esporta**, poi **Esporta in Documenti**.",
                "Slide 8: tempi onesti. Somma i minuti della scaletta a schermo, davanti a loro."],
      "dire": "È quello che distingue una scaletta da un indice: cosa proteggere, le riserve, cosa preparare."},
     {"titolo": "Caso d'uso 2: le slide", "tempo": "3 minuti", "prompt": 9, "slide": "9",
      "passi": ["Leggi il prompt. Fai notare: quattro tipi di slide, e prima l'elenco dei titoli.",
                "Incollalo nella stessa chat. Mostra l'elenco dei titoli che arriva.",
                "**Non generare le slide in diretta.** Apri la scheda con quelle già pronte, in Presentazioni."],
      "dire": "Le slide che escono vanno rifinite a mano. Gemini vi dà la struttura, non il deck finito.",
      "nota": "Sugli account della scuola le presentazioni generate al giorno sono limitate: una a testa basta."},
     {"titolo": "Caso d'uso 3: il foglio dei prompt", "tempo": "4 minuti", "prompt": 10, "slide": "10-11",
      "passi": ["Leggi il prompt.",
                "Slide 11: le tre regole. Per intero, provati prima, letti ad alta voce."],
      "dire": "Una volta abbiamo messo in slide il riassunto di un prompt invece del testo. Non serviva a nessuno."},
     {"titolo": "Chi fa cosa, sotto il cofano", "tempo": "3 minuti", "slide": "12-13",
      "passi": ["Slide 12: gli esempi veri vengono dai colleghi, non da Gemini.",
                "Slide 13: tre casi mostrati, una prova sola."]},
     {"titolo": "Tocca a voi", "tempo": "33 minuti", "slide": "14",
      "passi": ["12 minuti: la scaletta di **un solo incontro**. La correggono: i minuti si sommano? La pratica è almeno metà?",
                "10 minuti: l'elenco delle slide. Ogni blocco comincia con una domanda?",
                "8 minuti: il foglio dei prompt. Ne provano almeno uno in una chat nuova.",
                "3 minuti: esportano la scaletta e la segnano sulla scheda 3 del quaderno."],
      "dire": "Fammi vedere la somma dei minuti. Qual è la domanda che apre? Hai provato un prompt?",
      "nota": "**Se Canvas non c'è o non risponde:** tutto funziona anche nella chat normale. Si copia il testo in un documento."},
     {"titolo": "Condivisione e chiusura", "tempo": "5 minuti", "slide": "15-16",
      "passi": ["\"Quanto ci avete messo? E cosa avete dovuto correggere voi?\" Riprendi i numeri della lavagna.",
                "Aggancio al modulo 7: l'incontro c'è, la prossima volta si porta davanti a delle persone."]}])

# ------------------------------------------------------------------ MODULO 8
render(8, "La scaletta da seguire: cosa mostrare sullo schermo, in ordine. Un'ora: 22 minuti di guida, 33 di pratica, 5 di chiusura. **La ricerca si lancia al minuto 5 e si riapre al minuto 18.**",
    ["**Deep Research** provata il giorno prima sull'account che si userà. Verificare se è attiva e quante ricerche concede.",
     "In un'altra scheda: un rapporto già pronto, con una fonte già individuata da aprire dal vivo.",
     "I tre prompt (slide 6, 9, 11) in un file condiviso.",
     "Le tre risposte con l'errore già generate su un compito di esempio, con la **soluzione verificata**.",
     "Un dato di esempio da verificare in diretta."],
    {"titolo": "Apertura e perché", "tempo": "4 minuti", "slide": "1-4",
     "punti": ["Slide 3: i tre errori nostri, raccontati con i dettagli. Li abbiamo trovati perché abbiamo aperto le fonti.",
               "Slide 4: davanti a degli insegnanti, un dato sbagliato costa tutto il resto."]},
    [{"titolo": "Funzione 1: Deep Research", "tempo": "6 minuti", "prompt": 6, "slide": "5-7",
      "passi": ["In Gemini, **chat nuova**. Sotto la casella, il **più**, poi **Deep Research**.",
                "Incolla il prompt con il dato di esempio. Leggilo per intero.",
                "Gemini propone un **piano di ricerca**: mostralo, poi **Avvia ricerca**.",
                "**Non aspettare.** Torna alle slide: la regola dei tre controlli (slide 7).",
                "Apri la scheda con il rapporto già pronto: mostra i link accanto alle frasi. **Aprine uno**, davanti a loro."],
      "dire": "Vi dà i link, non la verità. Aprirli resta un lavoro vostro.",
      "nota": "Sugli account della scuola le ricerche sono contate e serve la maggiore età. **Chi non ce l'ha** usa lo stesso prompt in una chat normale."},
     {"titolo": "Funzione 2: il collega difficile", "tempo": "4 minuti", "prompt": 9, "slide": "8-9",
      "passi": ["**Chat nuova**, normale. Incolla il prompt e leggilo.",
                "Rispondi una volta sola, come faresti in aula.",
                "Mostra che insiste. Non finire i tre scambi."],
      "dire": "Nel modulo 7 l'avete fatto fra di voi. Questo serve la sera prima, quando un collega per provare non c'è."},
     {"titolo": "Funzione 3: la demo che non tradisce", "tempo": "4 minuti", "prompt": 11, "slide": "10-11",
      "passi": ["Slide 10: i tre materiali di una demo.",
                "Leggi il prompt (slide 11). Mostra le tre risposte già generate.",
                "Chiedi alla stanza: \"Quale usereste?\" Poi mostra la soluzione."],
      "dire": "Chi trova l'errore ha appena capito perché serve un insegnante.",
      "nota": "**Controllare sempre la soluzione.** L'errore lo sceglie Gemini: va verificato che sia davvero un errore."},
     {"titolo": "Lista dei controlli, sotto il cofano", "tempo": "4 minuti", "slide": "12-13",
      "passi": ["Slide 12: le cinque righe.",
                "**Riapri la ricerca lanciata al minuto 5.** Mostra il giudizio finale in una riga.",
                "Slide 13: un perché solo, tre funzioni, una prova alla fine."]},
     {"titolo": "Tocca a voi", "tempo": "33 minuti", "slide": "14",
      "passi": ["3 minuti: **per prima cosa** lanciano la ricerca sul proprio dato.",
                "10 minuti: il collega difficile, sull'obiezione che temono di più.",
                "8 minuti: le tre risposte con l'errore, su un loro caso d'uso. Controllano la soluzione.",
                "7 minuti: riaprono la ricerca, aprono almeno una fonte, scrivono il giudizio.",
                "5 minuti: la lista dei controlli, scheda 5 del quaderno."],
      "dire": "L'hai aperta, la fonte?",
      "nota": "**Riserva per chi non ha un dato:** verificare \"l'81% degli studenti italiani usa l'IA\"."},
     {"titolo": "Chiusura", "tempo": "5 minuti", "slide": "15-16",
      "passi": ["\"Chi ha scoperto che il suo dato non si poteva usare così com'era?\"",
                "Di' con precisione cosa portare al modulo 9: **sei minuti** della propria lezione."]}])

# ------------------------------------------------------------------ MODULO 9
render(9, "La scaletta da seguire. Un'ora: 9 minuti di regole, 36 di prova, 7 di condivisione, 8 di chiusura. **Al minuto 9 il primo deve stare conducendo.**",
    ["La **scheda 4** del quaderno, tre copie a testa.",
     "I gruppi da quattro già pensati, misti per ordine di scuola se possibile.",
     "Un cronometro per gruppo.",
     "A distanza: le stanze separate da quattro, già create."],
    {"titolo": "Apertura e regole", "tempo": "9 minuti", "slide": "1-8",
     "punti": ["Slide 3: sei minuti, tre minuti, quattro turni. Dillo due volte.",
               "Slide 5: chi osserva guarda **solo** le quattro domande della griglia.",
               "Slide 6: una cosa da tenere, una da cambiare. Chi riceve ascolta e ringrazia.",
               "Slide 8: **forma i gruppi adesso.**"]},
    [{"titolo": "La prova", "tempo": "36 minuti", "slide": "9",
      "passi": ["Minuto 0: parte il primo. Gli altri fanno i corsisti e compilano la scheda 4.",
                "Minuto 6: **stop**, anche a metà frase. Tre minuti di riscontro.",
                "Minuto 9: secondo turno. Minuto 18: terzo. Minuto 27: quarto.",
                "Annuncia tu ogni cambio, a voce o con un messaggio a tutte le stanze."],
      "dire": "Qui si può sbagliare. È il posto giusto per farlo.",
      "nota": "**Non intervenire** durante i sei minuti. Gira, ascolta, segnati due o tre cose viste, senza nomi. **Chi non ha preparato niente** conduce le slide 4-10 del modulo 2."},
     {"titolo": "Condivisione", "tempo": "7 minuti", "slide": "10",
      "passi": ["\"Cosa avete visto fare a un collega che da domani farete anche voi?\" Cinque o sei risposte.",
                "Aggiungi le cose che hai visto tu, come \"ho visto qualcuno fare\".",
                "\"E cosa vi hanno detto di cambiare, che non vi aspettavate?\""]},
     {"titolo": "Il dopo e la chiusura", "tempo": "8 minuti", "prompt": 11, "slide": "11-14",
      "passi": ["Slide 11: leggi il prompt. Si usa stasera, dentro il Progettista.",
                "Slide 12: breve, vero, con un riscontro subito.",
                "Slide 13: cosa portare all'ultimo modulo: la lezione corretta e il quaderno."],
      "dire": "Tre modifiche, non trenta."}])
