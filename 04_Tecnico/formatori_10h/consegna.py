# -*- coding: utf-8 -*-
"""Assembla _Consegna/ del percorso Formatori: PDF di deck, scalette, guide, quaderno, programma. E lo zip."""
import subprocess, pathlib, shutil, markdown, re, zipfile, sys
R = pathlib.Path(__file__).resolve().parents[2]
P = R / "02_Percorsi/10h/Formatori_10h"
C = P / "_Consegna"
TMP = pathlib.Path(sys.argv[1]); TMP.mkdir(parents=True, exist_ok=True)
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SLUG = {1:"Il_mestiere_di_chi_forma",2:"Gemini_la_base",3:"Dal_bisogno_alla_sequenza",4:"L_assistente_che_vi_conosce",5:"Costruire_la_lezione",
        6:"Dalla_scaletta_ai_materiali",7:"Condurre_l_aula",8:"La_demo_i_dati_le_obiezioni",9:"Sei_minuti_in_aula",10:"Dopo_l_aula"}
CSS = """
 @page{size:A4;margin:16mm 15mm;}
 body{font-family:'Inter','Segoe UI',-apple-system,Arial,sans-serif;color:#1A1730;font-size:10.5pt;line-height:1.45;}
 h1{font-size:20pt;color:#1E1B4B;margin:0 0 4mm;} h2{font-size:13pt;color:#1E1B4B;margin:7mm 0 2mm;border-bottom:2px solid #E6E3FB;padding-bottom:1mm;break-after:avoid;}
 h3{font-size:11pt;color:#4F46E5;margin:4mm 0 1mm;break-after:avoid;}
 blockquote{margin:0 0 4mm;padding:3mm 4mm;background:#F6F5FF;border-left:1.4mm solid #4F46E5;border-radius:2mm;}
 blockquote p{margin:0 0 1.2mm;} ul,ol{margin:1mm 0 2mm 5mm;} li{margin-bottom:.8mm;}
 table{border-collapse:collapse;width:100%;margin:2mm 0;font-size:9.5pt;} th{background:#1E1B4B;color:#fff;text-align:left;padding:1.6mm 2mm;} td{border:1px solid #E6E3FB;padding:1.6mm 2mm;vertical-align:top;}
 code{background:#F0EFFA;padding:0 1mm;border-radius:1mm;font-size:9.5pt;} pre{background:#FFF8F2;border:1px solid #F6D9C2;border-radius:2mm;padding:3mm;white-space:pre-wrap;font-size:9.3pt;font-family:inherit;break-inside:avoid;}
 pre code{background:none;padding:0;font-family:inherit;} hr{border:none;border-top:1px solid #E6E3FB;margin:5mm 0;}
 *{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
"""
def pdf(src_html, out_pdf):
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=4000",
                    "--print-to-pdf=%s" % out_pdf, "file://%s" % src_html], stderr=subprocess.DEVNULL, check=True)
def md_pdf(src_md, out_pdf):
    body = markdown.markdown(src_md.read_text(encoding="utf-8"), extensions=["tables", "fenced_code", "sane_lists", "nl2br"])
    body = body.replace("[ ]", "☐")
    h = TMP / (src_md.stem + ".html")
    h.write_text('<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8"><style>%s</style></head><body>%s</body></html>' % (CSS, body), encoding="utf-8")
    pdf(h, out_pdf)
if C.exists(): shutil.rmtree(C)
for n in range(1, 11):
    src = P / ("%02d_Modulo_%d" % (n, n)); dst = C / ("%02d_Modulo_%d" % (n, n))
    pdf(src / ("Modulo_%d.html" % n), dst / ("Modulo_%d_%s.pdf" % (n, SLUG[n])))
    md_pdf(src / ("MODULO_%d_SCALETTA.md" % n), dst / ("Modulo_%d_Scaletta.pdf" % n))
    g = src / ("Modulo_%d_guida_formatore.html" % n)
    if g.exists(): pdf(g, dst / ("Modulo_%d_Guida_pratica_formatore.pdf" % n))
    print("modulo", n, "ok")
pdf(R / "01_Progetto/Programmi/10h/PROGRAMMA_10h_Formare_i_Formatori.html", C / "00_Programma/Programma_Formare_i_Formatori_10h.pdf")
shutil.copy(C / "00_Programma/Programma_Formare_i_Formatori_10h.pdf", R / "01_Progetto/Programmi/10h/PROGRAMMA_10h_Formare_i_Formatori.pdf")
M = C / "Materiali"
pdf(P / "Materiali/Quaderno_del_formatore.html", M / "Quaderno_del_formatore.pdf")
md_pdf(P / "Materiali/PROMPT_PRONTI.md", M / "Prompt_pronti.pdf")
for f in ["Materiali/PROMPT_PRONTI.md", "04_Modulo_4/Asset_Assistente_Scrittore_di_Prompt.md", "04_Modulo_4/Asset_Assistente_Progettista_di_Percorsi.md"]:
    shutil.copy(P / f, M / pathlib.Path(f).name)
md_pdf(P / "NOTE_EROGAZIONE.md", C / "Note_di_erogazione.pdf")
(C / "LEGGIMI.md").write_text("""# Percorso Formatori 10h · pacchetto per chi conduce

Questa cartella è una **copia** assemblata dai file di lavoro. Se qualcosa va corretto, si corregge nella cartella del percorso e si riassembla.

- `00_Programma/` il programma da mandare alle scuole.
- `01_Modulo_1` … `10_Modulo_10` per ogni modulo: le slide, la scaletta di chi conduce e, nei moduli pratici (2, 4, 6, 8, 9), la guida pratica con cosa mostrare a schermo.
- `Materiali/` il quaderno da dare ai partecipanti, i prompt pronti (in PDF e in testo da copiare), i testi dei due assistenti.
- `Note_di_erogazione.pdf` da leggere per primo: le verifiche sugli account, Gem e Skill, le mail pronte.

Ordine di lettura consigliato: note di erogazione, programma, poi modulo per modulo scaletta e slide insieme.

Prima della prima aula: provare tutti i prompt dentro Gemini, sull'account che si userà.
""", encoding="utf-8")
z = C / "Percorso_Formatori_10h.zip"
with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
    for f in sorted(C.rglob("*")):
        if f.is_file() and f != z: zf.write(f, f.relative_to(C))
print("zip", round(z.stat().st_size / 1e6, 1), "MB;", sum(1 for f in C.rglob("*") if f.is_file()), "file")
