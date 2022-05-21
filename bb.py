from email.policy import default
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


#command 'rock scissors paper' in testing bot
@bot.command(name='rock', brief='play rock paper scissors as a leisure activity!')
async def rock(ctx):
    select = Select(
        placeholder = 'choose an action!',
        options = [
            discord.SelectOption(
                label='paper',
                emoji = '🧻'
            ),
            discord.SelectOption(
                label='scissors',
                emoji = '✂️'
            ),
            discord.SelectOption(
                label='rock',
                emoji = '🪨'
            ),
        ],
    )

    async def my_callback(interaction):
        hum = select.values[0]
        b = random.choice(['rock','paper','scissors'])
        await ctx.send(f'you chose: {hum}')
        await ctx.send(f'I chose: {b}')

        RULES = {
        ('scissors', 'paper'): 'scissors',
        ('scissors', 'rock'): 'rock',
        ('paper', 'rock'): 'paper',
        }
        vic = RULES.get((hum,b), RULES.get((b,hum), "it's a tie :D"))
        if hum == vic:
            await ctx.send('you won :)')
        elif b == vic:
            await ctx.send('I won!')
        else:
            await ctx.send(vic)

    select.callback = my_callback
    view = View()
    view.add_item(select)
    await ctx.send(view=view, delete_after=4)

bot.run('OTc0NjQ5ODUyNzExNTM4NzE4.GBYaPB.01qxusDMWdgS8M61NP-03mFB9zC-7PG7Tx-EbE')