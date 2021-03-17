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
 loda = event.pattern_match.group(1)
 if "|" in loda:
     iid, reasonn = quew.split("|")
     text = iid.strip()
     ab = reasonn.strip()
 else:
    text = loda
# get an image
 base = Image.open('./Luna/resources/IMG_20210316_204512_022.jpg').convert('RGBA')
# make a blank image for the text, initialized to transparent text color
 txt = Image.new('RGBA', base.size, (255,255,255,0))

# get a font
 fnt = ImageFont.truetype('./Luna/resources/Vermin Vibes V.otf', 160)
# get a drawing context
 d = ImageDraw.Draw(txt)

 image_width, image_height = base.size

# draw text, half opacity
 d.text((image_width/2, image_height/2), text, font=fnt, fill=(240,248,255,128))
# draw text, full opacity
 x = 500
 y = 40
 d.text((x,y), text, font=fnt, fill=(250,250,210,255), stroke_width=6, stroke_fill="black")
 d.text((500,600), ab, font=fnt, fill="red")
 out = Image.alpha_composite(base, txt)
 fname = 'lel.png'
 out.save(fname, "png")
 await tbot.send_file(event.chat_id, fname, caption="Made By Anie")
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
