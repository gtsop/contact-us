import typer

from contact_us.app import App, create_app
from contact_us.app.transmitter import Transmitter, TransmitterStrategies
from contact_us.app.storage import Storage, StorageStrategies


class CLI:
    def __init__(self, app: App):
        self.typer = typer.Typer()
        self.app = app

        @self.typer.command()
        def list_messages():
            messages = self.app.list_messages()
            print(f"{len(messages)} messages\n")
            for index, message in enumerate(messages):
                print(
                    f'{index + 1}. email="{message.email}" body="{message.body}"{" (sent)" if message.is_sent else ""}'
                )

        @self.typer.command()
        def create_message(email: str, body: str):
            message = self.app.create_message(email=email, body=body)
            print(f'Created message: email="{message.email}" body="{message.body}"')

        @self.typer.command()
        def send_message(message_index: int):
            messages = self.app.list_messages()
            message = messages[message_index - 1]
            self.app.send_message(message)

    def exec(self):
        return self.typer()


def create_cli(transmitter: type[Transmitter], storage: type[Storage]):
    app = create_app(transmitter=transmitter, storage=storage)
    return CLI(app=app)


def main():
    cli = create_cli(
        transmitter=TransmitterStrategies.setting(), storage=StorageStrategies.setting()
    )
    cli.exec()
