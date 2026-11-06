// Imprime un HTML a PDF A4 con Chromium (Playwright de Node). Uso: node render.js entrada.html salida.pdf "texto pie" version
const { chromium } = require("playwright");
(async () => {
  const [, , html, out, left, version] = process.argv;
  const b = await chromium.launch();
  const p = await b.newPage();
  await p.goto("file://" + require("path").resolve(html));
  const foot = `<div style="font:8px Inter,Arial;color:#777;width:100%;padding:0 18mm;display:flex;justify-content:space-between"><span>${left}</span><span class="pageNumber"></span><span>KAIROS ${version}</span></div>`;
  await p.pdf({ path: out, preferCSSPageSize: true, printBackground: true, displayHeaderFooter: true, headerTemplate: "<span></span>", footerTemplate: foot });
  await b.close();
})();
