
from Luna.events import register
from Luna import tbot, OWNER_ID
from time import sleep
client = tbot
chat = -1001309757591
@register(pattern="^/sleep( [0-9]+)?$")
async def sleepybot(time):
    if time.fwd_from:
        return
    if time.sender_id == OWNER_ID:
        pass
    else:
        return
    message = time.text
    if not message[0].isalpha() and message[0] not in ("/", "#", "@", "!"):
        if " " not in time.pattern_match.group(1):
            await time.reply("Syntax: `/sleep [seconds]`")
        else:
            counter = int(time.pattern_match.group(1))
            await time.reply("`I am sulking and snoozing....`")
            sleep(2)
            await time.client.send_message(
                    chat,
                    "Bot in sleep for " + str(counter) + " seconds",
                )
            sleep(counter)
