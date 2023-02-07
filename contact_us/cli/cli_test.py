import pytest
from contact_us.app.storage import DBStorage
from typer.testing import CliRunner

from .cli import CLI

def test_cli_create_message():
    cli = CLI()
    runner = CliRunner()
    result = runner.invoke(cli.typer, ["create-message", "foo@bar.com", "hello world"])
    assert result.exit_code == 0
    assert 'Created message: email="foo@bar.com" body="hello world"' in result.stdout

def test_cli_list_messages():
    cli = CLI(storage=DBStorage)
    runner = CliRunner()
    result = runner.invoke(cli.typer, ["list-messages"])

    assert result.exit_code == 0
    assert "0 messages\n" in result.stdout

    result = runner.invoke(cli.typer, ["create-message", "foo@bar.com", "hello world"])
    result = runner.invoke(cli.typer, ["create-message", "bar@foo.com", "goodbye world"])

    cli2 = CLI(storage=DBStorage)
    result = runner.invoke(cli2.typer, ["list-messages"])

    assert result.exit_code == 0
    assert ('2 messages\n\n'
        '1. email="foo@bar.com" body="hello world"\n'
        '2. email="bar@foo.com" body="goodbye world"') in result.stdout