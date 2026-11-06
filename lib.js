// Lógica pura (sin DOM): validar la Release y extraer novedades. Probada en tests/lib.test.mjs
export const REPO = "Marnsantana/kairos-releases";
export const INSTALLER = "KAIROS-Setup.exe";
export const API_LATEST = `https://api.github.com/repos/${REPO}/releases/latest`;
export const STABLE_TAG = /^v?(\d+\.\d+\.\d+)$/;

/** Devuelve {version, size, notesUrl, highlights} o null si la Release no es estable/verificable. */
export function parseRelease(rel) {
  if (!rel || rel.draft || rel.prerelease) return null;
  const m = STABLE_TAG.exec(rel.tag_name || "");
  if (!m) return null;
  const asset = (rel.assets || []).find((a) => a.name === INSTALLER);
  if (!asset) return null; // el botón descarga este archivo: sin él no mostramos versión
  return {
    version: m[1],
    size: asset.size || null,
    notesUrl: rel.html_url || `https://github.com/${REPO}/releases`,
    highlights: extractHighlights(rel.body || ""),
  };
}

const TECH = /`|test_|\.py|sqlite|esquema|libvlc|ffmpeg|ci\b|corregid|causa raíz|\/|\bapi\b/i;

/** 3–5 titulares legibles: la frase en negrita de cada viñeta, sin jerga técnica. */
export function extractHighlights(body, max = 5) {
  const out = [];
  for (const line of body.split(/\r?\n/)) {
    const m = /^\s*[-*]\s+\*\*(.+?)\*\*/.exec(line);
    if (!m) continue;
    let t = m[1].replace(/[:.\s]+$/, "").trim();
    if (t.length < 8 || t.length > 90 || TECH.test(t) || /^enlace permanente/i.test(t)) continue;
    if (!out.includes(t)) out.push(t);
    if (out.length >= max) break;
  }
  return out;
}

export function formatSize(bytes) {
  return bytes ? `${Math.round(bytes / 1048576)} MB` : null;
}

/** GET con un reintento ante errores temporales. Nunca lanza: devuelve null si falla. */
export async function fetchLatest(fetchImpl = fetch) {
  for (let i = 0; i < 2; i++) {
    try {
      const r = await fetchImpl(API_LATEST, {
        cache: "no-store",
        headers: { Accept: "application/vnd.github+json" },
      });
      if (r.ok) return parseRelease(await r.json());
      if (r.status < 500 && r.status !== 429) return null;
    } catch (_) { /* red: reintentar */ }
    await new Promise((res) => setTimeout(res, 600));
  }
  return null;
}
