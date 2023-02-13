import pytest
from .email_transmitter import EmailTransmitter
from contact_us.app.message import Message
from contact_us.testing import MockSMTPClient


def smtp_client():
    client = MockSMTPClient()
    yield client
    client.stop()


@pytest.mark.skip()
def test_actual_transmit():
    email_transmitter = EmailTransmitter(
        smtp_server="smtp.gmail.com", smtp_port=587
    )
    message = Message(email="gtsop.junk@gmail.com", body="test message")
    email_transmitter.transmit(message)

@pytest.mark.skip()
def test_transmit(smtp_client):
    email_transmitter = EmailTransmitter(
        smtp_server="localhost", smtp_port=smtp_client.server.socket.getsockname()[1]
    )
    message = Message(email="example@example.com", body="test message")
    email_transmitter.transmit(message)

    emails = smtp_client.get_emails()
    assert len(emails) == 1
    email = emails[0]
    assert email[2][0] == message.email
    assert message.body in email[3].decode('UTF-8')

# def test_email_transmitter_sends_mail(smtp_client):
#     email_transmitter = create_email_transmitter(smtp_client=smtp_client)

#     message = Message(email="example@example.com", body="test message")

#     email_transmitter.transmit(message)

#     emails = smtp_client.get_emails()
#     email = emails[0]

#     assert email[2][0] == message.email
#     assert message.body in email[3].decode('UTF-8')