from abc import ABC, abstractmethod

class BaseBot(ABC):

    def __init__(self, token: str):
        self.token = token

    @abstractmethod
    def send_message(self, channel_id: str, message: str):
        pass