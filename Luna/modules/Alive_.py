from Luna import tbot, OWNER_ID, StartTime



@register(pattern="^/alive")
async def _(event):
    reply = "**I'm Alive Master**\n\n"
    reply += f"**Awake Since:** {StartTime}"
    await event.reply(reply)
    
