from config import get_config
from utils.fantom import connect_to_fantom

from db.utils import get_db
from bot.discord import get_discord_bot

import logging

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="bot.log", encoding="utf-8", mode="w")
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

def main():
    config = get_config()
    logging.info('Tip Bot Started')
    db = get_db(config['DATABASE_FILE'])
    fantom = connect_to_fantom(config["PROVIDER_ADDRESS"])
    bot = get_discord_bot(config)
    bot.run(config["DISCORD_TOKEN"])
    return 

if __name__ == "__main__":
    main()
