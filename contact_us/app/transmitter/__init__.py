from .transmitter import Transmitter
from .strategies.stdout_transmitter import StdOutTransmitter
from contact_us.settings import settings

class TransmitterStrategies:
    StdOut: type[Transmitter] = StdOutTransmitter

    @staticmethod
    def setting() -> type[Transmitter]:
        if settings.transmitter_strategy == 'std-out':
            return StdOutTransmitter
        return StdOutTransmitter



