import urllib
import sys
import discord
import json
import requests
import asyncio
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import requests as req

client = discord.Client()

bot = commands.Bot(command_prefix="!", case_insensitive=True)

@bot.command(name="alts")
async def alts(ctx, arg):
	if ctx.guild.id == 834493092077502524 and ctx.channel.id == 834493092517117996: #change Guild & Channel ID to your server's


		response = requests.get(f"https://api.echo.ac/query/player?key=DzA5MD44DjYyMTkyMXc5OTY1NjIwNDY2Nzg1OTMDMDY3MTQwNTk=&player={arg}") #API example
		print(response.status_code)	
		if response.status_code == 200:
			data = response.json()
			embed=discord.Embed(title="Alts finder", url="https://discord.gg/MsUgs6vFzU", description="by jxkeh#0001", color = discord.Colour.random() #random color but you can use one in specific
			embed.set_thumbnail(url="https://weebware.net/images/logo.png?1367f38eed463b08ee64be9b4277bfd9")
			if len(data["result"]["alts"]) == 0: 
				embed.add_field(name="Alts", value="No scans were resolved", inline=True)
			else: 
				embed.add_field(name="Alts", value=', '.join(str(x) for x in data["result"]["alts"]), inline=True) 
			message = await ctx.send(embed=embed)

			await message.delete(delay=15) #deleting the msg after 15secs (remove if you dislike)

			await ctx.message.delete(delay=15) 

			#print(data)
			#await ctx.send(data["result"]["alts"])

		else:
			ctx.send("API returned a {response.status_code} status.")

bot.run("token")
