from Luna import tbot
from Luna.events import register
import os
import html
import json
import os
from typing import Optional
from Luna import DRAGONS
ELEVATED_USERS_FILE = os.path.join(os.getcwd(), "Luna/advanced_users.json")

@register(pattern="^/addsudo ?(.*)")
async def sudo(event):
    if event.reply_to_msg_id:
       reply_message = await event.get_reply_message()
       user_id = reply_message.sender_id
    else:
       cid = event.pattern_match.group(1)
       if cid.isnumeric():
           cid = int(cid)
       entity = await tbot.get_input_entity(cid)
       r_sender_id = entity.user_id
       user_id = r_sender_id
    with open(ELEVATED_USERS_FILE, "r") as infile:
        data = json.load(infile)
    if user_id in DRAGONS:
        await event.reply("This member is already a Dragon Disaster")
        return ""
    data["sudos"].append(user_id)
    DRAGONS.append(user_id)
    
    with open(ELEVATED_USERS_FILE, "w") as outfile:
        json.dump(data, outfile, indent=4)
    rep = "\nSuccessfully set Disaster level of {} to Dragon!".format(
            user_member.first_name
        )
    await event.reply("In Beta Weiti Adding")

   
