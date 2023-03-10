import smtplib
from email.mime.text import MIMEText
from contact_us.app.message import Message
from .smtp_client import SMTPClient

class SimpleClient(SMTPClient):

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def send(self, message: Message):
        msg = MIMEText(message.body)
        msg['Subject'] = 'Message from your app'
        msg['From'] = 'admin-simple@localhost'
        msg['To'] = message.email

        server = smtplib.SMTP(self.host, self.port)
        server.sendmail('admin-simple@localhost', [message.email], msg.as_string())
        server.quit()