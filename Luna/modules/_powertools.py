
from Luna.events import register
from Luna import tbot, OWNER_ID
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
       await event.reply("I'm Alive")
    else:
       await time.reply(f"I am sulking and snoozing....for 10'secs")
       sleep(10)
