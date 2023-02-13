from .smtp_client import SMTPClient

def test_smtp_client_has_send_method():
    assert hasattr(SMTPClient, 'send')