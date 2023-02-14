import asyncio
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink

class Handler(Sink):
    emails = []

    # async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
    #     envelope.rcpt_tos.append(address)
    #     return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        email = ''
        for ln in envelope.content.decode('utf8', errors='replace').splitlines():
            email += f'{ln}'.strip() + '\n'
        self.emails.append(email)
        return '250 Message accepted for delivery'

class SMTPServer:
    hostname: str = ''
    port: int = 0

    def __init__(self):
        self.handler = Handler()
        self.controller = Controller(self.handler)
        self.controller.start()
        self.hostname = self.controller.hostname
        self.port = self.controller.port
    
    def __dell__(self):
        self.controller.stop()

    def get_emails(self):
        return self.handler.emails