import asyncio
from discord import Client, Intents
from botality.base_bot import BaseBot


class DiscordBot(BaseBot):
    def __init__(self, token: str):
        super().__init__(token)
        intents = Intents.default()
        intents.message_content = True
        self.client = Client(intents=intents)
        self._ready = asyncio.Event()
        
        @self.client.event
        async def on_ready():
            self._ready.set()
            print(f"Discord bot logged in as {self.client.user}")
    
    async def start(self):
        self._start_task = asyncio.create_task(self.client.start(self.token))
        await self._ready.wait()
    
    async def close(self):
        await self.client.close()
    
    async def send_message(self, channel_id: str, message: str):
        channel_id = int(channel_id)

        if not self._ready.is_set():
            await self.start()

        channel = await self.client.fetch_channel(channel_id)
        await channel.send(message)
    
