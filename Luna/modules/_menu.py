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
pm_caption = "Hi, my name is Luna!\nI'm a powerful group management bot\nAdd me to your groups as admin\nto manage your groups with my\ncommands\nYou can find my list of available\ncommands with /help"
file1 = "https://telegra.ph/file/61dee0de08de48dcacce8.jpg"
@register(pattern="^/start$")
async def start(event):
   if not event.is_group:
        await tbot.send_message(
            event.chat_id,
            pm_caption,
            file=file1,
            buttons=[
                [
                    Button.url(
                        "Add To Group  👥", "t.me/aniegrpbot?startgroup=true"
                    ),
                    Button.url(
                        "Support Group 🎭", "https://t.me/lunabotsupport"
                    ),
                ],
                [
                    Button.inline("Commands ❓", data="help_menu"),
                    Button.inline("Close Menu 🔒", data="start_again"),
                ],
             ],
        )
   else:
        await event.reply("I am Alive 😌")


@tbot.on(events.CallbackQuery(pattern=r"start_again"))
async def start_again(event):
    if not event.is_group:
        await event.edit(
            "The menu is closed 🔒",
            buttons=[[Button.inline("Reopen Menu 🔑", data="reopen_again")]],
        )
    else:
        await event.reply("I am Alive 😊")


@tbot.on(events.CallbackQuery(pattern=r"reopen_again"))
async def reopen_again(event):
    if not event.is_group:
        await event.edit(
            pm_caption,
            buttons=[
                [
                    Button.url(
                        "Add To Group  👥", "t.me/aniegrpbot?startgroup=true"
                    ),
                    Button.url(
                        "Support Group 🎭", "https://t.me/lunabotsupport"
                    ),
                ],
                [
                    Button.inline("Commands ❓", data="help_menu"),
                    Button.inline("Close Menu 🔒", data="start_again"),
                ],
             ],
        )
   else:
        await event.reply("I am Alive 😌")


