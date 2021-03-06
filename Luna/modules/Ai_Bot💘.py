import requests
from Luna import tbot, CMD_HELP, BOT_ID
from Luna.events import register
from telethon import events
url = "https://iamai.p.rapidapi.com/ask"
import os
import Luna.modules.sql.chatbot_sql as sql
from time import time
from telethon import types
from telethon.tl import functions


async def can_change_info(message):
    try:
        result = await tbot(
            functions.channels.GetParticipantRequest(
                channel=message.chat_id,
                user_id=message.sender_id,
            )
        )
        p = result.participant
        return isinstance(p, types.ChannelParticipantCreator) or (isinstance(
            p, types.ChannelParticipantAdmin) and p.admin_rights.change_info)
    except Exception:
        return False




@register(pattern="^/eaichat")
async def _(event):
 if event.is_group:
        if not await can_change_info(message=event):
            return
    else:
        return
  chat = event.chat
  is_chat = sql.is_chat(chat.id)
  if not is_chat:
          sql.set_ses(chat.id)
          await event.reply("AI successfully enabled for this chat!")
          return
  await event.reply("AI is already enabled for this chat!")
  return ""

@register(pattern="Luna (.*)")
async def hmm(event):
  test = event.pattern_match.group(1)
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
      'content-type': "application/json",
      'x-forwarded-for': "<user's ip>",
      'x-rapidapi-key': "fef481fee3mshf99983bfc650decp104100jsnbad6ddb2c846",
      'x-rapidapi-host': "iamai.p.rapidapi.com"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  await event.reply(result)

@tbot.on(events.NewMessage(pattern=None))
async def _(event):
    if event.is_group:
        pass
    else:
        return
    reply_msg = await event.get_reply_message()
    if reply_msg:
        if reply_msg.sender_id == 1624337697:
            pass
        else:
            return
    else:
        return
    test = str(event.text)
    r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
    k = f"({r})"
    new_string = k.replace("(", "{")
    lol = new_string.replace(")","}")
    payload = lol
    headers = {
        'content-type': "application/json",
        'x-forwarded-for': "<user's ip>",
        'x-rapidapi-key': "fef481fee3mshf99983bfc650decp104100jsnbad6ddb2c846",
        'x-rapidapi-host': "iamai.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    lodu = response.json()
    result = (lodu['message']['text'])
    await event.reply(result)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - Luna: Ask any question and Get Answer From Machine Learning Ai
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})

