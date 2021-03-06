from Luna import tbot, OWNER_ID, StartTime

from Luna.events import register

@register(pattern="^/alive")
async def _(event):
    k = await tbot.get_entity(OWNER_ID)
    fname = k.first_name
    reply = "**I'm Up And Alive**\n\n"
    reply += f"**Awake Since:** {StartTime}"
    reply += f"\n\n**Owner: {fname}**\n"
    reply += "**Telethon Ver: 1.20.0**\n"
    reply += "**Bot_Ver: 1.8**"
    await event.reply(reply)
    
