from Luna.modules.sql.night_mode_sql import add_nightmode, rmnightmode, get_all_chat_id, is_nightmode_indb
from telethon.tl.types import ChatBannedRights
from apscheduler.schedulers.asyncio import AsyncIOScheduler 
from telethon import functions
from Luna.events import register
from Luna import tbot

hehes = ChatBannedRights(
    until_date=None,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    send_polls=True,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)
openhehe = ChatBannedRights(
    until_date=None,
    send_messages=False,
    send_media=False,
    send_stickers=False,
    send_gifs=False,
    send_games=False,
    send_inline=False,
    send_polls=False,
    invite_users=True,
    pin_messages=True,
    change_info=True,
)

@register(pattern="^/scgrp")
async def close_ws(event):
    if not event.is_group:
        await event.reply("You Can Only Enable Night Mode in Groups.")
        return
    if is_nightmode_indb(str(event.chat_id)):
        await event.reply("This Chat is Has Already Enabled Night Mode.")
        return
    add_nightmode(str(event.chat_id))
    await event.reply(f"**Added Chat {event.chat.title} With Id {event.chat_id} To Database. This Group Will Be Closed On 12Am(IST) And Will Opened On 06Am(IST)**")

@register(pattern="^/rsgrp")
async def disable_ws(event):
    if not event.is_group:
        await event.reply("You Can Only Disable Night Mode in Groups.")
        return
    if not is_nightmode_indb(str(event.chat_id)):
        await event.reply("This Chat is Has Not Enabled Night Mode.")
        return
    rmnightmode(str(event.chat_id))
    await event.reply(f"**Removed Chat {event.chat.title} With Id {event.chat_id} From Database. This Group Will Be No Longer Closed On 12Am(IST) And Will Opened On 06Am(IST)**")


async def job_close():
    ws_chats = get_all_chat_id()
    if len(ws_chats) == 0:
        return
    for warner in ws_chats:
        try:
            await tbot.send_message(
              int(warner.chat_id), "`12:00 Am, Group Is Closing Till 6 Am. Night Mode Started !` \n**Powered By @FRidayOT**"
            )
            await tbot(
            functions.messages.EditChatDefaultBannedRightsRequest(
                peer=int(warner.chat_id), banned_rights=hehes
            )
            )
        except Exception as e:
            logger.info(f"Unable To Close Group {warner} - {e}")

scheduler = AsyncIOScheduler(timezone="Asia/Kolkata")
scheduler.add_job(job_close, trigger="cron", hour=23, minute=55)
scheduler.start()
