from app.message import Message

from .transmitter import Transmitter

class StdOutTransmitter(Transmitter):
    def transmit(self, message: Message):
        print(f"From: {message.email}\n{message.body}")