import discord
from discord.ext import commands
import re

class eventsCog(commands.Cog):
    def __init__ (self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.client.user:
            return

        if message.content.lower() == "ha" or message.content.lower().startswith("ha?"):
            await message.add_reaction("<🌭>")

        if message.content.startswith("hi <@!721028903807877180>"):
            await message.channel.send("👋")

        if message.content == "musta? <@!721028903807877180>":
            response = "saks lang haha"
            await message.channel.send(response)

        if message.content.lower() == "magkano?" or message.content.lower() == "hm?":
            await message.add_reaction("<:budol:715151627652300821>")

        if message.content == "steam special":
            await message.add_reaction("<:budol:715151627652300821>")

        if re.search(r".*[hH][aA]\?.*", message.content):
            await message.add_reaction("<:hotdog:7b423a7d402beedfecb0bb81f9704953>")

    # When someone joins the server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(714387677155295276)
        directory = "714437490282332210"
        await channel.send("Hi <@{}>! it's dangerous to go alone, take this: <#{}>".format(member.id, directory))

def setup(client):
    client.add_cog(eventsCog(client))
