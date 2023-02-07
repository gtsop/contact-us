from .message_model import MessageModel
from .base_model import BaseModel

from contact_us.app.message import Message

def test_message_model_instantiates():
    assert MessageModel()

def test_message_model_extends_base_model():
    assert issubclass(MessageModel, BaseModel)

def test_message_model_from_message():
    message = Message(email="foo", body="bar", is_sent=True)
    model = MessageModel.from_message(message)

    assert message.email == model.email
    assert message.body == model.body
    assert message.is_sent == model.is_sent

def test_message_model_to_message():
    model = MessageModel(email="foo", body="bar", is_sent=True)
    message = model.to_message()

    assert message.email == model.email
    assert message.body == model.body
    assert message.is_sent == model.is_sent