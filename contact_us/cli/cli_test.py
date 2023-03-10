from contact_us.testing import create_cli
from typer.testing import CliRunner


def test_cli_create_message():
    cli = create_cli()
    runner = CliRunner()
    result = runner.invoke(cli.typer, ["create-message", "foo@bar.com", "hello world"])
    assert result.exit_code == 0
    assert 'Created message: email="foo@bar.com" body="hello world"' in result.stdout


def test_cli_list_messages():
    cli = create_cli()
    runner = CliRunner()
    result = runner.invoke(cli.typer, ["list-messages"])

    assert result.exit_code == 0
    assert "0 messages\n" in result.stdout

    runner.invoke(cli.typer, ["create-message", "foo@bar.com", "hello world"])
    runner.invoke(
        cli.typer, ["create-message", "bar@foo.com", "goodbye world"]
    )

    result = runner.invoke(cli.typer, ["list-messages"])

    assert result.exit_code == 0
    assert (
        "2 messages\n\n"
        '1. email="foo@bar.com" body="hello world"\n'
        '2. email="bar@foo.com" body="goodbye world"'
    ) in result.stdout

def test_cli_send_message():
    cli = create_cli()
    runner = CliRunner()
    runner.invoke(cli.typer, ["create-message", "foo@bar.com", "hello world"])

    result = runner.invoke(cli.typer, ["send-message", "1"])
    assert result.exit_code == 0
    assert (
        "Sending message: 1\n"
        "From: foo@bar.com\n"
        "hello world"
    )

    result = runner.invoke(cli.typer, ["list-messages"])
    assert (
        "1 messages\n\n"
        '1. email="foo@bar.com" body="hello world" (sent)\n'
    ) in result.stdout


