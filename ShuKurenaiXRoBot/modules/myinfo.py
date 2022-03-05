from telethon import custom, events, Button
import os,re
import asyncio

from ShuKurenaiXRoBot import telethn as bot
from ShuKurenaiXRoBot import telethn as tgbot
from ShuKurenaiXRoBot import telethn as aasf
from ShuKurenaiXRoBot.events import register 

edit_time = 5
Shu1 = "https://telegra.ph/file/0533c03077089c1888aca.jpg"
Shu2 = "https://te.legra.ph/file/fdd4730f27038b6a25a82.jpg"
Shu3 = "https://te.legra.ph/file/dce2e3e278de5ca987bfc.jpg"
Shu4 = "https://te.legra.ph/file/9df146a1a8cfdcfc48057.jpg"

@register(pattern="/myinfo")
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")]]
  on = await aasf.send_message(event.chat, f"**❦ Hᴇʏ {(event.sender.first_name)}**\n\n**❦ I AM YOUR FRIEND [𝑻𝒆𝒛𝒛𝒂❥︎](https://t.me/Tezza_Robot)**\n**❦ I Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ [𝑻𝒆𝒛𝒛𝒂❥︎ Team](t.me/tezzasupportgroup)**", file=Shu1, buttons=button)

  await asyncio.sleep(edit_time)
  ok = await aasf.edit_message(event.chat_id, on, file=Shu2, buttons=button) 

  await asyncio.sleep(edit_time)
  ok2 = await aasf.edit_message(event.chat_id, ok, file=Shu3, buttons=button)

  await asyncio.sleep(edit_time)
  ok3 = await aasf.edit_message(event.chat_id, ok2, file=Shu1, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok4 = await aasf.edit_message(event.chat_id, ok3, file=Shu3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok5 = await aasf.edit_message(event.chat_id, ok4, file=Shu2, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok6 = await aasf.edit_message(event.chat_id, ok5, file=Shu3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok7 = await aasf.edit_message(event.chat_id, ok6, file=Shu1, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    SHU = "YOUR DETAILS BY 𝑻𝒆𝒛𝒛𝒂❥︎ \n"
    SHU += f"FIRST NAME : {PRO.first_name} \n"
    SHU += f"LAST NAME : {PRO.last_name}\n"
    SHU += f"YOU BOT : {PRO.bot} \n"
    SHU += f"RESTRICTED : {PRO.restricted} \n"
    SHU += f"USER ID : {boy}\n"
    SHU += f"USERNAME : {PRO.username}\n"
    await event.answer(SHU, alert=True)
  except Exception as e:
    await event.reply(f"{e}")

__mod_name__ = "Myinfo"

__help__ = """
 ~ /myinfo *:* Get Your Details On Inline. 
"""
