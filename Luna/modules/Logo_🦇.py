from Luna import tbot, CMD_HELP
import os
from Luna.events import register


@register(pattern="^/logo ?(.*)")
async def logo(event):
     await event.reply("Soon... working On it.")

