class App:
    def create_message(self, email, body):
        return { "email": email, "body": body}
        
    def list_messages(self):
        return []