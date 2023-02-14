import pytest
from contact_us.app.message import Message
from contact_us.testing import SMTPServer
from .smtp_client import SMTPClient
from .simple_client import SimpleClient


@pytest.fixture
def smtp_server():
    server = SMTPServer()
    yield server


@pytest.mark.skip()
def test_simple_client_instantiates():
    assert SimpleClient("", 0)


@pytest.mark.skip()
def test_simple_client_instance_of_smtp_client():
    assert issubclass(SimpleClient, SMTPClient)


def test_simple_client_sends_mail(smtp_server):
    client = SimpleClient(smtp_server.hostname, smtp_server.port)

    message = Message(email="foo@bar.com", body="hello world")

    client.send(message)

    emails = smtp_server.get_emails()

    assert len(emails) == 1

    email = emails[0]

    assert message.email in email
    assert message.body in email
