from Luna import SUDO_USERS as k
from Luna.events import register
@register(pattern="^/frwd")
async def _(event):
   p = list(k)
   reply = "<b>Known Dragon Disasters 🔥:</b>\n"
   for m in p:
        user_id = int(m)
        try:
            entity = await tbot.get_input_entity(m)
            try:
               r_sender_id = entity.user_id
            except Exception:
               await event.reply("Couldn't fetch that user.")
              return
            reply += f"{r_sender_id}"
        except Exception:
            pass
   await event.reply(reply)
   await event.reply(p)
