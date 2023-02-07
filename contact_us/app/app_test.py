from unittest.mock import Mock
from contact_us.__test_utils__ import are_messages_equal
from contact_us.testing import create_app

from .app import App

def test_app_instantiates():
    transmitter = Mock()
    storage = Mock()

    assert App(transmitter=transmitter, storage=storage)


def test_app_creates_messages():
    app = create_app()
    message = app.create_message(email="foo", body="bar")

    assert message.email == "foo"
    assert message.body == "bar"


def test_app_lists_messages():
    app = create_app()

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_messages()

    assert are_messages_equal(messages, [messageA, messageB])


def test_app_sends_messages():
    transmitter = Mock
    app = create_app(transmitter=transmitter)

    messageA = app.create_message(email="a@a.com", body="a")

    app.send_message(messageA)

    app.transmitter.transmit.assert_called_with(messageA)
    assert messageA.is_sent == True


def test_app_lists_unsent_messages():
    app = create_app()

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_unsent_messages()
    assert are_messages_equal(messages, [messageA, messageB])

    app.send_message(messageA)

    messages = app.list_unsent_messages()
    assert are_messages_equal(messages, [messageB])
