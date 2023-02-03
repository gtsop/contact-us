from abc import ABC
from ..message import Message

class Transmitter(ABC):
    @abstractmethod
    def transmit(self, message: Message):
        pass