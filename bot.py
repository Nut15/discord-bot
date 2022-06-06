import discord
import random
import os
from discord.ext import commands
from discord.ui import Select, View

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='-',intents=intents)

#making sure the bot is online
@client.event
async def on_ready():
    print(f"{client.user} is online. use -")
    await client.change_presence(activity=discord.Game(name="-help to get help"))

#error box
@client.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(error)
        await ctx.message.delete()

#command 'kill'
@client.command(name='kill',brief='kill someone.',description='kill anyone you want. However the chance for them to die is 3%. Has cooldown for half a day (12 hrs). Kills are anonymous')
@commands.cooldown(1, 43200, commands.BucketType.user)
async def kill(ctx, member:discord.Member):
    chance = random.randint(0,32)
    if chance == 2:
        await ctx.send(f"@everyone {member.mention} killed.")
        await ctx.message.delete()
    else:
        await ctx.send(f"{member.mention} did not die")
        await ctx.message.delete()

#test command: 'test'
@client.command()
async def test(ctx):
    await ctx.send("test")

#command rock (rock scissors paper)
@client.command(name='rock', brief='play rock paper scissors.', description = 'play rock paper scissors as a leisure activity! You will battle against the bot for some fun :)')
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
        await ctx.send(f'human chose: {hum}')
        await ctx.send(f'bot chose: {b}')

        RULES = {
        ('scissors', 'paper'): 'scissors',
        ('scissors', 'rock'): 'rock',
        ('paper', 'rock'): 'paper',
        }
        vic = RULES.get((hum,b), RULES.get((b,hum), "it's a tie :D"))
        if hum == vic:
            await ctx.send('human won :)')
        elif b == vic:
            await ctx.send('bot won!')
        else:
            await ctx.send(vic)

    select.callback = my_callback
    view = View()
    view.add_item(select)
    await ctx.send(view=view, delete_after=4)

client.run("OTY4MzgzODQ5ODA3NjIyMTQ0.YmeDvQ.qrKSexMlEqK9POFF5GcdSi0ZJRc")