import fitz, sys
# uso: sheet.py file.pdf prefisso [colonne righe]
pdf, pref = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 3
rows = int(sys.argv[4]) if len(sys.argv) > 4 else 3
doc = fitz.open(pdf)
W, H = 640, 360
per = cols * rows
n = len(doc)
print("pagine:", n)
for s in range(0, n, per):
    sheet = fitz.open(); page = sheet.new_page(width=W * cols, height=H * rows)
    for k in range(s, min(s + per, n)):
        r, c = divmod(k - s, cols)
        rect = fitz.Rect(c * W, r * H, (c + 1) * W, (r + 1) * H)
        page.show_pdf_page(rect, doc, k)
    pix = page.get_pixmap(dpi=72)
    out = "%s_%02d.png" % (pref, s // per + 1)
    pix.save(out); print(out)
