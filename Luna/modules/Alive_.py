from Luna import tbot, OWNER_ID, StartTime

from Luna.events import register

@register(pattern="^/alive")
async def _(event):
    k = await tbot.get_entity(OWNER_ID)
    fname = k.first_name
    lname = k.last_name
    reply = "**I'm Alive Master**\n\n"
    reply += f"**Awake Since:** {StartTime}"
    reply += f"\n\n**Owner:** {fname}-{lname}\n"
    reply += "**Telethon Ver:** 1.20.0"
    reply += "\n**Logging:** Active"
    await event.reply(reply)
    
