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

@register(pattern="^/key (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/key {ok}")
          await asyncio.sleep(2)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/ss (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ss {ok}")
          await asyncio.sleep(12)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/pp (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/pp {ok}")
          await asyncio.sleep(12)
          response = await bot_conv.get_response()
          await event.reply(response)

@register(pattern="^/ch (.*)")
async def alive(event):
      ok = event.pattern_match.group(1)
      async with ubot.conversation("@Carol5_bot") as bot_conv:
          await bot_conv.send_message(f"/ch {ok}")
          await asyncio.sleep(12)
          response = await bot_conv.get_response()
          await event.reply(response)
