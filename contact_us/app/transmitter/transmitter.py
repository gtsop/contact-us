from abc import ABC, abstractmethod
from contact_us.app.message import Message

class Transmitter(ABC):
    @abstractmethod
    def transmit(self, message: Message):
        pass