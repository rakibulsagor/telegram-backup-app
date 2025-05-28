from telegram import Bot
import asyncio

BOT_TOKEN = "7682615010:AAEw4qJqGRSHci4cfcLTf8Q18RCMiisuKCg"

async def main():
    bot = Bot(token=BOT_TOKEN)
    updates = await bot.get_updates()
    for update in updates:
        if update.channel_post:
            print("Chat ID:", update.channel_post.chat.id)

asyncio.run(main())

