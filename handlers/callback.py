# (C) 2021 VeezMusic-Project

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from helpers.decorators import authorized_users_only
from config import BOT_NAME, BOT_USERNAME, OWNER_NAME, GROUP_SUPPORT, UPDATES_CHANNEL, ASSISTANT_NAME
from handlers.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>✨ **Welcome user, i'm {query.message.from_user.mention}** \n
💭 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝗮𝗹𝗹𝗼𝘄 𝘆𝗼𝘂 𝘁𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗼𝗻 𝗴𝗿𝗼𝘂𝗽𝘀 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗻𝗲𝘄 𝗧𝗲𝗹𝗲𝗴𝗿𝗮𝗺'𝘀 𝘃𝗼𝗶𝗰𝗲 𝗰𝗵𝗮𝘁𝘀 !**

💡 **𝗙𝗶𝗻𝗱 𝗼𝘂𝘁 𝗮𝗹𝗹 𝘁𝗵𝗲 𝗕𝗼𝘁'𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗮𝗻𝗱 𝗵𝗼𝘄 𝘁𝗵𝗲𝘆 𝘄𝗼𝗿𝗸 𝗯𝘆 𝗰𝗹𝗶𝗰𝗸𝗶𝗻𝗴 𝗼𝗻 𝘁𝗵𝗲 » 📚 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝗯𝘂𝘁𝘁𝗼𝗻 !**

❓ **𝗙𝗼𝗿 𝗶𝗻𝗳𝗼𝗿𝗺𝗮𝘁𝗶𝗼𝗻 𝗮𝗯𝗼𝘂𝘁 𝗮𝗹𝗹 𝗳𝗲𝗮𝘁𝘂𝗿𝗲 𝗼𝗳 𝘁𝗵𝗶𝘀 𝗯𝗼𝘁, 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Add me to your Group ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "❓ How to use Me", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "📚 Commands", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "💝 Donate", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "👥 Official Group", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Channel", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "🌐 Wiki's Page", url="https://github.com/levina-lab/veezmusic/wiki/Veez-Music-Wiki's")
                ],[
                    InlineKeyboardButton(
                        "🧪 Source Code 🧪", url="https://github.com/levina-lab/VeezMusic"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Selamat datang di menu bantuan !</b>

**di menu ini anda bisa membuka beberapa menu perintah yang tersedia, di setiap menu perintah juga ada penjelasan singkat dari masing-masing perintah**

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HELP", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 Perintah dasar Bot Music</b>

🎧 [ GROUP VC CMD ]

/play (nama lagu) - memutar lagu dari youtube
/ytp (nama lagu) - putar lagu langsung dari youtube
/stream (membalas audio) - memutar lagu menggunakan file audio
/playlist - tampilkan daftar lagu dalam antrian
/song (nama lagu) - download lagu dari youtube
/search (nama video) - cari video dari youtube secara detail
/vsong (nama video) - unduh video dari youtube detail
/lyric - (nama lagu) lirik scrapper
/vk (nama lagu) - unduh lagu dari mode inline

🎧 [ CHANNEL VC CMD ]

/cplay - streaming musik di obrolan suara saluran
/cplayer - tampilkan lagu dalam streaming
/cpause - menjeda musik streaming
/cresume - melanjutkan streaming yang dijeda
/cskip - lewati streaming ke lagu berikutnya
/cend - mengakhiri streaming musik
/admincache - menyegarkan cache admin
/ubjoinc - undang asisten untuk bergabung ke saluran Anda

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 di sini adalah perintah lanjutan</b>

/start (in group) - lihat status bot hidup
/reload - muat ulang bot dan refresh daftar admin
/cache - refresh admin cache
/uptime - periksa status waktu aktif bot
/id - tunjukkan grup/id pengguna & lainnya

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 ini perintah untuk admin</b>

/player - menampilkan status pemutaran musik
/pause - menjeda streaming musik
/resume - melanjutkan musik yang dijeda
/skip - lompat ke lagu berikutnya
/end - hentikan streaming musik
/userbotjoin - undang asisten bergabung ke grup Anda
/auth - pengguna resmi untuk menggunakan bot musik
/deauth - tidak sah untuk menggunakan bot musik
/control - buka panel pengaturan pemutar
/delcmd (on | off) - aktifkan / nonaktifkan fitur del cmd
/musicplayer (on / off) - nonaktifkan / aktifkan pemutar musik di grup Anda
/b dan /tb (ban / larangan sementara) - pengguna yang diblokir secara permanen atau sementara di grup
/ub - untuk pengguna yang tidak diblokir, Anda diblokir dari grup
/m dan /tm (bisu / bisu sementara) - bisu pengguna secara permanen atau sementara dalam grup
/um - untuk membunyikan pengguna Anda dibisukan dalam grup

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 ini perintah untuk pengguna sudo bot</b>


/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

/userbotleaveall - perintahkan asisten untuk keluar dari semua grup
/gcast - mengirim pesan siaran melalui asisten
/stats - tampilkan statistik bot
/rmd - hapus semua file yang diunduh


⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 ini perintah hanya untuk owner bot</b>

/stats - menampilkan statistik bot
/broadcast - mengirim pesan broadcast dari bot
/block (id pengguna - durasi - alasan) - blokir pengguna untuk menggunakan bot Anda
/unblock (id pengguna - alasan) - buka blokir pengguna yang Anda blokir karena menggunakan bot Anda
/blocklist - menunjukkan daftar pengguna yang diblokir karena menggunakan bot Anda

📝 note: semua perintah yang dimiliki oleh bot ini hanya dapat dijalankan oleh owner bot.

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>🏮 here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself
/tts (text) - text to speech

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 BACK", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ CARA MENGGUNAKAN BOT INI:

1.) Pertama, tambahkan saya ke grup Anda.
2.) Kemudian promosikan saya sebagai admin dan berikan semua izin kecuali admin anonim.
3.) Tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /userbotjoin untuk mengundangnya.
4.) Nyalakan obrolan suara terlebih dahulu sebelum mulai memutar musik.

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Command List", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**💡 di sini adalah menu kontrol bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⛔ anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🛄 group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🗑 Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ini dia informasi fiturnya :</b>

💡 **Feature:** Fitur ini berisi fungsi yang dapat memblokir, menonaktifkan, membuka larangan, mengaktifkan pengguna di grup Anda.

dan anda juga dapat mengatur waktu untuk ban dan mute hukuman bagi anggota di grup anda agar mereka dapat dibebaskan dari hukuman dengan waktu yang telah ditentukan.

❔ **usage:**

1️⃣ ban & temporarily ban user from your group:
   » type `/b username/reply to message` ban permanently
   » type `/tb username/reply to message/duration` temporarily ban user
   » type `/ub username/reply to message` to unban user

2️⃣ mute & temporarily mute user in your group:
   » type `/m username/reply to message` mute permanently
   » type `/tm username/reply to message/duration` temporarily mute user
   » type `/um username/reply to message` to unmute user

📝 Note: cmd /b, /tb dan /ub adalah fungsi untuk mem-ban/unbanned user dari group anda, sedangkan /m, /tm dan /um adalah perintah untuk mem-mute/unmute user di group anda.

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>ini dia informasi fiturnya :</b>
        
**💡 Feature:** hapus setiap perintah yang dikirim oleh pengguna untuk menghindari spam dalam grup!

❔ usage:**

 1️⃣ to turn on feature:
     » type `/delcmd on`
    
 2️⃣ to turn off feature:
     » type `/delcmd off`
      
⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>💡 Selamat datang di menu bantuan!</b>

**di menu ini anda bisa membuka beberapa menu perintah yang tersedia, di setiap menu perintah juga ada penjelasan singkat dari masing-masing perintah**

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 Basic Cmd", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "📕 Advanced Cmd", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📘 Admin Cmd", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "📗 Sudo Cmd", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📙 Owner Cmd", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "📔 Fun Cmd", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🏡 BACK TO HOME", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ CARA MENGGUNAKAN BOT:

1.) Pertama, tambahkan saya ke grup Anda.
2.) Kemudian promosikan saya sebagai admin dan berikan semua izin kecuali admin anonim.
3.) Tambahkan @{ASSISTANT_NAME} ke grup Anda atau ketik /userbotjoin untuk mengundangnya.
4.) Nyalakan obrolan suara terlebih dahulu sebelum mulai memutar musik.

⚡ __Powered by {BOT_NAME}__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏡 Kembali", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
