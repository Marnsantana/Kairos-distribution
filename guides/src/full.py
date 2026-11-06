"""Manual completo: «KAIROS — Guía de inicio rápido» (contenido de la 0.7.2 revisado hasta la 0.8.0)."""
from kit import *

CH = []      # (numero, titulo, [secciones], html)
_secs = []


def h2(t):
    _secs.append(t)
    return f"<h2>{t}</h2>"


def add(num, title, body_fn):
    _secs.clear()
    body = body_fn()
    CH.append((num, title, list(_secs), body))


def c0():  # Introducción
    return (h2("Qué vas a conseguir") +
        "<p>Seguirás un ejemplo único de principio a fin: un entrenador importa un partido, localiza varias acciones defensivas, "
        "crea cinco clips, los reúne en una sesión, la presenta al equipo y prepara un vídeo recopilatorio para sus jugadores.</p>"
        + fig("f02.png", "Pantalla principal de KAIROS con el proyecto de ejemplo. Los números se explican en el capítulo 2.") +
        h2("Cómo leer esta guía") +
        step(1, "Los números naranjas de las capturas coinciden con los pasos y las leyendas que las acompañan.") +
        step(2, "Los nombres de botones y menús aparecen tal y como los verás en pantalla. Una flecha ▸ indica un recorrido por menús: "
                "<b>Archivo ▸ Nuevo proyecto…</b>") +
        step(3, f"Las teclas se muestran así: {k('Ctrl','N')}.") +
        box("consejo", "Cada capítulo se puede leer por separado, pero si es tu primera vez, sigue el orden. Con unos 45 minutos tendrás tu primera sesión preparada.") +
        h2("Sobre las capturas y los vídeos de ejemplo") +
        "<p>Las capturas se tomaron con un proyecto de prueba. El vídeo que ves en ellas es un vídeo de ejemplo con jugadores simulados "
        "(no un partido real), creado solo para esta guía. Los nombres de jugadores, equipos y rivales son ficticios. Tu pantalla mostrará "
        "tus propios vídeos y datos.</p>" +
        box("nota", "<b>Capturas de la versión 0.7.2.</b> El texto de esta guía está revisado para la versión 0.8.0. Los controles y los flujos de trabajo "
                    "son los mismos, pero en la 0.8.0 el editor de clips y la línea de tiempo secundaria son más compactos, el panel derecho se puede plegar "
                    "y hay funciones nuevas (zoom de la línea de tiempo, importación de MARKER, modo concentración y espacios de trabajo). "
                    "Por eso tu pantalla puede verse algo distinta a algunas capturas.") +
        box("nota", "KAIROS no copia ni modifica tus vídeos originales: trabaja con referencias a ellos. Los clips son solo intervalos de tiempo anotados. "
                    "Por eso crear, borrar o reorganizar clips nunca daña tus grabaciones.") +
        h2("Qué necesitas") +
        "<ul><li>Un ordenador con Windows 10 u 11 (64 bits).</li><li>Uno o varios archivos de vídeo del partido (formatos <code>.mp4</code>, <code>.mov</code> o <code>.m4v</code>).</li>"
        "<li>No hace falta instalar Python, VLC ni FFmpeg: KAIROS ya los incluye.</li>"
        "<li>No hace falta conexión a Internet para analizar, crear clips, presentar ni exportar.</li></ul>")


add(0, "Antes de empezar", c0)


def c1():
    return ("<p>En este capítulo descargarás el instalador desde el enlace oficial, lo ejecutarás y abrirás KAIROS por primera vez. Son unos 10 minutos.</p>" +
        h2("Abrir el enlace oficial") +
        step(1, "Abre tu navegador y entra en la página oficial de descarga: <code>https://kairos-distribution.vercel.app</code> "
                "(también sirve <code>" + URL_HTTPS + "</code>).") +
        step(2, "Pulsa el botón <b>Descargar KAIROS para Windows</b>. La descarga empieza directamente, sin pasar por ninguna lista de archivos.") +
        step(3, "Si prefieres elegir el archivo tú mismo, entra en <code>" + URL_HTTPS + "</code>, baja hasta el apartado <b>Assets</b> y pulsa en el instalador "
                "<code>KAIROS-Setup.exe</code> (o en <code>KAIROS-Setup-" + VERSION + ".exe</code>).") +
        box("nota", "No necesitas cuenta de GitHub. Ignora «Source code (zip)» y «Source code (tar.gz)», si aparecen: no son el programa. "
                    "La página puede cambiar de aspecto con el tiempo, pero el enlace del paso 1 siempre lleva a la versión más reciente. "
                    "El mismo instalador está disponible con dos nombres, <code>KAIROS-Setup.exe</code> y <code>KAIROS-Setup-" + VERSION + ".exe</code>: son idénticos.") +
        h2("Comprobar que es el archivo esperado") +
        "<p>Antes de ejecutar nada, comprueba tres cosas:</p>" +
        step(1, "Lo has descargado desde el enlace oficial de arriba, no desde un correo, un mensaje ni otra web.") +
        step(2, "El nombre empieza por <b>KAIROS-Setup</b> y termina en <b>.exe</b>.") +
        step(3, "Pesa unos <b>138 MB</b> (si pesa unos pocos kilobytes, algo ha ido mal).") +
        box("consejo", "<b>Comprobación avanzada (opcional).</b> Junto al instalador se publica un archivo <code>.sha256</code> con su «huella digital». En PowerShell, en la carpeta "
                       "Descargas, ejecuta <code>Get-FileHash .\\KAIROS-Setup.exe</code> y comprueba que el valor coincide con el del archivo <code>.sha256</code>. Si no coincide, no lo instales.") +
        h2("Ejecutar el instalador y el aviso de Windows") +
        step(1, "Abre la carpeta Descargas y haz doble clic en el instalador.") +
        step(2, "Es posible que Windows muestre la pantalla azul <b>«Windows protegió su PC»</b> (Microsoft Defender SmartScreen) con un editor desconocido. "
                "Es normal: KAIROS todavía no está firmado con un certificado comercial de editor, y Windows avisa con cualquier programa poco conocido.") +
        step(3, "Si has descargado el instalador del enlace oficial y has comprobado que es el archivo esperado, pulsa <b>«Más información»</b>.") +
        step(4, "Aparecerá el botón <b>«Ejecutar de todas formas»</b>. Púlsalo para continuar.") +
        box("imp", "Haz esto solo con el instalador oficial. No desactives SmartScreen ni el antivirus de Windows: no es necesario y te dejaría desprotegido. "
                   "Si el archivo no viene del enlace oficial, o dudas de que sea el esperado, cancela y no lo ejecutes.") +
        box("nota", "Algunos navegadores también avisan al terminar la descarga («no se descarga habitualmente»). Si el archivo es el del enlace oficial, elige <b>Conservar</b>.") +
        h2("El asistente de instalación") +
        "<p>El asistente está en español. KAIROS se instala solo para tu usuario, sin permisos de administrador. Estas son las pantallas, en orden:</p>" +
        table(["Pantalla", "Qué hacer"], [
            ["Acuerdo de licencia (Condiciones de uso)", "Lee el texto, marca «Acepto el acuerdo» y pulsa <b>Siguiente</b>."],
            ["Carpeta de destino", "Se propone <code>%LOCALAPPDATA%\\Programs\\KAIROS</code>. Lo normal es dejarla tal cual y pulsar <b>Siguiente</b>."],
            ["Tareas adicionales", "«Crear un acceso directo en el escritorio» viene desmarcada. Márcala si quieres el icono en el escritorio."],
            ["Listo para instalar", "Revisa el resumen y pulsa <b>Instalar</b>."],
            ["Instalando", "Espera unos instantes."],
            ["Finalizando", "Deja marcada «Abrir KAIROS» y pulsa <b>Finalizar</b>."]]) +
        box("nota", "Los avisos de Windows y del navegador, y las pantallas del asistente, no llevan captura en esta guía porque su aspecto depende de tu versión de Windows "
                    "y de tu navegador. Si alguna pantalla difiere ligeramente de lo descrito, sigue el mismo orden: aceptar la licencia, dejar la carpeta propuesta, instalar y finalizar.") +
        box("consejo", "El instalador crea el acceso KAIROS en el menú Inicio. Tus datos (proyectos, clips, preferencias) se guardan aparte del programa, en "
                       "<code>%LOCALAPPDATA%\\BasketAnalisis</code>: actualizar o reinstalar KAIROS no los borra.") +
        h2("Abrir KAIROS por primera vez") +
        step(1, "Abre el menú Inicio y pulsa <b>KAIROS</b> (o deja marcada «Abrir KAIROS» al terminar la instalación).") +
        step(2, "Verás una breve pantalla de bienvenida, con un porcentaje discreto de avance en la esquina inferior derecha, y después la ventana principal, todavía vacía. "
                "El primer arranque tras instalar o actualizar es notablemente más rápido que en versiones anteriores.") +
        step(3, "El mensaje del centro te indica qué hacer: «Abre o crea un proyecto para empezar. Archivo ▸ Nuevo proyecto (Ctrl+N)».") +
        "<p>La barra de menús (<b>Archivo, Edición, Exportar, Importar, Proyecto, Reproducción, Ver, Sincronización y Ayuda</b>) reúne todas las funciones, "
        "y los módulos <b>Proyecto, Biblioteca y Sesiones</b> se explican en el capítulo 2.</p>" +
        h2("Avisos de actualización") +
        "<p>Cuando hay una versión nueva, KAIROS te lo dice al arrancar:</p>" +
        fig("f06.png", "Aviso de nueva versión (ejemplo de una actualización anterior; las cifras de tu aviso serán las de tu versión).", 45) +
        step(1, "<b>Actualizar ahora</b>: descarga la nueva versión, comprueba su firma digital, se reinicia solo y conserva todos tus datos.") +
        step(2, "<b>Más tarde</b>: cierra el aviso. Volverá a aparecer la próxima vez que abras KAIROS.") +
        "<p>También puedes buscar actualizaciones cuando quieras desde <b>Ayuda ▸ Buscar actualizaciones…</b>:</p>" +
        fig("f07.png", "Menú Ayuda: 1 menú, 2 Buscar actualizaciones….", 70) +
        box("nota", "Sin conexión a Internet no aparece ningún aviso ni error: KAIROS funciona con normalidad. Si no quieres que busque al iniciar, desmarca la casilla en "
                    "<b>Archivo ▸ Preferencias… ▸ Actualizaciones</b>. Allí también ves la versión instalada.") +
        fig("f08.png", "Preferencias ▸ Actualizaciones: 1 buscar actualizaciones al iniciar.", 80) +
        box("nota", "Si compartes la biblioteca con otros ordenadores mediante la sincronización, actualiza <b>todos</b> a la misma versión. Un equipo con una versión anterior "
                    "a la 0.7.3 te pedirá actualizar KAIROS al leer lo escrito por otro más nuevo."))


add(1, "Descargar e instalar KAIROS", c1)


def c2():
    return ("<p>Antes de crear nada, conviene saber qué es cada zona de la pantalla. Esta es la ventana principal con el proyecto de ejemplo abierto:</p>" +
        fig("f09.png", "Pantalla principal de KAIROS en el módulo Proyecto (captura de la 0.7.2).") +
        step(1, "<b>Barra de menús</b>: Archivo, Edición, Exportar, Importar, Proyecto, Reproducción, Ver, Sincronización y Ayuda.") +
        step(2, "<b>Módulos</b>: Proyecto, Biblioteca y Sesiones. Cambias de uno a otro con un clic.") +
        step(3, "<b>Modo presentación</b>: abre la presentación de una sesión o de un clip en una ventana propia (capítulo 8).") +
        step(4, "<b>Reproductor de vídeo</b>: aquí ves el partido.") +
        step(5, "<b>Línea de tiempo del vídeo</b>: te permite moverte por el partido. Las marcas de colores sobre ella señalan dónde hay clips.") +
        step(6, "<b>Controles de reproducción</b>: pausa, saltos, velocidad y volumen.") +
        step(7, "<b>Editor inferior «Nuevo clip»</b>: el formulario para crear y editar clips.") +
        step(8, "<b>Panel derecho</b> con tres pestañas: Clips, Vídeos y Categorías.") +
        step(9, "<b>Exportar… / Recopilatorio…</b>: sacan tus clips a archivos de vídeo.") +
        h2("Las marcas de colores") +
        "<p>Los clips aparecen sobre la línea de tiempo como pequeñas marcas del color de su valoración: <b>verde</b> positivo, <b>rojo</b> a mejorar, <b>gris</b> neutro. "
        "Si dejas el cursor quieto medio segundo sobre una marca, aparece un aviso con el título del clip y su categoría principal.</p>" +
        h2("Proyecto, Biblioteca y Sesiones") +
        "<p>KAIROS organiza el trabajo en tres módulos. Cada uno responde a una pregunta distinta:</p>" +
        table(["Módulo", "Para qué sirve", "Atajo"], [
            ["Proyecto", "Analizar un partido: ver el vídeo, marcar jugadas y crear clips. Un proyecto = un partido (con uno o varios archivos de vídeo).", k("Ctrl", "1")],
            ["Biblioteca", "Encontrar clips de todos tus partidos en una sola tabla, con filtros por equipo, rival, jugador, categoría, valoración, fechas…", k("Ctrl", "2")],
            ["Sesiones", "Preparar una presentación: una lista ordenada de clips, de uno o varios partidos, para enseñar al equipo.", k("Ctrl", "3")]]) +
        fig("f10.png", "Módulo Biblioteca (1): tabla de todos los clips con filtros.") +
        fig("f11.png", "Módulo Sesiones (1): listas de clips para presentar.") +
        box("nota", "Resumen en una frase: analizas en <b>Proyecto</b>, buscas en <b>Biblioteca</b> y presentas en <b>Sesiones</b>.") +
        h2("Adaptar la pantalla a tu forma de trabajar") +
        box("new", "La 0.8.0 permite ganar espacio para el vídeo y guardar tus propias distribuciones. Todo lo que sigue está en el menú <b>Ver</b> y no toca tus proyectos, clips ni sesiones.") +
        "<ul>"
        f"<li><b>Plegar el panel derecho</b> ({k('F8')}, <b>Ver ▸ Panel derecho desplegado</b>): el bloque lateral completo se pliega hacia el borde y deja una franja con su botón para volver a desplegarlo. "
        "KAIROS recuerda su anchura y su estado.</li>"
        f"<li><b>Editor inferior</b> ({k('F7')}, <b>Ver ▸ Editor inferior</b>): oculta o muestra el formulario de clips.</li>"
        f"<li><b>Modo concentración</b> ({k('F9')}, <b>Ver ▸ Modo concentración</b>): reproductor y línea de tiempo ocupan todo el espacio. Al salir, vuelve exactamente la distribución anterior. "
        f"No es lo mismo que la presentación ({k('F5')}), que abre una ventana aparte.</li>"
        f"<li><b>Pantalla completa</b> ({k('F11')}).</li>"
        "<li><b>Distribución de paneles</b> (<b>Ver ▸ Distribución de paneles</b>): <i>Clásica</i> o <i>Reorganizada</i>.</li>"
        "<li><b>Restablecer distribución…</b> (<b>Ver</b>): recupera paneles ocultos o con tamaños inválidos. Si vas a sobrescribir una distribución personalizada, pide confirmación.</li>"
        "</ul>"
        "<h3>Espacios de trabajo</h3>"
        "<p>Un espacio de trabajo es una distribución con nombre (por ejemplo «Análisis» o «Reunión»). En <b>Ver ▸ Espacios de trabajo</b> puedes activarlos; con "
        "<b>Guardar distribución actual como…</b> guardas la que tienes ahora y con <b>Administrar distribuciones…</b> puedes renombrarlas, eliminarlas o marcar una como predeterminada "
        "(la que recupera «Restablecer distribución»). Guardan proporciones y estados, nunca posiciones absolutas, así que funcionan también en otro monitor.</p>" +
        box("nota", "Si en algún momento el formulario o un panel «desaparece», usa <b>Ver ▸ Editor inferior</b>, <b>Ver ▸ Panel derecho desplegado</b> o <b>Ver ▸ Restablecer distribución…</b>."))


add(2, "Conocer la interfaz", c2)


def c3():
    return ("<p>Un proyecto es la carpeta de trabajo de un partido: reúne sus vídeos, sus clips y los datos del encuentro. En el ejemplo, crearemos el proyecto «Jornada 7 · Defensa vs Rival».</p>" +
        h2("Crear un proyecto nuevo y darle nombre") +
        step(1, f"Abre el menú <b>Archivo</b> y elige <b>Nuevo proyecto…</b> (o pulsa {k('Ctrl','N')}).") +
        fig("f12.png", "Menú Archivo: 1 menú, 2 Nuevo proyecto….", 70) +
        step(2, "Escribe el <b>nombre</b> del proyecto (1). Es lo único obligatorio.") +
        step(3, "Si ya tienes un equipo creado, elígelo en <b>Equipo</b> (2): sus jugadores quedarán convocados para el partido.") +
        step(4, "Opcionalmente, escribe el <b>rival</b> (3), la fecha, la competición, el resultado u observaciones. Sirven para filtrar después en la Biblioteca.") +
        step(5, "Pulsa <b>Aceptar</b> (4).") +
        fig("f13.png", "Diálogo «Nuevo proyecto»: 1 nombre, 2 equipo, 3 rival, 4 Aceptar.", 50) +
        box("consejo", "Un buen nombre incluye la jornada y el rival: «J7 · Cadete A vs CB Rival». Así lo reconocerás enseguida en la lista de proyectos.") +
        h2("Incorporar los vídeos del partido") +
        "<p>Al aceptar, KAIROS crea el proyecto y te abre automáticamente el selector de archivos de Windows.</p>" +
        step(1, f"Selecciona el vídeo (o varios a la vez, con {k('Ctrl')} + clic).") +
        step(2, "Pulsa <b>Abrir</b> (2).") +
        fig("f14.png", "Selector de archivos de Windows: 1 vídeos del partido, 2 Abrir.", 80) +
        box("nota", "Formatos admitidos: <code>.mp4</code>, <code>.mov</code> y <code>.m4v</code>. KAIROS no copia tus vídeos: guarda una referencia a su ubicación. "
                    "Los originales no se mueven ni se modifican nunca.") +
        "<p>El vídeo se abre en el reproductor, listo para empezar. Si no ves nada, el proyecto está vacío (así se ve justo después de crearlo, antes de añadir vídeos):</p>" +
        fig("f15.png", "Proyecto recién creado: 1 reproductor, todavía sin vídeo.") +
        f"<h3>Añadir más vídeos más tarde</h3><p>Elige <b>Archivo ▸ Añadir vídeo al proyecto…</b> ({k('Ctrl','Mayús','O')}) o usa <b>Añadir…</b> en la pestaña Vídeos.</p>" +
        h2("Partidos grabados por cuartos o mitades") +
        "<p>Muchos partidos se graban en varios archivos (un archivo por cuarto o por mitad). En KAIROS no hace falta unirlos: añádelos todos al mismo proyecto.</p>" +
        step(1, "Abre la pestaña <b>Vídeos</b> del panel derecho (1).") +
        step(2, "Comprueba que aparecen en el orden correcto (2). Si no, usa <b>Subir</b> y <b>Bajar</b>.") +
        step(3, "Pulsa <b>Añadir…</b> (3) para incluir otro archivo.") +
        fig("f16.png", "Pestaña Vídeos: 1 pestaña, 2 lista de vídeos del proyecto, 3 Añadir….", 60) +
        "<p>Fíjate en la columna <b>Tipo</b>: <i>Secuencia</i> significa «parte consecutiva del partido» (1.er cuarto, 2.º cuarto…) y <i>Alternativa</i>, «otra cámara o grabación del mismo partido». "
        "Se cambia con el botón <b>Secuencia / alternativa</b>. Arriba de la lista eliges cómo se reproducen:</p>"
        "<ul><li><b>Independiente</b>: cada archivo tiene su propia línea de tiempo y eliges cuál ver (por defecto).</li>"
        "<li><b>Continuo</b>: los archivos de la secuencia forman una única línea de tiempo; al acabar uno, empieza el siguiente. Lo verás en el capítulo 4.</li></ul>" +
        box("consejo", "Para no perderte, indica el cuarto en el editor «Nuevo clip» (campo <b>Cuarto activo</b>): los clips nuevos heredarán ese cuarto.") +
        h2("Abrir y reproducir el partido") +
        step(1, "En la pestaña <b>Vídeos</b>, haz doble clic sobre el archivo que quieras ver (o selecciónalo y pulsa <b>Abrir</b>).") +
        step(2, f"Pulsa el botón naranja ▶ o la tecla {k('Espacio')} para reproducir o pausar.") +
        "<p>KAIROS recuerda por dónde ibas en cada vídeo y te ofrece continuar desde ese punto.</p>" +
        h2("Guardar y recuperar un proyecto") +
        "<p>No hay botón «Guardar proyecto»: todo se guarda automáticamente en tu biblioteca a medida que trabajas (vídeos añadidos, clips, títulos, categorías…).</p>"
        "<ul><li>Al abrir KAIROS, se abre solo el último proyecto en el que trabajaste.</li>"
        f"<li>Para abrir otro: <b>Archivo ▸ Abrir proyecto…</b> ({k('Ctrl','O')}). Verás la lista con el número de vídeos y de clips de cada uno. Selecciona uno y pulsa <b>Abrir</b>.</li></ul>" +
        fig("f17.png", "Diálogo «Abrir proyecto»: nombre, vídeos, clips, último acceso y carpeta.", 70) +
        box("nota", "Para eliminar un proyecto: <b>Edición ▸ Mover el proyecto actual a la papelera…</b>. No se borra de golpe: queda 30 días en la papelera y puedes recuperarlo "
                    "(<b>Sincronización ▸ Sincronización y compartición… ▸ Papelera</b>). Los vídeos originales no se tocan."))


add(3, "Crear el primer proyecto", c3)


def c4():
    return ("<p>Para encontrar una jugada necesitas moverte con rapidez por el partido. KAIROS combina botones, línea de tiempo y teclado.</p>" +
        h2("Controles de reproducción") +
        "<p>Bajo el vídeo tienes la barra de control. Pasa el ratón por encima de cada botón para ver su ayuda.</p>" +
        fig("f18.png", "Barra de control del reproductor.") +
        step(1, f"«: retroceder un salto medio (5 s). Tecla {k('J')}.") + step(2, f"‹: retroceder un salto corto (1 s). Tecla {k('←')}.") +
        step(3, f"Fotograma anterior (aproximado). {k('Alt','←')}.") + step(4, f"▶ / Pausa. {k('Espacio')}.") +
        step(5, f"Fotograma siguiente. {k('Alt','→')}.") + step(6, f"›: avanzar un salto corto (1 s). {k('→')}.") +
        step(7, f"»: avanzar un salto medio (5 s). {k('L')}.") + step(8, "Tiempo: posición actual / duración del vídeo.") +
        step(9, "Velocidad: de 0,5× a 2×.") + step(10, "Volumen y silencio.") +
        step(11, "Línea de tiempo: arrastra el marcador o haz clic para saltar a ese punto.") +
        box("consejo", f"Para analizar una jugada con calma: pausa con {k('Espacio')}, retrocede con {k('←')} y avanza fotograma a fotograma con {k('Alt','→')}. "
                       f"Para buscar una acción, sube la velocidad con {k('+')} y bájala con {k('-')} (con {k('0')} vuelves a 1×).") +
        "<p>El menú <b>Reproducción</b> reúne también la velocidad, la relación de aspecto (Ajustar, Rellenar, Estirar) y los pasos por fotograma:</p>" +
        fig("f19.png", "Menú Reproducción.", 70) +
        h2("Desplazarse por la línea de tiempo") +
        "<ul><li>Haz clic en cualquier punto de la barra para saltar allí, o arrastra el marcador.</li>"
        "<li>Las marcas de colores te llevan a los clips ya creados: haz clic en una para seleccionarlo. Con el cursor quieto medio segundo sobre una marca verás su título y su categoría.</li>"
        "<li>Los saltos con el teclado son configurables en <b>Archivo ▸ Preferencias… ▸ Reproducción</b>.</li></ul>" +
        h2("Acercar la línea de tiempo (zoom)") +
        box("new", "En partidos largos, el zoom te deja ver unos pocos minutos con todo detalle. Es solo una vista: no cambia la velocidad, los tiempos ni los clips.") +
        "<ul><li>Bajo la línea de tiempo hay un <b>deslizador de zoom</b> con su porcentaje (de 100 % a 2000 %), un botón <b>100 %</b> para volver a la vista completa y una "
        "<b>barra de desplazamiento</b> horizontal (solo está activa si el zoom no deja ver toda la duración).</li>"
        f"<li>Con el ratón: {k('Ctrl')} + rueda acerca o aleja alrededor del puntero; la rueda sola desplaza la vista cuando hay zoom.</li>"
        "<li>Con dos horas de partido, al 400 % se ven 30 minutos en el mismo ancho. Cabezal, clips, marcas y separadores entre archivos se ajustan juntos, "
        "así que los clics y los arrastres siempre apuntan al tiempo correcto.</li>"
        "<li>Durante la reproducción, si el cabezal sale de la ventana, la vista pasa de página para mantenerlo visible. Al abrir otro proyecto o cambiar de modo vuelve al 100 %. "
        "La ventana de presentación no tiene zoom (su línea de tiempo es la contextual del clip).</li></ul>" +
        h2("Cambiar entre archivos de vídeo") +
        "<p>Si el partido está en varios archivos tienes dos opciones:</p>" +
        step(1, "<b>Cambio manual</b>: en la pestaña Vídeos, doble clic en el archivo que quieras.") +
        step(2, "<b>Timeline continuo</b>: <b>Proyecto ▸ Timeline continuo (secuencia de vídeos)</b> o el modo <b>Continuo</b> de la pestaña Vídeos. Los archivos se reproducen uno tras otro como si fueran un solo partido.") +
        fig("f20.png", "Menú Proyecto: 1 menú, 2 Timeline continuo (secuencia de vídeos).", 70) +
        "<p>Con el timeline continuo activado, la línea de tiempo muestra la duración total (en el ejemplo, 03:30, la suma de los dos cuartos) y las marcas de los clips de ambos archivos:</p>" +
        fig("f21.png", "Modo continuo: 1 opción Continuo, 2 archivos de la secuencia, 3 línea de tiempo única, 4 duración total.") +
        box("nota", "Un clip siempre pertenece a un solo archivo de vídeo: no puede empezar en un cuarto y terminar en otro. Los archivos originales no se unen ni se modifican.") +
        h2("Marcas de KAIROS MARKER (opcional)") +
        box("new", "Si tomas notas durante el partido con KAIROS MARKER, puedes traer esas marcas a la línea de tiempo. Las marcas <b>no son clips</b>: sirven de guía para saltar a los momentos importantes.") +
        step(1, "Con un proyecto abierto, elige <b>Importar ▸ Sesión de MARKER…</b> y selecciona el archivo <code>.kairosmarker</code> o <code>.kairosmarker.json</code>. "
                "KAIROS valida el archivo antes de guardar nada; si no es válido, lo rechaza con un mensaje claro y no importa nada a medias.") +
        step(2, "Bajo la línea de tiempo aparece una franja de marcas: <b>verdes</b> positivas, <b>rojas</b> negativas, <b>neutras</b> sin clasificar y las de fin de cuarto con las etiquetas 1C, 2C, 3C y FINAL. "
                "«FINAL» no detiene ni recorta la reproducción.") +
        step(3, "Pulsa una marca para llevar el reproductor a ese instante. No crea ningún clip ni cambia nada más.") +
        step(4, "Si las marcas no encajan con el vídeo, en <b>Importar ▸ Sesiones de MARKER importadas…</b> ajusta el desplazamiento de toda la sesión (en segundos, con precisión de milisegundos; "
                "«Restablecer a 0» lo anula). Las marcas que queden fuera del vídeo se conservan y se señalan «fuera de rango».") +
        box("nota", "Importar dos veces el mismo archivo solo avisa de que ya está importado. «Quitar sesión» borra la sesión y sus marcas, sin afectar a vídeos ni clips. "
                    "Las marcas importadas van en las copias de seguridad de la biblioteca, pero no viajan en la sincronización ni en los archivos <code>.basket</code>.") +
        h2("Atajos de teclado básicos") +
        "<p>Estos atajos funcionan con KAIROS en primer plano. No actúan mientras escribes en un campo de texto (por ejemplo, el título de un clip), así que puedes escribir una «S» sin guardar nada por error.</p>" +
        table(["Tecla", "Acción"], [
            [k("Espacio"), "Reproducir / pausa"], [k("←") + " / " + k("→"), "Retroceder / avanzar un salto corto (1 s)"],
            [k("J") + " / " + k("L"), "Retroceder / avanzar un salto medio (5 s)"], [k("Alt", "←") + " / " + k("Alt", "→"), "Fotograma anterior / siguiente"],
            [k("-") + " / " + k("+") + " / " + k("0"), "Bajar velocidad / subir velocidad / velocidad normal"],
            [k("I") + " / " + k("O"), "Marcar inicio / final de un clip nuevo"], [k("S"), "Guardar clip"],
            [k("Esc"), "Descartar las marcas y empezar un clip nuevo"], [k("1") + " – " + k("9"), "Crear un clip automático de esa categoría (capítulo 5)"],
            [k("P"), "Reproducir el clip seleccionado"], [k("Ctrl", "Z"), "Deshacer el último cambio de clips"],
            [k("X"), "Marcar el clip activo para exportar"], [k("Ctrl", "E"), "Exportar clips"],
            [k("F5"), "Modo presentación"], [k("Ctrl", "1") + " / 2 / 3", "Ir a Proyecto / Biblioteca / Sesiones"],
            [k("F7"), "Ocultar / mostrar el editor inferior (formulario de clips)"], [k("F8"), "Plegar / desplegar el panel derecho"],
            [k("F9"), "Modo concentración"], [k("F11"), "Pantalla completa"], [k("F1"), "Ayuda de atajos"]]) +
        "<p>La lista completa está siempre a mano en <b>Ayuda ▸ Atajos de teclado</b> (" + k("F1") + "):</p>" +
        fig("f22.png", "Ayuda ▸ Atajos de teclado.", 55) +
        box("consejo", "Puedes cambiar cualquier atajo en <b>Archivo ▸ Preferencias… ▸ Atajos</b>; KAIROS avisa si dos acciones chocan."))


add(4, "Reproducir y navegar por el vídeo", c4)


def c5():
    return ("<p>Un clip es un tramo de un vídeo con su información: título, categorías, jugadores, comentario y valoración. Es la pieza básica de KAIROS. "
        "En el ejemplo, vamos a crear el primer clip defensivo: «Balance defensivo tras pérdida», entre los segundos 12 y 19 del primer cuarto.</p>" +
        h2("Identificar la jugada y marcar el inicio") +
        step(1, f"Reproduce el partido hasta que veas la jugada. Cuando la acción esté a punto de empezar, pausa con {k('Espacio')}.") +
        step(2, f"Si te has pasado, retrocede con {k('←')} hasta el instante en el que empieza la jugada.") +
        step(3, f"Pulsa el botón <b>Inicio (I)</b> (1) o la tecla {k('I')}.") +
        step(4, "El tiempo aparece en el campo Inicio (2) y como marca naranja en la línea de tiempo (3). La barra de estado dice «Inicio marcado en…».") +
        fig("f23.png", "Inicio marcado: 1 botón Inicio (I), 2 campo Inicio, 3 marca en la línea de tiempo.") +
        h2("Marcar el final") +
        step(1, "Reproduce hasta que acabe la jugada y pausa.") +
        step(2, f"Pulsa <b>Final (O)</b> (1) o la tecla {k('O')}.") +
        step(3, "El tiempo del final aparece en su campo (2). Debajo se dibuja el tramo seleccionado (en naranja) y la duración (3).") +
        fig("f24.png", "Final marcado: 1 botón Final (O), 2 campo Final, 3 campo Inicio. Debajo, la línea de tiempo ampliada con el tramo seleccionado.") +
        h2("Ajustar los límites") +
        "<p>Casi nunca se acierta a la primera, y no pasa nada: puedes afinar el clip antes y después de guardarlo.</p>"
        "<ul><li>Escribe el tiempo exacto en los campos <b>Inicio</b> y <b>Final</b> (formato <code>mm:ss.mmm</code>, por ejemplo <code>00:12.000</code>).</li>"
        "<li>Usa los pequeños botones ◂ ▸ junto a Inicio y Final en la línea de tiempo ampliada para mover cada extremo.</li>"
        "<li>Arrastra los extremos naranjas del tramo.</li>"
        "<li>Con <b>Previsualizar</b> ves el clip tal y como quedaría; con − y + acercas o alejas la línea de tiempo y con <b>Ajustar</b> la encajas.</li>"
        f"<li>En un clip ya guardado, {k('Mayús','I')} y {k('Mayús','O')} ponen el inicio o el final en la posición actual del vídeo.</li></ul>" +
        box("nota", "En la 0.8.0 el editor de clips ocupa menos altura y la línea de tiempo secundaria es más pequeña, pero los controles, la precisión de entrada y salida y los atajos son los mismos.") +
        box("consejo", "Deja un par de segundos antes de que empiece la acción: sin el contexto previo, a los jugadores les cuesta entender de dónde viene la jugada.") +
        h2("Título, categorías, jugadores, comentario y valoración") +
        "<p>Completa el formulario «Nuevo clip». Todo es opcional salvo el tramo de vídeo, pero cuanto más completo, más fácil será encontrar el clip después.</p>" +
        step(1, "<b>Título</b> (opcional): un nombre corto y claro, por ejemplo «Balance defensivo tras pérdida». Si lo dejas vacío, el clip se identificará por su categoría.") +
        step(2, "<b>Categorías</b>: marca las casillas de la pestaña Categorías. Puedes elegir una o varias. KAIROS trae por defecto <i>Defensa</i> (Balance defensivo, Rebote defensivo, "
                "Defensa del bloqueo directo, Defensa individual, Rotaciones) y <i>Ataque</i>. La primera que marques es la <b>categoría principal</b>: es la que se muestra en las tarjetas y la que ordena los clips.") +
        step(3, "<b>Jugadores</b>: abre la pestaña Jugadores y marca a quienes intervienen en la jugada (si el proyecto tiene equipo convocado).") +
        step(4, "<b>Valoración</b>: Positivo, A mejorar o Neutro (por defecto). Úsala para separar lo que quieres reforzar de lo que hay que corregir.") +
        step(5, "<b>Comentario</b>: una nota interna del entrenador. No se exporta salvo que tú lo elijas.") +
        step(6, "<b>Guardar clip (S)</b>.") +
        fig("f25.png", "Formulario del clip: 1 título, 2 categorías, 3 pestañas (Categorías, Jugadores, Detalles), 4 valoración, 5 comentario, 6 Guardar clip (S).") +
        "<p>Marca también <b>★ Favorito</b> si quieres tener localizados tus mejores ejemplos.</p>"
        "<h3>Asociar jugadores</h3><p>La pestaña Jugadores muestra la convocatoria del partido (entre paréntesis, cuántos jugadores hay). Marca las casillas de los jugadores que aparecen en la acción.</p>" +
        fig("f26.png", "Pestaña Jugadores: 1 pestañas, 2 jugadores convocados.") +
        box("nota", "Si el proyecto no tiene equipo, verás el aviso «Sin convocatoria». Puedes crear equipos y jugadores en <b>Proyecto ▸ Equipos y jugadores…</b> y convocarlos en <b>Proyecto ▸ Equipo y convocatoria…</b>.") +
        "<h3>Los demás datos (opcionales)</h3><p>La pestaña <b>Detalles</b> permite indicar el cuarto, el reloj del partido, la situación de juego, un mensaje para el jugador y etiquetas. No los necesitas para tu primera sesión.</p>" +
        fig("f27.png", "Pestaña Detalles: datos opcionales del clip.") +
        h2("Guardar el clip y localizarlo después") +
        step(1, f"Pulsa <b>Guardar clip (S)</b> o la tecla {k('S')}.") +
        step(2, "Aparece el aviso verde «✓ Clip guardado 00:12 – 00:19» y el formulario queda listo para el siguiente clip.") +
        step(3, "El clip se añade a la pestaña <b>Clips</b> del panel derecho (1), con su color de valoración, su título, su categoría principal y sus jugadores.") +
        fig("f28.png", "Clip guardado: 1 tarjeta del nuevo clip en la pestaña Clips.") +
        "<p>Para localizarlo más tarde, búscalo en la pestaña Clips, haz clic en su marca de color sobre la línea de tiempo o encuéntralo en la Biblioteca (capítulo 6).</p>" +
        box("consejo", f"<b>Deshacer:</b> {k('Ctrl','Z')} deshace el último cambio de clips (crear, editar o eliminar) y {k('Ctrl','Y')} lo rehace.") +
        h2("Clips automáticos: una tecla y listo") +
        f"<p>Cuando ves una acción de una categoría, no hace falta marcar inicio y final: pulsa la tecla numérica de la categoría ({k('1')} a {k('9')}). "
        "Cada categoría por defecto tiene su número entre corchetes: [1] Balance defensivo, [2] Rebote defensivo, [3] Defensa del bloqueo directo, [4] Defensa individual, [5] Rotaciones… (puedes cambiarlos).</p>"
        "<p>KAIROS crea el clip automáticamente: empieza unos segundos antes del instante en el que pulsas la tecla y termina unos segundos después, siempre dentro del mismo archivo de vídeo. "
        "Por defecto, <b>10 segundos antes y 0 después</b>. Estos valores se ajustan en <b>Archivo ▸ Preferencias… ▸ Clips automáticos</b>:</p>" +
        fig("f29.png", "Preferencias ▸ Clips automáticos: 1 segundos anteriores, 2 segundos posteriores, 3 modo.", 80) +
        "<p>Además puedes decidir si el vídeo sigue reproduciéndose o se pausa al crear el clip, y qué valoración recibe por defecto.</p>"
        "<h3>Modo Revisión y modo Rápido</h3>" +
        table(["Modo", "Qué ocurre al pulsar la tecla", "Cuándo usarlo"], [
            ["Revisión (por defecto)", f"Prepara un borrador: ves el tramo y la categoría en el formulario y tú lo guardas con {k('S')} (o lo descartas con {k('Esc')}).", "Cuando quieres ajustar el inicio y el final o añadir título y jugadores."],
            ["Rápido", "El clip se guarda al instante.", "Cuando analizas en directo o a toda velocidad y retocas después."]]) +
        "<p>El modo Revisión se ve así: el clip está preparado pero aún no guardado.</p>" +
        fig("f30.png", "Clip automático en modo Revisión: 1 inicio, 2 final, 3 categoría ya marcada, 4 Guardar clip (S).") +
        box("consejo", f"Un buen flujo para ver un partido entero: reproduce a velocidad normal, pulsa la tecla de la categoría cada vez que veas una acción y revisa los clips al final. "
                       f"Si te equivocas, {k('Ctrl','Z')} deshace el último clip automático.") +
        h2("Cómo queda el ejemplo") +
        "<p>Repite el proceso hasta tener cinco jugadas defensivas. En el ejemplo, el primer cuarto aporta cuatro y el segundo cuarto, una:</p>" +
        table(["#", "Clip", "Categoría principal", "Valoración"], [
            ["1", "Balance defensivo tras pérdida", "Balance defensivo", "A mejorar"], ["2", "Ayuda en el bloqueo directo", "Defensa del bloqueo directo", "Positivo"],
            ["3", "Rebote defensivo y salida", "Rebote defensivo", "Positivo"], ["4", "Defensa individual en la esquina", "Defensa individual", "A mejorar"],
            ["5", "Rotaciones tras ayuda", "Rotaciones", "Neutro"]]))


add(5, "Crear el primer clip", c5)


def c6():
    return ("<p>Con cinco clips creados, ya puedes consultarlos, filtrarlos, corregirlos y ordenar tus proyectos.</p>" +
        h2("La lista de clips del proyecto") +
        "<p>La pestaña <b>Clips</b> del panel derecho muestra los clips del proyecto abierto. Cada clip es una tarjeta compacta: ocupa poco para que quepan muchos.</p>" +
        fig("f31.png", "Pestaña Clips con las tarjetas compactas.", 55) +
        step(1, "Buscar en título o comentario.") + step(2, "Filtrar por valoración (y, justo al lado, por categoría).") + step(3, "Filtrar por jugador.") + step(4, "Tarjetas de los clips.") +
        "<h3>Cómo leer una tarjeta</h3>" + fig("f32.png", "Una tarjeta compacta, en detalle.", 80) +
        step(1, f"Casilla: marca el clip para exportarlo o incluirlo en un recopilatorio ({k('X')} hace lo mismo).") +
        step(2, "Punto de color: valoración (verde positivo, rojo a mejorar, gris neutro).") + step(3, "★: clip favorito.") +
        step(4, "Título del clip (o su categoría, si no tiene título).") + step(5, "Categoría principal y jugadores (con dorsal).") +
        "<p>Al seleccionar una tarjeta se amplía y muestra más datos: tiempo de inicio y final, duración, todas las categorías y el archivo de vídeo.</p>" +
        h2("Consultar los detalles de un clip") +
        step(1, "Haz clic en una tarjeta (1). El vídeo salta al clip y la tarjeta se amplía.") +
        step(2, "El formulario de abajo pasa a «Editando clip» (2) y muestra todos los datos.") +
        step(3, f"Pulsa <b>Reproducir clip</b> (3) o {k('P')} para verlo solo, sin salirse de sus límites.") +
        fig("f33.png", "Clip seleccionado: 1 tarjeta ampliada, 2 formulario de edición, 3 Reproducir clip, 4 Eliminar.") +
        h2("Filtrar y localizar jugadas") +
        "<p>Los filtros se combinan entre sí. Por ejemplo, para ver solo las jugadas a mejorar:</p>" +
        fig("f34.png", "Filtro por valoración: 1 «A mejorar». Solo quedan los clips con ese color.", 55) +
        "<p>O para buscar por texto, escribe en el buscador (en el ejemplo, «bloqueo»):</p>" +
        fig("f35.png", "Búsqueda por texto: 1 buscador.", 55) +
        box("consejo", "Para quitar un filtro, vuelve a elegir «Todas las valoraciones» o borra el texto del buscador.") +
        h2("Editar clips existentes") +
        step(1, "Selecciona el clip.") +
        step(2, "Cambia lo que necesites en el formulario: tiempos, título, categorías, jugadores, valoración, comentario o favorito.") +
        step(3, "Los cambios se guardan automáticamente: no hay botón de guardar.") +
        f"<p>Para borrarlo, pulsa <b>Eliminar</b> (4) o {k('Supr')}; KAIROS pide confirmación y {k('Ctrl','Z')} lo recupera.</p>" +
        box("nota", "<b>Categoría principal.</b> Es la primera categoría asignada al clip. Si añades otras, no cambia; si quitas la principal, pasa a serlo la siguiente. "
                    "En los clips creados con versiones anteriores a la 0.7.2 se respeta el orden en que ya estaban guardados, así que la principal de algún clip antiguo puede verse distinta la primera vez.") +
        h2("La Biblioteca: todos tus clips") +
        f"<p>Cuando acumulas varios partidos, el módulo <b>Biblioteca</b> ({k('Ctrl','2')}) reúne todos los clips de todos los proyectos en una tabla. Sus filtros permiten cruzar equipo, temporada, partido, rival, jugador, categoría, valoración, etiquetas, cuarto, favoritos, fecha y duración.</p>" +
        step(1, "<b>Seleccionar visibles</b> marca todos los clips que ves ahora (con filtros aplicados o sin ellos).") +
        step(2, "La tabla muestra título, categorías, valoración, jugadores, proyecto, equipo, rival, fecha, duración…") +
        step(3, "<b>Exportar…</b> saca los clips marcados a archivos de vídeo.") + step(4, "<b>Recopilatorio…</b> los une en un solo vídeo.") +
        step(5, "<b>Añadir a sesión ▾</b> los incorpora a una sesión existente.") + step(6, "<b>+ Generar nueva sesión</b> crea una sesión con ellos.") +
        fig("f36.png", "Biblioteca con los clips marcados.") +
        h2("Organizar proyectos en carpetas") +
        "<p>Si tienes muchos proyectos, agrúpalos en carpetas (por temporada, competición, rival…). Es opcional: lo que no esté en una carpeta sigue en «(sin carpeta)».</p>" +
        step(1, "Abre <b>Archivo ▸ Carpetas…</b>.") + step(2, "Pulsa <b>Nueva carpeta</b> (2) para crear una; puedes crear carpetas dentro de otras.") +
        step(3, "Arrastra un proyecto hasta la carpeta donde quieras guardarlo (o hasta «(sin carpeta)»). También puedes usar <b>Mover a…</b>.") +
        step(4, "Con clic derecho sobre un proyecto, el menú contextual ofrece <b>Mover a…</b> y <b>Eliminar proyecto…</b> (va a la papelera, como siempre, con confirmación).") +
        fig("f37.png", "Carpetas: 1 árbol de carpetas y proyectos, 2 Nueva carpeta.") +
        box("nota", "Eliminar una carpeta no borra nada: su contenido sube un nivel."))


add(6, "Organizar y consultar clips", c6)


def c7():
    return (h2("Qué es una sesión y para qué sirve") +
        "<p>Una sesión es una lista ordenada de clips pensada para enseñar. Puede contener clips de un partido o de varios, de cualquier proyecto de tu biblioteca. "
        "Los clips no se copian: la sesión solo guarda referencias, así que si corriges un clip, la sesión lo refleja.</p>"
        "<p>Es la herramienta ideal para preparar la reunión de vídeo con el equipo, repasar un tema (por ejemplo, defensa del bloqueo directo) o enseñar a un jugador sus acciones.</p>" +
        h2("Ejemplo: cinco jugadas defensivas para el equipo") +
        "<p>Vamos a preparar la sesión «Defensa: 5 jugadas para el equipo» con los cinco clips del capítulo anterior.</p>" +
        h2("Crear una sesión nueva") + "<p>La forma más rápida es partir de los clips:</p>" +
        step(1, f"Entra en la <b>Biblioteca</b> ({k('Ctrl','2')}).") + step(2, "Marca los clips (con <b>Seleccionar visibles</b> o con las casillas).") +
        step(3, "Pulsa <b>+ Generar nueva sesión</b>.") +
        step(4, "Escribe el <b>nombre</b> (1). Opcionalmente, añade una descripción, una fecha, el equipo (2) o el jugador destinatarios.") + step(5, "Pulsa <b>Crear</b> (3).") +
        fig("f38.png", "Nueva sesión: 1 nombre, 2 equipo destinatario, 3 Crear. Abajo se indica cuántos clips se añadirán.", 60) +
        box("nota", f"También puedes empezar en el módulo Sesiones ({k('Ctrl','3')}): pulsa <b>+ Generar nueva sesión</b> y añade los clips después con <b>Añadir desde la biblioteca</b>.") +
        h2("La pantalla de Sesiones") + fig("f39.png", "Módulo Sesiones con la sesión del ejemplo.") +
        step(1, "<b>+ Generar nueva sesión</b>.") + step(2, "Lista de sesiones: elige la que quieras ver. Se guardan solas.") + step(3, "Clips de la sesión, numerados en orden.") +
        step(4, "Reproducción: <b>Continuo</b> (un clip detrás de otro) o <b>Pausado</b> (se detiene al acabar cada clip y tú decides cuándo seguir). Y <b>Repetir sesión</b>.") +
        step(5, "<b>Añadir desde la biblioteca</b>.") + step(6, "<b>Subir</b> y <b>Bajar</b>: cambian el orden del clip seleccionado.") + step(7, "<b>Añadir a otra sesión…</b>") +
        step(8, "<b>▶ Reproducir sesión</b>: la ves en el reproductor de esta misma ventana.") + step(9, "<b>Modo presentación</b>: la abre en una ventana propia (capítulo 8).") +
        step(10, "<b>Exportar…</b> y <b>Recopilatorio…</b>: sacan la sesión a vídeo (capítulo 9).") +
        h2("Incorporar clips y combinar partidos") +
        step(1, "En Biblioteca, marca clips de cualquier proyecto (puedes mezclar partidos distintos).") + step(2, "Pulsa <b>Añadir a sesión ▾</b> y elige la sesión.") +
        step(3, "KAIROS te dice cuántos clips ha añadido y cuántos ya estaban (no se duplican).") + "<p>También desde Sesiones: <b>Añadir desde la biblioteca</b>.</p>" +
        box("consejo", "Mezclar partidos es muy útil para comparar: por ejemplo, la misma defensa del bloqueo directo en dos jornadas distintas.") +
        h2("Ordenar los clips") + step(1, "Selecciona un clip de la lista.") + step(2, "Pulsa <b>Subir</b> o <b>Bajar</b> hasta dejarlo donde quieras.") +
        "<p>Para un mensaje claro al equipo, ordena de más sencillo a más complejo, o agrupa primero lo positivo y después lo que mejorar.</p>" +
        h2("Añadir clips a otra sesión") +
        "<p>Si quieres reutilizar clips en otra sesión (por ejemplo, para un jugador concreto), sin perderlos de la original:</p>" +
        step(1, f"Selecciona uno o varios clips de la sesión ({k('Ctrl')} + clic).") +
        step(2, "Pulsa <b>Añadir a otra sesión…</b> (1) (también está en el menú del clic derecho).") + step(3, "Elige la sesión de destino y pulsa <b>Añadir</b> (2).") +
        fig("f40.png", "Dos clips seleccionados: 1 clips elegidos, 2 Añadir a otra sesión….", 55) +
        fig("f41.png", "Elegir la sesión de destino: 1 sesiones disponibles (con su número de clips), 2 Añadir.", 45) +
        "<p>Los clips siguen también en la sesión original, se añaden al final de la de destino, en el mismo orden y sin duplicados. Funciona entre sesiones de proyectos distintos.</p>" +
        h2("Guardar y recuperar la sesión") +
        f"<p>Las sesiones se guardan solas. Para recuperar una más adelante, entra en Sesiones ({k('Ctrl','3')}) y elígela en la lista. "
        "Para quitar un clip de la sesión, selecciónalo y pulsa <b>Quitar de la sesión</b>: solo lo retira de la lista, no lo borra de tu biblioteca.</p>")


add(7, "Crear una sesión de vídeo", c7)


def c8():
    return ("<p>Cuando tengas la sesión preparada, puedes presentarla al equipo: en el monitor del ordenador, en una pantalla externa o con un proyector. "
        "La presentación se abre en su propia ventana, con su propio reproductor, para que no dependa de lo que hagas en la ventana principal.</p>" +
        h2("Abrir el modo Presentación") +
        step(1, "Entra en Sesiones y elige la sesión.") + step(2, "Selecciona el clip por el que quieras empezar (si no, empieza por el primero).") +
        step(3, f"Pulsa <b>Modo presentación</b> (o {k('F5')}, o <b>Ver ▸ Modo presentación</b>).") +
        h2("La ventana de presentación") +
        "<p>Se abre una ventana independiente, titulada con el nombre de la sesión, que ya empieza a reproducir:</p>" +
        fig("f42.png", "Ventana de presentación: 1 navegación, 2 vídeo, 3 línea de tiempo contextual, 4 controles.") +
        step(1, f"<b>Navegación</b>: Anterior, Siguiente, Repetir clip y Pantalla completa ({k('F11')}). En la cabecera se indica en qué clip estás («1/5 · Balance defensivo tras pérdida — Jornada 7 · Defensa vs Rival»).") +
        step(2, "Vídeo del clip actual.") + step(3, "Línea de tiempo contextual (ver abajo).") + step(4, "Controles de reproducción, igual que en la ventana principal.") +
        "<p>Teclas dentro de la ventana de presentación:</p>" +
        table(["Tecla", "Acción"], [
            [k("Espacio"), "Reproducir / pausa (y, en modo Pausado, continuar con el siguiente clip)"], [k("→") + " o " + k("Av Pág"), "Clip siguiente"],
            [k("←") + " o " + k("Re Pág"), "Clip anterior"], [k("R"), "Repetir el clip actual"],
            [k("F11") + " o " + k("F"), "Pantalla completa (también con doble clic sobre el vídeo)"], [k("Esc"), "Salir de la pantalla completa"]]) +
        h2("Llevar la presentación a un segundo monitor o proyector") +
        step(1, f"Conecta el monitor o el proyector y configura Windows para extender la pantalla ({k('Win','P')} ▸ Extender).") +
        step(2, "Arrastra la ventana de presentación hasta la otra pantalla.") + step(3, f"Pulsa {k('F11')} (o Pantalla completa) para que ocupe toda la pantalla.") +
        box("consejo", "Haz una prueba con el proyector antes de la reunión: comprueba imagen, sonido y que la ventana principal sigue en tu portátil.") +
        h2("Reproducir los clips") + "<p>La presentación sigue el modo de la sesión (lo eliges en Sesiones):</p>"
        "<ul><li><b>Continuo</b>: cuando acaba un clip, pasa solo al siguiente.</li>"
        "<li><b>Pausado</b>: al acabar cada clip se detiene. Tú decides cuándo continuar con Espacio o Siguiente. Es ideal para comentar cada jugada.</li></ul>"
        "<p>Cada clip se reproduce entre sus límites, sin añadir segundos.</p>" +
        h2("Timeline contextual") +
        "<p>Bajo el vídeo, la línea de tiempo muestra el clip resaltado y, a cada lado, el contexto del partido: por defecto 15 segundos antes y 15 después.</p>"
        "<ul><li>Sirve para revisar qué pasó antes o después de la jugada sin tocar el clip: haz clic o arrastra dentro del contexto.</li>"
        "<li>Al pulsar Siguiente, vuelves a los límites del siguiente clip.</li>"
        "<li>El contexto nunca se sale del vídeo: si el clip está cerca del inicio o del final del archivo, solo muestra lo que existe. En el ejemplo, el primer clip empieza en el segundo 12, así que el contexto solo muestra desde el segundo 0.</li>"
        "<li>Es una vista de consulta: no mueve los extremos del clip.</li></ul>"
        "<p>El margen se cambia en <b>Archivo ▸ Preferencias… ▸ Edición</b> (5, 10, 15 o 20 segundos).</p>" +
        fig("f43.png", "Preferencias ▸ Edición: 1 contexto del timeline.", 80) +
        h2("Seguir trabajando mientras presentas") +
        "<p>La ventana de presentación trabaja con una copia de la lista de clips del momento en que la abres. Mientras se presenta, en la ventana principal puedes:</p>"
        "<ul><li>Elegir otros clips, previsualizarlos y editar títulos o categorías.</li><li>Preparar otra sesión.</li><li>Cambiar de módulo o de proyecto.</li></ul>"
        "<p>Nada de eso cambia ni detiene lo que se está presentando. Cada ventana tiene su propio reproductor y su propio sonido.</p>" +
        box("nota", "Solo hay una presentación abierta a la vez. Si pides la misma de nuevo, simplemente se trae al frente. Si pides otra distinta, KAIROS pregunta antes de cerrar la actual y abrir la nueva. "
                    f"El modo concentración ({k('F9')}) es independiente de la presentación.") +
        h2("Cerrar la presentación sin cerrar KAIROS") +
        f"<p>Cierra la ventana de presentación con la X de su esquina (o pulsa {k('F5')} en la ventana principal). KAIROS sigue abierto tal y como lo dejaste.</p>")


add(8, "Presentar una sesión", c8)


def c9():
    return ("<p>Exportar convierte tus clips en archivos de vídeo MP4 que puedes enviar a los jugadores, subir a una nube o reproducir en cualquier ordenador o móvil, sin necesitar KAIROS. "
        "Los vídeos originales no se modifican: se generan archivos nuevos.</p><p>KAIROS ofrece dos formas de exportar:</p>" +
        table(["Opción", "Resultado", "Úsala para…"], [["Exportar…", "Un archivo MP4 por cada clip.", "Enviar a un jugador su jugada concreta."],
            ["Recopilatorio…", "Un único MP4 con varios clips unidos, en el orden que elijas.", "Preparar el vídeo de la reunión o un resumen del partido."]]) +
        h2("Exportar un clip individual") +
        step(1, "Selecciona el clip en la pestaña Clips (o márcalo con su casilla).") +
        step(2, f"Pulsa <b>Exportar…</b> (o {k('Ctrl','E')}, o el menú <b>Exportar ▸ Exportar clips (activo o marcados)…</b>).") +
        step(3, "Elige las opciones (ver abajo) y pulsa <b>Exportar</b> (5).") +
        fig("f44.png", "Diálogo de exportación de un clip: 1 carpeta, 2 modo, 3 calidad, 4 información superpuesta, 5 Exportar.", 60) +
        "<h3>Elegir las opciones</h3>"
        "<ul><li><b>Carpeta de destino</b> (1). Pulsa <b>Cambiar…</b> para elegir otra.</li>"
        "<li><b>Nombre</b>: se genera solo con el formato <code>Partido_Categoría_Minuto_Título.mp4</code>. Puedes editarlo cuando exportas un solo clip.</li>"
        "<li><b>Modo</b> (2): <b>Preciso</b> (recomendado) recodifica el vídeo y corta exactamente en los fotogramas marcados; es algo más lento. "
        "<b>Rápido</b> copia el vídeo sin recodificar y es muy veloz, pero los cortes son aproximados (se ajustan al fotograma clave más cercano).</li>"
        "<li><b>Calidad</b> (3): Máxima calidad, <b>Alta calidad</b> (por defecto), Equilibrada o Archivo reducido (720p).</li>"
        "<li><b>Conservar el audio</b>: marcada por defecto. La duración total y la nota «Los vídeos originales no se modifican» te recuerdan qué va a pasar.</li></ul>" +
        box("consejo", "Si dudas, deja Preciso y Alta calidad. Para enviar por mensajería o correo, usa Archivo reducido (720p): pesa mucho menos.") +
        "<h3>Información superpuesta al vídeo</h3>"
        "<p>Activa la casilla «Información superpuesta al vídeo» (4) para escribir datos sobre la imagen (arriba a la izquierda, una línea por dato): título del clip, categoría, jugadores asociados, "
        "proyecto y la duración (de 0,5 a 10 s) durante la que se muestran. Los datos vacíos no aparecen.</p>" +
        h2("Exportar varios clips") +
        step(1, "Marca los clips con sus casillas (o <b>Marcar visibles</b> en la pestaña Clips, o <b>Seleccionar visibles</b> en la Biblioteca).") +
        step(2, "Pulsa <b>Exportar…</b>: el diálogo es el mismo, y en lugar de un solo nombre te muestra la lista de nombres automáticos (1).") +
        step(3, "Pulsa <b>Exportar</b>: se crea un MP4 por clip en la carpeta elegida.") +
        fig("f45.png", "Exportar tres clips: 1 nombres de los archivos que se generarán.", 60) +
        h2("Generar un recopilatorio") +
        step(1, "Marca los clips que quieres unir (desde Proyecto, Biblioteca o una sesión).") +
        step(2, f"Pulsa <b>Recopilatorio…</b> (o {k('Ctrl','Mayús','E')}). Se abre la ventana «Crear recopilatorio».") +
        step(3, "Ordena los clips, configura los títulos y el archivo (ver abajo).") + step(4, "Pulsa <b>Exportar recopilatorio</b> (7).") +
        fig("f46.png", "Ventana «Crear recopilatorio».", 75) +
        "<h3>Ordenar los clips</h3>" +
        step(1, "<b>Orden</b>: elige Cronológico, Categoría, Jugador o Valoración y pulsa <b>Ordenar</b>.") +
        step(2, "La lista muestra los clips en el orden en que saldrán, con el tiempo, la categoría, los jugadores y el archivo de origen.") +
        step(3, "Ajusta a mano: arrastra los clips o usa <b>Subir</b>, <b>Bajar</b> y <b>Quitar</b>. <b>Añadir marcados</b> incorpora más.") +
        box("nota", "Si lo exportas desde una sesión, el recopilatorio conserva el orden que tú diste a la sesión.") +
        "<h3>Títulos de pantalla</h3>" +
        step(4, "<b>Pantallas de título</b>: elige <b>Con títulos</b> para intercalar una pantalla breve antes de cada clip (por defecto 3 segundos) con la categoría, el título, los jugadores o el proyecto. "
                "Con <b>Título inicial</b> añades una portada al principio con un título y un subtítulo (por ejemplo, «ANÁLISIS DEFENSIVO · Partido contra Rival»).") +
        "<h3>Elegir la carpeta de destino</h3>" +
        step(5, "En <b>Archivo</b> eliges la carpeta (<b>Cambiar…</b>), el nombre del archivo (ya propuesto, con el partido y la fecha), la calidad y si se conserva el audio.") +
        "<h3>Superposiciones sobre el vídeo</h3>" +
        step(6, "<b>Información superpuesta al vídeo</b>: igual que al exportar un clip, pero se aplica a todos los clips del recopilatorio.") +
        box("nota", "Los recopilatorios se exportan siempre en modo preciso (los fragmentos se igualan en resolución y audio antes de unirse). "
                    "Las opciones de la parte inferior sobre anotaciones y pausas puedes dejarlas como están: se explican en otros materiales.") +
        h2("Seguir la exportación y localizar el MP4") +
        step(1, "Al pulsar Exportar, KAIROS muestra una ventana de progreso. Puedes cancelar cuando quieras. La ventana principal sigue disponible mientras tanto.") +
        step(2, "Al terminar verás el aviso «✓ Exportación terminada».") +
        step(3, "Abre el Explorador de archivos de Windows y entra en la carpeta de destino que elegiste (la que ves en el campo Carpeta).") +
        step(4, "Haz doble clic en el MP4 para reproducirlo con el reproductor de Windows o con cualquier otro.") +
        box("consejo", "Mientras se exporta, KAIROS escribe un archivo temporal con extensión <code>.part</code> y solo lo convierte en MP4 definitivo al terminar con éxito. Así nunca te quedas con un MP4 «a medias» que parezca válido.") +
        h2("Qué has conseguido") +
        "<p>Has completado el recorrido: importaste un partido, identificaste cinco jugadas defensivas, creaste cinco clips, los reuniste en una sesión, la presentaste al equipo y generaste un recopilatorio para tus jugadores.</p>")


add(9, "Exportar clips y recopilatorios", c9)


def c10():
    return (h2("Consejos para trabajar mejor") +
        "<ul><li><b>Empieza con pocos datos.</b> Título, una categoría y valoración bastan. Ya completarás jugadores y comentarios cuando tengas tiempo.</li>"
        "<li><b>Nombres coherentes.</b> Usa siempre la misma forma de nombrar proyectos y sesiones (jornada, rival, tema).</li>"
        "<li><b>Haz copias de seguridad</b> de vez en cuando: <b>Archivo ▸ Copia de seguridad ▸ Exportar biblioteca…</b> Elige <i>Copia ligera</i> (proyectos, clips, categorías, equipos…, sin vídeos) "
        "o <i>Copia completa</i> (además, los vídeos originales que selecciones).</li>"
        "<li><b>Guarda los vídeos en una carpeta fija</b> y no los muevas: KAIROS los localiza por su ruta.</li>"
        f"<li><b>Aprende tres atajos</b> y notarás la diferencia: {k('Espacio')} (pausa), {k('I')} / {k('O')} / {k('S')} (marcar y guardar) y las teclas {k('1')} – {k('9')} (clips automáticos).</li>"
        f"<li><b>Gana espacio cuando analizas:</b> {k('F8')} pliega el panel derecho y {k('F9')} deja solo el reproductor y la línea de tiempo.</li></ul>" +
        h2("Preguntas frecuentes") +
        "<h3>¿Dónde se guardan mis proyectos?</h3><p>En tu propio ordenador, en la carpeta de datos de KAIROS: <code>%LOCALAPPDATA%\\BasketAnalisis</code> (se abre desde <b>Archivo ▸ Abrir carpeta de datos</b>). "
        "Allí están la biblioteca (proyectos, clips, sesiones, equipos, categorías) y tus preferencias. Los vídeos no están ahí: siguen en la carpeta donde los tenías.</p>"
        "<h3>¿Tengo que volver a importar el vídeo cada vez?</h3><p>No. El proyecto recuerda los archivos del partido. Al volver a abrirlo, el vídeo está listo y KAIROS incluso te ofrece continuar desde donde lo dejaste. Solo tienes que añadir el vídeo la primera vez.</p>"
        "<h3>¿Qué ocurre si muevo un archivo de vídeo?</h3><p>Como KAIROS guarda la ruta del vídeo, al moverlo o renombrarlo el proyecto aparece con el vídeo «no encontrado». No se pierde ningún clip. Para repararlo:</p>" +
        step(1, "Abre la pestaña <b>Vídeos</b> del proyecto.") + step(2, "Selecciona el vídeo ausente y pulsa <b>Relocalizar…</b> para indicar su nueva ubicación.") +
        step(3, "O pulsa <b>Buscar ausentes en carpeta…</b> y elige la carpeta donde ahora están: KAIROS los busca por nombre y tamaño.") +
        "<p>También puedes usar <b>Sincronización ▸ Localizar vídeos ausentes…</b>.</p>"
        "<h3>¿Cómo recupero un proyecto?</h3>"
        f"<ul><li>Un proyecto de la lista: <b>Archivo ▸ Abrir proyecto…</b> ({k('Ctrl','O')}).</li>"
        "<li>Un proyecto eliminado por error: estará 30 días en la papelera. Entra en <b>Sincronización ▸ Sincronización y compartición… ▸ Papelera</b> y restáuralo.</li>"
        "<li>Un problema grave (por ejemplo, un ordenador nuevo): restaura tu copia de seguridad con <b>Archivo ▸ Copia de seguridad ▸ Restaurar copia…</b> (archivo <code>.zip</code>). Si la copia era ligera, tendrás que volver a vincular los vídeos (ver arriba).</li></ul>"
        "<h3>¿Cómo actualizo KAIROS?</h3><p>Cuando hay una versión nueva, KAIROS te avisa al abrirlo. Pulsa <b>Actualizar ahora</b>: descarga, verifica, instala y reabre KAIROS solo, conservando tus datos. "
        "También puedes comprobarlo tú con <b>Ayuda ▸ Buscar actualizaciones…</b>. No hace falta volver a descargar el instalador a mano.</p>"
        "<h3>¿Puedo utilizarlo sin conexión?</h3><p>Sí. Analizar, crear clips, organizarlos, presentar y exportar funcionan sin Internet. La conexión solo se usa para buscar actualizaciones y para la sincronización opcional. Si no hay conexión, KAIROS simplemente no muestra avisos.</p>"
        "<h3>No veo el formulario o un panel (o la pantalla se ve rara)</h3>"
        "<p>Usa el menú <b>Ver</b>: <b>Editor inferior</b> (F7), <b>Panel derecho desplegado</b> (F8) o, si algo quedó con un tamaño imposible, <b>Restablecer distribución…</b>. "
        "No toca tus proyectos, clips ni sesiones. Si estás en modo concentración, sal con F9.</p>"
        "<h3>¿Cómo puedo llevar una sesión a otro ordenador?</h3><p>Hay dos caminos, según lo que necesites:</p>" +
        step(1, "<b>Solo el vídeo, para enseñar</b>: exporta la sesión como recopilatorio MP4 (capítulo 9) y llévalo en un pendrive o por la nube. Se reproduce en cualquier equipo.") +
        step(2, "<b>La sesión editable en otro KAIROS</b>: ve a <b>Sincronización ▸ Sincronización y compartición… ▸ Archivos y copias</b>, elige en la lista la <i>Sesión (autónoma)</i> y pulsa <b>Exportar…</b> (1). "
                "Se crea un archivo <code>.basket</code> (sin vídeos, pesa poco). En el otro ordenador, abre esa misma pestaña, pulsa <b>Importar archivo…</b> (2) y se añade como una copia nueva sin tocar lo que ya tienes. "
                "Después vincula los vídeos (<b>Relocalizar…</b>) en el otro equipo.") +
        fig("f47.png", "Sincronización ▸ Archivos y copias: 1 elegir, 2 Exportar…, 3 Importar archivo….", 60) +
        box("nota", "Los archivos <code>.basket</code> no incluyen los vídeos: solo los datos (clips, categorías, orden de la sesión…). Los vídeos hay que llevarlos aparte. Tampoco incluyen las marcas importadas de MARKER.") +
        "<h3>¿Qué hago si una exportación falla?</h3>" +
        step(1, "Lee el aviso: KAIROS muestra «Exportación fallida:» con el motivo.") +
        step(2, "Comprueba el espacio libre en el disco de la carpeta de destino y que tienes permiso de escritura (prueba con otra carpeta, por ejemplo en el Escritorio).") +
        step(3, "Comprueba que el vídeo original está disponible (que no esté «no encontrado» y que el disco externo esté conectado).") +
        step(4, "Cierra el MP4 si lo tienes abierto en un reproductor.") +
        step(5, "Vuelve a intentarlo. Los archivos temporales se borran siempre y no queda ningún MP4 incompleto con el nombre final.") +
        step(6, "Si falla siempre con el mismo clip, prueba el modo Preciso y calidad Equilibrada, o exporta ese clip aparte para localizar el problema.") +
        "<h3>¿Se modifican mis vídeos originales?</h3><p>Nunca. KAIROS solo los lee. Los clips son intervalos y las exportaciones son archivos nuevos.</p>" +
        h2("Dónde pedir ayuda") +
        "<p>Si algo no funciona como esperas, anota qué estabas haciendo y el mensaje exacto que aparece, y compártelo con la persona que te facilitó KAIROS. "
        "Las novedades de cada versión están en la página de descargas oficial:</p>"
        f"<p><code>{URL_HTTPS}</code></p>")


add(10, "Consejos y preguntas frecuentes", c10)


def build_html(pages=None):
    pages = pages or {}
    toc = ""
    for num, title, secs, _ in CH:
        label = ("Introducción: " if num == 0 else f"{num}. ") + title
        toc += f'<div class="tc"><span>{label}</span><span class="dots"></span><span class="pg">{pages.get(title, "")}</span></div>'
        toc += "".join(f'<div class="ts"><span>{s}</span><span class="dots"></span><span class="pg">{pages.get(s, "")}</span></div>'.replace('class="ts"', 'class="ts"') for s in secs)
    body = "".join(chap("Introducción" if n == 0 else n, t, b).replace("CAPÍTULO Introducción", "INTRODUCCIÓN") for n, t, s, b in CH)
    cover = (f'<div class="cover"><img src="{img_uri(LOGO)}" alt="KAIROS"><h1>KAIROS — Guía de inicio rápido</h1>'
             '<div class="sub">Del primer partido a tu primera sesión de vídeo</div>'
             f'<div class="ref">Versión de referencia: <b>KAIROS {VERSION}</b><br>Guía para entrenadores de baloncesto · {FECHA}<br>Descarga oficial: {URL_OFICIAL}</div></div>')
    return (f'<!doctype html><html lang="es"><meta charset="utf-8"><title>KAIROS — Guía de inicio rápido</title><style>{CSS}</style><body>{cover}'
            f'<section><h1 class="t">Índice</h1><div class="toc">{toc}</div></section>{body}</body></html>')


def titles():
    t = []
    for num, title, secs, _ in CH:
        t.append(title)
        t += secs
    return t


def build(out):
    render_pdf(build_html(), out, "KAIROS — Guía de inicio rápido")
    pages = find_pages(out, titles(), start=3)
    render_pdf(build_html(pages), out, "KAIROS — Guía de inicio rápido")
    pages2 = find_pages(out, titles(), start=3)
    if pages2 != pages:   # el índice puede mover páginas: una pasada más
        render_pdf(build_html(pages2), out, "KAIROS — Guía de inicio rápido")
    missing = [t for t in titles() if t not in pages2]
    return missing
