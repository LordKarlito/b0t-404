import discord
import random
from discord.ext import commands


class Loaders(commands.Cog, name = "Loaders"):

    def __init__(self, client):
        self.client = client

    @commands.command(hidden='true')
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')


    @commands.command(hidden='true')
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')

    @commands.command(hidden='true')
    async def reload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')

def setup(client):
    client.add_cog(Loaders(client))


