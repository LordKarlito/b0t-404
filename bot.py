import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os

# Function to create a certificate with the user's name
def cert_gen(name):
    img = Image.open("images/WC_Cert.png")

    text_container = Image.new('RGBA', (448, 90), (253,253,253))
    font = ImageFont.truetype("assets/BebasKai.ttf", 40)
    w,h=font.getsize(str(name))

    pointw = int((448 - w)/2)
    pointh = int((95 - h)/2)
    text_draw = ImageDraw.Draw(text_container)
    text_draw.text((pointw, pointh), name, font = font, fill="black")
    img.paste(text_container, (225,190))

    img.save("images/output.png", "PNG")
    output_file = "images/output.png"

    return(output_file)    

# Iniialize the client
client = discord.Client()

# Function that's triggered when a message is sent.
@client.event
async def on_message(message):
    # Specify the command to trigger the function to create the certificate
    if message.content.startswith("!cert"):
        # Send the result of the funtion as a file
        await message.channel.send(file=discord.File(cert_gen(message.author.name)))

    if message.content.startswith("<:kek:714402314743447594>"):
        await message.channel.send("<:kek:714402314743447594>")

client.run("NzIxMDI4OTAzODA3ODc3MTgw.XuTmvA.AxorsHjOS9rUlkambh3cp0Wr2Mc")
