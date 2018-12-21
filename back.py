import discord
import asyncio
from datetime import datetime

client = discord.Client()

async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='518870341171544070')
    while not client.is_closed:
        counter += 1
        counterDay = datetime.today().weekday()
        counterTime = datetime.today().hour
		
        if counterDay == 1 and counterTime == 12:
            await client.send_message(channel, '@everyone Внимание! Завтра начало в 21:00 Сбор в 20:15 в Пайоне')
        elif counterDay == 2 and counterTime == 14:
            await client.send_message(channel, '@everyone Внимание! Сегодня начало в 21:00 Сбор в 20:15 в Пайоне')
        elif counterDay == 5 and counterTime == 12:
            await client.send_message(channel, '@everyone Внимание! Завтра начало в 20:00 Сбор в 19:15 в Пайоне')
        elif counterDay == 6 and counterTime == 14:
            await client.send_message(channel, '@everyone Внимание! Сегодня начало в 20:00 Сбор в 19:15 в Пайоне')
        await asyncio.sleep(3600)
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.loop.create_task(my_background_task())
client.run('NTIzODIwODk4NTMzMjQ0OTI4.DvfOKw.Jr7ZdmfmzAtEg5tXzkAOmCDLC64')