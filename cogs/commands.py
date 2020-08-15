import discord
import random
from datetime import datetime
from discord.ext import commands
from discord.utils import get
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import re
import os
import textwrap
import re
import requests

def cert_gen(params):

    wrapper = textwrap.TextWrapper(width=30)
    word_list = wrapper.wrap(text=params[1])
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    # Dictionary format: {iteration: [base_x, base_y, font_face, font_size, string, paste_origin_x, paste_origin_y]}
    my_dict = {
        1: [447, 30, "assets/Verdana.ttf", 16, "This is to certify", 220, 120],
        2: [447, 56, "assets/Verdana.ttf", 30, params[2], 220, 165],
        3: [447, 30, "assets/Verdana.ttf", 16, "for attending", 220, 215],
        4: [447, 63, "assets/Verdana_Bold.ttf", 22, caption_new, 220, 250],
        5: [447, 34, "assets/Verdana.ttf", 16, "held online on {}".format(params[0]), 220, 325],
        6: [447, 28, "assets/Verdana.ttf", 16, "at the Tambayan 404 Discord Server", 220, 350],
        7: [447, 30, "assets/Verdana.ttf", 9, "This certificate was issued electronically. No signature required.", 220, 450]
    }

    # Create an image object
    img = Image.open("images/WC_blank.png")

    for x in my_dict:

        # Creating the "canvas" where the text will be entered
        # 220 118 667 148
        container = Image.new(
            'RGBA', (my_dict[x][0], my_dict[x][1]), (253, 253, 253))
        font = ImageFont.truetype(my_dict[x][2], my_dict[x][3])
        string = my_dict[x][4]
        # Get font size and make some computations to make the text centered horizontally and vertically in the specified canvass size
        w, h = font.getsize(string)
        pointw = int((448 - w)/2)
        pointh = int((30 - h)/2)

        # Start "drawing" on the canvas
        draw = ImageDraw.Draw(container)

        if x == 4:
            w, h = font.getsize(word_list[0])
            pointw = int((448 - w)/2)
            pointh = int((30 - h)/2)

        # The thing to draw, in this case, the text
        draw.text((pointw, pointh), string, font=font,
                  fill=(64, 64, 64), align='center')

        # Paste the canvas on top of our original image
        img.paste(container, (my_dict[x][5], my_dict[x][6]))

    # Create the output file
    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return(output_file)

def cynthiafy(avatar_url):

    avatar_url = str(avatar_url)
    avatar_url = avatar_url.replace(".webp?size=1024", ".png")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(str(avatar_url), 'images/user_avatar.png')
    img = Image.open("images/user_avatar.png")

    # dp1_image_bg = Image.new('RGBA', (146, 169), "white")

    dp1 = Image.open("images/travelingcynth.png")
    # img.paste(dp1_image_bg, (439, 41))
    img.paste(dp1, (88, 0), dp1)

    img.save("output.png", "PNG")
    output_file = "output.png"

    return (output_file)

def jsonParse(url):
    r = requests.get(url)
    response = r.json()
    print(response)
    return response

class commandsCog(commands.Cog, name="Commands"):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('bot is ready')

    @commands.command(hidden="true")
    async def logout(self, ctx):
        await self.client.logout()

    @commands.command(brief="8 Ball simulator, ask me a question!", description=
        """
        Simulates an 8-ball response
        """)
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don\'t count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        await ctx.send(f'**Question**: {question}\n🎱 Shaking...\n**Answer**: {random.choice(responses)}')

    @commands.command(brief="Generates a certificate", description=    
        """
        Generates a certificate for participating in Watercooler sessions!
        >certgen (mm/dd/yy), (Name of event), @user(don't forget to tag the user)
        >certgen 08/15/20, This is a test certificate, @LordKarlito
        """)
    async def certgen(self, ctx, *, args):
        # Cert generator
        params = args.split(', ')
        print(params)
        if len(params) == 3:
            try:

                params[2] = str(ctx.message.mentions[0].name).strip()
                date_object = datetime.strptime(params[0], '%m/%d/%y')
                params[0] = "{} {}, {}".format(date_object.strftime(
                        '%B'), date_object.strftime('%d'), date_object.strftime('%Y'))
                print(params[0])
                await ctx.channel.send(file=discord.File(cert_gen(params)))
            except ValueError:
                await ctx.channel.send("<:bugsNO:715101362207326208>")
            except IndexError:
                await ctx.channel.send("di ko gets. Try again")
        else:
            await ctx.channel.send("di ko gets. Try again plz")

    @commands.command(brief="Returns a random cat fact", description="Returns a random cat fact")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def catfact(self, ctx):
        fact = jsonParse('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1')
        await ctx.channel.send(fact['text'])

    @commands.command(brief="Get a random piece of advice", description="Get a random piece of advice\nThis command has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def advice(self, ctx):
        advice = jsonParse('https://api.adviceslip.com/advice')
        await ctx.channel.send(advice['slip']['advice'])

    @commands.command(brief="Get a random image of a dog", description="Get a random image of a dog\nThis command has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def woof(self, ctx):
        image = jsonParse('https://random.dog/woof.json')
        await ctx.channel.send(image['url'])

    @commands.command(brief="Get a random fox", description="Get a random fox\nThis command has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def floof(self, ctx):
        fox = jsonParse('https://randomfox.ca/floof/')
        await ctx.channel.send(fox['image'])

    @commands.command(brief="doge", description="Get a random doge\nThis commands has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def shibo(self, ctx):
        image = jsonParse('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')
        await ctx.channel.send(image[0])

    @commands.command(brief="cat", description="Get a random cat\nThis commands has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def meow(self, ctx):
        image = jsonParse('https://api.thecatapi.com/v1/images/search')
        await ctx.channel.send(image[0]['url'])

    @floof.error
    @woof.error
    @advice.error
    @catfact.error
    @shibo.error
    async def test_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.channel.send('Sorry! This command is on a cooldown. Try again in {:.2f}s'.format(error.retry_after))


    @commands.command(brief="Get a photo-op with CV", description="Get a photo-op with CV!")
    async def cynthiafy(self, ctx):
        await ctx.channel.send(file=discord.File(cynthiafy(ctx.author.avatar_url)))

def setup(client):
    client.add_cog(commandsCog(client))
