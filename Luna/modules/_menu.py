from Luna import CMD_LIST
from Luna import tbot
import io
import re
from math import ceil

from telethon import custom, events, Button

from Luna.events import register
from Luna import CMD_HELP

from telethon import types
from telethon.tl import functions

@register(pattern="^/start$")
async def start(event):
   if not event.is_group:
             return
   else:
     await event.reply("Heya! Luna Here, How Can I Help Ya!")
    
