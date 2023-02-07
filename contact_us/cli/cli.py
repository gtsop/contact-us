import typer

from typing import Callable
from contact_us.app import App
from contact_us.app.transmitter import Transmitter, StdOutTransmitter
from contact_us.app.storage import Storage, InMemoryStorage, DBStorage


def app_factory() -> App:
    return App(transmitter=StdOutTransmitter, storage=DBStorage)


class CLI:
    def __init__(self, create_app: Callable[[], App] = app_factory):
        self.typer = typer.Typer()
        self.app = create_app()

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

    def exec(self):
        return self.typer()

def main():
    cli = CLI()
    cli.exec()
