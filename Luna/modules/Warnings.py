from Luna.events import bot
from Luna import CMD_HELP
import os




file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /warn <userid> | <reason> or /warn <reason> in reply to a message: warn a user
 - /removelastwarn: remove the last warn that a user has received
 - /getwarns: list the warns that a user has received
 - /resetwarns: reset all warns that a user has received
 - /setwarnmode <kick/ban/mute>: set the warn mode for the chat
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
