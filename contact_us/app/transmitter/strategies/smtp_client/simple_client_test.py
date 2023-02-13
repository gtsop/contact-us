import pytest
from contact_us.app.message import Message
from contact_us.testing import MockSMTPClient
from .smtp_client import SMTPClient
from .simple_client import SimpleClient


@pytest.fixture
def simple_smtp_server():
    client = MockSMTPClient()
    yield client
    print("STOPPING")
    client.stop()
    print("STOPPED")


@pytest.mark.skip()
def test_simple_client_instantiates():
    assert SimpleClient("", 0)


@pytest.mark.skip()
def test_simple_client_instance_of_smtp_client():
    assert issubclass(SimpleClient, SMTPClient)


def test_simple_client_sends_mail(simple_smtp_server):
    client = SimpleClient("localhost", simple_smtp_server.server.socket.getsockname()[1])

    message = Message(email="foo@bar.com", body="hello world")

    client.send(message)

    emails = simple_smtp_server.get_emails()

    assert len(emails) == 1

    email = emails[0]

    assert email[2][0] == message.email
    assert message.body in email[3].decode("UTF-8")
