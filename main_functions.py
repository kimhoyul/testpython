import asyncio
import aiohttp
import json
from bs4 import BeautifulSoup
from config import route_table, site_funcs


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def process_site(session, site):
    html = await fetch(session, site['url'])
    soup = BeautifulSoup(html, 'html.parser')
    site_name = site['site_name']
    func = site_funcs.get(site_name, None)
    if func is not None:
        return func(soup)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for site in route_table:
            task = asyncio.ensure_future(process_site(session, site))
            tasks.append(task)
        news = await asyncio.gather(*tasks)
        json_str = json.dumps(news, ensure_ascii=False)
        print(json_str)