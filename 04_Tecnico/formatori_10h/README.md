# Tooling del percorso Formatori 10h

Gli script con cui sono stati prodotti i deck, le guide e la consegna di `02_Percorsi/10h/Formatori_10h/`.

> ⚠ **La sorgente dei deck resta l'HTML**, come per tutti gli altri percorsi: le revisioni `slide N: vecchio, nuovo` si fanno sul file `Modulo_N.html`.
> I file `mNN.py` servono solo per rigenerare un deck **da zero**, per esempio quando si aggiungono o si spostano slide e va rifatta la numerazione. **Rilanciarli sovrascrive il deck:** una correzione fatta a mano sull'HTML va riportata prima nel `.py`, altrimenti si perde.

| File | Cosa fa |
|---|---|
| `deckkit.py`, `base.css` | Il kit dei tipi di slide. `base.css` è il CSS del deck Gemini del 10h, senza modifiche |
| `common.py` | Titoli dei moduli, cartella di destinazione, i testi dei due assistenti |
| `m01.py` … `m10.py` | Il contenuto di ogni deck, una riga per slide. `python3 m03.py` rigenera `Modulo_3.html` |
| `guide.py` | Rigenera le cinque guide pratiche. I prompt li legge dai deck |
| `estrai_prompt.py` | Rilegge i deck e riscrive `PROMPT_PRONTI.md` e i due `Asset_Assistente_*.md`, identici alle slide. **Va lanciato dopo ogni correzione a un prompt**, anche se fatta a mano sull'HTML |
| `consegna.py` | Riassembla `_Consegna/` con tutti i PDF e lo zip. Uso: `python3 consegna.py /tmp/consegna_tmp`. Usa Chrome senza interfaccia: gli sfondi escono corretti |
| `sheet.py` | Mette le pagine di un PDF in un foglio di miniature, per controllare l'impaginazione a colpo d'occhio |

Servono Python 3, i moduli `markdown` e `pymupdf`, e Google Chrome.
