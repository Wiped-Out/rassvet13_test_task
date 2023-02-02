import asyncio
import os

from aiohttp import ClientSession, ClientResponse
from aiohttp.client_exceptions import InvalidURL, ClientConnectionError
from aiofile import async_open
from utils.utils import backoff


async def save_content(response: ClientResponse, host_to_index: dict):
    if not os.path.exists('content'):
        os.mkdir('content')

    host = response.url.host.replace('.', '_')
    if host not in host_to_index.keys():
        host_to_index[host] = 0
    host_to_index[host] += 1

    async with async_open(f'content/{host}_{host_to_index[host]}.html', 'wt') as page:
        await page.write(await response.text())


@backoff(exceptions=(ClientConnectionError,))
async def main():
    urls = input('Enter links separated by commas: ').split(',')

    host_to_index = {}

    async with ClientSession() as client:
        for url in urls:
            try:
                async with client.get(url=url) as response:
                    await save_content(response=response, host_to_index=host_to_index)
            except InvalidURL:
                print(f'{url} is invalid')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
