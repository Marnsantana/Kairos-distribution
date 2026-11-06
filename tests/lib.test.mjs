import test from "node:test";
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { parseRelease, extractHighlights, fetchLatest } from "../lib.js";

const notes = JSON.parse(readFileSync(new URL("./manifest-sample.json", import.meta.url))).notes;
const rel = (o = {}) => ({ tag_name: "v0.8.0", draft: false, prerelease: false, html_url: "https://x/r", body: notes,
  assets: [{ name: "KAIROS-Setup.exe", size: 144180120 }], ...o });

test("release estable válida", () => {
  const r = parseRelease(rel());
  assert.equal(r.version, "0.8.0"); assert.equal(r.size, 144180120);
  assert.ok(r.highlights.length >= 3 && r.highlights.length <= 5, r.highlights.join("|"));
});
test("excluye draft, prerelease, rc y sin instalador", () => {
  assert.equal(parseRelease(rel({ draft: true })), null);
  assert.equal(parseRelease(rel({ prerelease: true })), null);
  assert.equal(parseRelease(rel({ tag_name: "v0.9.0rc1" })), null);
  assert.equal(parseRelease(rel({ assets: [] })), null);
});
test("novedades sin jerga técnica", () => {
  assert.ok(extractHighlights(notes).every((t) => !/`|test_/.test(t)));
});
test("errores de GitHub: reintenta y nunca lanza", async () => {
  let n = 0;
  assert.equal(await fetchLatest(async () => { n++; return { ok: false, status: 503 }; }), null); assert.equal(n, 2);
  assert.equal(await fetchLatest(async () => { throw new Error("red"); }), null);
  assert.equal(await fetchLatest(async () => ({ ok: false, status: 403 })), null);
  const ok = await fetchLatest(async () => ({ ok: true, status: 200, json: async () => rel() }));
  assert.equal(ok.version, "0.8.0");
});
