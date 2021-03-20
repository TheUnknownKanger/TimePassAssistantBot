#Made by @RoseLoverX
from Luna import ubot, tbot
from telethon import events
from telethon.tl import functions
from telethon.tl import types
from Luna.events import register
import asyncio

async def inline_query(client, bot, query):
    from telethon import custom
    #RoseLoverX
    return custom.InlineResults(
        client,
        await client(
            functions.messages.GetInlineBotResultsRequest(
                bot=bot,
                peer="me",
                query=query,
                offset="",
                geo_point=types.InputGeoPointEmpty(),
            )
        ),
    )
@register(pattern="^/music (.*)")
async def lybot(event):
   k = event.pattern_match.group(1)
   async with tbot.conversation("@roseloverxm") as bot_conv:
      response = bot_conv.wait_event(
                events.NewMessage(incoming=True, from_users="@RoseLoverxm")
            )
      await (await inline_query(ubot, "@lybot", k))[0].click("@aniegrpbot")
      response = await response
      await asyncio.sleep(1)
      await response.forward_to(event.chat_id)

@register(pattern="^/gey ?(.*)")
async def lybot(event):
   m = event.pattern_match.group(1)
   from telethon.tl.functions.users import GetFullUserRequest
   if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await tbot(GetFullUserRequest(previous_message.sender_id))
        k = replied_user.user.first_name
   elif m:
        k = m
   else:
      sender = await event.get_sender()
      fname = sender.first_name
      k = fname
   async with tbot.conversation("@roseloverxm") as bot_conv:
      response = bot_conv.wait_event(
                events.NewMessage(incoming=True, from_users="@RoseLoverxm")
            )
      await (await inline_query(ubot, "@HowGayBot", k))[0].click("@aniegrpbot")
      response = await response
      await asyncio.sleep(1)
      await tbot.send_message(event.chat_id, response.text)


from Luna import tbot, ubot
from Luna.events import register
import requests
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

@register(pattern="^/shazam$")
async def _(event):
 try:
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.reply("Reply to an audio message.")
        return
    reply_message = await event.get_reply_message()
    stt = await event.reply("Identifying the song.")
    tmp = './'
    dl = await tbot.download_media(
            reply_message,
            tmp)
    chat = "@auddbot"
    await stt.edit("Identifying the song...")
    async with ubot.conversation(chat) as conv:
        try:
            await conv.send_file(dl)
            check = await conv.get_response()
            if not check.text.startswith("Audio received"):
                return await stt.edit("An error while identifying the song. Try to use a 5-10s long audio message.")
            await stt.edit("Wait just a sec...")
            result = await conv.get_response()
            await ubot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await stt.edit("Error Report at @lunasupport")
            return
    namem = f"Song Name : {result.text.splitlines()[0]}\
        \n\nDetails : {result.text.splitlines()[2]}"
    await stt.edit(namem)
 except Exception as e:
      await event.reply(e)
