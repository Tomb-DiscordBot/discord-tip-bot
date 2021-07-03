from config import config
from utils.fantom import connect_to_fantom
from bot.discord import run_discord_bot
from database.database import init_db

from utils.fantom import get_balance_for_address

import logging

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def main():
    fantom = connect_to_fantom(config["PROVIDER_ADDRESS"])
    conn = init_db(config["DATABASE_NAME"])

    addr = "0x248E0006472F08D5b06d3D252085B3cB7a595fB0"
    run_discord_bot(config["DISCORD_TOKEN"])
    bot.run(config["DISCORD_TOKEN"])
    return 

if __name__ == "__main__":
    main()
