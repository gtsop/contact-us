import smtpd
import asyncore
import threading

class MockSMTPServer(smtpd.SMTPServer):
    def __init__(self, host='localhost', port=2323, messages=None):
        if messages is None:
            messages = []
        self.messages = messages
        smtpd.SMTPServer.__init__(self, (host, port), ('', 0))

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        self.messages.append((peer, mailfrom, rcpttos, data))
    
    def get_emails(self):
        return self.messages

class SMTPServerThread(threading.Thread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        asyncore.loop()

class MockSMTPClient:
    def __init__(self):
        self.messages = []
        self.server = MockSMTPServer(messages=self.messages)
        self.thread = SMTPServerThread(self.server)
        self.thread.start()

    def get_emails(self):
        return self.messages

    def stop(self):
        self.server.close()
        # self.thread.join()