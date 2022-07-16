import os
from pyrogram import Client, filters
from pyrogram.types import *

from MashaRoBot.conf import get_str_key
from MashaRoBot import pbot
 
 # pls don't delete
REPO_TEXT = "**LISA [BOT](https://telegra.ph/file/85d22978cb6bda06397cf.jpg) will Make Your Groups Secured And it's have a lot of fun features (:  ! \n\n↼ Owner ⇀ : 『 [『🍁』༺⋆ͥ⋆ͣ⋆᭄ͫ⁣𓆩𝙻𝚄𝚃𝚃𝙰𝙿𝙿𝙸𓆪➳࿐𝆺𝅥⃝😈](t.me/LUTTAPPIMOVIE) 』\n╭──────────────\n┣─ » Python ~ 3.8.6\n┣─ » Update ~ Recently\n╰──────────────\n\n»»» @KOMBOTZZ«««"
  
BUTTONS = InlineKeyboardMarkup(
      [[
        InlineKeyboardButton("ʀᴇᴘᴏꜱɪᴛᴏʀʏ", url=f"https://t.me/Komassistantbot"),
        InlineKeyboardButton("Gɪᴛʜᴜʙ", url=f"https://t.me/Komassistantbot"),
      ],[
        InlineKeyboardButton("ᴏᴡɴᴇʀ ❣️", url="https://t.me/luttappimovie"),
        InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/kombotzz"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/luttappimovie"),
      ],[
        InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇꜱ", url="https://t.me/kombotzz"),
        InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/LUTTAPPIMOVIE"),
       InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/Komassistantbot"),
      ]]
    )
  
  
@pbot.on_message(filters.command(["repo"]))
async def repo(pbot, update):
    await update.reply_text(
        text=REPO_TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True,
        quote=True
    )
