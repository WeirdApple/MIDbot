import discord
import time
from discord.ext import tasks, bridge, commands
import random
from random import choice
import asyncio
import os
import io
import math
import tsg
from tsg import toposymbols

class TopoSymbols(discord.Cog):
	
	def __init__(self, client): #i use "client"
		self.client = client

	@commands.slash_command(description = 'A command to quiz topo symbols for SciOly')
	async def toposymbol(self, ctx):
		embed = discord.Embed(title = "What is this topo symbol?", description = "danke schon")
		embed.set_image(url = random.choice(toposymbols))
		await ctx.send(embed = embed)
		guess = await self.client.wait_for('message', check = lambda message: message.author == ctx.author)
		if str(guess.content) == "foreshore flat":
			await ctx.send("bingo!")
		else:
			await ctx.send("nein")


def setup(client): # this is called by Pycord to setup the cog
    client.add_cog(TopoSymbols(client)) # add the cog to the bot