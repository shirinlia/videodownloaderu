from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Send Youtube Video's Url"
    await message.reply_text(helptxt)
