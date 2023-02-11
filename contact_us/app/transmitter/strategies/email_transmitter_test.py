import pytest
from .email_transmitter import EmailTransmitter
from contact_us.app.message import Message
from contact_us.testing import MockSMTPClient


@pytest.fixture
def smtp_client():
    client = MockSMTPClient()
    yield client
    client.stop()


def test_transmit(smtp_client):
    email_transmitter = EmailTransmitter(
        smtp_server="localhost", smtp_port=smtp_client.server.socket.getsockname()[1]
    )
    message = Message(email="recipient@example.com", body="test message")
    email_transmitter.transmit(message)

    emails = smtp_client.get_emails()
    assert len(emails) == 1
    email = emails[0]
    assert email[2][0] == message.email
    assert message.body in email[3].decode('UTF-8')