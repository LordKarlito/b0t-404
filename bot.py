import discord
from discord.ext import commands
from discord.utils import get
import os

client = commands.Bot(command_prefix='>')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

token = os.getenv('token', 'default-token')
# client.run('NzIxMDI4OTAzODA3ODc3MTgw.XuOkfg.4FAkOfeBonB-G0e0DFxokt61T24')
client.run(token)
