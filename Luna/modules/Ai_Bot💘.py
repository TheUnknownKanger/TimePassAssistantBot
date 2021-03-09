import requests
from Luna import tbot, CMD_HELP, BOT_ID
from Luna.events import register
from telethon import events
url = "https://iamai.p.rapidapi.com/ask"
import os
from telethon import types
from telethon.tl import functions
import asyncio
import Luna.modules.sql.chatbot_sql as sql

@register(pattern="^/addchat$")
async def _(event):
    if event.is_group:
        pass
    else:
        return

    chat = event.chat
    send = await event.get_sender()
    user = await tbot.get_entity(send)
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        ses_id = "6969"
        expires = "6"
        sql.set_ses(chat.id, ses_id, expires)
        await event.reply("AI successfully enabled for this chat!")
        return
    await event.reply("AI is already enabled for this chat!")
    return ""


@register(pattern="^/rmchat$")
async def _(event):
    if event.is_group:
        pass
    else:
        return
    chat = event.chat
    send = await event.get_sender()
    user = await tbot.get_entity(send)
    is_chat = sql.is_chat(chat.id)
    if not is_chat:
        await event.reply("AI isn't enabled here in the first place!")
        return ""
    sql.rem_chat(chat.id)
    await event.reply("AI disabled successfully!")




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
  if "Thergiakis" in result:
   pro = "I am fairly yound and I was made by RoseloverX."
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "Jessica" in result:
   pro = "My name is Luna"
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(result)
    except CFError as e:
           print(e)
@tbot.on(events.NewMessage(pattern=None))
async def _(event):
    if event.is_group:
        pass
    else:
        return
    chat = event.chat
    is_chat = sql.is_chat(chat.id)  
    if not is_chat:
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
    if "Thergiakis" in result:
      pro = "I am fairly yound and I was made by RoseloverX."
      try:
        async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(pro)
      except CFError as e:
           print(e)
    elif "Jessica" in result:
      pro = "My name is Luna"
      try:
        async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(pro)
      except CFError as e:
           print(e)
    else:
      try:
         async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(1)
           await event.reply(result)
      except CFError as e:
           print(e)

@register(pattern="^/gey (.*)")
async def gey(event):

  site = "https://acobot-brainshop-ai-v1.p.rapidapi.com/get"

  querystring = {"bid":"178","key":"sX5A2PcYZbsN5EY6","uid":"mashape","msg":"My Name is Legend, Remember That."}


  headers = {
    'x-rapidapi-key': "570edf7b9cmshfb93d79bc816574p14c318jsn0e0bd91171a1",
    'x-rapidapi-host': "acobot-brainshop-ai-v1.p.rapidapi.com"
    }

  response = requests.request("GET", site, headers=headers, params=querystring)

  await event.reply(response.text)


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - Luna: Ask any question and Get Answer From Machine Learning Ai
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})

