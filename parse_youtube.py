import aiohttp
import asyncio
import aiofiles as aiof


async def parse_youtube():
    async with aiohttp.ClientSession() as session:
        async with aiof.open('result.txt', 'w') as f:
            for i in range(100000):
                async with session.get('https://www.googleapis.com/youtube/v3/search',
                                       params={'part': 'id,snippet',
                                               'key': 'AIzaSyA4q1eD08QbJer0kq4B2JynA03Hl2bGnyA',
                                               'q': i,
                                               'order': 'rating'}) as resp:
                    response = await resp.json()
                    items = response.get('items')
                    if items:
                        video_id = items[0]['id']['videoId']
                        await f.write(f'Query: {i} ======> Video_id: {video_id} \n')
                        await f.flush()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(parse_youtube())
