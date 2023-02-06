class Message:
    def __init__(self, email: str = '', body: str = ''):
        self.email = email
        self.body = body
        self.is_sent = False

    def send(self):
        self.is_sent = True
    
    def is_equal(self, other: 'Message'):
        return self.email == other.email and self.body == other.body