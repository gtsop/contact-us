from contact_us.app import App, create_app as _create_app
from contact_us.app.transmitter import Transmitter, StdOutTransmitter
from contact_us.app.storage import Storage, InMemoryStorage


# Provide some common sensible default arguments for unit testing purposes
def create_app(
    transmitter: type[Transmitter] = StdOutTransmitter,
    storage: type[Storage] = InMemoryStorage,
) -> App:
    return _create_app(transmitter=transmitter, storage=storage)
