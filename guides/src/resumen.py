"""Guía abreviada (4 páginas)."""
from kit import *


def fg(n, cap, w=100):
    return f'<figure style="margin:1.5mm 0"><img src="{img_uri(n)}" style="width:{w}%;max-height:62mm" alt="{esc(cap)}"><figcaption>{cap}</figcaption></figure>'


def build_html():
    b = f'<div class="sm">'
    b += (f'<div class="head"><img src="{img_uri(LOGO)}"><div><h1>KAIROS — Guía abreviada</h1><div class="o">Del primer partido a tu primera sesión de vídeo</div>'
          f'<div class="s">KAIROS {VERSION} · Descarga oficial: {URL_OFICIAL}</div></div></div>')
    b += "<h2 class='r'>Instalar KAIROS</h2>"
    b += step(1, "Entra en <b>https://kairos-distribution.vercel.app</b> (o en " + URL_HTTPS + ") y pulsa <b>«Descargar KAIROS para Windows»</b> "
                 "(el archivo se llama <code>KAIROS-Setup.exe</code> y pesa unos 138 MB). No necesitas cuenta de GitHub.")
    b += step(2, "Haz doble clic en el instalador. Si Windows muestra «Windows protegió su PC», pulsa <b>«Más información»</b> y luego <b>«Ejecutar de todas formas»</b>: es normal porque KAIROS aún no tiene "
                 "certificado comercial de editor. Hazlo solo con el archivo del enlace oficial y no desactives el antivirus.")
    b += step(3, "Acepta la licencia, deja la carpeta propuesta, pulsa <b>Instalar</b> y <b>Finalizar</b>. Se instala solo para tu usuario, sin permisos de administrador.")
    b += box("nota", "Tus datos (proyectos, clips, preferencias) se guardan aparte del programa: actualizar o reinstalar no los borra. Al abrir KAIROS, si hay versión nueva verás un aviso con <b>Actualizar ahora</b> o <b>Más tarde</b>.")
    b += "<h2 class='r'>Crear un proyecto y cargar el partido</h2>"
    b += (f"<p>Un proyecto es la carpeta de trabajo de un partido. KAIROS tiene tres módulos: <b>Proyecto</b>, <b>Biblioteca</b> y <b>Sesiones</b> ({k('Ctrl','1')} / {k('Ctrl','2')} / {k('Ctrl','3')}).</p>")
    b += '<div class="two"><div>'
    b += step(1, f"<b>Archivo ▸ Nuevo proyecto…</b> ({k('Ctrl','N')}).")
    b += step(2, "Escribe el nombre (1), elige el equipo (2) y, si quieres, el rival (3). Pulsa <b>Aceptar</b> (4).")
    b += step(3, f"Selecciona el vídeo en el selector de Windows (varios a la vez con {k('Ctrl')} + clic) y pulsa <b>Abrir</b>.")
    b += ("<p>Formatos: <code>.mp4</code>, <code>.mov</code> y <code>.m4v</code>. Si el partido está en varios archivos (uno por cuarto), añádelos todos al mismo proyecto con <b>Archivo ▸ Añadir vídeo al proyecto…</b>; "
          "no hace falta unirlos. KAIROS nunca modifica ni copia tus vídeos.</p></div><div>")
    b += fg("r01.png", "Nuevo proyecto: 1 nombre, 2 equipo, 3 rival, 4 Aceptar.", 80) + "</div></div>"
    b += "<h2 class='r'>Moverse por el vídeo</h2>" + fg("r02.png", "Barra de control del reproductor.")
    b += (f"<p>{k('Espacio')} reproducir/pausa · {k('←')} / {k('→')} salto de 1 s · {k('J')} / {k('L')} salto de 5 s · {k('Alt','←')} / {k('Alt','→')} fotograma a fotograma · "
          f"{k('+')} / {k('-')} / {k('0')} velocidad más, menos o normal. También puedes hacer clic en la línea de tiempo para saltar a ese punto, o acercarla con el <b>zoom</b> bajo ella "
          f"(deslizador, botón «100 %» o {k('Ctrl')} + rueda). Todos los atajos están en <b>Ayuda ▸ Atajos de teclado</b>.</p>")
    b += "<h2 class='r'>Crear tu primer clip</h2>"
    b += "<p>Un clip es un tramo del vídeo con su información (título, categorías, jugadores, valoración). Es la pieza básica de KAIROS.</p>"
    b += '<div class="two"><div>'
    b += step(1, f"Pausa justo cuando empieza la jugada y pulsa <b>Inicio</b> ({k('I')}).")
    b += step(2, f"Reproduce hasta que acabe, pausa y pulsa <b>Final</b> ({k('O')}). El tramo queda en naranja en la línea de tiempo.")
    b += step(3, "Ajusta si hace falta: escribe el tiempo exacto en los campos Inicio y Final (<code>mm:ss.mmm</code>) o arrastra los extremos. Deja un par de segundos antes de la acción.")
    b += step(4, "Completa el formulario: título, categorías (la primera que marques es la principal), jugadores y valoración (Positivo, A mejorar o Neutro).")
    b += step(5, f"Pulsa <b>Guardar clip</b> ({k('S')}). El clip aparece en la pestaña <b>Clips</b>. {k('Ctrl','Z')} deshace.")
    b += "</div><div>" + fg("r03.png", "Formulario del clip: 1 título, 2 categorías, 3 pestañas, 4 valoración, 5 comentario, 6 Guardar clip.") + "</div></div>"
    b += "<h3>Clips automáticos: una tecla y listo</h3>"
    b += (f"<p>Cuando veas una acción, pulsa la tecla numérica de su categoría ({k('1')} a {k('9')}; por defecto [1] Balance defensivo, [2] Rebote defensivo, [3] Defensa del bloqueo directo, "
          f"[4] Defensa individual, [5] Rotaciones). KAIROS crea el clip con 10 s antes y 0 s después del momento en que pulsas (ajustable en <b>Archivo ▸ Preferencias… ▸ Clips automáticos</b>).</p>"
          f"<ul><li><b>Modo Revisión</b> (por defecto): prepara un borrador; tú lo guardas con {k('S')} o lo descartas con {k('Esc')}.</li>"
          "<li><b>Modo Rápido</b>: se guarda al instante; ideal para analizar a toda velocidad y retocar después.</li></ul>")
    b += "<h2 class='r'>Consultar y organizar los clips</h2>"
    b += '<div class="two"><div>' + fg("r04.png", "Pestaña Clips: 1 buscar, 2 filtros, 3 jugador, 4 tarjetas.", 90) + "</div><div>"
    b += ("<p>La pestaña <b>Clips</b> muestra tarjetas compactas con punto de color (verde positivo, rojo a mejorar, gris neutro), ★ favorito, título, categoría principal y jugadores.</p>"
          "<ul><li>Busca y filtra por texto, valoración, categoría o jugador; los filtros se combinan.</li>"
          f"<li>Haz clic en una tarjeta para saltar al clip y editarlo; <b>Reproducir clip</b> ({k('P')}) lo ve solo. Con el cursor quieto sobre su marca en la línea de tiempo verás su título.</li>"
          f"<li>Marca varias con la casilla (o {k('X')}) para exportarlas o llevarlas a una sesión.</li>"
          "<li>La <b>Biblioteca</b> reúne los clips de todos tus proyectos. Ordena los proyectos en carpetas arrastrándolos.</li></ul>")
    b += "</div></div>"
    b += "<h2 class='r'>Preparar una sesión de vídeo</h2>"
    b += ("<p>Una sesión es una lista ordenada de clips para enseñar, de uno o varios partidos. Guarda referencias, no copias: si corriges un clip, la sesión lo refleja. Ejemplo: «Defensa: 5 jugadas para el equipo».</p>")
    b += step(1, "En la Biblioteca, marca los clips y pulsa <b>+ Generar nueva sesión</b>.")
    b += step(2, "Escribe el nombre (y, si quieres, el equipo destinatario) y pulsa <b>Crear</b>.")
    b += step(3, f"En Sesiones ({k('Ctrl','3')}) ordena los clips con <b>Subir / Bajar</b>. Las sesiones se guardan solas.")
    b += step(4, "Para reutilizar clips en otra sesión: selecciónalos y pulsa <b>Añadir a otra sesión…</b>. Siguen en la original, sin duplicados.")
    b += step(5, "Elige <b>Continuo</b> (un clip tras otro) o <b>Pausado</b> (se detiene al acabar cada clip).")
    b += fg("r05.png", "Módulo Sesiones: lista de sesiones, clips numerados, reproducción, Subir/Bajar, Modo presentación y Exportar.", 62)
    b += "<h2 class='r'>Presentar la sesión al equipo</h2>"
    b += (f"<p>Pulsa <b>Modo presentación</b> ({k('F5')}). Se abre una ventana independiente con su propio reproductor y una línea de tiempo con el contexto del clip. "
          f"Para un proyector o segundo monitor: {k('Win','P')} ▸ Extender, arrastra la ventana y pulsa {k('F11')}. Prueba el proyector antes de la reunión.</p>")
    b += table(["Tecla", "Acción"], [[k("Espacio"), "Reproducir / pausa (o seguir al siguiente clip en modo Pausado)"], [k("→") + " / " + k("←"), "Clip siguiente / anterior"],
                                     [k("R"), "Repetir el clip"], [k("F11") + " o " + k("F") + " / " + k("Esc"), "Pantalla completa / salir"]])
    b += fg("r06.png", "Ventana de presentación: 1 navegación, 2 vídeo, 3 línea de tiempo contextual, 4 controles.", 50)
    b += "<h2 class='r'>Exportar vídeo</h2>"
    b += "<p>Los vídeos exportados son MP4 nuevos que se pueden enviar sin KAIROS; los originales no se tocan.</p>"
    b += '<div class="two"><div><ul>'
    b += (f"<li><b>Exportar…</b> ({k('Ctrl','E')}): un MP4 por cada clip marcado.</li>"
          f"<li><b>Recopilatorio…</b> ({k('Ctrl','Mayús','E')}): un único MP4 con varios clips en el orden que elijas.</li>"
          "<li>Modo <b>Preciso</b> (recomendado) corta en los fotogramas exactos; <b>Rápido</b> es veloz pero aproximado.</li>"
          "<li>Alta calidad por defecto; para enviar por mensajería usa <b>Archivo reducido (720p)</b>.</li>"
          "<li><b>Información superpuesta</b> al vídeo: título, categoría o jugadores sobre la imagen.</li>")
    b += "</ul></div><div>" + fg("r07.png", "Diálogo de exportación: 1 carpeta, 2 modo, 3 calidad, 4 información superpuesta, 5 Exportar.", 75) + "</div></div>"
    b += "<h2 class='r'>Adaptar la pantalla</h2>"
    b += (f"<ul><li>{k('F7')} oculta o muestra el editor inferior de clips; {k('F8')} pliega el panel derecho; {k('F9')} activa el <b>modo concentración</b> (solo reproductor y línea de tiempo).</li>"
          "<li><b>Ver ▸ Restablecer distribución…</b> recupera cualquier panel perdido sin tocar tus datos; <b>Ver ▸ Espacios de trabajo</b> guarda tus distribuciones con nombre.</li>"
          "<li>Si usas KAIROS MARKER: <b>Importar ▸ Sesión de MARKER…</b> trae sus marcas a la línea de tiempo (no son clips).</li></ul>")
    b += "<h2 class='r'>Consejos esenciales</h2><ul>"
    b += ("<li><b>Copia de seguridad:</b> <b>Archivo ▸ Copia de seguridad ▸ Exportar biblioteca…</b> (copia ligera, sin vídeos, o completa) y, para recuperarla, <b>Restaurar copia…</b>.</li>"
          "<li><b>Papelera:</b> un proyecto eliminado se conserva 30 días (<b>Sincronización ▸ Sincronización y compartición… ▸ Papelera</b>).</li>"
          "<li><b>Vídeo «no encontrado»:</b> si moviste o renombraste el archivo, no se pierde ningún clip; usa <b>Relocalizar…</b> en la pestaña Vídeos para indicar su nueva ubicación.</li>"
          "<li>Al abrir KAIROS se reabre el último proyecto. Mientras escribes en un campo, los atajos de teclado no actúan.</li>"
          "<li>Sin Internet KAIROS funciona con normalidad; la red solo se usa para buscar actualizaciones y la sincronización opcional.</li></ul>"
          "<p><i>Esta es la versión abreviada. La guía completa explica cada paso con capturas.</i></p>")
    b += "<p style='font-size:8pt;color:#666'>Las capturas son de KAIROS 0.7.2; en la 0.8.0 el editor de clips es más compacto y el panel derecho se puede plegar.</p></div>"
    css = CSS.replace("@page :first { margin: 0; }", "") + """
@page { margin: 11mm 14mm 15mm 14mm; }
body { font-size: 9pt; line-height: 1.38; }
.sm .step, .sm p, .sm li { font-size: 8.8pt; } .step { margin-bottom: 1.4mm; } p { margin-bottom: 1.6mm; }
h2.r { margin: 3mm 0 1.6mm; padding: 1mm 2.5mm; font-size: 11pt; } h3 { margin: 2mm 0 1mm; font-size: 9.6pt; }
.head { padding: 2.5mm 5mm; margin-bottom: 2.5mm; } .head img { width: 15mm; height: 15mm; } .head h1 { font-size: 15pt; }
.box { padding: 1.4mm 3mm; margin: 1.6mm 0; } table { margin: 1mm 0 2mm; font-size: 8.6pt; } td, th { padding: .8mm 2mm; }
figcaption { font-size: 7.6pt; margin-top: .5mm; } figure img { max-height: 48mm !important; }
"""
    return f'<!doctype html><html lang="es"><meta charset="utf-8"><title>KAIROS — Guía abreviada</title><style>{css}</style><body>{b}</body></html>'


def build(out):
    render_pdf(build_html(), out, "KAIROS — Guía abreviada")
