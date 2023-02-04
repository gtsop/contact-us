import typer

from app.app import App
from app.transmitter import StdOutTransmitter

cli = typer.Typer()
app = App(StdOutTransmitter())

@cli.command()
def list_messages():
    print("0 messages\n")

@cli.command()
def create_message(email: str, body: str):
    pass

if __name__ == "__main__":
    cli()