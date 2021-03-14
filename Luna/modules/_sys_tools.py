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
  try:
    uname = platform.uname()
    softw = "System Information\n"
    softw += f"System   : {uname.system}\n"
    softw += f"Release  : {uname.release}\n"
    softw += f"Version  : {uname.version}\n"
    softw += f"Machine  : {uname.machine}\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"Boot Time: {bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}\n"
    # CPU Cores
    cpuu = "CPU Info\n"
    cpuu += "Physical cores   : " + str(psutil.cpu_count(logical=False)) + "\n"
    cpuu += "Total cores      : " + str(psutil.cpu_count(logical=True)) + "\n"
    # CPU frequencies
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
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "Memory Usage\n"
    memm += f"Total     : {get_size(svmem.total)}\n"
    memm += f"Available : {get_size(svmem.available)}\n"
    memm += f"Used      : {get_size(svmem.used)}\n"
    memm += f"Percentage: {svmem.percent}%\n"
    # Bandwidth Usage
    bw = "Bandwith Usage\n"
    bw += f"Upload  : {get_size(psutil.net_io_counters().bytes_sent)}\n"
    bw += f"Download: {get_size(psutil.net_io_counters().bytes_recv)}\n"
  except Exception:
     pass
  await event.reply(uname)