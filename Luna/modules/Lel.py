from Luna import SUDO_USERS as k

@register(pattern="^/s")
async def _(event):
   p = list(k)
   reply = "<b>Known Dragon Disasters 🔥:</b>\n"
   for m in p:
        user_id = int(m)
        try:
            reply += "Lel"
        except Exception:
            pass
  await event.reply(reply)
  await event.reply(p)
