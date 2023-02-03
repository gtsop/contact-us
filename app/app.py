from .message import Message

class App:

    def __init__(self):
        self.messages = list()

    def create_message(self, email, body):
        message = Message(email=email, body=body)
        self.messages.append(message)
        return message

    def send_message(self, message):
        message.send()

    def list_messages(self):
        return self.messages
    
    def list_unsent_messages(self):
        return [m for m in self.messages if not m.is_sent]