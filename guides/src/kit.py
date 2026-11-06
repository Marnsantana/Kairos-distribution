"""Utilidades comunes para generar las guías de KAIROS (HTML -> PDF con Chromium/Playwright).

Uso:  python guides/src/build.py            (genera los dos PDF en guides/)
Requisitos: Python 3, Node con Playwright (Chromium) y poppler-utils (pdftotext).
"""
import base64, html, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).parent
IMG = HERE / "img"
LOGO = HERE.parent.parent / "assets" / "kairos-logo.png"
VERSION = "0.8.0"
FECHA = "Noviembre de 2026"
URL_OFICIAL = "github.com/Marnsantana/kairos-releases/releases/latest"
URL_HTTPS = "https://github.com/Marnsantana/kairos-releases/releases/latest"

CSS = """
@page { size: A4; margin: 18mm 18mm 20mm 18mm; }
@page :first { margin: 0; }
* { box-sizing: border-box; }
body { font: 10.4pt/1.5 Inter, 'DejaVu Sans', Arial, sans-serif; color: #1c1c1c; margin: 0; }
.cover { height: 297mm; width: 210mm; background: #0c0c0c; color: #fff; text-align: center; page-break-after: always;
  display: flex; flex-direction: column; align-items: center; justify-content: center; }
.cover img { width: 105mm; height: 106mm; border-radius: 6mm; margin-bottom: 14mm; }
.cover h1 { font-size: 24pt; margin: 0 0 4mm; letter-spacing: .02em; }
.cover .sub { color: #fe7901; font-size: 13pt; margin-bottom: 20mm; }
.cover .ref { color: #cfcfcf; font-size: 9.6pt; line-height: 1.7; }
h1.t { font-size: 22pt; margin: 0 0 6mm; padding-bottom: 3mm; border-bottom: 2px solid #fe7901; }
.chap { page-break-before: always; }
.chap .kicker { color: #fe7901; font-size: 8.5pt; font-weight: 700; letter-spacing: .18em; margin: 0 0 1mm; }
h1.c { font-size: 20pt; margin: 0 0 4mm; padding-bottom: 2.5mm; border-bottom: 2px solid #fe7901; }
h2 { font-size: 12.4pt; margin: 6mm 0 2.6mm; padding: 1.6mm 3mm; background: #f2f2f2; border-left: 4px solid #fe7901; page-break-after: avoid; }
h3 { font-size: 10.8pt; margin: 4mm 0 1.5mm; page-break-after: avoid; }
p { margin: 0 0 2.6mm; }
ul { margin: 0 0 3mm; padding-left: 5mm; } li { margin: 0 0 1.2mm; }
.step { display: flex; gap: 3mm; margin: 0 0 2.4mm; page-break-inside: avoid; }
.step > div { flex: 1; }
.n { display: inline-flex; align-items: center; justify-content: center; width: 5.2mm; height: 5.2mm; min-width: 5.2mm; border-radius: 50%;
  background: #fe7901; color: #fff; font-weight: 700; font-size: 8.4pt; }
.step .n { margin-top: .5mm; }
kbd { font: 600 8.6pt 'DejaVu Sans Mono', monospace; background: #f4f4f4; border: 1px solid #c9c9c9; border-bottom-width: 2px;
  border-radius: 3px; padding: 0 1.6mm; white-space: nowrap; }
code { font: 8.8pt 'DejaVu Sans Mono', monospace; background: #f1f1f1; padding: 0 1mm; border-radius: 2px; }
.box { border-left: 4px solid #fe7901; background: #fff6ee; padding: 2.4mm 3.5mm; margin: 3mm 0; border-radius: 0 3px 3px 0; page-break-inside: avoid; }
.box b.l { display: block; color: #c85a00; font-size: 8pt; letter-spacing: .1em; margin-bottom: .6mm; }
.box.imp { background: #fdeeee; border-color: #c62828; } .box.imp b.l { color: #c62828; }
.box.tip { background: #eef7ef; border-color: #2e7d32; } .box.tip b.l { color: #2e7d32; }
.box.new { background: #eef3fb; border-color: #1f5fbf; } .box.new b.l { color: #1f5fbf; }
figure { margin: 3mm 0; text-align: center; page-break-inside: avoid; }
figure img { max-width: 100%; max-height: 112mm; border: 1px solid #d5d5d5; border-radius: 3px; }
figcaption { font-size: 8.4pt; color: #555; margin-top: 1.2mm; }
table { border-collapse: collapse; width: 100%; margin: 2mm 0 4mm; font-size: 9.4pt; page-break-inside: auto; }
th { background: #1c1c1c; color: #fff; text-align: left; padding: 1.6mm 2.5mm; }
td { border-bottom: 1px solid #ddd; padding: 1.5mm 2.5mm; vertical-align: top; } tr { page-break-inside: avoid; }
.toc { columns: 2; column-gap: 12mm; font-size: 9.2pt; }
.toc .tc { font-weight: 700; margin-top: 3.4mm; break-after: avoid; } .toc .ts { padding-left: 4mm; color: #333; }
.toc .tc, .toc .ts { display: flex; } .toc .dots { flex: 1; border-bottom: 1px dotted #999; margin: 0 1.5mm 3px; } .toc .pg { min-width: 6mm; text-align: right; }
.sm .step, .sm p, .sm li { font-size: 9.4pt; }
.head { display: flex; align-items: center; gap: 5mm; background: #0c0c0c; color: #fff; border-radius: 3mm; padding: 4mm 6mm; margin-bottom: 5mm; }
.head img { width: 20mm; height: 20mm; border-radius: 2mm; } .head h1 { margin: 0; font-size: 18pt; } .head .o { color: #fe7901; font-size: 10.4pt; }
.head .s { color: #cfcfcf; font-size: 8.2pt; }
h2.r { margin-top: 4mm; }
.two { display: flex; gap: 4mm; align-items: flex-start; } .two > * { flex: 1; }
"""


def esc(t):
    return html.escape(t, quote=False)


def img_uri(name):
    p = IMG / name if not str(name).startswith("/") else Path(name)
    return "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()


def k(*keys):
    return " + ".join(f"<kbd>{esc(x)}</kbd>" for x in keys)


def step(n, body):
    return f'<div class="step"><span class="n">{n}</span><div>{body}</div></div>'


def box(kind, body, label=None):
    labels = {"nota": "NOTA", "consejo": "CONSEJO", "imp": "IMPORTANTE", "new": "NOVEDAD 0.8.0"}
    cls = {"nota": "", "consejo": "tip", "imp": "imp", "new": "new"}[kind]
    return f'<div class="box {cls}"><b class="l">{label or labels[kind]}</b>{body}</div>'


def fig(name, cap, w=None):
    st = f' style="width:{w}%"' if w else ""
    return f'<figure><img src="{img_uri(name)}"{st} alt="{esc(cap)}"><figcaption>{cap}</figcaption></figure>'


def table(head, rows):
    h = "".join(f"<th>{c}</th>" for c in head)
    r = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in row) + "</tr>" for row in rows)
    return f"<table><tr>{h}</tr>{r}</table>"


def chap(num, title, body):
    return f'<section class="chap"><div class="kicker">CAPÍTULO {num}</div><h1 class="c">{title}</h1>{body}</section>'


def render_pdf(html_doc, out, footer_left):
    import os
    tmp = out.with_suffix(".html")
    tmp.write_text(html_doc, encoding="utf-8")
    env = dict(os.environ)
    env.setdefault("NODE_PATH", subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip())
    subprocess.run(["node", str(HERE / "render.js"), str(tmp), str(out), footer_left, VERSION], check=True, env=env)
    tmp.unlink()


def page_texts(pdf):
    n = int(re.search(r"Pages:\s+(\d+)", subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True).stdout).group(1))
    return [subprocess.run(["pdftotext", "-f", str(i), "-l", str(i), "-layout", str(pdf), "-"], capture_output=True, text=True).stdout
            for i in range(1, n + 1)]


def find_pages(pdf, titles, start=3):
    """Página (numeración del pie = física) de la primera línea que coincide exactamente con cada título."""
    pages = page_texts(pdf)
    res = {}
    for t in titles:
        for i, tx in enumerate(pages, 1):
            if i >= start and any(l.strip() == t for l in tx.splitlines()):
                res[t] = i
                break
    return res
