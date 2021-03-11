import os
from Luna.events import register
from Luna import tbot, OWNER_ID, CMD_HELP
from time import sleep
client = tbot
chat = -1001309757591
@register(pattern="^/sleep ?(.*)")
async def sleepybot(time):
    if time.fwd_from:
        return
    if time.sender_id == OWNER_ID:
        pass
    else:
        return
    message = time.pattern_match.group(1)
    if message:
       counter = int(time.pattern_match.group(1))
       await time.reply(f"I am sulking and snoozing....for {counter}'secs")
       sleep(counter)
    else:
       await time.reply(f"I am sulking and snoozing....for 10'secs")
       sleep(10)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - @AniegrpBot yt <query>: Inline YouTube Search.

**Note:** Optional, Add ; after Query to Specify No. Of Results.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
