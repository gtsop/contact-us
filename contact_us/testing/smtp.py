import asyncio
import ssl
import os
from aiosmtpd.controller import Controller
from aiosmtpd.handlers import Sink
from aiosmtpd.smtp import AuthResult

dir_path = os.path.dirname(os.path.abspath(__file__))


class Handler:
    emails = list()

    async def handle_AUTH(self, *args):
        return "235 2.7.0  Authentication Succeeded"

    async def handle_DATA(self, server, session, envelope):
        email = ""
        for ln in envelope.content.decode("utf8", errors="replace").splitlines():
            email += f"{ln}".strip() + "\n"
        self.emails.append(email)
        return "250 Message accepted for delivery"


class SMTPServer:
    hostname: str = ""
    port: int = 0

    def __init__(self, port=8025, has_ssl=False):
        self.handler = Handler()
        if has_ssl:
            self.context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
            self.context.load_cert_chain(f"{dir_path}/cert.pem", f"{dir_path}/key.pem")
            self.controller = Controller(
                handler=self.handler,
                port=port,
                tls_context=self.context,
            )
        else:
            self.context = None
            self.controller = Controller(
                handler=self.handler,
                port=port,
            )
        self.controller.start()
        self.hostname = self.controller.hostname
        self.port = self.controller.port

    def __dell__(self):
        self.controller.stop()

    def get_emails(self):
        return self.handler.emails
