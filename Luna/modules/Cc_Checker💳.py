from Luna import ubot
from Luna.events import register
import asyncio

@register(pattern="^/au (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/au {ok}")
          await asyncio.sleep(12)
          response = await bot_conv.get_response()
          await event.reply(response)
