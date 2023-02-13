from abc import ABC, abstractmethod

class SMTPClient(ABC):
    @abstractmethod
    def send(self):
        pass