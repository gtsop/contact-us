from typing import List
from abc import ABC, abstractmethod
from contact_us.app.message import Message


class Storage(ABC):
    @abstractmethod
    def append(self, message: Message):
        raise NotImplementedError

    @abstractmethod
    def all(self) -> List[Message]:
        raise NotImplementedError

    @abstractmethod
    def update(self, message: Message):
        raise NotImplementedError
