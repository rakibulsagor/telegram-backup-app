import os
import zipfile
import asyncio
from tkinter import Tk, filedialog, Label, Button, Checkbutton, IntVar, messagebox
from telegram import Bot
from telegram.constants import ChatAction

# ==== CONFIG ====
BOT_TOKEN = "XXXXXXXXXX:XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
CHANNEL_ID = "-XXXXXXXXXXXXX"
# ================

bot = Bot(token=BOT_TOKEN)

async def send_file(file_path):
    try:
        await bot.send_chat_action(chat_id=CHANNEL_ID, action=ChatAction.UPLOAD_DOCUMENT)
        with open(file_path, 'rb') as f:
            await bot.send_document(chat_id=CHANNEL_ID, document=f, filename=os.path.basename(file_path))
        return True
    except Exception as e:
        print(f"Error uploading {file_path}: {e}")
        return False

def zip_folder(folder_path):
    zip_name = folder_path.rstrip("/").split("/")[-1] + ".zip"
    zip_path = os.path.join("/tmp", zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk(folder_path):
            for file in files:
                full_path = os.path.join(root, file)
                arcname = os.path.relpath(full_path, folder_path)
                zipf.write(full_path, arcname)
    return zip_path

class TelegramBackupApp:
    def __init__(self, master):
        self.master = master
        master.title("Telegram Backup App")

        self.label = Label(master, text="Select file or folder to back up:")
        self.label.pack()

        self.zip_option = IntVar()
        self.check = Checkbutton(master, text="Auto-zip before sending", variable=self.zip_option)
        self.check.pack()

        self.select_button = Button(master, text="Select File/Folder", command=self.select_file_or_folder)
        self.select_button.pack()

    def select_file_or_folder(self):
        path = filedialog.askopenfilename()
        if not path:
            path = filedialog.askdirectory()
        if not path:
            return

        if os.path.isdir(path) and self.zip_option.get():
            path = zip_folder(path)
        elif os.path.isfile(path) and self.zip_option.get():
            zip_path = os.path.join("/tmp", os.path.basename(path) + ".zip")
            with zipfile.ZipFile(zip_path, 'w') as zipf:
                zipf.write(path, os.path.basename(path))
            path = zip_path

        self.upload_file(path)

    def upload_file(self, path):
        self.label.config(text="Uploading...")
        asyncio.run(self.run_upload(path))
        self.label.config(text="Upload Complete")
        messagebox.showinfo("Success", f"{os.path.basename(path)} sent to Telegram!")

    async def run_upload(self, path):
        await send_file(path)

# Run the app
root = Tk()
root.geometry("300x180")
app = TelegramBackupApp(root)
root.mainloop()

