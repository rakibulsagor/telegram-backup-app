# Telegram Backup App

A simple Python desktop app to backup files or folders to a Telegram channel via a bot.

## Features
- Select files or folders
- Optional auto-zip before upload
- Uploads directly to your Telegram channel

## Requirements
- Python 3.x
- python-telegram-bot library
- tkinter (usually included with Python)
- zip utility (for compressing folders)

## Usage

1. Create a Telegram bot and get its token.
2. Create a private channel and add the bot as admin.
3. Get the channel ID.
4. Edit `telegram_backup_gui.py` and set your `BOT_TOKEN` and `CHANNEL_ID`.
5. Run the app:

   ```bash
   python telegram_backup_gui.py

