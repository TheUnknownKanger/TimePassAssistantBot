from Luna import CMD_HELP
import os
from Luna import tbot
import requests

from Luna import CASH_API_KEY

from telethon import types
from telethon.tl import functions
from Luna.events import register


@register(pattern="^/cash")
async def _(event):

    cmd = event.text

    args = cmd.split(" ")

    if len(args) == 4:
        try:
            orig_cur_amount = float(args[1])

        except ValueError:
            await event.reply("Invalid Amount Of Currency")
            return

        orig_cur = args[2].upper()

        new_cur = args[3].upper()

        request_url = (
            f"https://www.alphavantage.co/query"
            f"?function=CURRENCY_EXCHANGE_RATE"
            f"&from_currency={orig_cur}"
            f"&to_currency={new_cur}"
            f"&apikey={CASH_API_KEY}"
        )
        response = requests.get(request_url).json()
        try:
            current_rate = float(
                response["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
            )
        except KeyError:
            await event.reply("Currency Not Supported.")
            return
        new_cur_amount = round(orig_cur_amount * current_rate, 5)
        await event.reply(f"{orig_cur_amount} {orig_cur} = {new_cur_amount} {new_cur}")

    elif len(args) == 1:
        await event.reply(__help__)

    else:
        await event.reply(
            f"**Invalid Args!!:** Required 3 But Passed {len(args) -1}",
        )


file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /cash : currency converter
Example syntax: `/cash 1 USD INR`
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
