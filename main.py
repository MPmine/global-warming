import discord
from discord.ext import commands
from discord import Embed, Color, ButtonStyle, Button, ui

TOKEN = 'ТОКЕН'
intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!',intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def prevent_global_warming(ctx):
    await ctx.send('Чтобы предотвратить глобальное потепление, вы можете использовать энергосберегающие лампы, ездить на общественном транспорте, сортировать мусор и многое другое.')

@bot.command()
async def climate_stats(ctx):
    await ctx.send('Глобальное потепление – это явление повышения средней температуры Земли из-за увеличения выбросов парниковых газов, таких как углекислый газ и метан.')

@bot.command()
async def carbon_footprint(ctx):
    await ctx.send('Калькулятор углеродного следа поможет вам оценить количество выбросов парниковых газов, связанных с вашим повседневным образом жизни.')

@bot.command()
async def energy_efficiency(ctx):
    await ctx.send('Энергосберегающие меры, такие как установка солнечных батарей и энергосберегающих устройств, помогают снизить потребление энергии и уменьшить выбросы парниковых газов.')

@bot.command()
async def eco_tips(ctx):
    embed = Embed(title='Экологичные советы', description='Несколько простых способов сделать вашу жизнь более экологичной:', color=Color.green())
    embed.add_field(name='1. Используйте велосипед или общественный транспорт', value='Это помогает снизить выбросы CO2 от автомобилей.')
    embed.add_field(name='2. Сортируйте мусор', value='Переработка важна для уменьшения загрязнения окружающей среды.')
    embed.add_field(name='3. Сократите потребление пластика', value='Используйте многоразовую посуду и сумки.')
    await ctx.send(embed=embed)

@bot.command()
async def resources(ctx):
    message = 'Ниже приведены полезные ресурсы для борьбы с глобальным потеплением:\n'
    message += '1. [Программа United Nations Climate Change](https://unfccc.int/ru) - Официальный сайт климатической программы ООН\n'
    message += '2. [World Wildlife Fund](https://www.worldwildlife.org) - Мировой фонд дикой природы\n'
    await ctx.send(message)

bot.run(TOKEN)
