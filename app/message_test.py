import pytest
from .message import Message

def test_message_instatiates():
    message = Message()

def test_message_property_email():
    message = Message(email="foo@bar.com")

    assert message.email == "foo@bar.com"

def test_message_property_body():
    message = Message(body="hello world")

    assert message.body == "hello world"

def test_message_property_is_sent():
    message = Message()

    assert message.is_sent == False

def test_message_method_send():
    message = Message()
    message.send()
    assert message.is_sent == True
