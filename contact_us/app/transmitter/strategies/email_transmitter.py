from email.mime.text import MIMEText
from contact_us.app.message import Message
from .smtp_client import SimpleClient
from ..transmitter import Transmitter


class EmailTransmitter(Transmitter):
    def __init__(self, smtp_server: str, smtp_port: int):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port

    def transmit(self, message: Message):
        # msg = MIMEText(message.body)
        # msg['Subject'] = 'Message from your app'
        # msg['From'] = 'yourapp@example.com'
        # msg['To'] = message.email

        client = SimpleClient(self.smtp_server, self.smtp_port)
        client.send(message)

        # server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        # server.ehlo()
        # server.starttls()
        # server.ehlo()
        # server.login(google_email, google_pass)
        # server.sendmail(google_email, [message.email], msg.as_string())
        # server.quit()


# def create_email_transmitter(smtp_client: SMTPClient) -> Transmitter:
#     return EmailTransmitter()
