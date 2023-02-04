from .transmitter import Transmitter
from app.message import Message

class StdOutTransmitter(Transmitter):
    def transmit(self, message: Message):
        print(f"From: {message.email}\n{message.body}")