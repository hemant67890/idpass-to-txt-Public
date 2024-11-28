import os

api_id = 26512964
api_hash = os.environ.get("API_HASH", "e5d187c6c7a0919ccb8866f76f655701")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "2052075731")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "2052075731")
owner_users = [int(num) for num in osowner_users.split(",")]
