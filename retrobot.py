import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import discordtoken
import Quotes from Quotes

Client = discord.Client()
client = commands.Bot(command_prefix = ",")
lastmessage = None
lastmessageuser = None
admin_prefix = ',ADMINHELP'

quotes = Quotes({"aaron": "You can't call a 13-year-old a faggot! THAT'S' -Aaron 2018",
          "dad": "Why do I even bother with you?' -My dad upon walking into my room ",
          "christ": "‘Chiristward’ -Grimm",
          "glazeit": "'Grimm, you can glaze me any day of the week.' - James",
          "skux": "'Does anyone still use the the word skux?' - Speedy being old as fuq",
          "leo": "Looks like leo's tryna be clever."
          })

@client.event
async def on_ready():
    print("Bot is alive my dude")

@client.event
async def on_message(message):
    global lastmessage
    global lastmessageuser
    global admin_prefix
    global quotes

    userID = message.author.id
    channelID = message.channel.name
    message_string = message.contents

    if message.content.upper().startswith(",GRIMMALIVE"):
        await client.send_message(message.channel, "<@%s> Yes, Grimm is still alive. **Smh**" % (userID))
    if message.content.upper().startswith(',SAY'):
        args = message.content.split(" ")
        await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
    if not (lastmessage == message.content and lastmessageuser == userID):
        if message.content.upper().startswith(admin_prefix):
            await client.send_message(client.get_channel('342772018980061184'), "@here <@%s> needs admin assistance in %s reason: %s"
                                      % (userID, channelID, message_string.upper().replace(admin_prefix, '')))
    lastmessage = message_string
    lastmessageuser = userID

    if message.content.upper().startswith(',QUOTES'):
        await client.send_message(message.channel, quotes.get_random_quote())

client.run(discordtoken.token)
