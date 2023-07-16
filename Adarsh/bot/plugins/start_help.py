# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","login🔑","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["start⚡️","help📚","DC"],
                ["follow❤️","ping📡","status📊","maintainers😎"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('start⚡️')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ:** \n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sᴛᴀʀᴛᴇᴅ Yᴏᴜʀ Bᴏᴛ !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__ꜱᴏʀʀʏ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ__\n\n  **ʜᴇ ᴡɪʟʟ ʜᴇʟᴘ ʏᴏᴜ**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/9d94fc0af81234943e1a9.jpg",
                caption="<i> 💢 ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜꜱᴇ ᴍᴇ 🔐👇🏻</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>ꜱᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ ᴡʀᴏɴɢ 👀</i> <b> <a href='https://github.com/adarsh-goel'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://graph.org/file/edae8bc953cbef30c4179.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\nɪ ᴀᴍ ᴛᴇʟᴇɢʀᴀᴍ ꜰɪʟᴇ ᴛᴏ ʟɪɴᴋ ɢᴇɴᴇʀᴀᴛᴏʀ ʙᴏᴛ ᴡɪᴛʜ ᴄʜᴀɴɴᴇʟ ꜱᴜᴘᴘᴏʀᴛ.\nꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ ᴀɴᴅ ꜱᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ.!',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('help📚')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nᴇᴡ Usᴇʀ Jᴏɪɴᴇᴅ **\n\n__Mʏ Nᴇᴡ Fʀɪᴇɴᴅ__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>ꜱᴏʀʀʏ ꜱɪʀ ʏᴏᴜ ᴀʀᴇ ʙᴀɴɴᴇᴅ ꜰʀᴏᴍ ᴜꜱɪɴɢ ᴍᴇ. ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴅᴇᴠᴇʟᴏᴘᴇʀ</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/ca10e459bc6f48a4ad0f7.jpg",
                Caption="**𝙹𝙾𝙸𝙽 𝚂𝚄𝙿𝙿𝙾𝚁𝚃 𝙶𝚁𝙾𝚄𝙿 𝚃𝙾 𝚄𝚂𝙴 ᴛʜɪs Bᴏᴛ!**\n\n__Dᴜᴇ ᴛᴏ Oᴠᴇʀʟᴏᴀᴅ, Oɴʟʏ Cʜᴀɴɴᴇʟ Sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ Bᴏᴛ!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🤖 Jᴏɪɴ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sᴏᴍᴇᴛʜɪɴɢ ᴡᴇɴᴛ Wʀᴏɴɢ. Cᴏɴᴛᴀᴄᴛ ᴍᴇ__ [ADARSH GOEL](https://github.com/adarsh-goel/-pro/issues).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ꜰɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ꜱᴛʀᴇᴀᴍᴀʙʟᴇ ʟɪɴᴋ ᴀɴᴅ ᴅᴏᴡɴʟᴏᴀᴅ ʟɪɴᴋ.</b>\n
<b> I ᴀʟꜱᴏ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟꜱ, ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ꜱᴇɴᴅ ᴀɴʏ ᴍᴇᴅɪᴀ ꜰɪʟᴇꜱ ᴀɴᴅ ꜱᴇᴇ ᴍɪʀᴀᴄʟᴇ✨ ᴀʟꜱᴏ ꜱᴇɴᴅ /ʟɪꜱᴛ ᴛᴏ ᴋɴᴏᴡ ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅꜱ""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💁‍♂️ DEV", url="https://github.com/adarsh-goel")],
                [InlineKeyboardButton("💥 Source Code", url="https://github.com/adarsh-goel/-pro/")]
            ]
        )
    )
