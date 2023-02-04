from typer.testing import CliRunner

from .cli import cli

runner = CliRunner()

def test_cli():
    result = runner.invoke(cli, ["list-messages"])
    assert result.exit_code == 0
    assert "0 messages\n" in result.stdout

def test_cli_create_message():
    result = runner.invoke(cli, ["create-message", "foo@bar.com", "hello world"])
    assert result.exit_code == 0
    assert 'Created message: email="foo@bar.com" body="hello world"' in result.stdout