import requests
url = "https://iamai.p.rapidapi.com/ask"
from Luna import tbot, OWNER_ID
from Luna.events import register
from telethon import events
from telethon import types
from telethon.tl import functions
import asyncio

@register(pattern="q (.*)")
async def hmm(event):
  if event.sender_id == OWNER_ID:
        pass
  else:
        return
  test = event.pattern_match.group(1)
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
    'content-type': "application/json",
    'x-forwarded-for': "<user's ip>",
    'x-rapidapi-key': "33b8b1a671msh1c579ad878d8881p173811jsn6e5d3337e4fc",
    'x-rapidapi-host': "iamai.p.rapidapi.com"
    }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  if "Thergiakis" in result:
   pro = "I am fairly yound and I was made by RoseloverX."
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  elif "Jessica" in result:
   pro = "My name is Luna"
   try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(pro)
   except CFError as e:
           print(e)
  else:
    try:
      async with tbot.action(event.chat_id, 'typing'):
           await asyncio.sleep(2)
           await event.reply(result)
    except CFError as e:
           print(e)
