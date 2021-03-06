from Luna import tbot, OWNER_ID, StartTime
import time
from Luna.events import register

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
    
