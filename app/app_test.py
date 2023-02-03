import pytest
from unittest.mock import Mock

from .app import App

transmitter = Mock()

def test_app_instantiates():
    assert App(transmitter)

def test_app_creates_messages():
    app = App(transmitter)
    message = app.create_message(email="foo", body="bar")

    assert message.email == 'foo'
    assert message.body == 'bar'

def test_app_lists_messages():
    app = App(transmitter)

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_messages()

    assert messages == [messageA, messageB]

def test_app_sends_messages():
    app = App(transmitter)

    messageA = app.create_message(email="a@a.com", body="a")

    app.send_message(messageA)

    transmitter.transmit.assert_called_with(messageA)
    assert messageA.is_sent == True

def test_app_lists_unsent_messages():
    app = App(transmitter)

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_unsent_messages()
    assert messages == [messageA, messageB]

    app.send_message(messageA)

    messages = app.list_unsent_messages()
    assert messages == [messageB]
