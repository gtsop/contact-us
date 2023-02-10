from .transmitter import Transmitter
from .strategies.stdout_transmitter import StdOutTransmitter
from .strategies.noop_transmitter import NoopTransmitter
from contact_us.settings import settings

class TransmitterStrategies:
    StdOut: type[Transmitter] = StdOutTransmitter
    Noop: type[Transmitter] = NoopTransmitter

    @staticmethod
    def setting() -> type[Transmitter]:
        if settings.transmitter_strategy == 'std-out':
            return StdOutTransmitter
        if settings.transmitter_strategy == 'no-op':
            return NoopTransmitter
        return NoopTransmitter



