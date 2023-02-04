import typer

from app.app import App
from app.transmitter import StdOutTransmitter

cli = typer.Typer()

transmitter = StdOutTransmitter()
storage = None

def create_app():
    return App(transmitter=transmitter)

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

if __name__ == "__main__":
    cli()