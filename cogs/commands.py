import discord
import random
from datetime import datetime
from datetime import date
from discord.ext import commands
from discord.utils import get
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import re
import os
import textwrap
import re
import requests
import pytz
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

bot = discord.Client()

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

    dp1 = Image.open("images/travelingcynth.png")
    
    img = img.resize((256,256))
    # img.paste(dp1_image_bg, (439, 41))
    width, height = dp1.size
    dp1 = dp1.resize((width*2, height*2))
    img.paste(dp1, (176, 0), dp1)

    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return (output_file)

def samify(avatar_url):

    avatar_url = str(avatar_url)
    avatar_url = avatar_url.replace(".webp?size=1024", ".png")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(str(avatar_url), 'images/user_avatar.png')
    img = Image.open("images/user_avatar.png")

    img = img.resize((256,256))

    dp1 = Image.open("images/sam_transparent.png")
    # img.paste(dp1_image_bg, (439, 41))
    dp1 = dp1.resize((147,121))
    img.paste(dp1, (0, 135), dp1)

    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return (output_file)

def characterPain(avatar_url):

    avatar_url = str(avatar_url)
    avatar_url = avatar_url.replace(".webp?size=1024", ".png")
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

    urllib.request.urlretrieve(str(avatar_url), 'images/user_avatar.png')
    img = Image.open("images/painBase.png").convert("RGBA")
    
    
    dp1 = Image.open("images/user_avatar.png").convert("RGBA")
    dp1 = dp1.resize((352,398), Image.ANTIALIAS)
    img.paste(dp1, (10, 102), dp1)

    dp2 = Image.open("images/painCorners.png").convert("RGBA")
    img.paste(dp2, (0,0), dp2)

    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return (output_file)

client_id = os.getenv('SPOTIFY_CLIENT_ID', 'default-token')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET', 'default-token')

def songsearch(query):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                               client_secret=client_secret))

    resultList = []

    results = sp.search(q=query, limit=5)
    for idx, track in enumerate(results['tracks']['items']):
        resultList.append({
            "title": track['name'],
            "artist": track['artists'][0]['name'],
            "external_url": track['external_urls']['spotify'],
            "type": track['type']
        })
    return resultList

def tweeterte(tweet):

    wrapper = textwrap.TextWrapper(width=50)
    word_list = wrapper.wrap(text=tweet)
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    img = Image.open("images/tweeterte.png")
    container = Image.new('RGBA', (550, 99), (21,32,43))
    font = ImageFont.truetype("assets/segoeui.ttf", 24)
    draw = ImageDraw.Draw(container)

    draw.text((0, 0), caption_new, font=font,
                  fill=(252, 252, 252), align='left')

    img.paste(container, (12,72))

    container2 = Image.new('RGBA', (550,18),(21,32,43))

    font = ImageFont.truetype("assets/SEGOEUI.ttf", 14)
    draw = ImageDraw.Draw(container2)
    # date_object = datetime.strptime(str(date.today()), '%Y-%m-%d')
    now = datetime.now()
    timezone = pytz.timezone('Asia/Manila')
    timenowstr = str(timezone.localize(now))[:-5]
    
    time_aware = datetime.strptime(timenowstr, '%Y-%m-%d %H:%M:%S.%f+')
    print('============================================================================================================')
    print(time_aware)

    today = "{} {}, {}".format(time_aware.strftime('%b'), time_aware.strftime('%d'), time_aware.strftime('%Y'))
    print(today)
    current_time = '{}:{} {}'.format(time_aware.strftime('%H'), time_aware.strftime('%M'), now.strftime('%p'))
    print(current_time)

    draw.text((0,0), '{} · {} · '.format(current_time, today), font = font, fill=(136,153,166), align='left')
    draw.text((168,0), 'Twitter for Android', font = font, fill=(27,149,224), align='left')

    img.paste(container2, (11,176))

    img.save("images/output.png",'PNG')
    output_file = 'images/output.png'

    return(output_file)

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
        >certgen (mm/dd/yy), (Name of event)
        >certgen 08/15/20, This is a test certificate
        """)
    async def certgen(self, ctx, *, args):
        # Cert generator
        params = args.split(', ')

        params.append(ctx.author.display_name)
        if len(params) == 3:
            try:

                params[2] = str(ctx.author.display_name).strip()
                date_object = datetime.strptime(params[0], '%m/%d/%y')
                params[0] = "{} {}, {}".format(date_object.strftime(
                        '%B'), date_object.strftime('%d'), date_object.strftime('%Y'))
                await ctx.channel.send(file=discord.File(cert_gen(params)))
            except ValueError:
                await ctx.channel.send("<:bugsNO:715101362207326208>")
            except IndexError:
                await ctx.channel.send("di ko gets. Try again")
        else:
            await ctx.channel.send("di ko gets. Try again plz")

    @commands.command(brief="Returns a random taco recipe", description="Returns a random taco recipe")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def taco(self, ctx):
        recipe = jsonParse('http://taco-randomizer.herokuapp.com/random/?full-taco=true')
        
        await ctx.channel.send("```{}```".format(recipe['base_layer']['recipe']))

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

    @commands.command(brief="Random cat pic", description="Get a random cat\nThis commands has a 5 second cooldown.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def meow(self, ctx):
        image = jsonParse('https://api.thecatapi.com/v1/images/search')
        await ctx.channel.send(image[0]['url'])

    @commands.command(brief="Latest Covid-19 Stats (Philippines only)", description="Get the latest COVID-19 Stats for the Philippines.")
    @commands.cooldown(1, 10.0, commands.BucketType.member)
    async def covidlatest(self, ctx):
        stats = jsonParse('https://api.apify.com/v2/key-value-stores/lFItbkoNDXKeSWBBA/records/LATEST?disableRedirect=true')
        await ctx.channel.send('**Total Cases:** {}\n**Total ACTIVE Cases:** {}\n**Recoveries:** {}\n**Deaths:** {}'.format(stats['infected'], stats['activeCases'], stats['recovered'], stats['deceased']))

    @commands.command(brief="Search for a spotify song to preview", description="Returns a list of songs based on a search query. Just react with the emoji that your song is assigned to. User is given 15 seconds to make a decision.")
    @commands.cooldown(1, 5.0, commands.BucketType.member)
    async def songsearch(self, ctx, *, query):
        spotifySearchResults = songsearch(query)

        msg = """
Alright {}, please select the song you want previewed. \n
1️⃣ - {} by {}
2️⃣ - {} by {}
3️⃣ - {} by {}
4️⃣ - {} by {}
5️⃣ - {} by {}
            """.format(ctx.author.display_name, 
                        spotifySearchResults[0]['title'], spotifySearchResults[0]['artist'], 
                        spotifySearchResults[1]['title'], spotifySearchResults[1]['artist'],
                        spotifySearchResults[2]['title'], spotifySearchResults[2]['artist'],
                        spotifySearchResults[3]['title'], spotifySearchResults[3]['artist'],
                        spotifySearchResults[4]['title'], spotifySearchResults[4]['artist'])

        embed = discord.Embed(title='')
        embed.add_field(name='Search Results', value = msg, inline=False)
            
        message = await ctx.channel.send(embed=embed)

        emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

        for emoji in emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            print("""reaction.message = {}
message = {}
reaction_emoji = {}
emojis = {}
user = {}""".format(reaction.message, message, reaction.emoji, emojis, user))
            return ((reaction.message.id == message.id) and (reaction.emoji in emojis) and (user == ctx.author))

        try:
            reaction, user =  await self.client.wait_for('reaction_add', timeout=15.0, check=check)
        except ascyncio.TimeoutError:
            await self.client.delete_message(message)
        else:
            
            if reaction.emoji == "1️⃣":
                await message.delete()
                await ctx.channel.send("{}".format(spotifySearchResults[0]['external_url']))
            elif reaction.emoji == "2️⃣":
                await message.delete()
                await ctx.channel.send("{}".format(spotifySearchResults[1]['external_url']))
            elif reaction.emoji == "3️⃣":
                await message.delete()
                await ctx.channel.send("{}".format(spotifySearchResults[2]['external_url']))
            elif reaction.emoji == "4️⃣":
                await message.delete()
                await ctx.channel.send("{}".format(spotifySearchResults[3]['external_url']))
            elif reaction.emoji == "5️⃣":
                await message.delete()
                await ctx.channel.send("{}".format(spotifySearchResults[4]['external_url']))
   
    

    @covidlatest.error
    @floof.error
    @woof.error
    @advice.error
    @catfact.error
    @shibo.error
    @songsearch.error

    async def test_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.message.channel.send('Sorry! This command is on a cooldown. Try again in {:.2f}s'.format(error.retry_after))

    @commands.command(brief="Get a photo-op with CV", description="Get a photo-op with CV!")
    async def cynthiafy(self, ctx):
        await ctx.channel.send(file=discord.File(cynthiafy(ctx.author.avatar_url)))

    @commands.command(brief="Add a squatting tanod to your picture", description="Add a squatting tanod to your avatar")
    async def samify(self, ctx):
        await ctx.channel.send(file=discord.File(samify(ctx.author.avatar_url))) 

    @commands.command(brief="Use this if you went through more pain than her (doesnt work with gif avatars :c)", description="Use this if you went through more pain than her (doesnt work with gif avatars :c)")
    async def pain(self, ctx):
        await ctx.channel.send(file=discord.File(characterPain(ctx.author.avatar_url)))

    @commands.command(brief="Make a fake tweet", description="Make a fake tweet from the supreme leader's account", hidden = 'true')
    async def tweeterte(self, ctx, *, tweet):
        try:
            await ctx.channel.send(file=discord.File(tweeterte(tweet)))
        except OSError:
            await ctx.channel.send("Uh-oh, this command seems to be facing some technical difficulties. Sorry for the inconveniece :(")

    @commands.command(brief="Get link to steamdb's sales table", description="Get link to steamdb's sales table", hidden = 'false')
    async def steamsales(self, ctx):
        await ctx.channel.send('https://steamdb.info/sales/')

def setup(client):
    client.add_cog(commandsCog(client))
