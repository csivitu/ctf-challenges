const puppeteer = require('puppeteer');

const FLAG = process.env.FLAG || 'csictf{fake_flag}';
async function run(url, host) {
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

        return true;
    } catch (e) {
        return false;
    } finally {
        await browser.close();
    }
}

module.exports = run;
