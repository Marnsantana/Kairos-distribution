# KAIROS Distribution

Web pública de una página para descargar KAIROS. Estática (HTML + CSS + JS, sin dependencias ni build). Sin código privado ni secretos.

## Cómo funciona
- **Botón**: enlace permanente `https://github.com/Marnsantana/kairos-releases/releases/latest/download/KAIROS-Setup.exe`. Funciona aunque la API falle.
- **Versión, tamaño y novedades**: `app.js` consulta en el navegador `api.github.com/repos/Marnsantana/kairos-releases/releases/latest` (`cache: no-store`, 1 reintento). `lib.js` solo acepta Releases que no sean draft ni prerelease, con tag `vX.Y.Z` y con el asset `KAIROS-Setup.exe` (el mismo que descarga el botón). Si algo no cuadra o la API falla, **no se muestra versión**.
- **Novedades**: se toman las frases en negrita de las viñetas del cuerpo de la Release (3–5, sin jerga técnica). Menos de 3 → la sección se oculta. Para controlarlas, escribe viñetas `- **Frase corta**: detalle` en las notas.
- No se toca `update-manifest.json` ni su firma.

## Sustituir las guías
Copia los PDF en `guides/` con **estos nombres** y haz commit: `KAIROS-Guia-resumen.pdf` (rápida) y `KAIROS-Guia-de-inicio-rapido-Full.pdf` (manual). Mientras falte uno, su tarjeta muestra «Próximamente». Las rutas están en `index.html` (`data-guide`).

## Textos y estilos
`index.html` (textos, metadatos), `styles.css` (colores en `:root`; naranja `#fe7901`). `assets/` contiene el logo oficial. Tras desplegar, pon la URL **absoluta** en `og:image` (WhatsApp lo exige).

## Despliegue (Vercel)
Proyecto importado desde este repositorio, framework «Other», sin build, directorio de salida `/`. Cada push a `main` despliega a producción; el resto de ramas, a preview.

## Probar
`node --test tests/lib.test.mjs` (Node 18+). Tras publicar una Release nueva, recarga la web: debe mostrar su versión, y `…/releases/latest/download/KAIROS-Setup.exe` debe descargar su instalador. No hace falta tocar la web.
