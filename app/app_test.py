import pytest

from .app import App

def test_app_instantiates():
    assert App()

def test_app_creates_messages():
    app = App()
    message = app.create_message(email="foo", body="bar")

    assert message.email == 'foo'
    assert message.body == 'bar'

def test_app_lists_messages():
    app = App()

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_messages()

    assert messages == [messageA, messageB]


def test_app_sends_messages():
    app = App()

    messageA = app.create_message(email="a@a.com", body="a")

    app.send_message(messageA)

    assert messageA.is_sent == True

def test_app_lists_unsent_messages():

    app = App()

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    messages = app.list_unsent_messages()
    assert messages == [messageA, messageB]

    app.send_message(messageA)

    messages = app.list_unsent_messages()
    assert messages == [messageB]
