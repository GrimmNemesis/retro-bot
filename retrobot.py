import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = ",")
lastmessage = None
lastmessageuser = None

@client.event
async def on_ready():
    print("Bot is alive my dude")

@client.event
async def on_message(message):
    userID = message.author.id
    channelID = message.channel.name
    homosex = message.content
    global lastmessage
    global lastmessageuser

    if message.content.upper().startswith(",GRIMMALIVE"):
        await client.send_message(message.channel, "<@%s> Yes, Grimm is still alive. **Smh**" % (userID))
    if message.content.upper().startswith(',SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if not (lastmessage == message.content and lastmessageuser == userID):
        if message.content.upper().startswith(',ADMINHELP'):
            await client.send_message(client.get_channel('342772018980061184'), "<@%s> needs admin assistance in %s"
                                      % (userID, channelID))
    lastmessage = homosex
    lastmessageuser = userID
    if message.content.upper().startswith(',QUOTES'):
        quotes = ["```'You can't call a 13-year-old a faggot! THAT'S RAPE' -Aaron 2018```",
                  "```'Why do I even bother with you?' -My dad upon walking into my room as I was whipping out my dick```",
                  "```‘Chiristward’ -Grimm```", "```'Grimm, you can glaze me any day of the week.' - James```", "```'Does anyone still use the the word skux?' - Speedy being old as fuq```", "```'Looks like leo's tryna be clever.'```",
                  ]
        await client.send_message(message.channel, random.choice(quotes))




client.run("Mzg4NDA2MDU2NjcxMjQ4Mzg0.DTkNpg.9eRFY6O3bFg2RyYWMqGvGZ2oSfg")
