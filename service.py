import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InlineKeyboardButton, User, Message

Client = Client(
    "Service message remover",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('ғᴏʀ ᴄʜᴀᴛ👻', url="https://t.me/houseofghost")
        ]], 
        [[
        InlineKeyboardButton('ɢʜᴏsᴛ👻', url="https://t.me/My_Dear_lightbright")
        ]]
    ) 

@Client.on_message(filters.private & filters.command(["start"]))
async def start(bot, message):
    await message.reply_sticker("CAACAgIAAxkBAAIlnWKDiLoKLgZ5vv1DO730tIFB7pCVAAK3AAMw1J0Rmj-D7OSiEk8kBA")
    await message.reply_text(
        f""" Hai {message.from_user.mention} am Service Message, command and link deleter bot.""", 
        disable_web_page_preview=True,
        reply_markup=START_BUTTON
    )
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
 await message.delete()

Client.run()
