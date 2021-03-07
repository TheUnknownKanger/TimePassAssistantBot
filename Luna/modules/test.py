from Luna.events import register
from telethon import custom, events, Button
pm_caption = "Your Info"
from Luna import tbot as bot
from Luna import tbot
@register(pattern="^/nfo")
async def nfo(event):
  await tbot.send_message(
            event.chat_id,
            pm_caption,
            buttons=[
                [
                    Button.inline("Info 💥", data="start_again"),
                ],
            ],
        )

boy = event.sender_id

PRO = await tbot.get_entity(boy)
LEGENDX = "Your Details By Luna\n\n"
LEGENDX += f"First Name : {PRO.first_name} \n"
LEGENDX += f"Last Name : {PRO.last_name}\n"
LEGENDX += f"Scam : {PRO.scam}\n"
LEGENDX += f"Support : {PRO.support}\n"
LEGENDX += f"Restricted : {PRO.restricted} \n"
LEGENDX += f"ID : {boy}\n"
LEGENDX += f"Username : {PRO.username}\n\n"
LEGENDX += "Thenks for Uzing Mi ☺️☺️☺️"
@tbot.on(events.CallbackQuery(pattern=r"start_again"))
async def start_again(event):
        await event.reply(LEGENDX)
