import typer

from typing import Type
from contact_us.app import App
from contact_us.app.transmitter import Transmitter, StdOutTransmitter
from contact_us.app.storage import Storage, InMemoryStorage, DBStorage


def create_app():
    return


class CLI:
    def __init__(
        self,
        transmitter: Type[Transmitter] = StdOutTransmitter,
        storage: Type[Storage] = InMemoryStorage,
    ):
        self.typer = typer.Typer()
        self.app = App(transmitter=transmitter, storage=storage)

        @self.typer.command()
        def list_messages():
            messages = self.app.list_messages()
            print(f"{len(messages)} messages\n")
            for index, message in enumerate(messages):
                print(f'{index + 1}. email="{message.email}" body="{message.body}"')

        @self.typer.command()
        def create_message(email: str, body: str):
            message = self.app.create_message(email=email, body=body)
            print(f'Created message: email="{message.email}" body="{message.body}"')


def main():
    cli = CLI(storage=DBStorage)
    cli.typer()
