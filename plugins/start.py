from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Developer's Website", url="http://shirinlia.com")],
        ])
    welcomed = f"Hey, Welcome <b>{message.from_user.first_name}</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
