
from hydrogram import Client

games = {}
player_game = {}

timeout = 120
minimum_players = 2

sudoers = [123456789]

API_ID = "24244839"
API_HASH = "b655ca9e79f3969e8301909ca911aadf"
BOT_TOKEN = "7973811618:AAE0tzebBXljYEqZtneqgpLLuBWbZHGtcjE"

# --- Telegram config ---

bot = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN, plugins={"root": "unu.plugins"})
