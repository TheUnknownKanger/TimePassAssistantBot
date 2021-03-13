from Luna import CMD_HELP
import os
from Luna import tbot
from random import randint

import requests as r

from Luna import WALL_API

from Luna.events import register
from telethon import types
from telethon.tl import functions


@register(pattern="^/wall (.*)")
async def wallpaper(event):
    
    chat_id = event.chat_id
    args = event.pattern_match.group(1)
    if not args:
        await event.reply("Please enter some argument!")
        return
    caption = args
    term = args.replace(" ", "%20")
    json_rep = r.get(
        f"https://wall.alphacoders.com/api2.0/get.php?auth={WALL_API}&method=search&term={term}"
    ).json()
    if not json_rep.get("success"):
        await event.reply("An error occurred! Report this at @MissJuliaRobotSupport")
    else:
        wallpapers = json_rep.get("wallpapers")
        if not wallpapers:
            await event.reply("No results found! Refine your search.")
            return
        index = randint(0, len(wallpapers) - 1)
        wallpaper = wallpapers[index]
        wallpaper = wallpaper.get("url_image")
        wallpaper = wallpaper.replace("\\", "")
        await tbot.send_file(
            chat_id,
            file=wallpaper,
            caption=args,
            reply_to=event.id,
        )


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /wall <topic>: Searches best wallpaper on the given topic and returns them
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
