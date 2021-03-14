import platform
import sys
from datetime import datetime

import psutil
from telethon import version
from Luna import tbot, OWNER_ID, SUDO_USERS, DEV_USERS
from Luna.events import register

def get_size(inputbytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if inputbytes < factor:
            return f"{inputbytes:.2f}{unit}{suffix}"
        inputbytes /= factor

@register(pattern="^/echo ?(.*)")
async def echo(event):
  if event.fwd_from:
        return
  if event.sender_id == OWNER_ID:
        pass
  elif event.sender_id in SUDO_USERS:
        pass
  elif event.sender_id in DEV_USERS:
        pass
  else:
        return
  if event.reply_to_msg_id:
          await event.delete()
          previous_message = await event.get_reply_message()
          k = await tbot.send_message(
                event.chat_id,
                previous_message
             )
  else:
          ok = event.pattern_match.group(1)
          await event.delete()
          await tbot.send_message(event.chat_id, ok)

@register(pattern="^/cpu")
async def cpunfo(event):
    if event.sender_id == OWNER_ID:
         pass
    else:
         return
    cpuu += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    cpuu += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    cpufreq = psutil.cpu_freq()
    cpuu += f"Max Frequency    : {cpufreq.max:.2f}Mhz\n"
    cpuu += f"Min Frequency    : {cpufreq.min:.2f}Mhz\n"
    cpuu += f"Current Frequency: {cpufreq.current:.2f}Mhz\n\n"
    # CPU usage
    cpuu += "CPU Usage Per Core\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"Core {i}  : {percentage}%\n"
    cpuu += "Total CPU Usage\n"
    cpuu += f"All Core: {psutil.cpu_percent()}%\n"
    help_string = "**Cpu Info**"
    help_string += f"{str(cpuu)}\n"
    await event.reply(help_string)
