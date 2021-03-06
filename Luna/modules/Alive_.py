from Luna import tbot, OWNER_ID, StartTime

from Luna.events import register

@register(pattern="^/alive")
async def _(event):
    k = await tbot.get_entity(OWNER_ID)
    fname = k.first_name
    lname = k.last_name
    reply = "**I'm Alive Master**\n\n"
    reply += f"**Awake Since:** {StartTime}"
    reply += f"**Owner:** {fname}-{lname}"
    await event.reply(reply)
    
