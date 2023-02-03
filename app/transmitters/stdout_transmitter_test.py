from .stdout_transmitter import StdOutTransmitter
from ..message import Message

def test_stdout_transmitter_instantiates():
    assert StdOutTransmitter()

def test_stdout_transmitter_method_transmit(capsys):
    transmitter = StdOutTransmitter()
    message = Message(email="foo@bar.com", body="hello world")

    transmitter.transmit(message)

    captured = capsys.readouterr()
    assert "From: foo@bar.com\nhello world" in captured.out

