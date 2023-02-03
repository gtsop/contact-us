from abc import ABC, abstractmethod
from ..message import Message

class Transmitter(ABC):
    @abstractmethod
    def transmit(self, message: Message):
        pass