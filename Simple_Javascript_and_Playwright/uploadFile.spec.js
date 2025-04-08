const { test, expect, chromium } = require('@playwright/test');
const path = require('path');

test('File upload on the-internet.herokuapp.com', async () => {
  const browser = await chromium.launch({ headless: false }); // Launch the browser in headed mode
  const page = await browser.newPage();

  await page.goto('https://the-internet.herokuapp.com/upload');
  const filePath = path.resolve(__dirname, 'testFile.txt');
  await page.setInputFiles('#file-upload', filePath);
  await page.click('#file-submit');
  await expect(page.locator('h3')).toHaveText('File Uploaded!');
  await expect(page.locator('#uploaded-files')).toHaveText('testFile.txt');

  // Wait for 2 seconds before closing the browser
  await page.waitForTimeout(2000); // 2000 milliseconds = 2 seconds

  await browser.close();
});