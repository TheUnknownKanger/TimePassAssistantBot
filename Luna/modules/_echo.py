from Luna import tbot, OWNER_ID as owner, SUDO_USERS as su, DEV_USERS as dev
from Luna.events import register
@register(pattern="^/echo ?(.*)")
async def legend(are):
  if event.sender_id == owner:
             pass
  elif event.sender_id in su:
             pass
  elif event.sender_id in dev:
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
