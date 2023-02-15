import pytest
from contact_us.app.message import Message
from contact_us.testing import SMTPServer
from .smtp_client import SMTPClient
from .auth_client import AuthClient


@pytest.fixture
def ssl_smtp_server():
    server = SMTPServer(8026, has_ssl=True)
    yield server


def test_auth_client_instantiates():
    assert AuthClient("", 0)


def test_auth_client_instance_of_smtp_client():
    assert issubclass(AuthClient, SMTPClient)


def test_auth_client_sends_mail(ssl_smtp_server):
    client = AuthClient(ssl_smtp_server.hostname, ssl_smtp_server.port)

    message = Message(email="auth@localhost", body="hello world auth")

    client.send(message)

    emails = ssl_smtp_server.get_emails()

    assert len(emails) == 1

    email = emails[0]

    assert message.email in email
    assert message.body in email
