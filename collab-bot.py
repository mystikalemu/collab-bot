import discord
import asyncio
import random
import pickle
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.name)
    print('------')
                        
@client.event
async def on_message(message): 
    if( message.content.lower().startswith("is mat awesome?") ):
        await client.send_message(message.channel, "Of course")
client.run('MzY3NDE5NDc1ODAyMzI1MDIz.DL7Tcg.9XiuryVqkQ_-wu9ozMH7FyVSxOM')
