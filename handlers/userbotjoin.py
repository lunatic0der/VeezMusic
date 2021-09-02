import asyncio
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from helpers.filters import command
from helpers.decorators import authorized_users_only, errors
from callsmusic.callsmusic import client as USER
from config import BOT_USERNAME, SUDO_USERS, ASSISTANT_NAME


@Client.on_message(command(["userbotjoin", f"userbotjoin@{BOT_USERNAME}"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Tambahkan saya sebagai admin grup Anda terlebih dahulu</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
    except UserAlreadyParticipant:
        await message.reply_text(
            f"<b>{user.first_name} sudah ada di obrolan Anda</b>",
        )
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>⛑ Flood Wait Error ⛑\n{user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung untuk userbot! Pastikan pengguna tidak dibanned dalam grup."
            f"\n\nAtau tambahkan @{ASSISTANT_NAME} secara manual ke Grup Anda dan coba lagi.</b>",
        )
        return
    await message.reply_text(
        f"<b>{user.first_name} berhasil bergabung dengan obrolan Anda</b>",
    )


@Client.on_message(command(["userbotleave", f"userbotleave@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
@authorized_users_only
async def rem(client, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:
        await message.reply_text(
            f"<b>Pengguna tidak dapat meninggalkan grup Anda! Mungkin menunggu floodwaits."
            "\n\nAtau keluarkan saya secara manual dari ke Grup Anda</b>",
        )
        return
    
@Client.on_message(command(["userbotleaveall", f"userbotleaveall@{BOT_USERNAME}"]))
async def bye(client, message):
    if message.from_user.id in SUDO_USERS:
        left=0
        failed=0
        lol = await message.reply("Assistant Leaving all chats")
        async for dialog in USER.iter_dialogs():
            try:
                await USER.leave_chat(dialog.chat.id)
                left = left+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            except:
                failed=failed+1
                await lol.edit(f"Assistant leaving... Left: {left} chats. Failed: {failed} chats.")
            await asyncio.sleep(0.7)
        await client.send_message(message.chat.id, f"Left {left} chats. Failed {failed} chats.")


@Client.on_message(command(["userbotjoinchannel", "ubjoinc"]) & ~filters.private & ~filters.bot)
@authorized_users_only
@errors
async def addcchannel(client, message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("is the chat even linked ?")
      return    
    chat_id = chid
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>promote me as group admin first !</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name = "helper"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id, "🤖: i joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>helper already in your channel</b>",
        )
        return
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>⛑ Flood Wait Error ⛑\n{user.first_name} tidak dapat bergabung dengan grup Anda karena banyaknya permintaan bergabung untuk userbot! Pastikan pengguna tidak dibanned dalam grup."
            f"\n\nAtau tambahkan @{ASSISTANT_NAME} secara manual ke Grup Anda dan coba lagi.</b>",
        )
        return
    await message.reply_text(
        "<b>helper userbot joined your channel</b>",
    )
