import discord
from discord.ext import commands
from datetime import datetime
from discord.utils import get
import urllib.request
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os
import textwrap

# Function to create a certificate with the user's name


def cert_gen(params):

    wrapper = textwrap.TextWrapper(width=30)
    word_list = wrapper.wrap(text=params[2])
    caption_new = ''
    for ii in word_list[:-1]:
        caption_new = caption_new + ii + '\n'
    caption_new += word_list[-1]

    # Dictionary format: {iteration: [base_x, base_y, font_face, font_size, string, paste_origin_x, paste_origin_y]}
    my_dict = {
        1: [447, 30, "assets/Verdana.ttf", 16, "This is to certify", 220, 118],
        2: [447, 56, "assets/Verdana.ttf", 30, params[3], 220, 158],
        3: [447, 30, "assets/Verdana.ttf", 16, "for attending", 220, 208],
        4: [447, 63, "assets/Verdana_Bold.ttf", 20, caption_new, 220, 252],
        5: [447, 34, "assets/Verdana.ttf", 16, "held online on {}".format(params[1]), 220, 305],
        6: [447, 28, "assets/Verdana.ttf", 16, "at the Tambayan 404 Discord Server", 220, 331],
        7: [447, 30, "assets/Verdana.ttf", 12, "This certificate was issued electronically. No signature required.", 220, 395]
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

        if x==4:
            w, h = font.getsize(word_list[0])
            pointw = int((448 - w)/2)
            pointh = int((30 - h)/2)

        # The thing to draw, in this case, the text
        draw.text((pointw, pointh), string, font=font, fill=(64, 64, 64), align = 'center')

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


# Iniialize the client
client = discord.Client()

# Function that's triggered when a message is sent.


@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower() == "ha" or message.content.lower().startswith("ha?"):
        await message.add_reaction("<🌭>")

    if message.content == "!cynthiafy":
        await message.channel.send(file=discord.File(cynthiafy(message.author.avatar_url)))

    if message.content.startswith("hi <@!721028903807877180>"):

        await message.channel.send("👋")

    if message.content == "musta? <@!721028903807877180>":
        response = "saks lang haha"
        await message.channel.send(response)

    if message.content.lower() == "magkano?" or message.content.lower() == "hm?":
        await message.add_reaction("<:budol:715151627652300821>")

    if message.content == "steam special":
        await message.add_reaction("<:budol:715151627652300821>")

    # Cert help
    if message.content.startswith("!cert help"):
        embed = discord.Embed(
            title="Cert Generator", description="Certificate para mukang official lol", color=0x00ff00)
        embed.add_field(
            name="Command", value="!cert gen", inline=False)
        embed.add_field(
            name="Params", value="date(mm/dd/yy), event_name, username(@username)", inline=False)
        embed.add_field(
            name="Example", value="!cert gen, 06/19/20, Watercooler 01, @Karlito", inline=False)
        await message.channel.send(embed=embed)

    # Cert generator
    if message.content.startswith("!cert gen"):
        params = message.content.split(', ')
        if len(params) == 4:
            try:
                
                params[3] = str(message.mentions[0].name).strip()
                date_object = datetime.strptime(params[1], '%m/%d/%y')

                params[1] = "{} {}, {}".format(date_object.strftime(
                '%B'), date_object.strftime('%d'), date_object.strftime('%Y'))
                await message.channel.send(file=discord.File(cert_gen(params)))
            except ValueError:
                await message.channel.send("<:bugsNO:715101362207326208>")
            except IndexError:
                await message.channel.send("di ko gets. Try '!cert help'")
        else:
            await message.channel.send("di ko gets. Try '!cert help'")

# When someone joins the server
@client.event
async def on_member_join(member):
    channel = client.get_channel(714387677155295276)
    directory = "714437490282332210"

    await channel.send("Hi <@{}>! it's dangerous to go alone, take this: <#{}>".format(member.id, directory))

f = open('token.txt', 'r')
token = f.read()

client.run(token)
