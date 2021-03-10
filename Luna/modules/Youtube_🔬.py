from Luna import CMD_HELP, tbot
import os
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - @AnieGrpBot <query>: YouTube Inline Search

**Note:** Optional, add ; after query to specify Number of Results
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
