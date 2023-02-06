from setuptools import setup

setup(
    name='contact_us',
    version='0.1',
    install_requires=[
        "click==8.1.3",
        "fastapi==0.89.1",
        "httpx==0.23.3",
        "pydantic==1.10.4",
        "SQLAlchemy==2.0.1",
        "starlette==0.22.0",
        "typer==0.7.0"
    ],
    entry_points={
        "console_scripts": [
            "contact-us=contact_us.cli.cli:main"
        ]
    }
)
