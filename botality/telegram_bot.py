from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from botality.base_bot import BaseBot


class TelegramBot(BaseBot):
    def __init__(self, token: str):
        super().__init__(token)
        self.telegram = Application.builder().token(token).build() 
    
    async def send_message(self, channel_id: str, message: str):
        chat_id = int(channel_id)
        await self.telegram.bot.send_message(chat_id=chat_id, text=message)  
