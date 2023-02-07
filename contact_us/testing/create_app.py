from contact_us.app import App
from contact_us.app.storage import InMemoryStorage
from contact_us.app.transmitter import StdOutTransmitter


def create_app() -> App:
    return App(transmitter=StdOutTransmitter, storage=InMemoryStorage)
