class Message:
    def __init__(self, email: str = '', body: str = ''):
        self.email = email
        self.body = body
        self.is_sent = False

    def send(self):
        self.is_sent = True