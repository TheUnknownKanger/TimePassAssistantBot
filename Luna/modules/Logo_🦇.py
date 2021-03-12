from Luna import tbot, CMD_HELP
import os
from Luna.events import register


@register(pattern="^/logo ?(.*)")
async def logo(event):
     await event.reply("Soon... working On it.")

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 **Soon Working on It!.**
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
