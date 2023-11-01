"""
    __main__

    Initializes the discord client object and runs the async main function

    Made with love and care by Vaughn Woerpel
"""

# built-in
import asyncio

import certifi

# external
import discord
import pymongo

# project modules
from bot import constants
from bot.bot import Sexybabeycord


async def main() -> None:
    """Define bot parameters and initialize the client object"""

    intents = discord.Intents.all()

    mongo_client = None
    uri = constants.Database.connection_uri
    if uri is not None:
        mongo_client = pymongo.MongoClient(uri)

    client = Sexybabeycord(
        mongo_client=mongo_client,
        intents=intents,
        command_prefix=constants.Bot.prefix,
    )

    await client.start(constants.Bot.token)


if __name__ == "__main__":
    """Run the bot"""

    asyncio.run(main())
