from abc import ABC, abstractmethod
from app.message import Message

class Transmitter(ABC):
    @abstractmethod
    def transmit(self, message: Message):
        pass