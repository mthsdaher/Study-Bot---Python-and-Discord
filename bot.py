from discord.ext import commands
import discord

BOT_TOKEN = "MTIyMDM4MzgzOTQzMjYwOTgyMw.G3laaz.T_hzwajSSEErdUqZCcRC07cmmLVjik_vAwFs-4"
CHANNEL_ID = 1222899794612191242

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

"""function to print the message on the discord"""
@bot.event
async def on_ready():
    message = print("Hello! Study bot is ready!")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Study bot is ready!")

"""the commando to type the message with the prefix (!) on discord and them reply on discord"""
@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

@bot.command()
async def add(ctx, x, y):
    result = int(x) + int(y)
    await ctx.send(f"The result is: {result}")

@bot.command()
async def sub(ctx, x, y):
    result = int(x) - int(y)
    await ctx.send(f"The result is: {result}")

@bot.command()
async def multply(ctx, x, y):
    result = int(x) * int(y)
    await ctx.send(f"The result is: {result}")

@bot.command()
async def divide(ctx, x, y):
    result = int(x) / int(y)
    await ctx.send(f"The result is: {result}")


bot.run(BOT_TOKEN)