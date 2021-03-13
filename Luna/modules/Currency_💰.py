from Luna import CMD_HELP
import os
from Luna import tbot
import requests
import cryptocompare
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


@register(pattern="^/crypto (.*)")
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stark = input_str.split(" ", 1)
    curreo = stark[0]
    currency1 = stark[1]
    curre = curreo.upper()
    currency = currency1.upper()
    take = ""
    take = cryptocompare.get_price(currency, curr=curre)
    t = take.get(currency)
    k = curre
    q = str(t.get(curre))

    await event.reply(
        f"<b><u>Conversion complete</b></u> \n<b>cryptocurrency</b>:-  <code>{currency}</code> \n<b>cryptocurrency value in </b> <code>{k}</code> <b> is :- </b> <code> {q}</code>",
        parse_mode="HTML",
    )

file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 - /cash : currency converter
Example syntax: `/cash 1 USD INR`
 - /crypto : Crypto Value
Example syntax: `/crypto inr btc`
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
