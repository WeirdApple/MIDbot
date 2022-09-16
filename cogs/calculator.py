import discord
import time
from discord.ext import tasks, bridge, commands
import random
from random import choice
import asyncio
import os
import io
import math

class Calculator(discord.Cog):
	
	def __init__(self, client): #i use "client"
		self.client = client

	#calculator
	@commands.slash_command(description = 'M A T H')
	async def calculate(self, ctx,x,*,y):
			
		class Add(discord.ui.View): #Add
			#Add
			@discord.ui.button(label = "+", row = 0, style = discord.ButtonStyle.primary)
			async def button_callback(self, button, interaction):
				try:
					answer = int(x) + int(y)
					await interaction.response.send_message(f"{x}+{y} = {answer}")
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self) #note to self, do ctx.edit. it works better
				except:
					await ctx.respond("Put actual integers")
					button.disabled = True
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self)
					
			#Subtract
			@discord.ui.button(label = "-", row = 0, style = discord.ButtonStyle.primary)
			async def second_button_callback(self, button, interaction):
				try:
					answer = int(x) - int(y)
					await interaction.response.send_message(f"{x}-{y} = {answer}")
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self) #note to self, do ctx.edit. it works better
				except:
					await ctx.respond("Put actual integers")
					button.disabled = True
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self)
			#Multiply
			@discord.ui.button(label = "*", style = discord.ButtonStyle.primary)
			async def third_button_callback(self, button, interaction):
				try:
					answer = int(x) * int(y)
					await interaction.response.send_message(f"{x}*{y} = {answer}")
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self) #note to self, do ctx.edit. it works better
				except:
					await ctx.respond("Put actual integers")
					button.disabled = True
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self)
			#Divide
			@discord.ui.button(label = "/", style = discord.ButtonStyle.primary)
			async def fourth_button_callback(self, button, interaction):
				try:
					answer = int(x) / int(y)
					await interaction.response.send_message(f"{x}/{y} = {answer}")
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self) #note to self, do ctx.edit. it works better
				except:
					await ctx.respond("Put actual integers")
					button.disabled = True
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self)
				
			#x^y
			@discord.ui.button(label = "x^y", row = 1, style = discord.ButtonStyle.success)
			async def fifth_button_callback(self, button, interaction):
				try:
					answer = pow(int(x), int(y))
					await interaction.response.send_message(f"{x}^{y} = {answer}")
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self) #note to self, do ctx.edit. it works better
				except:
					await ctx.respond("Put actual integers")
					button.disabled = True
					for child in self.children:
						child.disabled = True
					await ctx.edit(view = self)
					
		await ctx.respond("Pick an operation", view = Add())
					
def setup(client): # this is called by Pycord to setup the cog
    client.add_cog(Calculator(client)) # add the cog to the bot