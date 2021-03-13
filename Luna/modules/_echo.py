from Luna import tbot, OWNER_ID, SUDO_USERS, DEV_USERS
from Luna.events import register
@register(pattern="^/echo ?(.*)")
async def echo(event):
  if event.fwd_from:
        return
  if event.sender_id == OWNER_ID:
        pass
  elif event.sender_id in SUDO_USERS:
        pass
  elif event.sender_id in DEV_USERS:
        pass
  else:
        return
  if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          ok = lel.text
  else:
          ok = event.pattern_match.group(1)
  await event.delete()
  await tbot.send_message(event.chat_id, ok)
