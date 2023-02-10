from ..transmitter import Transmitter

from contact_us.app.message import Message

class NoopTransmitter(Transmitter):
    def transmit(self, message: Message):
        pass