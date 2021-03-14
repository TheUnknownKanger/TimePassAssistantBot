from Luna import CMD_HELP, OWNER_ID
from Luna.events import register
import os

@register(pattern="^/teg")
async def sleepybot(time):
    if time.fwd_from:
        return
    if time.sender_id == OWNER_ID:
        pass
    else:
        return
    await time.reply("AntiSpam Py In App 2")

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /addnsfw: Adds The Group to nsfw Watch List
 - /rmnsfw: Removes The Group From nsfw Watch List

**Use:** Nsfw Contents in group gets deleted and logged.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})


