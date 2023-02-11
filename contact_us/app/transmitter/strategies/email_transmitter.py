import smtplib
from email.mime.text import MIMEText
from contact_us.app.message import Message

class EmailTransmitter:
    def __init__(self, smtp_server: str, smtp_port: int):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
    
    def transmit(self, message: Message):
        msg = MIMEText(message.body)
        msg['Subject'] = 'Message from your app'
        msg['From'] = 'yourapp@example.com'
        msg['To'] = message.email
        
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.send_message(msg)
        server.quit()