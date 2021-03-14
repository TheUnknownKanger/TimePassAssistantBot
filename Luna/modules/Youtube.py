import os
import sys
from os import execl
from Luna.events import register
from Luna import tbot, OWNER_ID, CMD_HELP
from time import sleep
import speedtest
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

def convert(speed):
    return round(int(speed)/1048576, 2)

@register(pattern="^/restart$")
async def _(event):
    chat = -1001309757591
    if event.sender_id == OWNER_ID:
        pass
    else:
       return
    if event.fwd_from:
        return
    await event.client.send_message(chat, "#RESTART \n" "Bot Restarted")
    await event.reply("Restarted. I'll Be back in a Minute.!")
    await tbot.disconnect()
    execl(sys.executable, sys.executable, *sys.argv)


@register(pattern="^/speedtest ?(.*)")
async def seedtest(event):
    if event.sender_id == OWNER_ID:
        pass
    elif event.sender_id in SUDO_USERS:
        pass
    elif event.sender_id in DEV_USERS:
        pass
    else:
        return
    message = event.pattern_match.group(1)
    speed = speedtest.Speedtest()
    speed.get_best_server()
    speed.download()
    speed.upload()
    result = speed.results.dict()
    speedtest_image = speed.results.share()
    if "pic" in message:
             await client.send_file(event.chat, speedtest_image)
    else:
      replymsg = "**Speed Test**"
      replymsg += f"\nDownload: {convert(result['download'])}Mb/s\nUpload: {convert(result['upload'])}Mb/s\nPing: {result['ping']}"
      await client.send_message(event.chat, replymsg)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - @AniegrpBot yt <query>: Inline YouTube Search.

**Note:** Optional, Add ; after Query to Specify No. Of Results.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
