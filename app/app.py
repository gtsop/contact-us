class App:

    def __init__(self):
        self.messages = list()

    def create_message(self, email, body):
        message = { "email": email, "body": body}
        self.messages.append(message)
        return message

    def list_messages(self):
        return self.messages