from Luna import tbot, OWNER_ID, StartTime
from time import time
from Luna.events import register

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time



@register(pattern="^/alive")
async def _(event):
    uptime = get_readable_time((time.time() - StartTime))
    ok = event.chat.title
    reply = "**I'm Up And Alive**\n\n"
    reply += f"**Awake Since: {uptime}**\n"
    reply += "**Telethon Ver: 1.20.0**\n"
    reply += "**Bot_Ver: 1.8**\n"
    reply += f"**Chat: {ok}**"
    await event.reply(reply)
    
