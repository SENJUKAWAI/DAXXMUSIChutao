import logging
import random
import asyncio
from pyrogram import filters
from pyrogram.types import Message
from DAXXMUSIC import app

waifu_images = [
    "https://envs.sh/SfF.jpg",
    "https://envs.sh/Sft.jpg",
    "https://envs.sh/Sfe.jpg",
    "https://envs.sh/Sfi.jpg",
    "https://envs.sh/Sfb.jpg",
    "https://envs.sh/SfQ.jpg",
    "https://envs.sh/Sfh.jpg",
    "https://envs.sh/Sfd.jpg",
    "https://envs.sh/Sfd.jpg",
    "https://envs.sh/Sf2.jpg",
    "https://envs.sh/Sfu.jpg",
    "https://envs.sh/Sg6.jpg",
    "https://envs.sh/SgV.jpg",
    "https://envs.sh/SfE.jpg",
    "https://envs.sh/Sg-.jpg",
    "https://envs.sh/Sgx.jpg",
    "https://envs.sh/Sgf.jpg",
    "https://envs.sh/Sga.jpg",
    "https://envs.sh/SgO.jpg",
    "https://envs.sh/SgO.jpg",
    "https://envs.sh/SgM.jpg",
    "https://envs.sh/SgX.jpg",
    "https://envs.sh/Sgr.jpg",
    "https://envs.sh/Sgs.jpg",
    "https://envs.sh/Sg9.jpg",
    "https://envs.sh/Sgg.jpg",
    "https://envs.sh/SgH.jpg",
    "https://envs.sh/Sg3.jpg",
    "https://envs.sh/SgC.jpg",
    "https://envs.sh/SgR.jpg",
]

@app.on_message(filters.command("waifus"))
async def es_img(_, message):
    image = random.choice(waifu_images)
    sent_message = await message.reply_video(video=image, caption=f"ʙʏ [𝙃𝙪 𝙩𝙖𝙤](https://t.me/@HU_TAO_xbot)")

    await asyncio.sleep(20)

    await sent_message.delete()
