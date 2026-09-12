const pptxgen = require("pptxgenjs");
const p = new pptxgen();
p.defineLayout({ name: "W", width: 13.33, height: 7.5 });
p.layout = "W";

const INK="1E1B4B", INDIGO="4F46E5", VIOLET="7C3AED", CYAN="06B6D4", CORAL="F97316",
      LIGHT="F6F5FF", TEXT="1A1730", MUTED="6B6790", WHITE="FFFFFF", CFCB="CFCBF0", FAINT="8E8AC4";
const HF="Arial", BF="Arial";
let N=0;

function foot(s, dark){ N++; const c=dark?FAINT:MUTED;
  s.addText("AI INSEGNANTI · Formazione PNRR",{x:0.5,y:7.0,w:7,h:0.3,fontFace:BF,fontSize:9,color:c});
  s.addText(`${N} / 22`,{x:11.4,y:7.0,w:1.43,h:0.3,fontFace:BF,fontSize:9,color:c,align:"right"});
}
function chip(s,label,fill,txt){ s.addText(label.toUpperCase(),{x:0.7,y:0.6,w:3.2,h:0.42,fontFace:HF,fontSize:12,bold:true,color:txt||WHITE,align:"center",valign:"middle",fill:{color:fill},rectRadius:0.21,charSpacing:2}); }
function dots(s,x,y,cs){ cs.forEach((c,i)=>s.addShape(p.ShapeType.ellipse,{x:x+i*0.42,y,w:0.26,h:0.26,fill:{color:c}})); }
function circlesDark(s){ s.addShape(p.ShapeType.ellipse,{x:10.4,y:-1.4,w:4.6,h:4.6,fill:{color:INDIGO,transparency:55}}); s.addShape(p.ShapeType.ellipse,{x:11.8,y:4.4,w:3.4,h:3.4,fill:{color:VIOLET,transparency:60}}); s.addShape(p.ShapeType.ellipse,{x:-1.1,y:5.2,w:3.2,h:3.2,fill:{color:CYAN,transparency:70}}); }

// ---- slide type builders ----
function statement(runs, {bg=INK, dark=true, chipL, chipC}={}){
  const s=p.addSlide(); s.background={color:bg};
  if(dark) circlesDark(s);
  if(chipL) chip(s,chipL,chipC||CYAN, bg===INK?undefined:WHITE);
  s.addShape(p.ShapeType.rect,{x:0.9,y:2.55,w:0.6,h:0.1,fill:{color:CORAL}});
  s.addText(runs,{x:0.85,y:2.8,w:11.6,h:2.2,fontFace:HF,fontSize:40,bold:true,color:dark?WHITE:TEXT,lineSpacingMultiple:1.05,valign:"top"});
  if(!dark) foot(s,false); else N++;
  return s;
}
function debate(titleRuns, sub){
  const s=p.addSlide(); s.background={color:CORAL};
  s.addShape(p.ShapeType.ellipse,{x:10.6,y:-1.6,w:5,h:5,fill:{color:WHITE,transparency:88}});
  s.addShape(p.ShapeType.ellipse,{x:-1.4,y:4.6,w:4,h:4,fill:{color:INK,transparency:80}});
  s.addText("DIBATTITO",{x:0.7,y:0.7,w:3.0,h:0.46,fontFace:HF,fontSize:13,bold:true,color:CORAL,align:"center",valign:"middle",fill:{color:WHITE},rectRadius:0.23,charSpacing:2});
  s.addText("Parla la stanza",{x:3.85,y:0.74,w:3,h:0.4,fontFace:BF,fontSize:13,italic:true,color:"FFE4D3",valign:"middle"});
  s.addText(titleRuns,{x:0.7,y:2.2,w:11.7,h:2.7,fontFace:HF,fontSize:38,bold:true,color:WHITE,lineSpacingMultiple:1.05});
  if(sub) s.addText(sub,{x:0.72,y:5.35,w:11.2,h:0.9,fontFace:BF,fontSize:16,color:"FFEAD9"});
  dots(s,0.72,6.5,[WHITE,"FFD9C2",INK]); N++;
  return s;
}
function confronto(chipL, chipC, title, L, R){
  const s=p.addSlide(); s.background={color:LIGHT};
  chip(s,chipL,chipC); s.addText(title,{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:36,bold:true,color:TEXT});
  const cols=[{x:0.7,...L},{x:6.93,...R}];
  cols.forEach(c=>{
    s.addShape(p.ShapeType.roundRect,{x:c.x,y:2.45,w:5.7,h:4.05,fill:{color:WHITE},line:{color:"E6E3FB",width:1},rectRadius:0.12});
    s.addShape(p.ShapeType.roundRect,{x:c.x,y:2.45,w:5.7,h:0.85,fill:{color:c.color},rectRadius:0.12});
    s.addShape(p.ShapeType.rect,{x:c.x,y:2.95,w:5.7,h:0.35,fill:{color:c.color}});
    s.addText(c.head,{x:c.x,y:2.45,w:5.7,h:0.85,fontFace:HF,fontSize:20,bold:true,color:WHITE,align:"center",valign:"middle"});
    let yy=3.6; c.items.forEach(it=>{
      s.addShape(p.ShapeType.ellipse,{x:c.x+0.35,y:yy+0.07,w:0.16,h:0.16,fill:{color:c.color}});
      s.addText(it,{x:c.x+0.7,y:yy-0.05,w:4.7,h:0.75,fontFace:BF,fontSize:14.5,color:TEXT,valign:"top"});
      yy+=0.92;
    });
  });
  foot(s,false); return s;
}
function cards(chipL, chipC, title, rows){
  const s=p.addSlide(); s.background={color:LIGHT};
  chip(s,chipL,chipC); s.addText(title,{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
  let yy=2.45;
  rows.forEach(r=>{
    s.addShape(p.ShapeType.roundRect,{x:0.7,y:yy,w:11.9,h:1.25,fill:{color:WHITE},line:{color:"E6E3FB",width:1},rectRadius:0.12});
    s.addShape(p.ShapeType.ellipse,{x:1.0,y:yy+0.28,w:0.68,h:0.68,fill:{color:r.c}});
    s.addText(r.ic,{x:1.0,y:yy+0.28,w:0.68,h:0.68,fontFace:BF,fontSize:22,color:WHITE,align:"center",valign:"middle"});
    s.addText(r.t,{x:2.0,y:yy+0.18,w:10.3,h:0.5,fontFace:HF,fontSize:20,bold:true,color:TEXT});
    s.addText(r.d,{x:2.0,y:yy+0.62,w:10.3,h:0.5,fontFace:BF,fontSize:14,color:MUTED});
    yy+=1.42;
  });
  foot(s,false); return s;
}

// ===================== DECK =====================

// S1 COVER
let s=p.addSlide(); s.background={color:INK}; circlesDark(s);
s.addText("USARE L'INTELLIGENZA ARTIFICIALE",{x:0.7,y:1.5,w:9.5,h:0.5,fontFace:HF,fontSize:16,bold:true,color:CYAN,charSpacing:3});
s.addText("In modo potenziante",{x:0.66,y:2.05,w:11,h:1.6,fontFace:HF,fontSize:54,bold:true,color:WHITE,lineSpacingMultiple:0.95});
s.addShape(p.ShapeType.rect,{x:0.72,y:3.95,w:0.55,h:0.09,fill:{color:CORAL}});
s.addText("Incontro 1 — Cos'è l'IA e perché ti riguarda",{x:0.7,y:4.2,w:10,h:0.6,fontFace:BF,fontSize:22,color:CFCB});
dots(s,0.72,5.5,[CYAN,INDIGO,VIOLET,CORAL]);
s.addText("Formazione docenti sull'Intelligenza Artificiale · PNRR DM 219/2025",{x:0.7,y:6.95,w:10,h:0.35,fontFace:BF,fontSize:11,color:FAINT}); N++;

// S2 PATTO — cards
cards("Patto d'aula", VIOLET, "Come funziona questo corso",[
 {ic:"⚡",t:"Interattivo e pratico",d:"Non una lezione frontale: si fa, si prova, si sbaglia. L'IA si impara usandola.",c:INDIGO},
 {ic:"💬",t:"Uno spazio di confronto",d:"Oggi più che mai serve: sull'IA siamo tutti, in parte, principianti.",c:CYAN},
 {ic:"🚀",t:"Serve la vostra partecipazione",d:"Porterete i vostri casi reali, non esempi astratti. Più mettete, più portate a casa.",c:CORAL},
]);

// S3 STATEMENT palestra (dark)
statement([{text:"Questa è una ",options:{color:WHITE}},{text:"palestra",options:{color:CYAN}},{text:", non un ",options:{color:WHITE}},{text:"cinema",options:{color:CORAL}},{text:".",options:{color:WHITE}}],{chipL:"Patto d'aula",chipC:VIOLET});

// S4 DEBATE-opener (room question)
debate([{text:"Quanti dei vostri studenti\nusano l'IA ",options:{color:WHITE}},{text:"ogni giorno?",options:{color:INK}}], "→ Prima di rispondere con i numeri: cosa pensate voi?");

// S5 DATA 81 vs 25
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"Il gap",CYAN);
s.addText("I tuoi studenti sono già avanti",{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
s.addShape(p.ShapeType.roundRect,{x:0.7,y:2.5,w:5.75,h:3.1,fill:{color:INK},rectRadius:0.14});
s.addText("81%",{x:0.7,y:2.75,w:5.75,h:1.5,fontFace:HF,fontSize:92,bold:true,color:CYAN,align:"center"});
s.addText("degli studenti italiani usa l'IA",{x:1.0,y:4.35,w:5.15,h:0.8,fontFace:BF,fontSize:18,color:WHITE,align:"center"});
s.addShape(p.ShapeType.roundRect,{x:6.85,y:2.5,w:5.75,h:3.1,fill:{color:WHITE},line:{color:"E6E3FB",width:1.5},rectRadius:0.14});
s.addText("25%",{x:6.85,y:2.75,w:5.75,h:1.5,fontFace:HF,fontSize:92,bold:true,color:CORAL,align:"center"});
s.addText("degli insegnanti la usa",{x:7.15,y:4.35,w:5.15,h:0.8,fontFace:BF,fontSize:18,color:TEXT,align:"center"});
s.addText("Sei l'unico adulto che può ancora insegnare la differenza tra usarla bene e usarla male.",{x:0.7,y:5.95,w:11.9,h:0.6,fontFace:HF,fontSize:18,italic:true,bold:true,color:INDIGO});
s.addText("Fonte: GoStudent Education Future Report 2025",{x:0.7,y:6.95,w:7,h:0.3,fontFace:BF,fontSize:9,color:MUTED});
s.addText("5 / 22",{x:11.4,y:6.95,w:1.43,h:0.3,fontFace:BF,fontSize:9,color:MUTED,align:"right"}); N++;

// S6 STATEMENT non siete indietro (light)
statement([{text:"Non siete indietro.\n",options:{color:TEXT}},{text:"Siete gli unici",options:{color:INDIGO}},{text:" che possono ancora insegnare la ",options:{color:TEXT}},{text:"differenza",options:{color:CORAL}},{text:".",options:{color:TEXT}}],{bg:LIGHT,dark:false,chipL:"Il gap",chipC:CYAN});

// S7 STATEMENT non pensa (dark)
statement([{text:"L'IA non pensa.\n",options:{color:WHITE}},{text:"Non capisce. Non ha opinioni.",options:{color:CYAN}}],{chipL:"Demistificazione",chipC:INDIGO});

// S8 CONCEPT cosa fa davvero
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"Demistificazione",INDIGO);
s.addText("Cosa fa davvero",{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
s.addShape(p.ShapeType.roundRect,{x:0.7,y:2.5,w:11.9,h:1.7,fill:{color:WHITE},line:{color:"E6E3FB",width:1},rectRadius:0.12});
s.addText("Riconosce pattern nel linguaggio e predice la parola più probabile.",{x:1.1,y:2.75,w:11.1,h:0.6,fontFace:HF,fontSize:21,bold:true,color:TEXT});
s.addText([{text:'"La capitale d\'Italia è…" → ',options:{color:TEXT,fontSize:18}},{text:"Roma",options:{color:INDIGO,fontSize:18,bold:true}}],{x:1.1,y:3.4,w:11,h:0.5,fontFace:BF});
s.addShape(p.ShapeType.roundRect,{x:0.7,y:4.5,w:11.9,h:1.5,fill:{color:INK},rectRadius:0.12});
s.addText([{text:"Non perché lo sa.  ",options:{color:CFCB}},{text:"Perché l'ha visto un miliardo di volte.",options:{color:CYAN,bold:true}}],{x:1.1,y:4.5,w:11.1,h:1.5,fontFace:HF,fontSize:22,valign:"middle"});
foot(s,false);

// S9 ANALOGY stagista
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"L'analogia",VIOLET);
s.addText("Lo stagista brillante",{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
s.addShape(p.ShapeType.ellipse,{x:1.0,y:2.9,w:3.0,h:3.0,fill:{color:VIOLET}});
s.addText("🎓",{x:1.0,y:2.9,w:3.0,h:3.0,fontFace:BF,fontSize:90,align:"center",valign:"middle"});
s.addText([{text:"Ha letto tutto",options:{bold:true,color:TEXT}},{text:" — ogni libro, articolo, manuale. Conosce tutte le teorie del mondo.\n\n",options:{color:TEXT}},{text:"Non ha vissuto niente",options:{bold:true,color:CORAL}},{text:" — non conosce la tua scuola, le tue classi, i tuoi studenti.",options:{color:TEXT}}],{x:4.5,y:3.0,w:8.1,h:2.8,fontFace:BF,fontSize:20,valign:"middle",lineSpacingMultiple:1.1});
s.addText("\"Sa tutto e non sa niente del tuo contesto.\"",{x:4.5,y:5.7,w:8.1,h:0.5,fontFace:HF,fontSize:16,italic:true,bold:true,color:VIOLET});
foot(s,false);

// S10 CONFRONTO scorciatoia vs superpotere
confronto("I due framing", VIOLET, "La scelta che cambia tutto",
 {color:MUTED, head:"SCORCIATOIA", items:["Delego il pensiero, accetto e vado","Effetto a breve: faccio prima","Effetto a lungo: debito cognitivo","Un muscolo che non si usa si atrofizza"]},
 {color:INDIGO, head:"SUPERPOTERE", items:["Amplifico le mie capacità","Uso il mio giudizio sull'output","Jagged frontier: il confine è irregolare","Cresce nel tempo, non si spegne"]});

// S11 CITAZIONE Mollick (dark)
s=p.addSlide(); s.background={color:INK}; circlesDark(s);
s.addText("“",{x:0.6,y:1.0,w:3,h:2.2,fontFace:"Georgia",fontSize:200,bold:true,color:CYAN});
s.addText("L'IA eccelle dove non te lo aspetti\ne fallisce dove sembrerebbe banale.",{x:1.4,y:2.7,w:11,h:2.0,fontFace:HF,fontSize:34,bold:true,color:WHITE,lineSpacingMultiple:1.1});
s.addText([{text:"Ethan Mollick",options:{color:CYAN,bold:true}},{text:"  ·  Co-Intelligence (2024)",options:{color:CFCB}}],{x:1.45,y:5.0,w:11,h:0.5,fontFace:BF,fontSize:18}); N++;

// S12 CONFRONTO eccelle/fallisce
confronto("Jagged frontier", CYAN, "Dove eccelle, dove fallisce",
 {color:CYAN, head:"DOVE ECCELLE", items:["20 varianti di una spiegazione in 30 sec","Sintetizza 50 pagine in un minuto","Differenzia un materiale per livelli","Bozza di circolare o verifica"]},
 {color:CORAL, head:"DOVE FALLISCE", items:["Capire che Marco va incoraggiato","Leggere l'umore della classe","Giudicare se “va bene così” qui","Decidere cosa conta davvero"]});

// S13 STATEMENT la differenza (dark, key)
statement([{text:"La differenza non è lo ",options:{color:WHITE}},{text:"strumento",options:{color:CORAL}},{text:".\nÈ il ",options:{color:WHITE}},{text:"metodo",options:{color:CYAN}},{text:".",options:{color:WHITE}}],{chipL:"Il cuore del corso",chipC:CORAL});

// S14 GRAFICO fatica
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"Il concetto di fatica",INDIGO);
s.addText("Stessa fatica, più risultato",{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
s.addChart(p.ChartType.line,[
 {name:"Fatica",labels:["1","2","3","4","5","6"],values:[9,7,5,4,3,2.5]},
 {name:"Output",labels:["1","2","3","4","5","6"],values:[4,5,6.2,7,7.5,8]},
],{x:0.7,y:2.4,w:8.0,h:4.0,chartColors:[CORAL,CYAN],lineSize:4,showLegend:true,legendPos:"b",legendColor:TEXT,legendFontFace:BF,legendFontSize:13,showValue:false,catAxisTitle:"Sessioni",showCatAxisTitle:true,catAxisTitleColor:MUTED,catAxisTitleFontSize:11,valAxisHidden:true,catAxisLabelColor:MUTED,catGridLine:{style:"none"},valGridLine:{color:"ECEAF8"}});
s.addShape(p.ShapeType.roundRect,{x:9.0,y:2.7,w:3.6,h:3.4,fill:{color:WHITE},line:{color:"E6E3FB",width:1},rectRadius:0.12});
s.addText([{text:"Calo della fatica\n",options:{bold:true,color:TEXT,fontSize:17}},{text:"≠\n",options:{bold:true,color:CORAL,fontSize:26}},{text:"spegnere il cervello.\n\n",options:{bold:true,color:TEXT,fontSize:17}},{text:"Il monitoraggio resta sempre tuo.",options:{color:MUTED,fontSize:13}}],{x:9.2,y:2.9,w:3.2,h:3.0,fontFace:HF,align:"center",valign:"middle",lineSpacingMultiple:1.05});
foot(s,false);

// S15 CONFRONTO passivo/attivo
confronto("Due modi opposti", INDIGO, "Uso passivo vs uso attivo",
 {color:CORAL, head:"PASSIVO", items:["“Scrivimi la relazione” → copia-incolla","Accetto l'output senza valutarlo","Erode il pensiero critico nel tempo"]},
 {color:CYAN, head:"ATTIVO", items:["“Scrivimi una bozza, poi la correggo”","Valuto, itero, uso il mio giudizio","Allena e mantiene il pensiero critico"]});

// S16 DATA r=-0.75
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"Il dato",INDIGO);
s.addText("Usare male l'IA costa caro",{x:0.7,y:1.15,w:12,h:0.9,fontFace:HF,fontSize:38,bold:true,color:TEXT});
s.addShape(p.ShapeType.roundRect,{x:0.7,y:2.6,w:5.6,h:3.2,fill:{color:INK},rectRadius:0.14});
s.addText("r = −0,75",{x:0.7,y:3.3,w:5.6,h:1.4,fontFace:HF,fontSize:64,bold:true,color:CORAL,align:"center"});
s.addText("correlazione tra uso passivo dell'IA e calo del pensiero critico",{x:1.1,y:4.55,w:4.8,h:1.0,fontFace:BF,fontSize:15,color:WHITE,align:"center"});
s.addText([{text:"Ma c'è una buona notizia.\n\n",options:{bold:true,color:TEXT,fontSize:20}},{text:"La ",options:{color:TEXT,fontSize:17}},{text:"AI literacy",options:{bold:true,color:INDIGO,fontSize:17}},{text:" attenua l'effetto: chi capisce come funziona lo strumento delega meno ciecamente.",options:{color:TEXT,fontSize:17}}],{x:6.7,y:2.9,w:5.9,h:2.6,fontFace:HF,valign:"middle",lineSpacingMultiple:1.1});
s.addText("Fonte: Gerlich 2025 (MDPI Societies)",{x:0.7,y:6.95,w:7,h:0.3,fontFace:BF,fontSize:9,color:MUTED});
s.addText("16 / 22",{x:11.4,y:6.95,w:1.43,h:0.3,fontFace:BF,fontSize:9,color:MUTED,align:"right"}); N++;

// S17 STATEMENT non di meno (dark)
statement([{text:"Non vi fa fare di ",options:{color:WHITE}},{text:"meno",options:{color:CORAL}},{text:".\nVi fa fare ",options:{color:WHITE}},{text:"meglio",options:{color:CYAN}},{text:".",options:{color:WHITE}}],{chipL:"Il concetto di fatica",chipC:INDIGO});

// S18-20 DEBATE
debate([{text:"I confini reali dell'IA.\n",options:{color:WHITE}},{text:"Cosa pensavi NON potesse fare… e invece fa?",options:{color:INK}}], "→ Due facce della stessa scoperta: il confine non è dove ce lo immaginiamo.");
debate([{text:"Se l'IA può fare tutto questo…\n",options:{color:WHITE}},{text:"cosa resta che deve fare l'insegnante?",options:{color:INK}}], "→ Il ruolo non sparisce: si sposta. Da chi trasmette nozioni a chi guida il rapporto con la conoscenza.");
debate([{text:"Cosa pensi che l'IA\n",options:{color:WHITE}},{text:"non potrà mai fare?",options:{color:INK}}], "→ Questa domanda resta aperta. La riapriamo alla fine del corso.");

// S21 PONTE
s=p.addSlide(); s.background={color:LIGHT}; chip(s,"La prossima volta",VIOLET);
s.addText("Il metodo",{x:0.7,y:1.7,w:12,h:1.0,fontFace:HF,fontSize:52,bold:true,color:TEXT});
s.addText("I 3 principi per usare l'IA da professionisti, non da chi ci prova.",{x:0.72,y:2.95,w:11,h:0.7,fontFace:BF,fontSize:22,color:MUTED});
const pr=[{n:"1",t:"Non spegnere il cervello",c:INDIGO},{n:"2",t:"L'IA è un collega",c:CYAN},{n:"3",t:"Obiettivi chiari + AI First",c:CORAL}];
let px=0.7; pr.forEach(r=>{ s.addShape(p.ShapeType.roundRect,{x:px,y:4.1,w:3.85,h:2.0,fill:{color:WHITE},line:{color:"E6E3FB",width:1},rectRadius:0.12});
 s.addShape(p.ShapeType.ellipse,{x:px+0.35,y:4.45,w:0.8,h:0.8,fill:{color:r.c}}); s.addText(r.n,{x:px+0.35,y:4.45,w:0.8,h:0.8,fontFace:HF,fontSize:28,bold:true,color:WHITE,align:"center",valign:"middle"});
 s.addText(r.t,{x:px+0.3,y:5.35,w:3.3,h:0.7,fontFace:HF,fontSize:16,bold:true,color:TEXT}); px+=4.07; });
foot(s,false);

// S22 CLOSING (dark)
s=p.addSlide(); s.background={color:INK}; circlesDark(s);
s.addText([{text:"Amplifica il tuo ",options:{color:WHITE}},{text:"potenziale",options:{color:CYAN}},{text:".\nUsala ogni giorno.",options:{color:WHITE}}],{x:0.85,y:2.6,w:11.6,h:2.2,fontFace:HF,fontSize:46,bold:true,lineSpacingMultiple:1.05});
s.addText("L'IA non sostituisce l'intelligenza umana — la potenzia con metodo.",{x:0.88,y:4.9,w:11,h:0.6,fontFace:BF,fontSize:18,color:CFCB});
dots(s,0.9,5.9,[CYAN,INDIGO,VIOLET,CORAL]); N++;

p.writeFile({fileName:"/Users/lucademarco/Desktop/AI Insegnanti/Incontro_1_AI_Insegnanti.pptx"}).then(f=>console.log("written:",f,"slides:",N));
