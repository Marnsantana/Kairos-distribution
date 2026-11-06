import { fetchLatest, formatSize } from "./lib.js";

const $ = (id) => document.getElementById(id);

async function init() {
  const rel = await fetchLatest();
  if (!rel) return; // sin verificación: el botón permanente sigue funcionando y no se muestra versión
  $("version").textContent = `Última versión estable: ${rel.version}`;
  $("footer-version").textContent = `Versión ${rel.version}`;
  const size = formatSize(rel.size);
  if (size) $("size").textContent = `· ${size}`;
  $("notes-link").href = rel.notesUrl;
  if (rel.highlights.length >= 3) {
    $("news-list").replaceChildren(...rel.highlights.map((t) => Object.assign(document.createElement("li"), { textContent: t })));
    $("news-title").textContent = `Novedades de la ${rel.version}`;
    $("news").hidden = false;
  }
}

// Guías: si el PDF aún no está publicado se avisa en lugar de dar un 404.
document.querySelectorAll("a[data-guide]").forEach(async (a) => {
  try {
    const r = await fetch(a.href, { method: "HEAD" });
    if (!r.ok) throw 0;
  } catch (_) {
    a.removeAttribute("href");
    a.setAttribute("aria-disabled", "true");
    a.querySelector(".state").textContent = "Próximamente";
  }
});

init();
