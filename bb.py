import discord
from discord.ui import Select, View
import random
from discord.ext import commands

bot = commands.Bot(command_prefix='.')

#loading...
@bot.event
async def on_ready():
    print('hot dogging')
    await bot.change_presence(activity=discord.Game(name=".help to get help"))

#test command
@bot.command()
async def test(ctx):
    await ctx.send("test")
    await ctx.message.delete()

#command 'battle' in testing bot
@bot.command(name='battle', brief='battle with someone.')
async def battle(ctx, member=discord.Member):
    select = Select(placeholder = 'choose a game',
    options = [
        discord.SelectOption(
            label='paper scissors rock'
        )
    ]
)
    view = View()
    await ctx.send('which game do you want to do?', view=view)

bot.run('OTc0NjQ5ODUyNzExNTM4NzE4.GANtid.92JPjb70WJHBgZ-BoZAJhVjxBATuPAaFWvBeLA')