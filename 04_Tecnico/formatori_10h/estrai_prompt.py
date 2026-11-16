# -*- coding: utf-8 -*-
"""Rilegge i deck del percorso Formatori e riscrive, identici alle slide:
   Materiali/PROMPT_PRONTI.md e i due Asset_Assistente_*.md del modulo 4.
   Da lanciare dopo ogni correzione a un prompt sulle slide:  python3 estrai_prompt.py"""
import re, html, pathlib
P = pathlib.Path(__file__).resolve().parents[2] / "02_Percorsi/10h/Formatori_10h"
TIT = {2: "Gemini: la base, fatta bene", 4: "L'assistente che vi conosce", 6: "Dalla scaletta ai materiali", 8: "La demo, i dati, le obiezioni", 9: "Sei minuti in aula"}


def clean(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    return html.unescape(re.sub(r"<[^>]+>", "", s)).strip()


out = ["# Prompt pronti · Percorso Formatori 10h", "",
       "> Tutti i testi da copiare del percorso, **identici a quelli sulle slide**. Sono estratti dai deck: se si corregge un prompt, si corregge sulla slide e si rigenera questo file.",
       "> Le parti fra parentesi quadre sono quelle che ognuno cambia. Ogni prompt va provato sull'account che si userà in aula, il giorno prima.", ""]
store = {}
for n in (2, 4, 6, 8, 9):
    t = (P / ("%02d_Modulo_%d" % (n, n)) / ("Modulo_%d.html" % n)).read_text(encoding="utf-8")
    out += ["---", "", "## Modulo %d · %s" % (n, TIT[n]), ""]
    for m in re.finditer(r'<!-- SLIDE (\d+) · DA COPIARE -->.*?<div class="chip[^"]*">(.*?)</div>.*?<div class="title">(.*?)</div>.*?<div class="copysub">(.*?)</div>.*?<div class="codebox[^"]*"[^>]*>(.*?)</div>\s*<div class="foot">', t, re.S):
        num, title, sub, body = m.group(1), clean(m.group(3)), clean(m.group(4)), clean(m.group(5)).strip('"')
        store[(n, int(num))] = body
        out += ["### %s (slide %s)" % (title, num), "", "*%s*" % sub, "", "```", body, "```", ""]
(P / "Materiali/PROMPT_PRONTI.md").write_text("\n".join(out), encoding="utf-8")
NOTA = "> Testo da incollare nelle istruzioni dell'assistente su misura di Gemini (Gem oppure Skill, a seconda di cosa mostra l'account)."
a = ["# Assistente · Scrittore di prompt", "", NOTA,
     "> È lo stesso testo dei percorsi da 10 ore per docenti e segreteria: uguale per tutti, tre minuti di lavoro.",
     "> **Nome:** Scrittore di prompt. **File:** nessuno. **Piano B:** se l'assistente non è disponibile, si incolla questo testo come prima riga di una chat normale.", "",
     "```", store[(4, 9)], "```", ""]
(P / "04_Modulo_4/Asset_Assistente_Scrittore_di_Prompt.md").write_text("\n".join(a), encoding="utf-8")
a = ["# Assistente · Progettista di percorsi", "", NOTA,
     "> Contiene il metodo del percorso in sei regole. Le due parti si incollano una di seguito all'altra, nello stesso campo.",
     "> **Nome:** Progettista di percorsi. **File da aggiungere, se l'account lo permette:** la scheda del pubblico. **Piano B:** se l'assistente non è disponibile, si incolla questo testo come prima riga di una chat normale.",
     "> ⚠ Da provare una volta sull'account prima dell'aula: è stato scritto e riletto, non ancora provato dentro Gemini.", "",
     "## Parte 1 · Chi è e come lavora", "", "```", store[(4, 11)], "```", "",
     "## Parte 2 · Il metodo che segue", "", "```", store[(4, 12)], "```", ""]
(P / "04_Modulo_4/Asset_Assistente_Progettista_di_Percorsi.md").write_text("\n".join(a), encoding="utf-8")
print(len(store), "prompt riscritti")
