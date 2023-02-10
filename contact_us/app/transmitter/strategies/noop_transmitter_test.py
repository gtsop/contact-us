from contact_us.app.message import Message
from .noop_transmitter import NoopTransmitter

def test_noop_instantiates():
    assert NoopTransmitter()

def test_noop_transmitter_does_nothing():
    message = Message()
    transmitter = NoopTransmitter()
    transmitter.transmit(message)