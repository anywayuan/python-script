const puppeteer = require('puppeteer');

(async () => {
  const browser = await puppeteer.launch({
    defaultViewport: null,
    headless: true,
    args: ['--start-maximized']
  });
  const page = await browser.newPage();
  await page.goto('https://yuanki.cn');
  await page.evaluate(() => {
    window.scrollBy({
      top: window.innerHeight,
      left: 0,
      behavior: 'smooth'
    });
  });
  await page.screenshot({path: 'images/yuanki.png', fullPage: true});

  await browser.close();
})();