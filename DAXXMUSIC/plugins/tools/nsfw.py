import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from DAXXMUSIC import app  # Ensure this import is correct for your project

# URL for NSFW content
url_nsfw = "https://api.waifu.pics/nsfw/"

# Define your bot client (replace "your_bot" with your bot's name)
client = Client("hutao")


# Check if the user is an admin (you need to define this function)
async def is_admin(chat_id, user_id):
    # Implement your admin check here
    return True


# Check if NSFW is enabled for the chat
async def is_nsfw_on(chat_id):
    # Implement the logic to check if NSFW is enabled for the chat
    return True


# Enable NSFW mode
async def nsfw_on(chat_id):
    # Implement the logic to enable NSFW mode for the chat
    pass


# Disable NSFW mode
async def nsfw_off(chat_id):
    # Implement the logic to disable NSFW mode for the chat
    pass


# Command to add NSFW mode
@client.on_message(filters.command("addnsfw"))
async def add_nsfw(client, message: Message):
    if not await is_admin(message.chat.id, message.from_user.id):
        return await message.reply("You are not an admin.")

    is_nsfw = await is_nsfw_on(message.chat.id)
    if not is_nsfw:
        await nsfw_on(message.chat.id)
        await message.reply("Activated NSFW Mode!")
    else:
        await message.reply("NSFW Mode is already activated for this chat!")


# Command to remove NSFW mode
@client.on_message(filters.command("rmnsfw"))
async def rem_nsfw(client, message: Message):
    if not await is_admin(message.chat.id, message.from_user.id):
        return await message.reply("You are not an admin.")

    is_nsfw = await is_nsfw_on(message.chat.id)
    if is_nsfw:
        await nsfw_off(message.chat.id)
        await message.reply("Rolled Back to SFW Mode!")
    else:
        await message.reply("NSFW Mode is already deactivated.")


# Command to send blowjob NSFW content
@client.on_message(filters.command("blowjob"))
async def blowjob(client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        is_nsfw = await is_nsfw_on(message.chat.id)
        if not is_nsfw:
            return await message.reply("NSFW is not activated in this chat.")

    url = f"{url_nsfw}blowjob"
    response = requests.get(url).json()
    img_url = response["url"]

    await client.send_photo(message.chat.id, img_url, reply_to_message_id=message.message_id)


# Command to send trap NSFW content
@client.on_message(filters.command("trap"))
async def trap(client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        is_nsfw = await is_nsfw_on(message.chat.id)
        if not is_nsfw:
            return await message.reply("NSFW is not activated in this chat.")

    url = f"{url_nsfw}trap"
    response = requests.get(url).json()
    img_url = response["url"]

    await client.send_photo(message.chat.id, img_url, reply_to_message_id=message.message_id)


# Command to send NSFW waifu content
@client.on_message(filters.command(["nsfwwaifu", "nwaifu"]))
async def nsfwwaifu(client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        is_nsfw = await is_nsfw_on(message.chat.id)
        if not is_nsfw:
            return await message.reply("NSFW is not activated in this chat.")

    url = f"{url_nsfw}waifu"
    response = requests.get(url).json()
    img_url = response["url"]

    await client.send_photo(message.chat.id, img_url, reply_to_message_id=message.message_id)


# Command to send NSFW neko content
@client.on_message(filters.command(["nsfwneko", "nneko"]))
async def nsfwneko(client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        is_nsfw = await is_nsfw_on(message.chat.id)
        if not is_nsfw:
            return await message.reply("NSFW is not activated in this chat.")

    url = f"{url_nsfw}neko"
    response = requests.get(url).json()
    img_url = response["url"]

    await client.send_photo(message.chat.id, img_url, reply_to_message_id=message.message_id)


# Command to send lewd content
@client.on_message(filters.command("lewd"))
async def lewd(client, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        is_nsfw = await is_nsfw_on(message.chat.id)
        if not is_nsfw:
            return await message.reply("NSFW is not activated in this chat.")

    response = requests.get("https://waifu-api.vercel.app/items/1").json()
    img_url = response["url"]

    await client.send_photo(message.chat.id, img_url, reply_to_message_id=message.message_id)


# Start the bot
client.run()
