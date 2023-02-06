import typer

from contact_us.app import App
from contact_us.app.transmitter import StdOutTransmitter
from contact_us.app.storage import InMemoryStorage

cli = typer.Typer()

def create_app():
    return App(transmitter=StdOutTransmitter, storage=InMemoryStorage)

@cli.command()
def list_messages():
    app = create_app()
    messages = app.list_messages()
    print(f"{len(messages)} messages\n")
    for index, message in enumerate(messages):
        print(f'{index + 1}. email="{message.email}" body="{message.body}"')

@cli.command()
def create_message(email: str, body: str):
    app = create_app()
    message = app.create_message(email=email, body=body)
    print(f'Created message: email="{message.email}" body="{message.body}"')

def main():
    cli()