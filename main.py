import discord
from discord.ext import commands
import reicikler

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='a!', intents=intents)
TOKEN = "bot_token"
word_list = ["hello", "Evangelion", "Hi chat", "Helloo", "Hello", "Greetings", "evangelion", "good nights", "good sleeps", "hi.", "Neon Genesis Evangelion"]

@bot.event
async def on_ready():
    print("«««««««««««««««««««««««««««««««««««")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    # Special reactions to Asuka and Rei
    elif "asuka" in message.content.lower() and message.content.lower().index("asuka") == 0:
        await message.channel.typing()
        await reicikler.asukaspeak(message)
        return
    
    elif "<@bot_id>" in message.content.lower(): 
        await message.channel.typing()
        await reicikler.asukaspeak(message)
        return
        
    elif "rei" in message.content.lower() and message.content.lower().index("rei") == 0:
        await message.channel.typing()
        await reicikler.reispeak(message)
        return

    # Checking the words in the list
    elif any(word.lower() in message.content.lower() for word in liste):
        await message.channel.typing()
        await reicikler.asukaspeak(message)
        return

    # check whether the reply message was sent by a bot or not
    elif message.reference and message.reference.message_id and message.reference.resolved.author.id == bot.user.id:
        await message.channel.typing()
        await reicikler.asukaspeak(message)
        return

    await bot.process_commands(message)

@bot.command()
async def yaz(ctx, *, context):
        await message.channel.typing()
        await ctx.send(context)
        await ctx.message.delete()

@bot.command()
async def ping(ctx):
    await message.channel.typing()
    await ctx.send("Pong")
    await reicikler.reimsj("Pong")

bot.run(TOKEN)