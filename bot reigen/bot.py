import discord
import random
import os
import requests
from discord.ext import commands

from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)

@bot.event
async def on_ready():
    print(f'Estamos logados como {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Olá, {ctx.author.mention}! eu sou o {bot.user}!')

@bot.command()
async def pasw(ctx):
    senha = gen_pass(10)
    await ctx.send(f'Sua senha gerada é:', {senha})

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command()
async def meme(ctx):
    img_name = random.choice(os.listdir('imagens'))
    # E é assim que você pode substituir o nome do arquivo por uma variável!
    with open(f'imagens/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_fox_image_url():
    url = 'https://randomfox.ca/floof/'
    res = requests.get(url)

    data = res.json()
    print(data)
    return data['image']

@bot.command('fox')
async def fox(ctx):
    '''Uma vez que chamamos o comando fox, o programa chama a função get_fox_image_url '''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run("-")
