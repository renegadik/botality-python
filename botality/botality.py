import asyncio
from botality.telegram_bot import TelegramBot
from botality.discord_bot import DiscordBot

class Botality:
    def __init__(self, bots):
        self.bots = bots
        self.discord_bot = None
        self.telegram_bot = None

        if 'discord' in self.bots:
            self.discord_bot = DiscordBot(self.bots['discord'])
        if 'telegram' in self.bots:
            self.telegram_bot = TelegramBot(self.bots['telegram'])

    async def start(self):
        if self.discord_bot:
            await self.discord_bot.start()
    
    async def close(self):
        if self.discord_bot:
            await self.discord_bot.close()

    async def send_message(self, bot_type, channel_id, message):
        if bot_type == 'discord' and self.discord_bot:
            await self.discord_bot.send_message(channel_id, message)
        elif bot_type == 'telegram' and self.telegram_bot:
            await self.telegram_bot.send_message(channel_id, message)

    async def send_message_to_all(self, channel_ids, message):
        if channel_ids['discord'] and self.discord_bot:
            await self.discord_bot.send_message(channel_ids['discord'], message)
        if channel_ids['telegram'] and self.telegram_bot:
            await self.telegram_bot.send_message(channel_ids['telegram'], message)