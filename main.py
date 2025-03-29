import asyncio
from botality.telegram_bot import TelegramBot
from botality.discord_bot import DiscordBot
from botality.botality import Botality
from config.config import TELEGRAM_TOKEN, DISCORD_TOKEN



async def main():
    tokens = {
        'discord': DISCORD_TOKEN,
        'telegram': TELEGRAM_TOKEN
    }

    botality = Botality(tokens)
    await botality.start()

    # await botality.send_message('discord', '1355321005148471306', 'test from discord')
    # await botality.send_message('telegram', '-1002679332116', 'test from telegram')

    await botality.send_message_to_all({'discord': '1355321005148471306', 'telegram': '-1002679332116'}, 'TEST FOR ALL')

    await botality.close()


if __name__ == "__main__":
    asyncio.run(main())