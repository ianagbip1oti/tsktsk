import logging
from pathlib import Path

from dotenv import load_dotenv
from smalld import SmallD
from smalld_click import SmallDCliRunner

from tsktsk import db
from tsktsk.commands import root

load_dotenv(Path(".env"))


def cli():
    import tsktsk.commands.cli  # noqa

    root()


def bot():
    import tsktsk.commands.bot  # noqa

    logging.basicConfig(level=logging.INFO)

    db.apply_migrations()

    smalld = SmallD()

    create_message = lambda msg: {"content": f"```\n{msg}\n```"}

    with SmallDCliRunner(smalld, root, create_message=create_message):
        smalld.run()
