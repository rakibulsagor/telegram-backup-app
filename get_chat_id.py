from telegram import Bot
import asyncio

BOT_TOKEN = "XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" // Replace with your bot token
CHANNEL_ID = "-XXXXXXXXXXXXX"  # Replace with your channel ID (e.g., "-1001234567890" for a channel)

async def main():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()
    for update in updates:
        if update.channel_post:
            print("Chat ID:", update.channel_post.chat.id)

asyncio.run(main())

