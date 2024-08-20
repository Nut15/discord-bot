from email.policy import default
from itertools import tee
import discord
import random
from discord.ext import commands
from discord.ui import View, Select, Button

#reading in the token
with open("MrHotDog.txt") as f:
    TOKEN = f.readline()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.',intents=intents)

#loading...
@bot.event
async def on_ready():
    print('hot dogging')
    await bot.change_presence(activity=discord.Game(name=".help"))

#error box
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
        await ctx.message.delete()

#test command
@bot.command()
async def test(ctx):
    tee = 'hello'
    await ctx.send("test")
    await ctx.message.delete()

#testing
@bot.command()
async def abc(ctx):
    print(tee)


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
    await ctx.send(view=view)
    def check(res):
      return ctx.author == res.user
    while True:
      res = await bot.wait_for("button_click",timeout=60, check=check)

#command 'send messages to specific channel'
@bot.command(name='kill',brief='kill someone.',description='kill anyone you want. However the chance for them to die is 3%. Has cooldown for half a day (12 hrs). Kills are anonymous')
@commands.cooldown(1, 1, commands.BucketType.user)
async def kill(ctx, member:discord.Member):
    chance = random.randint(0,32)
    if chance == 2:
        await ctx.send(f"@everyone {member.mention} killed.")
        await ctx.message.delete()
    else:
        await ctx.send(f"{member.mention} did not die")
        await ctx.message.delete()
    channel = bot.get_channel(866922982281838616)
    await channel.send(chance)

#command 'shogun'
@bot.command(name ='shogun')
async def shogun(ctx):
    await ctx.send('Choose your action.')

bot.run(TOKEN)