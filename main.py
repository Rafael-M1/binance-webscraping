import asyncio
import re
from datetime import datetime, timezone, timedelta
from playwright.async_api import async_playwright

URL = "https://www.binance.com/pt-BR/trade/SOL_USDT?type=spot"
INTERVAL_SECONDS = 1
TIMEZONE=0

async def run(page):
    await page.goto(URL, wait_until="domcontentloaded")
    await page.wait_for_function("document.title.includes('Binance Spot')")
    title = await page.title()
    match = re.search(r"(\d+\.\d+)", title)
    value = float(match.group(1))
    print(f'{value} - {current_time()}')

async def main():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()

        while True:
            await run(page)
            await asyncio.sleep(INTERVAL_SECONDS)

def current_time():
    return datetime.now(timezone(timedelta(hours=TIMEZONE))).strftime("%d/%m/%Y %H:%M:%S %Z")

asyncio.run(main())