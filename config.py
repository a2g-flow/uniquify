#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6451502236:AAGfqXVRtesMnJq_b5ej0UGwj5i_de_IudY")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "29310987"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "336c28913a45587a4c10af8cd620b68f")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQG_QAsAZmfr10ktvw0PJqvWBmDMtjGJYJRkCAJ02Wak9SJ9XteFXOCVcHwDC85GKKUCLysGJlduob5N8heu9uv9tUsYpc0_tsssyfE_6pMWr7FWZ3JtgOfHebJxrY3ac4uuPJ_4AAhiLNqdq8fsxnK0523UHGl_nMwhLvkEasEkbp7OnlMIh_eE7OFtvM-B7TJFPw25nMW-_EZnSIGJxYIehJ-E4uvBlohibWqJCbQdMH8ph3T07vnCfvxCoXhl9AfgA-kLBouyjPE9YvtAX_47XPThe4Nh9aWtQpPVlSDbnRjz8Ff0-1yUkgwMTDskoa9Gt1bPkLpkCALrJqLXie5t9YtaZAAAAAGEYMR0AA")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
