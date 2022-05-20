import discord
import random
from discord.ext import commands
from discord.ui import View, Select

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.',intents=intents)

#loading...
@bot.event
async def on_ready():
    print('hot dogging')
    await bot.change_presence(activity=discord.Game(name=".help"))

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
    view.add_item(select)
    await ctx.send('which game do you want to do?', view=view)

bot.run('OTc0NjQ5ODUyNzExNTM4NzE4.GBYaPB.01qxusDMWdgS8M61NP-03mFB9zC-7PG7Tx-EbE')