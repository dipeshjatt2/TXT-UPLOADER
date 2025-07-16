import os

API_ID = 22118129
API_HASH = "43c66e3314921552d9330a4b05b18800"
BOT_TOKEN = "7485383982:AAFuRY-6wQjfHzAloZLRJyYPi9Jp_TzYNR4"

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = 5203820046

LOG = -4818795203 ,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5203820046").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


