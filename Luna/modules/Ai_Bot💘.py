import requests
from Luna import tbot, CMD_HELP
from Luna.events import register
url = "https://iamai.p.rapidapi.com/ask"
import os

@register(pattern="Luna (.*)")
async def hmm(event):
  test = event.pattern_match.group(1)
  r = ('\n    \"consent\": true,\n    \"ip\": \"::1\",\n    \"question\": \"{}\"\n').format(test)
  k = f"({r})"
  new_string = k.replace("(", "{")
  lol = new_string.replace(")","}")
  payload = lol
  headers = {
      'content-type': "application/json",
      'x-forwarded-for': "<user's ip>",
      'x-rapidapi-key': "fef481fee3mshf99983bfc650decp104100jsnbad6ddb2c846",
      'x-rapidapi-host': "iamai.p.rapidapi.com"
      }

  response = requests.request("POST", url, data=payload, headers=headers)
  lodu = response.json()
  result = (lodu['message']['text'])
  await event.reply(result)

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - Luna: Ask any question and Get Answer From Machine Learning Ai
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})

