# Copyright (c) 2021 Itz-fork
# Don't kang this else your dad is gae

import os
import shutil
import asyncio

from pyrogram import Client
from pyrogram.errors import FloodWait

# Send file to a user
async def send_file(unzip_bot, c_id, doc_f, query, full_path):
    try:
        # Checks if url file size is bigger than 2GB (Telegram limit)
        u_file_size = os.stat(doc_f).st_size
        if Config.TG_MAX_SIZE < int(u_file_size):
            return await unzip_bot.send_message(
                chat_id=c_id,
                text="`File Size is too large to send in telegram 🥶!` \n\n**Sorry, but I can't do anything about this as it's a telegram limitation 😔!**"
            )
        await unzip_bot.send_document(chat_id=c_id, document=doc_f, caption="**Extracted by @NexaUnzipper_Bot**")
        os.remove(doc_f)
    except FloodWait as f:
        asyncio.sleep(f.x)
        return send_file(c_id, doc_f)
    except FileNotFoundError:
        await query.answer("Sorry! I can't find that file", show_alert=True)
    except BaseException:
        shutil.rmtree(full_path)
