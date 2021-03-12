import os
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
