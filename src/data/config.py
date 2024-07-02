import os

from dotenv import load_dotenv


load_dotenv()


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))


ADMINS_ID = [
    7336285462, # мой телеграм id
    1485578170 # егора телеграм id
]
