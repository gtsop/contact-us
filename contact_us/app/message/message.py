class Message:
    def __init__(self, email: str = '', body: str = '', is_sent: bool = False):
        self.email = email
        self.body = body
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True
    
    def is_equal(self, other: 'Message'):
        return self.email == other.email and self.body == other.body