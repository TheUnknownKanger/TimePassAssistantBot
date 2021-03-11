from Luna import CMD_HELP
import os

k = 'News Py Files In Another Repo'


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /news <country code> <LanguageCode>: Returns today's American News Headlines (ONLY WORKS IN PM)
**Example:**
 - /news US en: This will return news for US in english language.
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
