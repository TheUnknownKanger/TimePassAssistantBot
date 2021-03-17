from Luna import CMD_HELP
from Luna.events import register
tmp = './'
from Luna import tbot, OWNER_ID
import os
from PIL import Image, ImageDraw, ImageFont

@register(pattern="^/logo ?(.*)")
async def lego(event):
 if event.sender_id == OWNER_ID:
     pass
 else:
     if event.is_group:
       await event.reply('Currently This Module Only Works in my PM!\n[Pls Click Here](tg://user?id=1624337697)')
       return
     else:
       pass
 await event.reply('Processing! Pls Weit...')
 text = event.pattern_match.group(1)
 img = Image.open('./Luna/resources/IMG_20210316_204512_022.jpg').convert('RGBA')
 draw = ImageDraw.Draw(img)
 image_widthz, image_heightz = img.size
 pointsize = 500
 fillcolor = "white"
 shadowcolor = "black"
 font = ImageFont.truetype('./Luna/resources/Vermin Vibes V.otf', 160)
 w, h = draw.textsize(text, font=font)
 h += int(h*0.21)
 image_width, image_height = img.size
 draw.text(((image_widthz-w)/2, (image_heightz-h)/2), text, font=font, fill=(240,248,255,128))
 x = (image_widthz-w)/2
 y= ((image_heightz-h)/2+6)
 draw.text((x, y), text, font=fnt, fill=(250,250,210,255), stroke_width=6, stroke_fill="black")
 fname2 = "lel.png"
 img.save(fname2, "png")
 await tbot.send_file(event.chat_id, fname2, caption="Made By Anie")
 if os.path.exists(fname2):
         os.remove(fname2)
 
file_help = os.path.basename(__file__)
file_help = file_help.replace(".py", "")
file_helpo = file_help.replace("_", " ")

__help__ = """
 In Beta!.
 - /logo <text>
Module Not Finished.!
"""

CMD_HELP.update({file_helpo: [file_helpo, __help__]})
