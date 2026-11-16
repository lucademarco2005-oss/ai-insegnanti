# -*- coding: utf-8 -*-
"""Kit per generare i deck HTML del percorso Formatori nello stile AI Insegnanti.
Usa il CSS dei deck esistenti (base.css, preso dal deck Gemini 10h) piu' le classi
dei deck teorici (stat, quote, bigicon, pex). Nessuna classe di stile inventata,
tranne .pcard p e .rowcards (varianti di posizione di blocchi gia' esistenti)."""
import re, pathlib

HERE = pathlib.Path(__file__).parent
BASE_CSS = (HERE / "base.css").read_text(encoding="utf-8")

EXTRA_CSS = """
  /* dati (dai deck teorici) */
  .datawrap{position:absolute;top:30cqh;left:5.5cqw;right:5.5cqw;display:flex;gap:3cqh;}
  .stat{flex:1;border-radius:2.6cqh;padding:4cqh 2cqh;text-align:center;}
  .stat.dark{background:var(--ink);} .stat.lite{background:#fff;border:1.5px solid var(--line);}
  .stat .num{font-size:16cqh;font-weight:800;line-height:1;}
  .stat .lab{font-size:3.2cqh;margin-top:2cqh;}
  .stat.sm .num{font-size:11cqh;} .stat.sm .lab{font-size:2.7cqh;}

  /* citazione */
  .qmark{position:absolute;top:6cqh;left:3.5cqw;font-size:46cqh;font-weight:800;color:var(--cyan);font-family:Georgia,serif;line-height:1;}
  .quote{position:absolute;top:30cqh;left:11cqw;right:8cqw;font-size:5.8cqh;font-weight:800;color:#fff;line-height:1.12;}
  .qgloss{position:absolute;top:60cqh;left:11.4cqw;right:8cqw;font-size:2.9cqh;color:var(--cfcb);line-height:1.25;}
  .qauth{position:absolute;top:78cqh;left:11.4cqw;font-size:3.2cqh;}

  /* big icon + text (analogia) */
  .bigicon{position:absolute;top:36cqh;left:7cqw;width:24cqh;height:24cqh;border-radius:50%;
           display:flex;align-items:center;justify-content:center;font-size:12cqh;}
  .bigtext{position:absolute;top:34cqh;left:33cqw;right:6cqw;font-size:3.5cqh;color:var(--text);line-height:1.3;}
  .bigquote{position:absolute;top:78cqh;left:33cqw;right:6cqw;font-size:2.9cqh;font-style:italic;font-weight:700;}

  /* esempi: fatto male / fatto bene */
  .pex{position:absolute;left:5.5cqw;right:5.5cqw;border-radius:1.8cqh;padding:2.4cqh 3cqh;background:#fff;border:1px solid var(--line);box-shadow:0 4px 14px rgba(80,70,160,.08);}
  .pex .lab{font-size:2.2cqh;font-weight:700;letter-spacing:.1em;text-transform:uppercase;margin-bottom:1cqh;}
  .pex.bad{top:22cqh;border-left:7px solid var(--muted);}
  .pex.bad .lab{color:var(--muted);}
  .pex.bad .txt{font-size:3cqh;color:var(--text);font-style:italic;line-height:1.3;}
  .pex.good{top:39cqh;border:1.5px solid var(--indigo);border-left:7px solid var(--indigo);}
  .pex.good .lab{color:var(--indigo);}
  .pex.good .txt{font-size:2.55cqh;color:var(--text);line-height:1.34;}
  .pex-tags{position:absolute;left:5.5cqw;right:5.5cqw;top:80cqh;font-size:2.4cqh;color:var(--muted);font-weight:600;}
  .pex-tags b{color:var(--indigo);font-weight:700;}

  /* fila di passi (stesse card del ponte, piu' in alto e con una riga di testo) */
  .pcards.rowcards{top:31cqh;}
  .pcards.rowcards .pnum{width:9cqh;height:9cqh;font-size:4.2cqh;margin-bottom:1.6cqh;}
  .pcard p{font-size:2.6cqh;color:var(--muted);line-height:1.28;margin-top:1cqh;}
"""

# ---------- mini markup ----------
_COL = {"cy": "cy", "co": "co", "in": "in", "vi": "vi", "ink": "inkc", "mu": "mu", "wh": "wh"}


def mk(s):
    """{cy:testo} -> span colorato, {b:testo} -> grassetto, | -> a capo."""
    if s is None:
        return ""
    def rep(m):
        k, v = m.group(1), m.group(2)
        if k == "b":
            return "<strong>%s</strong>" % v
        if k == "slot":
            return '<span class="slot">%s</span>' % v
        return '<span class="%s">%s</span>' % (_COL[k], v)
    for _ in range(3):
        s = re.sub(r"\{(cy|co|in|vi|ink|mu|wh|b|slot):([^{}]*)\}", rep, s)
    return s.replace("|", "<br>")


def var(c):
    return "var(--%s)" % c


CIRC_COVER = (
    '<div class="circ" style="top:-19%;left:78%;width:34%;height:60%;background:var(--indigo);opacity:.45;"></div>\n'
    '    <div class="circ" style="top:58%;left:88%;width:25%;height:45%;background:var(--violet);opacity:.4;"></div>\n'
    '    <div class="circ" style="top:70%;left:-8%;width:24%;height:42%;background:var(--cyan);opacity:.3;"></div>')
CIRC_HOOK = '<div class="circ" style="top:-20%;left:75%;width:38%;height:66%;background:#fff;opacity:.08;"></div>'
CIRC_DEB = ('<div class="circ" style="top:-21%;left:80%;width:38%;height:67%;background:#fff;opacity:.12;"></div>\n'
            '    <div class="circ" style="top:62%;left:-10%;width:30%;height:53%;background:var(--ink);opacity:.2;"></div>')
DOTS = ('<span style="background:var(--cyan)"></span><span style="background:var(--indigo)"></span>'
        '<span style="background:var(--violet)"></span><span style="background:var(--coral)"></span>')


class Deck:
    def __init__(self, title, foot, note, cover_foot="Formazione docenti sull'Intelligenza Artificiale · PNRR DM 219/2025"):
        self.title, self.foot, self.note, self.cover_foot = title, foot, note, cover_foot
        self.slides = []  # (label, bg, body, dark)

    def _add(self, label, bg, body, dark):
        self.slides.append((label, bg, body, dark))

    # ----- tipi di slide -----
    def cover(self, eyebrow, title, sub):
        b = ('%s\n    <div class="eyebrow">%s</div>\n    <div class="cover-title">%s</div>\n'
             '    <div class="cover-bar"></div>\n    <div class="cover-sub">%s</div>\n'
             '    <div class="dots" style="top:74%%;left:5.6%%;">%s</div>\n    <div class="cover-foot">%s</div>'
             % (CIRC_COVER, mk(eyebrow), mk(title), mk(sub), DOTS, self.cover_foot))
        self._add("COPERTINA", "ink", b + "{NOPN}", True)

    def hook(self, eyebrow, q, sub=None, label="GANCIO", size=None):
        st = ' style="font-size:%scqh;"' % size if size else ""
        b = '%s\n    <div class="hook-eyebrow">%s</div>\n    <div class="hook-q wh"%s>%s</div>' % (CIRC_HOOK, mk(eyebrow), st, mk(q))
        if sub:
            b += '\n    <div class="deb-sub" style="color:#D9D5F2;">%s</div>' % mk(sub)
        self._add(label, "indigobg", b, True)

    def stmt(self, chip, text, chipcolor="violet", size=None, label="STATEMENT"):
        st = ' style="font-size:%scqh;"' % size if size else ""
        b = ('<div class="chip %s">%s</div>\n    <div class="stbar"></div>\n    <div class="statement wh"%s>%s</div>'
             % (chipcolor, mk(chip), st, mk(text)))
        self._add(label, "ink", b, True)

    def closing(self, chip, text, size="6.4", label="CHIUSURA"):
        b = ('%s\n    <div class="chip violet">%s</div>\n    <div class="stbar"></div>\n'
             '    <div class="statement wh" style="font-size:%scqh;">%s</div>\n'
             '    <div class="dots" style="top:80%%;left:6.6%%;">%s</div>' % (CIRC_COVER, mk(chip), size, mk(text), DOTS))
        self._add(label, "ink", b, True)

    def cards(self, chip, title, items, chipcolor="indigo", takeaway=None, label="CONCETTO", compact=None):
        """items: (icona, colore, titolo, testo)."""
        if compact is None:
            compact = len(items) >= 4 or takeaway is not None
        out = []
        for ic, col, h, p in items:
            if compact:
                out.append('<div class="card" style="padding:2.1cqh 3cqh;"><div class="card-ic" style="background:%s;width:7cqh;height:7cqh;font-size:3.2cqh;">%s</div>'
                           '<div><h3 style="font-size:3cqh;margin:0">%s</h3><p>%s</p></div></div>' % (var(col), ic, mk(h), mk(p)))
            else:
                out.append('<div class="card"><div class="card-ic" style="background:%s">%s</div><div><h3>%s</h3><p>%s</p></div></div>'
                           % (var(col), ic, mk(h), mk(p)))
        style = ' style="top:30cqh;gap:1.8cqh;"' if compact else ""
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="cards"%s>\n      %s\n    </div>'
             % (chipcolor, mk(chip), mk(title), style, "\n      ".join(out)))
        if takeaway:
            b += '\n    <div class="takeaway" style="top:81cqh;">%s</div>' % mk(takeaway)
        self._add(label, "light", b, False)

    def row(self, chip, title, items, chipcolor="indigo", takeaway=None, label="PASSI"):
        """items: (numero o icona, colore, titolo, testo)."""
        out = []
        for n, col, h, p in items:
            out.append('<div class="pcard"><div class="pnum" style="background:%s">%s</div><h3>%s</h3>%s</div>'
                       % (var(col), n, mk(h), ("<p>%s</p>" % mk(p)) if p else ""))
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="pcards rowcards">\n      %s\n    </div>'
             % (chipcolor, mk(chip), mk(title), "\n      ".join(out)))
        if takeaway:
            b += '\n    <div class="takeaway" style="top:81cqh;">%s</div>' % mk(takeaway)
        self._add(label, "light", b, False)

    def cols(self, chip, title, left, right, chipcolor="indigo", takeaway=None, label="CONFRONTO"):
        """left/right: (testata, colore, lista di voci oppure stringa)."""
        def col(c):
            head, color, content = c
            cd = {"coral": "cdcoral", "cyan": "cdcyan", "indigo": "cdindigo", "muted": "cdmuted", "violet": "cdindigo", "ink": "cdindigo"}[color]
            if isinstance(content, str):
                inner = '<div class="para" style="font-size:2.8cqh;line-height:1.3;">%s</div>' % mk(content)
            else:
                inner = "<ul>%s</ul>" % "".join("<li><span>%s</span></li>" % mk(x) for x in content)
            return '<div class="col %s"><div class="col-head" style="background:%s">%s</div>%s</div>' % (cd, var(color), mk(head), inner)
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="cols">\n      %s\n      %s\n    </div>'
             % (chipcolor, mk(chip), mk(title), col(left), col(right)))
        if takeaway:
            b += '\n    <div class="takeaway" style="top:82cqh;">%s</div>' % mk(takeaway)
        self._add(label, "light", b, False)

    def stat(self, chip, title, stats, takeaway, source, chipcolor="cyan", label="DATO", small=False):
        """stats: (numero, didascalia, 'dark'|'lite')."""
        out = []
        for i, (num, lab, kind) in enumerate(stats):
            nc, lc = ("cy", "wh") if kind == "dark" else ("co", "tx")
            out.append('<div class="stat %s%s"><div class="num %s">%s</div><div class="lab %s">%s</div></div>'
                       % (kind, " sm" if small else "", nc, num, lc, mk(lab)))
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="datawrap">\n      %s\n    </div>\n'
             '    <div class="takeaway">%s</div>' % (chipcolor, mk(chip), mk(title), "\n      ".join(out), mk(takeaway)))
        self._add(label, "light", b, False)
        self.slides[-1] = (label, "light", b + "{SRC:%s}" % source, False)

    def quote(self, text, gloss, author, work, label="CITAZIONE", size=None):
        st = ' style="font-size:%scqh;"' % size if size else ""
        b = ('<div class="circ" style="top:-19%%;left:78%%;width:34%%;height:60%%;background:var(--indigo);opacity:.4;"></div>\n'
             '    <div class="qmark">“</div>\n    <div class="quote wh"%s>%s</div>\n    <div class="qgloss">%s</div>\n'
             '    <div class="qauth"><strong class="cy">%s</strong><span style="color:var(--cfcb)">&nbsp;&nbsp;·&nbsp;&nbsp;%s</span></div>'
             % (st, mk(text), mk(gloss), mk(author), mk(work)))
        self._add(label, "ink", b, True)

    def analogy(self, chip, title, icon, color, text, quote, chipcolor="violet", label="ANALOGIA"):
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="bigicon" style="background:%s">%s</div>\n'
             '    <div class="bigtext">%s</div>\n    <div class="bigquote vi">%s</div>' % (chipcolor, mk(chip), mk(title), var(color), icon, mk(text), mk(quote)))
        self._add(label, "light", b, False)

    def debate(self, q, sub=None, room="Parla la stanza", tag="DIBATTITO", flag=False, small=False, label="DIBATTITO"):
        left = round(8.5 + (len(tag) * 2.05 + 4.8) / 1.778, 1)
        b = ('%s\n    <div class="deb-tag">%s</div><div class="deb-room" style="left:%scqw;">%s</div>\n    <div class="deb-q%s wh">%s</div>'
             % (CIRC_DEB, tag, left, mk(room), " sm" if small else "", mk(q)))
        if sub:
            b += '\n    <div class="deb-sub">%s</div>' % mk(sub)
        if flag:
            b += ('\n    <div class="flag onbg"><b>Se avanza tempo</b><span>Altrimenti resta uno spunto: ci ragionate voi.</span></div>')
        self._add(label, "coralbg", b, True)

    def practice(self, chip, text, sub, size="6.2", label="PRATICA"):
        b = ('<div class="circ" style="top:-20%%;left:75%%;width:38%%;height:66%%;background:#fff;opacity:.10;"></div>\n'
             '    <div class="circ" style="top:62%%;left:-10%%;width:30%%;height:53%%;background:var(--ink);opacity:.16;"></div>\n'
             '    <div class="chip" style="background:#fff;color:var(--coral)">%s</div>\n'
             '    <div class="statement wh" style="font-size:%scqh;">%s</div>\n    <div class="deb-sub">%s</div>'
             % (mk(chip), size, mk(text), mk(sub)))
        self._add(label, "coralbg", b, True)

    def code(self, chip, title, sub, text, sm=False, chipcolor="indigo", label="DA COPIARE", size=None):
        st = ' style="font-size:%scqh;"' % size if size else ""
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="copysub">%s</div>\n'
             '    <div class="codebox%s"%s>%s</div>' % (chipcolor, mk(chip), mk(title), mk(sub), " sm" if sm else "", st, mk(text)))
        self._add(label, "light", b, False)

    def pex(self, chip, bad, good, tags, badlab="Fatto male", goodlab="Fatto bene", label="ESEMPIO"):
        b = ('<div class="chip indigo">%s</div>\n    <div class="pex bad"><div class="lab">%s</div><div class="txt">%s</div></div>\n'
             '    <div class="pex good"><div class="lab">%s</div><div class="txt">%s</div></div>\n    <div class="pex-tags">%s</div>'
             % (mk(chip), badlab, mk(bad), goodlab, mk(good), tags))
        self._add(label, "light", b, False)

    def boxes(self, chip, title, white_h, white_ex, dark_p, chipcolor="coral", label="REGOLA"):
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n'
             '    <div class="cbox white" style="top:32cqh;"><h4>%s</h4>\n      <div class="ex">%s</div></div>\n'
             '    <div class="cbox dark" style="top:62cqh;"><p>%s</p></div>' % (chipcolor, mk(chip), mk(title), mk(white_h), mk(white_ex), mk(dark_p)))
        self._add(label, "light", b, False)

    def qlist(self, chip, title, items, note=None, chipcolor="indigo", label="ELENCO", size=None):
        st = ' style="font-size:%scqh;margin-bottom:%scqh;"' % (size, round(float(size) * 0.7, 2)) if size else ""
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <ul class="qlist">%s</ul>'
             % (chipcolor, mk(chip), mk(title), "".join("<li%s>%s</li>" % (st, mk(x)) for x in items)))
        if note:
            b += '\n    <div class="qnote" style="top:82cqh;">%s</div>' % mk(note)
        self._add(label, "light", b, False)

    def field(self, chip, title, paras, chipcolor="cyan", label="SCHEDA", size=None):
        st = ' style="font-size:%scqh;"' % size if size else ""
        b = ('<div class="chip %s">%s</div>\n    <div class="title">%s</div>\n    <div class="fieldbox">%s</div>'
             % (chipcolor, mk(chip), mk(title), "".join("<p%s>%s</p>" % (st, mk(p)) for p in paras)))
        self._add(label, "light", b, False)

    def ponte(self, chip, big, sub, items, label="PONTE"):
        out = "".join('<div class="pcard"><div class="pnum" style="background:%s">%s</div><h3>%s</h3></div>' % (var(c), n, mk(h)) for n, c, h in items)
        b = ('<div class="chip violet">%s</div>\n    <div class="ponte-big">%s</div>\n    <div class="ponte-sub">%s</div>\n    <div class="pcards">%s</div>'
             % (mk(chip), mk(big), mk(sub), out))
        self._add(label, "light", b, False)

    def source(self, text):
        """Aggiunge la fonte in fondo all'ultima slide (solo slide chiare)."""
        label, bg, body, dark = self.slides[-1]
        assert not dark, "fonte solo su slide chiare"
        self.slides[-1] = (label, bg, body + "{SRC:%s}" % text, dark)

    # ----- render -----
    def render(self):
        n = len(self.slides)
        parts = []
        for i, (label, bg, body, dark) in enumerate(self.slides, 1):
            src = None
            m = re.search(r"\{SRC:(.*?)\}$", body, re.S)
            if m:
                src = m.group(1); body = body[:m.start()]
            nopn = body.endswith("{NOPN}")
            if nopn:
                body = body[:-6]
            tail = ""
            if not dark:
                tail += '\n    <div class="foot">%s</div>' % (("Fonte: " + src) if src else self.foot)
            if not nopn:
                tail += '\n    <div class="pageno%s">%d / %d</div>' % (" dark" if dark else "", i, n)
            parts.append('  <!-- SLIDE %d · %s -->\n  <section class="slide"><div class="canvas %s">\n    %s%s\n  </div></section>\n'
                         % (i, label, bg, body, tail))
        return ("""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<!--
%s
  Colori: ink = statement · light = contenuto · indigobg = gancio · coralbg = pratica e dibattito.
-->
<style>
%s%s</style>
</head>
<body>
<div class="deck" id="deck">
%s</div>
<div class="hint">↑ ↓ frecce · F schermo intero · Cmd/Ctrl+P per esportare PDF</div>
<script>
  const deck=document.getElementById('deck');
  const slides=[...document.querySelectorAll('.slide')];
  let i=0;
  function go(n){i=Math.max(0,Math.min(slides.length-1,n));slides[i].scrollIntoView({behavior:'smooth'});}
  deck.addEventListener('scroll',()=>{i=Math.round(deck.scrollTop/window.innerHeight);},{passive:true});
  window.addEventListener('keydown',e=>{
    if(['ArrowDown','ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();go(i+1);}
    else if(['ArrowUp','ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();go(i-1);}
    else if(e.key==='Home'){e.preventDefault();go(0);}
    else if(e.key==='End'){e.preventDefault();go(slides.length-1);}
    else if(e.key.toLowerCase()==='f'){if(!document.fullscreenElement)document.documentElement.requestFullscreen();else document.exitFullscreen();}
  });
</script>
</body>
</html>
""" % (self.title, self.note, BASE_CSS, EXTRA_CSS, "\n".join(parts)))

    def save(self, path):
        p = pathlib.Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        out = self.render()
        assert "—" not in out, "em-dash trovato in %s" % path
        p.write_text(out, encoding="utf-8")
        print("scritto %s (%d slide)" % (p.name, len(self.slides)))
