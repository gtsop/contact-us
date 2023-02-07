from contact_us.testing import create_app
from contact_us.cli import CLI


def create_cli() -> CLI:
    return CLI(create_app)
