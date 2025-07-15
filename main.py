import discord
from discord.ext import commands
from config import Token, DATABASE
from logic import DB_Manager, AnimalInfo

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
animal_info = AnimalInfo(DB_Manager(DATABASE))

@bot.event
async def on_ready():
    print(f'{bot.user.name} çalışmaya başladı!')

@bot.command()
async def hayvan(ctx):
    bilgi = animal_info.get_random_info()
    await ctx.send(bilgi)

bot.run(Token)