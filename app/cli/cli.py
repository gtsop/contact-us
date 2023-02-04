import typer

from app.app import App
from app.transmitter import StdOutTransmitter

cli = typer.Typer()
app = App(StdOutTransmitter())

def create_cli():
    return typer.Typer()

@cli.command()
def list_messages():
    messages = app.list_messages()
    print(f"{len(messages)} messages\n")
    for index, message in enumerate(messages):
        print(f'{index + 1}. email="{message.email}" body="{message.body}"')

@cli.command()
def create_message(email: str, body: str):
    message = app.create_message(email=email, body=body)
    print(f'Created message: email="{message.email}" body="{message.body}"')

if __name__ == "__main__":
    cli()