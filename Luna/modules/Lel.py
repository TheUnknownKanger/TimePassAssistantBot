from Luna import SUDO_USERS as k
from Luna import DEV_USERS as l
from Luna.events import register
@register(pattern="^/sudolist")
async def _(event):
   p = list(k)
   reply = "**Sudo Users 🔥:**\n"
   for m in p:
        user_id = int(m)
        try:
            reply += "• [{}](tg://user?id={})\n".format(m, m)
        except Exception:
            pass
   await event.client.send_message(
                event.chat_id, reply)
