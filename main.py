import asyncio
import re
from datetime import datetime
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium # or "firefox" or "webkit".
    browser = await chromium.launch(headless=True)
    page = await browser.new_page()
    await page.goto("https://www.binance.com/pt-BR/trade/BTC_USDT?type=spot")
    await page.wait_for_function("document.title.includes('Binance Spot')")
    current_datetime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    title = await page.title()
    match = re.search(r"(\d+\.\d+)", title)
    value = float(match.group(1))
    print(f'{value} - {current_datetime}')
    await browser.close()

async def repeated_task(playwright: Playwright, interval: int):
    while True:
        await run(playwright)
        await asyncio.sleep(interval) 

async def main():
    async with async_playwright() as playwright:
        interval_seconds = 1
        await repeated_task(playwright, interval_seconds)
asyncio.run(main())