from Luna import SUDO_USERS as k
from Luna.events import register
@register(pattern="^/frwd")
async def _(event):
   p = list(k)
   reply = "**Known Dragon Disasters 🔥:**\n"
   for m in p:
        user_id = int(m)
        try:
            reply += f"• {m}\n"
        except Exception:
            pass
   await event.reply(reply)
