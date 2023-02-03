from app.message import Message

class StdOutTransmitter:
    def transmit(self, message: Message):
        print(f"From: {message.email}\n{message.body}")