const puppeteer = require('puppeteer');

const FLAG = process.env.FLAG || 'csictf{fake_flag}';
async function run(url, host, color) {
    const { hostname, port } = new URL(url);

    if (`${hostname}:${port}` !== host) {
        return false;
    }

    const browser = await puppeteer.launch();
    try {
        const page = await browser.newPage();
        await page.setCookie({
            'name': 'password',
            'value': FLAG,
            'domain': hostname,
        });
        await page.goto(url);

        await page.waitFor('input[type=password]');
        await page.waitForSelector('#colorize');
        await page.waitForSelector('#submit');
        await page.evaluate((color) => {
            document.getElementsByTagName('input')[1].value = color;
            document.getElementById('submit').click();
        }, color);
        await page.waitFor(1000);
        return true;
    } catch (e) {
        return false;
    } finally {
        await browser.close();
    }
}

module.exports = run;
