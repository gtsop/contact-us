from typing import List
from abc import ABC, abstractmethod
from app.message import Message

class Storage(ABC):
    @abstractmethod
    def append(self, message: Message):
        pass

    @abstractmethod
    def all(self) -> List[Message]:
        pass