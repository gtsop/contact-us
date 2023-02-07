from contact_us.cli import CLI, create_cli as _create_cli
from contact_us.app.transmitter import Transmitter, StdOutTransmitter
from contact_us.app.storage import Storage, InMemoryStorage


# Provide some common sensible default arguments for unit testing purposes
def create_cli(
    transmitter: type[Transmitter] = StdOutTransmitter,
    storage: type[Storage] = InMemoryStorage,
) -> CLI:
    return _create_cli(transmitter=transmitter, storage=storage)
