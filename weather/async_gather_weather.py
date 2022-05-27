import asyncio
import time
import aiohttp


async def get_weather(city):
    async with aiohttp.ClientSession() as session:
        url = f'http://api.openweathermap.org/data/2.5/weather' \
                f'?q={city}&APPID=2a4ff86f9aaa70041ec8e82db64abf56'

        async with session.get(url) as response:
            weather_json = await response.json()
            return f'{city}: {weather_json["weather"][0]["main"]}'

async def main(cities_):
    tasks = []
    for city in cities_:
        tasks.append(asyncio.create_task(get_weather(city)))            

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

cities = ['Bratsk', 'Novosibirsk', 'St. Petersburg']        

print(time.strftime('%X'))

asyncio.run(main(cities))

print(time.strftime('%X'))