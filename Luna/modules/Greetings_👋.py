from Luna import CMD_HELP, OWNER_ID
from Luna.events import register
import os

k = 'News Py Files In Another Repo'
@register(pattern="^/teg ?(.*)")
async def sleepybot(time):
    if time.fwd_from:
        return
    if time.sender_id == OWNER_ID:
        pass
    else:
        return
    await time.reply("Greetings Py In App 2")

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
**Welcome**
 - /setwelcome <welcome message> or <reply to a text>: Saves the message as a welcome note in the chat.
 - /checkwelcome: Check whether you have a welcome note in the chat.
 - /clearwelcome: Deletes the welcome note for the current chat.
 - /welcomecaptcha <on/off>: Mutes a user on joining and unmutes as he/she solves a image captcha.
 - /cleanwelcome <on/off>: Clean previous welcome message before welcoming a new user

**Goodbye**
 - /setgoodbye <goodbye message> or <reply to a text>: Saves the message as a goodbye note in the chat.
 - /checkgoodbye: Check whether you have a goodbye note in the chat.
 - /cleargoodbye: Deletes the goodbye note for the current chat.
 - /cleangoodbye <on/off>: Clean previous goodbye message before farewelling a new user

**Available variables for formatting greeting message:**
`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`

**Note**: __You can't set new welcome/goodbye message before deleting the previous one.__
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
