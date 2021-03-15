from Luna import ubot, tbot
from telethon import events
from telethon.tl import functions
from telethon.tl import types
from Luna.events import register

async def inline_query(client, bot, query):
    from telethon import custom

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
   await (await inline_query(ubot, "@lybot", k))[0].click("@lunasonggrp")
   async with tbot.conversation("@lunasonggrp") as bot_conv:
      response = bot_conv.wait_event(
                events.NewMessage(incoming=True)
            )
      pro = await response
      await pro.forward_to(event.chat_id)
