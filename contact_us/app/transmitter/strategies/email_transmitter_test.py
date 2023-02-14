import pytest
from .email_transmitter import EmailTransmitter
from contact_us.app.message import Message


@pytest.mark.skip()
def test_actual_transmit():
    email_transmitter = EmailTransmitter(smtp_server="smtp.gmail.com", smtp_port=587)
    message = Message(email="gtsop.junk@gmail.com", body="test message")
    email_transmitter.transmit(message)


# def test_email_transmitter_sends_mail(smtp_client):
#     email_transmitter = create_email_transmitter(smtp_client=smtp_client)

#     message = Message(email="example@example.com", body="test message")

#     email_transmitter.transmit(message)

#     emails = smtp_client.get_emails()
#     email = emails[0]

#     assert email[2][0] == message.email
#     assert message.body in email[3].decode('UTF-8')
