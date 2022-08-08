import os

from telethon import Button, events

from startup import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/8039084ae718d0eff674c.jpg"
)
ms = 4

)

CAPTION = f"**꧁•⊹٭Ping٭⊹•꧂**\n\n   ⚜ {ms}\n   ⚜ ❝𝐌𝐲 𝐌𝐚𝐬𝐭𝐞𝐫❞ ~『Telethon』"


@bot.on(events.NewMessage(pattern="^/ping"))
async def _(event):
    UMM = [[Button.url("⚜ Cԋαɳɳҽʅ ⚜", "https://t.me/Murat_30")]]
    await bot.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
