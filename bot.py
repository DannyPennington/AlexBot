# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} is here to fuck shit up')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('$Alex'):
        await message.channel.send(':grimacing:')

    if message.content.content(':grimacing:'):
        await message.channel.send('Agreed')

client.run(TOKEN)