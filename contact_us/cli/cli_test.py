import pytest
from typer.testing import CliRunner

from .cli import cli

def test_cli_create_message():
    runner = CliRunner()
    result = runner.invoke(cli, ["create-message", "foo@bar.com", "hello world"])
    assert result.exit_code == 0
    assert 'Created message: email="foo@bar.com" body="hello world"' in result.stdout

@pytest.mark.skip()
def test_cli_list_messages():
    runner = CliRunner()
    result = runner.invoke(cli, ["list-messages"])

    assert result.exit_code == 0
    assert "0 messages\n" in result.stdout

    result = runner.invoke(cli, ["create-message", "foo@bar.com", "hello world"])
    result = runner.invoke(cli, ["create-message", "bar@foo.com", "goodbye world"])
    result = runner.invoke(cli, ["list-messages"])

    assert result.exit_code == 0
    assert ('2 messages\n\n'
        '1. email="foo@bar.com" body="hello world"\n'
        '2. email="bar@foo.com" body="goodbye world"') in result.stdout