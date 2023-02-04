from typer.testing import CliRunner

from .cli import cli

runner = CliRunner()

def test_cli():
    result = runner.invoke(cli, ["list-messages"])
    assert result.exit_code == 0
    assert "0 messages\n" in result.stdout