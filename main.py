import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User
from pyrogram.types.messages_and_media import Message
from pyrogram import Client, filters
import time

import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import asyncio
import datetime
import shutil, psutil, traceback, os
import random
import string
import time
import traceback
import aiofiles
from pyrogram import Client, filters, __version__
from pyrogram.types import Message
from pyrogram.errors import (
    FloodWait,
    InputUserDeactivated,
    PeerIdInvalid,
    UserIsBlocked,
)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
OWNER_ID = int(os.environ.get("OWNER_ID"))
BOT_USERNAME = os.environ.get("BOT_USERNAME")
OWNER_ID = int(os.environ.get("OWNER_ID"))
LANGAUGE = os.environ.get("LANGAUGE", "TR")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

@client.on(events.NewMessage(pattern="^/start$"))
async def info(event):
  await event.reply("**Merhaba ben Redanon Oyun Botuyum.\n\nKomutları görmek için /yardim yazın\n\nSahibim: @Plaguexx **",
                    buttons=(
                      [
                       Button.url('Beni Grubuna Ekle ➕', 'https://t.me/redanongamebot?startgroup=a')
                      ],
                      [
                       Button.url('📢 Kanal', 'https://t.me/redanonchannel'),
                       Button.url('🇹🇷 Sahibim', 'https://t.me/Plagexx')
                      ],
                      [
                       Button.inline("Yardım", data="yardim")
                      ],
                    ),
                    link_preview=False
                   )

@client.on(events.callbackquery.CallbackQuery(data="komutlar"))
async def handler(event):
    await event.edit(f"**Yardım Menüsü:\n\n/dsor - Doğruluk Sorusu sorar.\n/csor - Cesaret sorusu sorar.\n/cancel - Oyunu Durdururum...\n\n❕ Yalnızca yöneticileri bu komutları kullanabilir.**", buttons=(
                      [
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)