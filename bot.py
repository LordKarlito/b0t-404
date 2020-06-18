import discord
from discord.ext import commands

from discord.utils import get
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

# Function to create a certificate with the user's name
def cert_gen(name):
    # Create an image object
    img = Image.open("images/WC_Cert.png")

    # Creating the "canvas" where the text will be entered
    text_container = Image.new('RGBA', (448, 90), (253,253,253))

    font = ImageFont.truetype("assets/BebasKai.ttf", 40)

    # Get font size and make some computations to make the text centered horizontally and vertically in the specified canvass size
    w,h=font.getsize(str(name))
    pointw = int((448 - w)/2)
    pointh = int((95 - h)/2)

    # Start "drawing" on the canvas
    text_draw = ImageDraw.Draw(text_container)

    # The thing to draw, in this case, the text
    text_draw.text((pointw, pointh), name, font = font, fill="black")

    # Paste the canvas on top of our original image
    img.paste(text_container, (225,190))

    # Create the output file
    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return(output_file)    

# Iniialize the client
client = discord.Client()

# Function that's triggered when a message is sent.
@client.event
async def on_message(message):

    if message.author == client.user:
        return

    # Specify the command to trigger the function to create the certificate
    if message.content.startswith("!cert"):
        # Send the result of the funtion as a file
        await message.channel.send(file=discord.File(cert_gen(message.author.name)))

    if message.content.startswith("hi <@!721028903807877180>"):
        
        await message.channel.send("👋")

    if message.content == "musta? <@!721028903807877180>":
        response = "saks lang haha"
        await message.channel.send(response)

    if "magkano?" in message.content.lower() or "hm?" in message.content.lower():
        await message.add_reaction("<:budol:715151627652300821>")


client.run("NzIxMDI4OTAzODA3ODc3MTgw.XuuoxQ.UeDNTGo8S_Ce-p6FV6Xxy8mB3Hg")
