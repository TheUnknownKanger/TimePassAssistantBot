from Luna import tbot
from Luna.events import register
import secureme
@register(pattern="^/encrypt (.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          cmd = await event.get_reply_message()
    else:
          cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)

@register(pattern="^/decrypt (.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          ok = await event.get_reply_message()
    else:
          ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)
