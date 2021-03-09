import aiohttp
from Luna import tbot, CMD_HELP
from Luna.events import register
from telethon import events
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
    if event.is_group:
        pass
    else:
        return
    chat = event.chat
    is_chat = sql.is_chat(chat.id)  
    if not is_chat:
        return
    test = event.pattern_match.group(1)
    url = f"https://lunabot.tech/?query={test}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            res = await res.json()
            text = res["response"]
    
    try:
      async with tbot.action(event.chat_id, 'typing'):
          await asyncio.sleep(1)
          await event.reply(text)
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
    url = f"https://lunabot.tech/?query={test}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as res:
            res = await res.json()
            text = res["response"]
    
    try:
      async with tbot.action(event.chat_id, 'typing'):
          await asyncio.sleep(1)
          await event.reply(text)
    except CFError as e:
           print(e)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - Luna: Ask any question and Get Answer From Machine Learning Ai
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})

