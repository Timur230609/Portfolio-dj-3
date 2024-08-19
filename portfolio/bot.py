import requests

from environs import Env

env = Env()
env.read_env()


def  send_message(text):
  BOT_TOKEN = env.str("BOT_TOKEN")
  CHAT_ID = env.str("CHAT_ID")
  PHOTO = "https://www.uhdpaper.com/2024/07/moon-palm-trees-synthwave-4k-2150k.html"
  TEXT = text
  url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendphoto?chat_id={CHAT_ID}&photo={PHOTO}&caption={TEXT}"
  print(url)
  response = requests.get(url)
