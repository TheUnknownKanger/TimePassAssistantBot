from Luna import tbot, OWNER_ID, StartTime

from Luna.events import register

@register(pattern="^/alive")
async def _(event):
    reply = "**I'm Up And Alive**\n\n"
    reply += f"**Awake Since:** {StartTime}"
    reply += "**Telethon Ver: 1.20.0**\n"
    reply += "**Bot_Ver: 1.8**"
    await event.reply(reply)
    
