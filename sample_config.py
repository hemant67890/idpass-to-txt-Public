import os

api_id = 21250782
api_hash = os.environ.get("API_HASH", "458edca2c67a2c299d925b6a71e")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "7045471")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "70145471")
owner_users = [int(num) for num in osowner_users.split(",")]
