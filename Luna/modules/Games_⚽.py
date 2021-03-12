from Luna import CMD_HELP, OWNER_ID
import os
from Luna import tbot
from telethon import *
from telethon import events
from telethon.tl import functions
from telethon.tl import types
from telethon.tl.types import *

from Luna import *

from Luna.events import register, lunabot



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


## -- THANKS TO LONAMI FOR THIS FUNCTION --#

# -- MADE BY @MissJulia_Robot


@juliabot(pattern="^/gameed")
async def ramdomgames(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "1+2=3"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/mathbattle$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    

    chat = "@AnieGrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/gameed")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jsusxjxhxhxshsjs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "MotoFX"))[0].click("MissJuliaRobot")


@register(pattern="^/motofx$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsusxjxhxhxshsjs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jsuskhfkhdxjzhsjs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Penalty Shooter"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/penaltyshooter$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsuskhfkhdxjzhsjs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jslgggfsslaxvuoqdjlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "F1"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/racingcar$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jslgggfsslaxvuoqdjlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jsdndbbduoqdjlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Karate"))[1].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/karate$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsdndbbduoqdjlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jsdndbafjaffajlxvqs")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Football"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/footballstar$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsdndbafjaffajlxvqs")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/jsddjdhiwws")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Neon Blaster"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/neonblaster$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/jsddjdhiwws")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/whwyywwhewws")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Disco"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/discoball$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/whwyywwhewws")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


@juliabot(pattern="^/wssksskxxskss")
async def ramdomgamesk(event):
    if event.fwd_from:
        return
    await (await inline_query(ubot, "@gamee", "Gravity"))[0].click(
        "MissJuliaRobot", hide_via=True
    )


@register(pattern="^/gravityninja$")
async def ramdomgamess(event):
    if event.fwd_from:
        return
    
    chat = "@Aniegrpbot"
    async with tbot.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=OWNER_ID)
            )
            entity = await tbot.get_entity(OWNER_USERNAME)
            await tbot.send_message(entity, "/wssksskxxskss")
            response = await response
            await response.forward_to(event.chat_id)
        except Exception:
            pass


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
**Here are some cool games for you enjoy them, more coming in the future !**

 - /motofx
 - /mathbattle
 - /penaltyshooter
 - /racingcar
 - /karate
 - /footballstar
 - /gravityninja
 - /discoball
 - /neonblaster
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
