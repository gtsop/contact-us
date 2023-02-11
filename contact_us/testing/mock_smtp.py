import smtpd
import asyncore
import threading

class MockSMTP(smtpd.SMTPServer):
    def __init__(self, localaddr, remoteaddr, messages=None):
        if messages is None:
            messages = []
        self.messages = messages
        smtpd.SMTPServer.__init__(self, localaddr, remoteaddr)

    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        self.messages.append((peer, mailfrom, rcpttos, data))

class SMTPServerThread(threading.Thread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        asyncore.loop()

class MockSMTPClient:
    def __init__(self):
        self.messages = []
        self.server = MockSMTP(('localhost', 2323), None, self.messages)
        self.thread = SMTPServerThread(self.server)
        self.thread.start()

    def get_emails(self):
        return self.messages

    def stop(self):
        self.server.close()
        self.thread.join()