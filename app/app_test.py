from .app import App

def test_app_instantiates():
    assert App()

def test_app_creates_messages():
    app = App()
    message = app.create_message(email="foo", body="bar")

    assert message == { "email": "foo", "body": "bar" }

def test_app_lists_messages():
    app = App()
    messages = app.list_messages()

    assert messages == []