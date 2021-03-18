from Luna import CMD_HELP, OWNER_ID
from Luna.events import register
import os

k = 'News Py Files In Another Repo'
@register(pattern="^/tgoogodasicious ?(.*)")
async def sleepybot(time):
    if time.fwd_from:
        return
    if time.sender_id == OWNER_ID:
        pass
    else:
        return
    await time.reply("Google Py In App 2")

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /google: Performs A Google Search With given Query
 - /img: Search Google for images and returns them\nFor greater no. of results specify lim, For eg: `/img hello lim=10`
 - /reverse: Does a reverse image search of the media which it was replied to.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
