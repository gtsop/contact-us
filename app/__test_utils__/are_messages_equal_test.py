from app.message import Message
from .are_messages_equal import are_messages_equal 

def test_are_messages_equal():

    messageA = Message('foo', 'a')
    messageB = Message('bar', 'b')
    messageC = Message('baz', 'c')

    messageA2 = Message('foo', 'a')
    messageB2 = Message('bar', 'b')
    messageC2 = Message('baz', 'c')

    assert are_messages_equal([], [])
    assert are_messages_equal([messageA], [messageA2])
    assert are_messages_equal([messageA, messageB], [messageA2, messageB2])
    assert are_messages_equal([messageA, messageB, messageC], [messageA2, messageB2, messageC2])

    assert not are_messages_equal([messageA], [])
    assert not are_messages_equal([messageA], [messageB])