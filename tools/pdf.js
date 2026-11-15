// Converts a description page to PDF: node tools/pdf.js <in.html> <out.pdf>
// Used by tools/build.py for apartments whose Drive folder has no description PDF.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(src), { waitUntil: 'load' });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
})().catch(e => { console.error(e.message); process.exit(1); });
