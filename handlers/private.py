from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):

       await message.reply_text(
        f"""**Hallo Selamat Databg, Saya {bn} 🎵

Saya adalah bot musik yang dapat menghiburmu 😉.

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan Ke Group ➕ ",  url="https://t.me/zankemusicbot?startgroup=true")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/xbotgrup"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "✉️ DONATE ✉️",Hai Terimaksih Jika kamu ingin berdonasi kepada pemilik saya 😊

Setiap donasi yang kalian berikan
Akan kami kumpulkan untuk 
Memperpanjang ataupun meningkatkan VPS saya
Agar saya dapat berfungsi lebih maksimal.,

Jika kalian ingin memberikan donasi
Silahkan PM Owner saya 👉 [Zankee]url="https://t.me/zankizaif"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/")
                ]
            ]
        )
   )


