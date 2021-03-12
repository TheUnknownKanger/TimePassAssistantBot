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
@register(pattern="^/music (*.)")

await (await inline_query(ubot, "@lybot", "Despacito"))[0].click(-1001454532285)
async with tbot.conversation("@lunasonggrp") as bot_conv:
    response = bot_conv.wait_event(
                events.NewMessage(incoming=True)
            )
    response = await response
    await response.forward_to(event.chat_id)
