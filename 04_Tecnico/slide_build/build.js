const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W", width: 13.33, height: 7.5 });
p.layout = "W";

// ---- Palette ----
const INK    = "1E1B4B"; // deep indigo (dark bg)
const INK2   = "2A2566"; // lighter indigo panel
const INDIGO = "4F46E5"; // primary
const VIOLET = "7C3AED"; // support
const CYAN   = "06B6D4"; // data accent
const CORAL  = "F97316"; // debate accent ("parla la stanza")
const LIGHT  = "F6F5FF"; // content bg
const TEXT   = "1A1730";
const MUTED  = "6B6790";
const WHITE  = "FFFFFF";

const HF = "Arial"; // header
const BF = "Arial"; // body

// ---- helpers ----
function footer(slide, n, dark) {
  const c = dark ? "8E8AC4" : MUTED;
  slide.addText("AI INSEGNANTI · Formazione PNRR", { x:0.5, y:7.0, w:6, h:0.3, fontFace:BF, fontSize:9, color:c, align:"left" });
  slide.addText(`${n} / 22`, { x:11.4, y:7.0, w:1.43, h:0.3, fontFace:BF, fontSize:9, color:c, align:"right" });
}
function chip(slide, label, fill) {
  slide.addText(label.toUpperCase(), { x:0.7, y:0.6, w:3.2, h:0.42, fontFace:HF, fontSize:12, bold:true, color:WHITE, align:"center", valign:"middle", fill:{color:fill}, rectRadius:0.21, charSpacing:2 });
}
// decorative corner dots motif
function dots(slide, x, y, colors) {
  colors.forEach((c,i)=> slide.addShape(p.ShapeType.ellipse, { x:x+i*0.42, y, w:0.26, h:0.26, fill:{color:c} }));
}

// ============ SLIDE 1 — COVER (dark) ============
let s = p.addSlide();
s.background = { color: INK };
// motif: big soft circles
s.addShape(p.ShapeType.ellipse, { x:10.4, y:-1.4, w:4.6, h:4.6, fill:{color:INDIGO, transparency:55} });
s.addShape(p.ShapeType.ellipse, { x:11.8, y:4.4, w:3.4, h:3.4, fill:{color:VIOLET, transparency:60} });
s.addShape(p.ShapeType.ellipse, { x:-1.1, y:5.2, w:3.2, h:3.2, fill:{color:CYAN, transparency:70} });
s.addText("USARE L'INTELLIGENZA ARTIFICIALE", { x:0.7, y:1.5, w:9.5, h:0.5, fontFace:HF, fontSize:16, bold:true, color:CYAN, charSpacing:3 });
s.addText("In modo potenziante", { x:0.66, y:2.05, w:11, h:1.6, fontFace:HF, fontSize:54, bold:true, color:WHITE, lineSpacingMultiple:0.95 });
s.addShape(p.ShapeType.rect, { x:0.72, y:3.95, w:0.55, h:0.09, fill:{color:CORAL} });
s.addText("Incontro 1 — Cos'è l'IA e perché ti riguarda", { x:0.7, y:4.2, w:10, h:0.6, fontFace:BF, fontSize:22, color:"CFCBF0" });
dots(s, 0.72, 5.5, [CYAN, INDIGO, VIOLET, CORAL]);
s.addText("Formazione docenti sull'Intelligenza Artificiale · PNRR DM 219/2025", { x:0.7, y:6.95, w:10, h:0.35, fontFace:BF, fontSize:11, color:"8E8AC4" });

// ============ SLIDE 2 — CONCEPT: Patto d'aula (light, medium text) ============
s = p.addSlide();
s.background = { color: LIGHT };
chip(s, "Patto d'aula", VIOLET);
s.addText("Come funziona questo corso", { x:0.7, y:1.15, w:12, h:0.9, fontFace:HF, fontSize:40, bold:true, color:TEXT });

const rows = [
  { ic:"⚡", t:"Interattivo e pratico", d:"Non una lezione frontale: si fa, si prova, si sbaglia. L'IA si impara usandola.", c:INDIGO },
  { ic:"💬", t:"Uno spazio di confronto", d:"Oggi più che mai serve: sull'IA siamo tutti, in parte, principianti.", c:CYAN },
  { ic:"🚀", t:"Serve la vostra partecipazione", d:"Porterete i vostri casi reali, non esempi astratti. Più mettete, più portate a casa.", c:CORAL },
];
let yy = 2.45;
rows.forEach(r => {
  s.addShape(p.ShapeType.roundRect, { x:0.7, y:yy, w:11.9, h:1.25, fill:{color:WHITE}, line:{color:"E6E3FB", width:1}, rectRadius:0.12, shadow:{type:"outer", color:"D9D5F2", blur:6, offset:2, angle:90, opacity:0.5} });
  s.addShape(p.ShapeType.ellipse, { x:1.0, y:yy+0.28, w:0.68, h:0.68, fill:{color:r.c} });
  s.addText(r.ic, { x:1.0, y:yy+0.28, w:0.68, h:0.68, fontFace:BF, fontSize:22, color:WHITE, align:"center", valign:"middle" });
  s.addText(r.t, { x:2.0, y:yy+0.18, w:10.3, h:0.5, fontFace:HF, fontSize:21, bold:true, color:TEXT });
  s.addText(r.d, { x:2.0, y:yy+0.62, w:10.3, h:0.5, fontFace:BF, fontSize:14.5, color:MUTED });
  yy += 1.42;
});
footer(s, 2, false);

// ============ SLIDE 3 — DATA SHOCK: 81% vs 25% ============
s = p.addSlide();
s.background = { color: LIGHT };
chip(s, "Il gap", CYAN);
s.addText("I tuoi studenti sono già avanti", { x:0.7, y:1.15, w:12, h:0.9, fontFace:HF, fontSize:40, bold:true, color:TEXT });

// left stat card (students)
s.addShape(p.ShapeType.roundRect, { x:0.7, y:2.5, w:5.75, h:3.1, fill:{color:INK}, rectRadius:0.14 });
s.addText("81%", { x:0.7, y:2.75, w:5.75, h:1.5, fontFace:HF, fontSize:96, bold:true, color:CYAN, align:"center" });
s.addText("degli studenti italiani usa l'IA", { x:1.0, y:4.35, w:5.15, h:0.8, fontFace:BF, fontSize:18, color:WHITE, align:"center" });

// right stat card (teachers)
s.addShape(p.ShapeType.roundRect, { x:6.85, y:2.5, w:5.75, h:3.1, fill:{color:WHITE}, line:{color:"E6E3FB", width:1.5}, rectRadius:0.14 });
s.addText("25%", { x:6.85, y:2.75, w:5.75, h:1.5, fontFace:HF, fontSize:96, bold:true, color:CORAL, align:"center" });
s.addText("degli insegnanti la usa", { x:7.15, y:4.35, w:5.15, h:0.8, fontFace:BF, fontSize:18, color:TEXT, align:"center" });

s.addText("Sei l'unico adulto che può ancora insegnare la differenza tra usarla bene e usarla male.", { x:0.7, y:5.95, w:11.9, h:0.6, fontFace:HF, fontSize:18, italic:true, bold:true, color:INDIGO });
s.addText("Fonte: GoStudent Education Future Report 2025", { x:0.7, y:6.95, w:6, h:0.3, fontFace:BF, fontSize:9, color:MUTED });
s.addText("3 / 22", { x:11.4, y:6.95, w:1.43, h:0.3, fontFace:BF, fontSize:9, color:MUTED, align:"right" });

// ============ SLIDE 4 — DEBATE QUESTION (coral) ============
s = p.addSlide();
s.background = { color: CORAL };
s.addShape(p.ShapeType.ellipse, { x:10.6, y:-1.6, w:5, h:5, fill:{color:WHITE, transparency:88} });
s.addShape(p.ShapeType.ellipse, { x:-1.4, y:4.6, w:4, h:4, fill:{color:INK, transparency:80} });
s.addText("DIBATTITO", { x:0.7, y:0.7, w:3.0, h:0.46, fontFace:HF, fontSize:13, bold:true, color:CORAL, align:"center", valign:"middle", fill:{color:WHITE}, rectRadius:0.23, charSpacing:2 });
s.addText("Parla la stanza", { x:3.85, y:0.74, w:3, h:0.4, fontFace:BF, fontSize:13, italic:true, color:"FFE4D3", valign:"middle" });
s.addText("Se l'IA può fare tutto questo…\ncosa resta che deve fare l'insegnante?", { x:0.7, y:2.3, w:11.6, h:2.6, fontFace:HF, fontSize:40, bold:true, color:WHITE, lineSpacingMultiple:1.05 });
s.addText("→ Il ruolo non sparisce: si sposta. Da chi trasmette nozioni a chi guida il rapporto con la conoscenza.", { x:0.72, y:5.3, w:11, h:0.8, fontFace:BF, fontSize:16, color:"FFEAD9" });
dots(s, 0.72, 6.4, [WHITE, "FFD9C2", INK]);

p.writeFile({ fileName: "/Users/lucademarco/Desktop/AI Insegnanti/ESEMPIO_SLIDE_Incontro1.pptx" }).then(f => console.log("written:", f));
