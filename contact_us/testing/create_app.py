from contact_us.app import App, create_app as _create_app
from contact_us.app.storage import Storage, InMemoryStorage
from contact_us.app.transmitter import Transmitter, StdOutTransmitter

# Essentially provides some common sensible defaults for testing purposes
# over the `create_app` function
def create_app(
    transmitter: type[Transmitter] = StdOutTransmitter,
    storage: type[Storage] = InMemoryStorage,
) -> App:
    return _create_app(transmitter=transmitter, storage=storage)
