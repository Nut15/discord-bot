import discord
import random
import os
from discord.ext import commands

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
@client.command(name='kill',brief='kill someone.',description='kill anyone you want. However the chance for them to die is 1%. Has cooldown for 1 day. Kills are anonymous')
@commands.cooldown(1, 86400, commands.BucketType.user)
async def kill(ctx, member:discord.Member):
    chance = random.randint(0,99)
    if chance == 1:
        await ctx.send(f"@everyone {member.mention} killed.")
        await ctx.message.delete()
    else:
        await ctx.send(f"{member.mention} did not die")
        await ctx.message.delete()

#test command: 'test'
@client.command()
async def test(ctx):
    await ctx.send("test")

#command battle (on its way)

client.run("OTY4MzgzODQ5ODA3NjIyMTQ0.YmeDvQ.qrKSexMlEqK9POFF5GcdSi0ZJRc")