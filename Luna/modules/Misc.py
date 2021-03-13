from Luna import tbot, CMD_HELP
import os
from Luna.events import register
import secureme

@register(pattern="^/encrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          cmd = lel.text
    else:
          cmd = event.pattern_match.group(1)
    Text = cmd
    k = secureme.encrypt(Text)
    await event.reply(k)

@register(pattern="^/decrypt ?(.*)")
async def hmm(event):
    if event.reply_to_msg_id:
          lel = await event.get_reply_message()
          ok = lel.text
    else:
          ok = event.pattern_match.group(1)
    Text = ok
    k = secureme.decrypt(Text)
    await event.reply(k)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /cash : currency converter
Example syntax: `/cash 1 USD INR`
 - /crypto : Crypto Value
 - /read <lang>: Type in reply to a image to extract the text from it
Example syntax: `/crypto inr btc`
 - /wall <topic>: Searches best wallpaper on the given topic and returns them
 - /country: Gather's Info About The Given Country
 - /encrypt: Encrypts The Given Text
 - /decrypt: Decrypts Previously Ecrypted Text

**Note:** Encrypted Using 69 Bit RSA Encryption
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
