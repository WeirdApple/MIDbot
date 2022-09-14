import discord
import time
from discord.ext import tasks, bridge
import random
from random import choice
import asyncio
import os
import io

class Calculator(discord.Cog):
	def __