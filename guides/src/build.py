"""Genera guides/KAIROS-Guia-resumen.pdf y guides/KAIROS-Guia-de-inicio-rapido-Full.pdf. Ejecutar: python guides/src/build.py"""
import subprocess, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import full, resumen
G = Path(__file__).parent.parent
missing = full.build(G / "KAIROS-Guia-de-inicio-rapido-Full.pdf")
resumen.build(G / "KAIROS-Guia-resumen.pdf")
print("títulos sin página en el índice:", missing)
for f in ("KAIROS-Guia-resumen.pdf", "KAIROS-Guia-de-inicio-rapido-Full.pdf"):
    print(f, subprocess.run(["pdfinfo", str(G / f)], capture_output=True, text=True).stdout.split("Pages:")[1].split()[0], "páginas")
