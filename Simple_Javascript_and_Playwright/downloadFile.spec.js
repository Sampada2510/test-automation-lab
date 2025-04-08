const { test, expect, chromium } = require('@playwright/test');
const path = require('path');

test('Download file from The Internet website', async () => {
  const browser = await chromium.launch({ headless: false });
  const page = await browser.newPage();

  const downloadPath = path.resolve(__dirname, 'downloads');
  
  // Listen for the download event
  page.on('download', (download) => {
    download.saveAs(path.join(downloadPath, download.suggestedFilename()));
  });

  await page.goto('https://the-internet.herokuapp.com/download');
  await page.click('a[href="download/logback.xml"]');
  await page.waitForTimeout(5000);

  console.log(`File downloaded to: ${downloadPath}`);

  await browser.close();
});