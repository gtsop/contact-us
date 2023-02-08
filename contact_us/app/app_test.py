from contact_us.testing import Mock, create_app, are_messages_equal

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

    assert are_messages_equal(app.list_messages(), [messageA, messageB])


def test_app_sends_messages():
    transmitter = Mock
    app = create_app(transmitter=transmitter)

    message = app.create_message(email="a@a.com", body="a")

    app.send_message(message)

    app.transmitter.transmit.assert_called_with(message)
    assert message.is_sent == True


def test_app_lists_unsent_messages():
    transmitter = Mock
    app = create_app(transmitter=transmitter)

    messageA = app.create_message(email="a@a.com", body="a")
    messageB = app.create_message(email="b@b.com", body="b")

    assert are_messages_equal(app.list_unsent_messages(), [messageA, messageB])

    app.send_message(messageA)

    assert are_messages_equal(app.list_unsent_messages(), [messageB])
