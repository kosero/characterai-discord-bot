import discord
import asyncio
import random
import aiohttp
from characterai import PyAsyncCAI
from discord.ext import commands

async def reimsj(message):
    webhook_url = "webhook"
    
    async with aiohttp.ClientSession() as session:
        payload = {
            "content": message
        }

        async with session.post(webhook_url, json=payload) as response:
            if response.status == 204:
                print("Gönderildi.")
            else:
                print(f"HTTP kodu: {response.status}")

async def asukaspeak(message):
    client = PyAsyncCAI('char_token')
    char = 'char'

    await message.channel.typing()

    author_name = message.author.name
    chat = await client.chat2.get_chat(char)
    author = {'name': author_name, 'author_id': chat['chats'][0]['creator_id']}

    async with client.connect() as chat2:
        data = await chat2.send_message(
            char, chat['chats'][0]['chat_id'],
            f"Person named {author_name} says to you: {message.content}",  
            author
        )

    text = data['turn']['candidates'][0]['raw_content']

    await message.channel.send(text, reference=message)
    return

async def reispeak(message):
    client = PyAsyncCAI('char_token')
    char = 'char'

    author_name = message.author.name
    chat = await client.chat2.get_chat(char)
    author = {'name': author_name, 'author_id': chat['chats'][0]['creator_id']}

    async with client.connect() as chat2:
        data = await chat2.send_message(
            char, chat['chats'][0]['chat_id'],
            f"Person named {author_name} says to you: {message.content}",  
            author
        )

    text = data['turn']['candidates'][0]['raw_content']

    await reimsj(text)
    return