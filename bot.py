#Test bot by Minä!

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import chalk


bot = commands.Bot(command_prefix='.')

@bot.event
async def on_ready():
    print("En ole valmis!")

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!!")

@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Käyttäjänimi on: {}".format(user.name))
    await bot.say("Käyttäjän id on: {}".format(user.id))
    await bot.say("Käyttäjän tila on: {}".format(user.status))

@bot.command(pass_context=True)
async def embed(ctx):
    embed = discord.Embed(Title="Testi", description="Minun nimeni on Lauri", color=0x00ff00)
    embed.set_footer(text="Tämä on jalustin")
    embed.set_author(name="Lauri Lalli")
    embed.add_field(name="Tämä on kenttä", value="ei se olekkaan", inline=True)
    await bot.say(embed=embed)

bot.run("NDg0NDY4MDM4Nzg0MTIyODgx.Dmiclg.3yg9KwZJnwAA_G9euL-csmTDSe8")

