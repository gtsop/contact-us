import smtplib
from email.mime.text import MIMEText
from contact_us.app.message import Message
from .smtp_client import SMTPClient

class AuthClient(SMTPClient):

    login_user: str = 'user'
    login_pass: str = 'pass'

    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port

    def send(self, message: Message):
        msg = MIMEText(message.body)
        msg['Subject'] = 'Message from your app'
        msg['From'] = 'admin-auth@localhost'
        msg['To'] = message.email

        server = smtplib.SMTP(self.host, self.port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.login_user, self.login_pass)

        server.sendmail('admin-auth@localhost', [message.email], msg.as_string())
        server.quit()